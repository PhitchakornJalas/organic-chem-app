import pandas as pd
import os

def chemical(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ หาไฟล์ไม่เจอที่: {file_path}")
        return

    df = pd.read_excel(file_path)
    
    df = df[df.iloc[:, 0] != 'id'] 

    for index, row in df.iterrows():
        c_id = row.iloc[0]
        IUPAC = row.iloc[1]
        molecularFormula = row.iloc[2]
        
        print(f'(c{c_id}:Chemical {{IUPAC: "{IUPAC}", molecularFormula: "{molecularFormula}"}}),')

    for index, row in df.iterrows():
        c_id = row.iloc[0]
        f_id = row.iloc[3]
        
        print(f'(c{c_id})-[:TYPE_OF]->(f{f_id}),')

if __name__ == "__main__":
    chemical('chem.xlsx')