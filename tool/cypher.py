import pandas as pd
import os
from werkzeug.security import generate_password_hash

def chemical(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path, sheet_name='Chemical')
    
    df = df[df.iloc[:, 0] != 'IUPAC'] 

    for index, row in df.iterrows():
        IUPAC = row.iloc[0]
        molecularFormula = row.iloc[1]

        if pd.isna(IUPAC) or str(IUPAC).strip().lower() == 'nan' or str(IUPAC).strip() == '':
            continue
        
        print(f"""(c{index}:Chemical {{IUPAC: "{IUPAC}", molecularFormula: "{molecularFormula}", createdAt: datetime({{timezone: '+07:00'}})}}),<br>""")

    grouped = df.groupby(df.columns[2])

    for f_name, group in grouped:
        if pd.isna(f_name) or str(f_name).strip().lower() == 'nan' or str(f_name).strip() == '':
            continue

        iupac_list = group.iloc[:, 0].tolist()
        iupac_formatted = ", ".join([f'"{name}"' for name in iupac_list])
        
        print(f'MATCH (f:FunctionalGroup {{name_en: "{f_name}"}})<br>')
        print(f'MATCH (c:Chemical) WHERE c.IUPAC IN [{iupac_formatted}]<br>')
        print(f'CREATE (c)-[:TYPE_OF]->(f);<br>')

def condition(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path, sheet_name='Condition')
    
    df = df[df.iloc[:, 0] != 'name_en'] 

    for index, row in df.iterrows():
        name_en = row.iloc[0]
        name_th = row.iloc[1]
        symbol = row.iloc[2]

        print(f"""(con{index}:Condition {{name_en: "{name_en}", name_th: "{name_th}", symbol: "{symbol}", createdAt: datetime({{timezone: '+07:00'}})}}),<br>""")

def reaction(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path, sheet_name='Reaction')
    
    df = df[df.iloc[:, 0] != 'name_en'] 

    for index, row in df.iterrows():
        name_en = row.iloc[0]
        name_th = row.iloc[1]

        print(f"""(r{index}:Reaction {{name_en: "{name_en}", name_th: "{name_th}", createdAt: datetime({{timezone: '+07:00'}})}}),<br>""")

def user(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path, sheet_name='User')
    
    df = df[df.iloc[:, 0] != 'username'] 

    for index, row in df.iterrows():
        username = row.iloc[0]
        password = row.iloc[1]
        role = row.iloc[2]
        name = row.iloc[3]

        print(f"""(u{index}:User {{username: "{username}", password: "{generate_password_hash(str(password))}", role: "{role}", name: "{name}", createdAt: datetime({{timezone: '+07:00'}})}}),<br>""")

def functionGroup(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path, sheet_name='FunctionalGroup')
    
    df = df[df.iloc[:, 0] != 'name_en'] 

    for index, row in df.iterrows():
        name_en = row.iloc[0]
        name_th = row.iloc[1]
        formula = row.iloc[2]
        molecularFormula = row.iloc[3]
        groupName = row.iloc[4]
        image = row.iloc[5]

        print(f"""(f{index}:FunctionalGroup {{name_en: "{name_en}", name_th: "{name_th}", formula: "{formula}", molecularFormula: "{molecularFormula}", groupName: "{groupName}", image: {image}, createdAt: datetime({{timezone: '+07:00'}})}}),<br>""")

if __name__ == "__main__":
    print("============================== Chemical ==============================")
    # chemical('chem.xlsx')
    print("============================== Reaction ==============================")
    reaction('chem.xlsx')
    print("============================== Condition ==============================")
    condition('chem.xlsx')
    print("============================== User ==============================")
    user('chem.xlsx')
    print("============================== FunctionGroup ==============================")
    functionGroup('chem.xlsx')