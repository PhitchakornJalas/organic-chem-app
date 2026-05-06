import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from neo4j import GraphDatabase
from werkzeug.security import generate_password_hash, check_password_hash

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

@app.route('/reactions')
def reactions():
    query = """
        MATCH (r:Reaction)
        WHERE NOT (r)-[:TYPE_OF]->()  // หาหมวดหมู่หลัก
        OPTIONAL MATCH (sr:SubReaction)-[:TYPE_OF]->(r) // หาปฏิกิริยาย่อย
        
        // 1. จัดการสารตั้งต้น (Reactants) - เรียงลำดับก่อน collect
        OPTIONAL MATCH (f_rect:FunctionalGroup)-[:REACTANT_IN]->(sr)
        OPTIONAL MATCH (c_rect:Chemical)-[:REACTANT_IN]->(sr)
        WITH r, sr, f_rect, c_rect
        ORDER BY elementId(f_rect) ASC, elementId(c_rect) ASC  // จัดเรียงตาม ID ของโหนด
        WITH r, sr, 
            collect(DISTINCT f_rect.name_en) + collect(DISTINCT c_rect.molecularFormula) AS reactants_list

        // 2. จัดการผลิตภัณฑ์ (Products) - เรียงลำดับก่อน collect
        OPTIONAL MATCH (sr)-[:MAIN_PRODUCT]->(f_prod:FunctionalGroup)
        OPTIONAL MATCH (sr)-[:MAIN_PRODUCT]->(c_prod:Chemical)
        OPTIONAL MATCH (sr)-[:BY_PRODUCT]->(cb_prod:Chemical)
        WITH r, sr, reactants_list, f_prod, c_prod, cb_prod
        ORDER BY elementId(f_prod) ASC, elementId(c_prod) DESC, elementId(cb_prod) ASC
        WITH r, sr, reactants_list,
            collect(DISTINCT f_prod.name_en) + 
            collect(DISTINCT c_prod.molecularFormula) + 
            collect(DISTINCT cb_prod.molecularFormula) AS products_list

        // 3. ดึงเงื่อนไข
        OPTIONAL MATCH (con:Condition)-[:REQUIRED_FOR]->(sr)

        // 4. รวบรวมข้อมูลและจัดเรียงหมวดหมู่หลัก
        RETURN 
            elementId(r) AS r_id,
            r.name_en AS category_en,
            r.name_th AS category_th,
            collect({
                sub_name: sr.name_en,
                description: sr.description,
                reactants: reactants_list,
                products: products_list,
                condition_symbol: con.symbol,
                condition_name: con.name_th
            }) AS sub_reactions
        ORDER BY r_id ASC
    """

    with driver.session() as session:
        result = session.run(query)
        categories = [dict(record) for record in result]
        
    return render_template('reactions.html', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not username[0].isalpha() or len(password) < 8:
            flash("ข้อมูลไม่ถูกต้องตามเงื่อนไข", "error")
            return redirect(url_for('register'))
        
        # กำหนด Role เป็น student เสมอ
        role = "student" 

        with driver.session() as db_session:
            # 1. ตรวจสอบก่อนว่ามี Username นี้หรือยัง
            check_user = db_session.run("MATCH (u:User {username: $u}) RETURN u", u=username).single()
            
            if check_user:
                flash("ชื่อผู้ใช้นี้ถูกใช้งานแล้ว กรุณาใช้ชื่ออื่น", "error")
                return redirect(url_for('register'))

            # 2. ทำการ Hash รหัสผ่านก่อนบันทึก
            hashed_password = generate_password_hash(str(password))

            # 3. สร้างโหนด User ใหม่ใน Neo4j
            create_query = """
            CREATE (u:User {
                username: $username,
                password: $password,
                name: $name,
                role: $role,
                createdAt: datetime({timezone: '+07:00'})
            })
            """
            db_session.run(create_query, 
                           username=username, 
                           password=hashed_password, 
                           name=name, 
                           role=role)
            
            flash("สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ", "success")
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/check_username')
def check_username():
    username = request.args.get('username', '').strip()
    
    if not username:
        return jsonify({"exists": False})

    with driver.session() as db_session:
        # ใช้คำสั่ง Cypher เช็คว่ามี Node User ที่มีชื่อนี้ไหม
        result = db_session.run("MATCH (u:User {username: $u}) RETURN u LIMIT 1", u=username)
        user = result.single()
        
        # ถ้าเจอ user แสดงว่าซ้ำ (exists: True) ถ้าไม่เจอแสดงว่าไม่ซ้ำ (exists: False)
        exists = user is not None
        
    return jsonify({"exists": exists})

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