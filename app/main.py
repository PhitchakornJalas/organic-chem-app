import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from neo4j import GraphDatabase
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# ดึงค่าจาก environment ที่ตั้งไว้ใน docker-compose
uri = os.getenv("NEO4J_URI", "bolt://neo4j:7687") 
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(user, password))

@app.route('/')
def index():
    with driver.session() as session:
        query = """
        MATCH (f:FunctionalGroup) 
        RETURN f.name_en AS name_en, 
               f.name_th AS name_th, 
               f.formula AS formula,
               f.molecularFormula AS molecularFormula, 
               f.groupName AS groupName, 
               f.image AS image
        ORDER BY f.id ASC
        """
        results = session.run(query)
        functional_groups = [record.data() for record in results]

    with driver.session() as session:
        query = """
        MATCH (f:FunctionalGroup)
        OPTIONAL MATCH (i:Items)-[:FUNCTIONALGROUP_IS]->(f)
        RETURN collect(distinct f.name_en) + collect(distinct f.name_th) + 
            collect(distinct f.groupName) + collect(distinct i.name_th) AS all_names
        """

        names = session.run(query).single()['all_names']
        # กรองค่าที่เป็น None ออก
        search_suggestions = [n for n in names if n is not None]
        
    return render_template('index.html', functional_groups=functional_groups, all_searchable_names=search_suggestions)

@app.route('/details/<group_name>')
def details(group_name):
    with driver.session() as session:
        query = """
        MATCH (f:FunctionalGroup {name_en: $name})
        OPTIONAL MATCH (i:Items)-[:FUNCTIONALGROUP_IS]->(f)
        RETURN f, collect(i) AS examples
        """
        result = session.run(query, name=group_name).single()
        
        if not result:
            return "ไม่พบข้อมูล", 404
            
        group_data = result['f']
        examples = result['examples']
        
    return render_template('details.html', group=group_data, examples=examples)

@app.route('/search', methods=['POST'])
def search():
    search_text = request.form.get('organicChemSearch', '').strip()
    
    if not search_text:
        return redirect(url_for('index'))
    
    with driver.session() as session:
        query = """
        MATCH (f:FunctionalGroup)
        WHERE toLower(trim(f.name_en)) = toLower(trim($q))
        OR toLower(trim(f.name_th)) = toLower(trim($q))
        OR toLower(trim(f.groupName)) = toLower(trim($q))
        RETURN f.name_en AS name_en

        UNION

        MATCH (i:Items)-[:FUNCTIONALGROUP_IS]->(f:FunctionalGroup)
        WHERE toLower(trim(i.name_th)) = toLower(trim($q))
        RETURN f.name_en AS name_en

        LIMIT 1
        """

        result = session.run(query, q=search_text).single()
        
        if result:
            return redirect(url_for('details', group_name=result['name_en']))
        else:
            # ถ้าพิมพ์เองแล้วไม่ตรงกับที่มีในระบบเลย
            flash("ไม่พบข้อมูลสารหรือสิ่งของที่คุณค้นหา", "error")
            return redirect(url_for('index'))

def create_neo4j_session(username):
    session_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    with driver.session() as db_session:
        # Step 1 & 2: ค้นหา Session เก่าของ User นี้ที่ยัง 'active' แล้วสั่ง 'expired' ให้หมด
        # จากนั้นค่อยสร้าง Session ใหม่เชื่อมเข้าไป
        query = """
        MATCH (u:User {username: $username})
        OPTIONAL MATCH (u)-[:HAS_SESSION]->(old_s:Session {status: 'active'})
        SET old_s.status = 'expired', old_s.terminated_at = $now
        WITH u
        CREATE (s:Session {
            id: $session_id, 
            status: 'active', 
            login_at: $now
        })
        CREATE (u)-[:HAS_SESSION]->(s)
        """
        db_session.run(query, username=username, session_id=session_id, now=now)
    return session_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with driver.session() as db_session:
            # ดึงข้อมูล User มาตรวจสอบ (ดึง name มาด้วย)
            result = db_session.run("MATCH (u:User {username: $u}) RETURN u", u=username)
            user_record = result.single()

            if user_record:
                user_node = user_record['u']
                # ตรวจสอบ Password ที่ Hash ไว้
                if check_password_hash(user_node['password'], password):
                    # จัดการชื่อ: ตัดเอาเฉพาะก้อนแรก
                    full_name = user_node.get('name', username)
                    first_name = full_name.split()[0] if full_name else username
                    
                    sid = create_neo4j_session(username)
                    session['sid'] = sid
                    session['user'] = first_name # เก็บเฉพาะชื่อหน้าใน Session
                    return redirect(url_for('index'))
            
            flash("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง", "error")
    return render_template('login.html')

@app.route('/logout')
def logout():
    sid = session.get('sid')
    if sid:
        with driver.session() as db_session:
            # ค้นหาโหนด Session ตาม ID แล้วแก้สถานะเป็น expired
            query = """
            MATCH (s:Session {id: $sid})
            SET s.status = "expired", s.logout_at = $now
            """
            db_session.run(query, sid=sid, now=datetime.now().isoformat())

    # ล้าง Session ใน Browser
    session.clear()
    return redirect(url_for('login'))

@app.before_request
def check_session_status():
    # ไม่เช็คในหน้า Login, Logout และไฟล์ Static
    if request.endpoint in ['login', 'logout', 'static'] or not request.endpoint:
        return

    sid = session.get('sid')
    if sid:
        with driver.session() as db_session:
            # เช็คว่า Session ID ในคุกกี้ ยังมีสถานะเป็น 'active' ใน Neo4j หรือไม่
            query = "MATCH (s:Session {id: $sid, status: 'active'}) RETURN s"
            result = db_session.run(query, sid=sid).single()

            if not result:
                # ถ้าไม่เจอ หรือสถานะเปลี่ยนเป็น expired แล้ว ให้ล้างคุกกี้และเด้งไปหน้า Login
                session.clear()
                flash("เซสชันของคุณหมดอายุ หรือมีการเข้าสู่ระบบจากอุปกรณ์อื่น", "info")
                return redirect(url_for('login'))

if __name__ == '__main__':
    # host='0.0.0.0' สำคัญมากเพื่อให้เข้าถึงจากนอก Container ได้
    app.run(host='0.0.0.0', port=5000, debug=True)