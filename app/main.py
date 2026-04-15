import os
from flask import Flask, render_template, request
from neo4j import GraphDatabase

app = Flask(__name__)

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
        
    return render_template('index.html', functional_groups=functional_groups)

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

if __name__ == '__main__':
    # host='0.0.0.0' สำคัญมากเพื่อให้เข้าถึงจากนอก Container ได้
    app.run(host='0.0.0.0', port=5000, debug=True)