import os
from flask import Flask, render_template, request, redirect, url_for, flash
from neo4j import GraphDatabase

app = Flask(__name__)

app.secret_key = 'pp222324'

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

if __name__ == '__main__':
    # host='0.0.0.0' สำคัญมากเพื่อให้เข้าถึงจากนอก Container ได้
    app.run(host='0.0.0.0', port=5000, debug=True)