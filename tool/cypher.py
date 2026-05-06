import pandas as pd
import os

def chemical(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path)
    
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

if __name__ == "__main__":
    chemical('chem.xlsx')