## FunctionalGroup
MATCH (f:FunctionalGroup)<br>
DETACH DELETE f<br><br>
CREATE<br>
(f1:FunctionalGroup {name_en: "Alkane", name_th: "แอลเคน", formula: "-", molecularFormula: "CnH2n+2", groupName: "พันธะเดี่ยว", image: "Alkane.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f2:FunctionalGroup {name_en: "Alkene", name_th: "แอลคีน", formula: "-", molecularFormula: "CnH2n", groupName: "พันธะคู่", image: "Alkene.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f3:FunctionalGroup {name_en: "Alkyne", name_th: "แอลไคน์", formula: "-", molecularFormula: "CnH2n-2", groupName: "พันธะสาม", image: "Alkyne.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f4:FunctionalGroup {name_en: "Aromatic", name_th: "อะโรมาติก", formula: "-", molecularFormula: "-", groupName: "พันธะเดี่ยวสลับกับพันธะคู่และมีลักษณะเป็นวงกลม", image: "Aromatic.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f5:FunctionalGroup {name_en: "Alcohol", name_th: "แอลกอฮอล์", formula: "R-OH", molecularFormula: "CnH2n+2O", groupName: "ไฮดรอกซิล", image: "Alcohol.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f6:FunctionalGroup {name_en: "Ether", name_th: "อีเทอร์", formula: "R-O-R’", molecularFormula: "CnH2n+2O", groupName: "แอลคอกซี", image: "Ether.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f7:FunctionalGroup {name_en: "Aldehyde", name_th: "แอลดีไฮด์", formula: "R-CHO", molecularFormula: "CnH2nO", groupName: "คาร์บอกซาลดีไฮด์", image: "Aldehyde.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f8:FunctionalGroup {name_en: "Ketone", name_th: "คีโตน", formula: "R-CO-R’", molecularFormula: "CnH2nO", groupName: "คาร์บอนิล", image: "Ketone.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f9:FunctionalGroup {name_en: "Carboxylic acid", name_th: "กรดคาร์บอกซิลิก", formula: "R-COOH", molecularFormula: "CnH2nO2", groupName: "คาร์บอกซิล", image: "Carboxylic_acid.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f10:FunctionalGroup {name_en: "Ester", name_th: "เอสเทอร์", formula: "R-COO-R’", molecularFormula: "CnH2nO2", groupName: "แอลคอกซีคาร์บอกนิล", image: "Ester.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f11:FunctionalGroup {name_en: "Amine", name_th: "เอมีน", formula: "R-NH2", molecularFormula: "CnH2n+3N", groupName: "อะมิโน", image: "Amine.png", createdAt: datetime({timezone: '+07:00'})}),<br>
(f12:FunctionalGroup {name_en: "Amide", name_th: "เอไมด์", formula: "R-CONH2", molecularFormula: "CnH2n+1NO", groupName: "เอไมด์", image: "Amide.png", createdAt: datetime({timezone: '+07:00'})})<br>
## ProductItem

## Chemical
MATCH (c:Chemical)<br>
DETACH DELETE c<br><br>
CREATE<br>
(c1:Chemical {IUPAC: "Methane", molecularFormula: "CH₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c2:Chemical {IUPAC: "Ethane", molecularFormula: "C₂H₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c3:Chemical {IUPAC: "Propane", molecularFormula: "C₃H₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c4:Chemical {IUPAC: "Butane", molecularFormula: "C₄H₁₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c5:Chemical {IUPAC: "Pentane", molecularFormula: "C₅H₁₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c6:Chemical {IUPAC: "Hexane", molecularFormula: "C₆H₁₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c7:Chemical {IUPAC: "Heptane", molecularFormula: "C₇H₁₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c8:Chemical {IUPAC: "Octane", molecularFormula: "C₈H₁₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c9:Chemical {IUPAC: "Nonane", molecularFormula: "C₉H₂₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c10:Chemical {IUPAC: "Decane", molecularFormula: "C₁₀H₂₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c11:Chemical {IUPAC: "Undecane", molecularFormula: "C₁₁H₂₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c12:Chemical {IUPAC: "Dodecane", molecularFormula: "C₁₂H₂₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c13:Chemical {IUPAC: "Bromomethane", molecularFormula: "CH₃Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c14:Chemical {IUPAC: "Bromoethane", molecularFormula: "C₂H₅Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c15:Chemical {IUPAC: "2-Bromopropane", molecularFormula: "C₃H₇Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c16:Chemical {IUPAC: "2-Bromobutane", molecularFormula: "C₄H₉Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c17:Chemical {IUPAC: "2-Bromopentane", molecularFormula: "C₅H₁₁Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c18:Chemical {IUPAC: "2-Bromohexane", molecularFormula: "C₆H₁₃Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c19:Chemical {IUPAC: "2-Bromoheptane", molecularFormula: "C₇H₁₅Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c20:Chemical {IUPAC: "2-Bromooctane", molecularFormula: "C₈H₁₇Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c21:Chemical {IUPAC: "2-Bromononane", molecularFormula: "C₉H₁₉Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c22:Chemical {IUPAC: "2-Bromodecane", molecularFormula: "C₁₀H₂₁Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c23:Chemical {IUPAC: "2-Bromoundecane", molecularFormula: "C₁₁H₂₃Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c24:Chemical {IUPAC: "2-Bromododecane", molecularFormula: "C₁₂H₂₅Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c25:Chemical {IUPAC: "1,2-Dibromoethane", molecularFormula: "C₂H₄Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c26:Chemical {IUPAC: "1,2-Dibromopropane", molecularFormula: "C₃H₆Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c27:Chemical {IUPAC: "1,2-Dibromobutane", molecularFormula: "C₄H₈Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c28:Chemical {IUPAC: "1,2-Dibromopentane", molecularFormula: "C₅H₁₀Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c29:Chemical {IUPAC: "1,2-Dibromohexane", molecularFormula: "C₆H₁₂Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c30:Chemical {IUPAC: "1,2-Dibromoheptane", molecularFormula: "C₇H₁₄Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c31:Chemical {IUPAC: "1,2-Dibromooctane", molecularFormula: "C₈H₁₆Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c32:Chemical {IUPAC: "1,2-Dibromononane", molecularFormula: "C₉H₁₈Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c33:Chemical {IUPAC: "1,2-Dibromodecane", molecularFormula: "C₁₀H₂₀Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c34:Chemical {IUPAC: "1,2-Dibromoundecane", molecularFormula: "C₁₁H₂₂Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c35:Chemical {IUPAC: "1,2-Dibromododecane", molecularFormula: "C₁₂H₂₄Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c36:Chemical {IUPAC: "1,1,2,2-Tetrabromoethane", molecularFormula: "C₂H₂Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c37:Chemical {IUPAC: "1,1,2,2-Tetrabromopropane", molecularFormula: "C₃H₄Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c38:Chemical {IUPAC: "1,1,2,2-Tetrabromobutane", molecularFormula: "C₄H₆Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c39:Chemical {IUPAC: "1,1,2,2-Tetrabromopentane", molecularFormula: "C₅H₈Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c40:Chemical {IUPAC: "1,1,2,2-Tetrabromohexane", molecularFormula: "C₆H₁₀Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c41:Chemical {IUPAC: "1,1,2,2-Tetrabromoheptane", molecularFormula: "C₇H₁₂Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c42:Chemical {IUPAC: "1,1,2,2-Tetrabromooctane", molecularFormula: "C₈H₁₄Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c43:Chemical {IUPAC: "1,1,2,2-Tetrabromononane", molecularFormula: "C₉H₁₆Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c44:Chemical {IUPAC: "1,1,2,2-Tetrabromodecane", molecularFormula: "C₁₀H₁₈Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c45:Chemical {IUPAC: "1,1,2,2-Tetrabromoundecane", molecularFormula: "C₁₁H₂₀Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c46:Chemical {IUPAC: "1,1,2,2-Tetrabromododecane", molecularFormula: "C₁₂H₂₂Br₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c47:Chemical {IUPAC: "1,2-Dibromoethene", molecularFormula: "C₂H₂Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c48:Chemical {IUPAC: "1,2-Dibromopropene", molecularFormula: "C₃H₄Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c49:Chemical {IUPAC: "1,2-Dibromobut-1-ene", molecularFormula: "C₄H₆Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c50:Chemical {IUPAC: "1,2-Dibromopent-1-ene", molecularFormula: "C₅H₈Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c51:Chemical {IUPAC: "1,2-Dibromohex-1-ene", molecularFormula: "C₆H₁₀Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c52:Chemical {IUPAC: "1,2-Dibromohept-1-ene", molecularFormula: "C₇H₁₂Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c53:Chemical {IUPAC: "1,2-Dibromooct-1-ene", molecularFormula: "C₈H₁₄Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c54:Chemical {IUPAC: "1,2-Dibromonon-1-ene", molecularFormula: "C₉H₁₆Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c55:Chemical {IUPAC: "1,2-Dibromodec-1-ene", molecularFormula: "C₁₀H₁₈Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c56:Chemical {IUPAC: "1,2-Dibromoundec-1-ene", molecularFormula: "C₁₁H₂₀Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c57:Chemical {IUPAC: "1,2-Dibromododec-1-ene", molecularFormula: "C₁₂H₂₂Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c58:Chemical {IUPAC: "Ethene", molecularFormula: "C₂H₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c59:Chemical {IUPAC: "Propene", molecularFormula: "C₃H₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c60:Chemical {IUPAC: "Butene", molecularFormula: "C₄H₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c61:Chemical {IUPAC: "Pentene", molecularFormula: "C₅H₁₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c62:Chemical {IUPAC: "Hexene", molecularFormula: "C₆H₁₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c63:Chemical {IUPAC: "Heptene", molecularFormula: "C₇H₁₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c64:Chemical {IUPAC: "Octene", molecularFormula: "C₈H₁₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c65:Chemical {IUPAC: "Nonene", molecularFormula: "C₉H₁₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c66:Chemical {IUPAC: "Decene", molecularFormula: "C₁₀H₂₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c67:Chemical {IUPAC: "Undecene", molecularFormula: "C₁₁H₂₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c68:Chemical {IUPAC: "Dodecene", molecularFormula: "C₁₂H₂₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c69:Chemical {IUPAC: "Ethyne", molecularFormula: "C₂H₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c70:Chemical {IUPAC: "Propyne", molecularFormula: "C₃H₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c71:Chemical {IUPAC: "Butyne", molecularFormula: "C₄H₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c72:Chemical {IUPAC: "Pentyne", molecularFormula: "C₅H₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c73:Chemical {IUPAC: "Hexyne", molecularFormula: "C₆H₁₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c74:Chemical {IUPAC: "Heptyne", molecularFormula: "C₇H₁₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c75:Chemical {IUPAC: "Octyne", molecularFormula: "C₈H₁₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c76:Chemical {IUPAC: "Nonyne", molecularFormula: "C₉H₁₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c77:Chemical {IUPAC: "Decyne", molecularFormula: "C₁₀H₁₈", createdAt: datetime({timezone: '+07:00'})}),<br>
(c78:Chemical {IUPAC: "Undecyne", molecularFormula: "C₁₁H₂₀", createdAt: datetime({timezone: '+07:00'})}),<br>
(c79:Chemical {IUPAC: "Dodecyne", molecularFormula: "C₁₂H₂₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c80:Chemical {IUPAC: "Benzene", molecularFormula: "C₆H₆", createdAt: datetime({timezone: '+07:00'})}),<br>
(c81:Chemical {IUPAC: "Bromobenzene ", molecularFormula: "C₆H₅Br", createdAt: datetime({timezone: '+07:00'})}),<br>
(c82:Chemical {IUPAC: "Methanol", molecularFormula: "CH₄O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c83:Chemical {IUPAC: "Ethanol", molecularFormula: "C₂H₆O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c84:Chemical {IUPAC: "Propan-1-ol", molecularFormula: "C₃H₈O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c85:Chemical {IUPAC: "Butan-1-ol", molecularFormula: "C₄H₁₀O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c86:Chemical {IUPAC: "Pentan-1-ol", molecularFormula: "C₅H₁₂O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c87:Chemical {IUPAC: "Hexan-1-ol", molecularFormula: "C₆H₁₄O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c88:Chemical {IUPAC: "Heptan-1-ol", molecularFormula: "C₇H₁₆O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c89:Chemical {IUPAC: "Octan-1-ol", molecularFormula: "C₈H₁₈O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c90:Chemical {IUPAC: "Nonan-1-ol", molecularFormula: "C₉H₂₀O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c91:Chemical {IUPAC: "Decan-1-ol", molecularFormula: "C₁₀H₂₂O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c92:Chemical {IUPAC: "Undecan-1-ol", molecularFormula: "C₁₁H₂₄O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c93:Chemical {IUPAC: "Dodecan-1-ol", molecularFormula: "C₁₂H₂₆O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c94:Chemical {IUPAC: "Ethane-1,2-diol", molecularFormula: "C₂H₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c95:Chemical {IUPAC: "Propane-1,2-diol", molecularFormula: "C₃H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c96:Chemical {IUPAC: "Butane-1,2-diol", molecularFormula: "C₄H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c97:Chemical {IUPAC: "Pentane-1,2-diol", molecularFormula: "C₅H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c98:Chemical {IUPAC: "Hexane-1,2-diol", molecularFormula: "C₆H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c99:Chemical {IUPAC: "Heptane-1,2-diol", molecularFormula: "C₇H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c100:Chemical {IUPAC: "Octane-1,2-diol", molecularFormula: "C₈H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c101:Chemical {IUPAC: "Nonane-1,2-diol", molecularFormula: "C₉H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c102:Chemical {IUPAC: "Decane-1,2-diol", molecularFormula: "C₁₀H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c103:Chemical {IUPAC: "Undecane-1,2-diol", molecularFormula: "C₁₁H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c104:Chemical {IUPAC: "Dodecane-1,2-diol", molecularFormula: "C₁₂H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c105:Chemical {IUPAC: "Butane-2,3-dione", molecularFormula: "C₄H₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c106:Chemical {IUPAC: "Pentane-2,3-dione", molecularFormula: "C₅H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c107:Chemical {IUPAC: "Hexane-2,3-dione", molecularFormula: "C₆H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c108:Chemical {IUPAC: "Heptane-2,3-dione", molecularFormula: "C₇H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c109:Chemical {IUPAC: "Octane-2,3-dione", molecularFormula: "C₈H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c110:Chemical {IUPAC: "Methanoic acid", molecularFormula: "CH₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c111:Chemical {IUPAC: "Ethanoic acid", molecularFormula: "C₂H₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c112:Chemical {IUPAC: "Propanoic acid", molecularFormula: "C₃H₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c113:Chemical {IUPAC: "Butanoic acid", molecularFormula: "C₄H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c114:Chemical {IUPAC: "Pentanoic acid", molecularFormula: "C₅H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c115:Chemical {IUPAC: "Hexanoic acid", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c116:Chemical {IUPAC: "Heptanoic acid", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c117:Chemical {IUPAC: "Octanoic acid", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c118:Chemical {IUPAC: "Nonanoic acid", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c119:Chemical {IUPAC: "Decanoic acid", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c120:Chemical {IUPAC: "Undecanoic acid", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c121:Chemical {IUPAC: "Dodecanoic acid", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c122:Chemical {IUPAC: "Methyl methanoate", molecularFormula: "C₂H₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c123:Chemical {IUPAC: "Methyl ethanoate", molecularFormula: "C₃H₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c124:Chemical {IUPAC: "Methyl propanoate", molecularFormula: "C₄H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c125:Chemical {IUPAC: "Methyl butanoate", molecularFormula: "C₅H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c126:Chemical {IUPAC: "Methyl pentanoate", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c127:Chemical {IUPAC: "Methyl hexanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c128:Chemical {IUPAC: "Methyl heptanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c129:Chemical {IUPAC: "Methyl octanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c130:Chemical {IUPAC: "Methyl nonanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c131:Chemical {IUPAC: "Methyl decanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c132:Chemical {IUPAC: "Methyl undecanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c133:Chemical {IUPAC: "Methyl dodecanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c134:Chemical {IUPAC: "Ethyl methanoate", molecularFormula: "C₃H₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c135:Chemical {IUPAC: "Ethyl ethanoate", molecularFormula: "C₄H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c136:Chemical {IUPAC: "Ethyl propanoate", molecularFormula: "C₅H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c137:Chemical {IUPAC: "Ethyl butanoate", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c138:Chemical {IUPAC: "Ethyl pentanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c139:Chemical {IUPAC: "Ethyl hexanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c140:Chemical {IUPAC: "Ethyl heptanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c141:Chemical {IUPAC: "Ethyl octanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c142:Chemical {IUPAC: "Ethyl nonanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c143:Chemical {IUPAC: "Ethyl decanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c144:Chemical {IUPAC: "Ethyl undecanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c145:Chemical {IUPAC: "Ethyl dodecanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c146:Chemical {IUPAC: "Propyl methanoate", molecularFormula: "C₄H₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c147:Chemical {IUPAC: "Propyl ethanoate", molecularFormula: "C₅H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c148:Chemical {IUPAC: "Propyl propanoate", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c149:Chemical {IUPAC: "Propyl butanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c150:Chemical {IUPAC: "Propyl pentanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c151:Chemical {IUPAC: "Propyl hexanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c152:Chemical {IUPAC: "Propyl heptanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c153:Chemical {IUPAC: "Propyl octanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c154:Chemical {IUPAC: "Propyl nonanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c155:Chemical {IUPAC: "Propyl decanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c156:Chemical {IUPAC: "Propyl undecanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c157:Chemical {IUPAC: "Propyl dodecanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c158:Chemical {IUPAC: "Butyl methanoate", molecularFormula: "C₅H₁₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c159:Chemical {IUPAC: "Butyl ethanoate", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c160:Chemical {IUPAC: "Butyl propanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c161:Chemical {IUPAC: "Butyl butanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c162:Chemical {IUPAC: "Butyl pentanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c163:Chemical {IUPAC: "Butyl hexanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c164:Chemical {IUPAC: "Butyl heptanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c165:Chemical {IUPAC: "Butyl octanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c166:Chemical {IUPAC: "Butyl nonanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c167:Chemical {IUPAC: "Butyl decanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c168:Chemical {IUPAC: "Butyl undecanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c169:Chemical {IUPAC: "Butyl dodecanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c170:Chemical {IUPAC: "Pentyl methanoate", molecularFormula: "C₆H₁₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c171:Chemical {IUPAC: "Pentyl ethanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c172:Chemical {IUPAC: "Pentyl propanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c173:Chemical {IUPAC: "Pentyl butanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c174:Chemical {IUPAC: "Pentyl pentanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c175:Chemical {IUPAC: "Pentyl hexanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c176:Chemical {IUPAC: "Pentyl heptanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c177:Chemical {IUPAC: "Pentyl octanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c178:Chemical {IUPAC: "Pentyl nonanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c179:Chemical {IUPAC: "Pentyl decanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c180:Chemical {IUPAC: "Pentyl undecanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c181:Chemical {IUPAC: "Pentyl dodecanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c182:Chemical {IUPAC: "Hexyl methanoate", molecularFormula: "C₇H₁₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c183:Chemical {IUPAC: "Hexyl ethanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c184:Chemical {IUPAC: "Hexyl propanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c185:Chemical {IUPAC: "Hexyl butanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c186:Chemical {IUPAC: "Hexyl pentanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c187:Chemical {IUPAC: "Hexyl hexanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c188:Chemical {IUPAC: "Hexyl heptanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c189:Chemical {IUPAC: "Hexyl octanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c190:Chemical {IUPAC: "Hexyl nonanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c191:Chemical {IUPAC: "Hexyl decanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c192:Chemical {IUPAC: "Hexyl undecanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c193:Chemical {IUPAC: "Hexyl dodecanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c194:Chemical {IUPAC: "Heptyl methanoate", molecularFormula: "C₈H₁₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c195:Chemical {IUPAC: "Heptyl ethanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c196:Chemical {IUPAC: "Heptyl propanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c197:Chemical {IUPAC: "Heptyl butanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c198:Chemical {IUPAC: "Heptyl pentanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c199:Chemical {IUPAC: "Heptyl hexanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c200:Chemical {IUPAC: "Heptyl heptanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c201:Chemical {IUPAC: "Heptyl octanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c202:Chemical {IUPAC: "Heptyl nonanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c203:Chemical {IUPAC: "Heptyl decanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c204:Chemical {IUPAC: "Heptyl undecanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c205:Chemical {IUPAC: "Heptyl dodecanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c206:Chemical {IUPAC: "Octyl methanoate", molecularFormula: "C₉H₁₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c207:Chemical {IUPAC: "Octyl ethanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c208:Chemical {IUPAC: "Octyl propanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c209:Chemical {IUPAC: "Octyl butanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c210:Chemical {IUPAC: "Octyl pentanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c211:Chemical {IUPAC: "Octyl hexanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c212:Chemical {IUPAC: "Octyl heptanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c213:Chemical {IUPAC: "Octyl octanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c214:Chemical {IUPAC: "Octyl nonanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c215:Chemical {IUPAC: "Octyl decanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c216:Chemical {IUPAC: "Octyl undecanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c217:Chemical {IUPAC: "Octyl dodecanoate", molecularFormula: "C₂₀H₄₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c218:Chemical {IUPAC: "Nonyl methanoate", molecularFormula: "C₁₀H₂₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c219:Chemical {IUPAC: "Nonyl ethanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c220:Chemical {IUPAC: "Nonyl propanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c221:Chemical {IUPAC: "Nonyl butanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c222:Chemical {IUPAC: "Nonyl pentanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c223:Chemical {IUPAC: "Nonyl hexanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c224:Chemical {IUPAC: "Nonyl heptanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c225:Chemical {IUPAC: "Nonyl octanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c226:Chemical {IUPAC: "Nonyl nonanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c227:Chemical {IUPAC: "Nonyl decanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c228:Chemical {IUPAC: "Nonyl undecanoate", molecularFormula: "C₂₀H₄₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c229:Chemical {IUPAC: "Nonyl dodecanoate", molecularFormula: "C₂₁H₄₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c230:Chemical {IUPAC: "Decyl methanoate", molecularFormula: "C₁₁H₂₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c231:Chemical {IUPAC: "Decyl ethanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c232:Chemical {IUPAC: "Decyl propanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c233:Chemical {IUPAC: "Decyl butanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c234:Chemical {IUPAC: "Decyl pentanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c235:Chemical {IUPAC: "Decyl hexanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c236:Chemical {IUPAC: "Decyl heptanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c237:Chemical {IUPAC: "Decyl octanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c238:Chemical {IUPAC: "Decyl nonanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c239:Chemical {IUPAC: "Decyl decanoate", molecularFormula: "C₂₀H₄₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c240:Chemical {IUPAC: "Decyl undecanoate", molecularFormula: "C₂₁H₄₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c241:Chemical {IUPAC: "Decyl dodecanoate", molecularFormula: "C₂₂H₄₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c242:Chemical {IUPAC: "Undecyl methanoate", molecularFormula: "C₁₂H₂₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c243:Chemical {IUPAC: "Undecyl ethanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c244:Chemical {IUPAC: "Undecyl propanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c245:Chemical {IUPAC: "Undecyl butanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c246:Chemical {IUPAC: "Undecyl pentanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c247:Chemical {IUPAC: "Undecyl hexanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c248:Chemical {IUPAC: "Undecyl heptanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c249:Chemical {IUPAC: "Undecyl octanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c250:Chemical {IUPAC: "Undecyl nonanoate", molecularFormula: "C₂₀H₄₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c251:Chemical {IUPAC: "Undecyl decanoate", molecularFormula: "C₂₁H₄₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c252:Chemical {IUPAC: "Undecyl undecanoate", molecularFormula: "C₂₂H₄₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c253:Chemical {IUPAC: "Undecyl dodecanoate", molecularFormula: "C₂₃H₄₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c254:Chemical {IUPAC: "Dodecyl methanoate", molecularFormula: "C₁₃H₂₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c255:Chemical {IUPAC: "Dodecyl ethanoate", molecularFormula: "C₁₄H₂₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c256:Chemical {IUPAC: "Dodecyl propanoate", molecularFormula: "C₁₅H₃₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c257:Chemical {IUPAC: "Dodecyl butanoate", molecularFormula: "C₁₆H₃₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c258:Chemical {IUPAC: "Dodecyl pentanoate", molecularFormula: "C₁₇H₃₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c259:Chemical {IUPAC: "Dodecyl hexanoate", molecularFormula: "C₁₈H₃₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c260:Chemical {IUPAC: "Dodecyl heptanoate", molecularFormula: "C₁₉H₃₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c261:Chemical {IUPAC: "Dodecyl octanoate", molecularFormula: "C₂₀H₄₀O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c262:Chemical {IUPAC: "Dodecyl nonanoate", molecularFormula: "C₂₁H₄₂O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c263:Chemical {IUPAC: "Dodecyl decanoate", molecularFormula: "C₂₂H₄₄O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c264:Chemical {IUPAC: "Dodecyl undecanoate", molecularFormula: "C₂₃H₄₆O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c265:Chemical {IUPAC: "Dodecyl dodecanoate", molecularFormula: "C₂₄H₄₈O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c266:Chemical {IUPAC: "Methanamine", molecularFormula: "CH₅N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c267:Chemical {IUPAC: "Ethanamine", molecularFormula: "C₂H₇N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c268:Chemical {IUPAC: "Propan-1-amine", molecularFormula: "C₃H₉N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c269:Chemical {IUPAC: "Butan-1-amine", molecularFormula: "C₄H₁₁N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c270:Chemical {IUPAC: "Pentan-1-amine", molecularFormula: "C₅H₁₃N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c271:Chemical {IUPAC: "Hexan-1-amine", molecularFormula: "C₆H₁₅N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c272:Chemical {IUPAC: "Heptan-1-amine", molecularFormula: "C₇H₁₇N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c273:Chemical {IUPAC: "Octan-1-amine", molecularFormula: "C₈H₁₉N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c274:Chemical {IUPAC: "Nonan-1-amine", molecularFormula: "C₉H₂₁N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c275:Chemical {IUPAC: "Decan-1-amine", molecularFormula: "C₁₀H₂₃N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c276:Chemical {IUPAC: "Undecan-1-amine", molecularFormula: "C₁₁H₂₅N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c277:Chemical {IUPAC: "Dodecan-1-amine", molecularFormula: "C₁₂H₂₇N", createdAt: datetime({timezone: '+07:00'})}),<br>
(c278:Chemical {IUPAC: "Methanamide", molecularFormula: "CH₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c279:Chemical {IUPAC: "Ethanamide", molecularFormula: "C₂H₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c280:Chemical {IUPAC: "Propanamide", molecularFormula: "C₃H₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c281:Chemical {IUPAC: "Butanamide", molecularFormula: "C₄H₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c282:Chemical {IUPAC: "Pentanamide", molecularFormula: "C₅H₁₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c283:Chemical {IUPAC: "Hexanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c284:Chemical {IUPAC: "Heptanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c285:Chemical {IUPAC: "Octanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c286:Chemical {IUPAC: "Nonanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c287:Chemical {IUPAC: "Decanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c288:Chemical {IUPAC: "Undecanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c289:Chemical {IUPAC: "Dodecanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c290:Chemical {IUPAC: "N-methylmethanamide", molecularFormula: "C₂H₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c291:Chemical {IUPAC: "N-ethylmethanamide", molecularFormula: "C₃H₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c292:Chemical {IUPAC: "N-propylmethanamide", molecularFormula: "C₄H₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c293:Chemical {IUPAC: "N-butylmethanamide", molecularFormula: "C₅H₁₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c294:Chemical {IUPAC: "N-pentylmethanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c295:Chemical {IUPAC: "N-hexylmethanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c296:Chemical {IUPAC: "N-heptylmethanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c297:Chemical {IUPAC: "N-octylmethanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c298:Chemical {IUPAC: "N-nonylmethanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c299:Chemical {IUPAC: "N-decylmethanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c300:Chemical {IUPAC: "N-undecylmethanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c301:Chemical {IUPAC: "N-dodecylmethanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c302:Chemical {IUPAC: "N-methylethanamide", molecularFormula: "C₃H₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c303:Chemical {IUPAC: "N-ethylethanamide", molecularFormula: "C₄H₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c304:Chemical {IUPAC: "N-propylethanamide", molecularFormula: "C₅H₁₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c305:Chemical {IUPAC: "N-butylethanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c306:Chemical {IUPAC: "N-pentylethanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c307:Chemical {IUPAC: "N-hexylethanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c308:Chemical {IUPAC: "N-heptylethanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c309:Chemical {IUPAC: "N-octylethanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c310:Chemical {IUPAC: "N-nonylethanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c311:Chemical {IUPAC: "N-decylethanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c312:Chemical {IUPAC: "N-undecylethanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c313:Chemical {IUPAC: "N-dodecylethanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c314:Chemical {IUPAC: "N-methylpropanamide", molecularFormula: "C₄H₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c315:Chemical {IUPAC: "N-ethylpropanamide", molecularFormula: "C₅H₁₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c316:Chemical {IUPAC: "N-propylpropanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c317:Chemical {IUPAC: "N-butylpropanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c318:Chemical {IUPAC: "N-pentylpropanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c319:Chemical {IUPAC: "N-hexylpropanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c320:Chemical {IUPAC: "N-heptylpropanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c321:Chemical {IUPAC: "N-octylpropanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c322:Chemical {IUPAC: "N-nonylpropanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c323:Chemical {IUPAC: "N-decylpropanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c324:Chemical {IUPAC: "N-undecylpropanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c325:Chemical {IUPAC: "N-dodecylpropanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c326:Chemical {IUPAC: "N-methylbutanamide", molecularFormula: "C₅H₁₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c327:Chemical {IUPAC: "N-ethylbutanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c328:Chemical {IUPAC: "N-propylbutanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c329:Chemical {IUPAC: "N-butylbutanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c330:Chemical {IUPAC: "N-pentylbutanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c331:Chemical {IUPAC: "N-hexylbutanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c332:Chemical {IUPAC: "N-heptylbutanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c333:Chemical {IUPAC: "N-octylbutanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c334:Chemical {IUPAC: "N-nonylbutanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c335:Chemical {IUPAC: "N-decylbutanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c336:Chemical {IUPAC: "N-undecylbutanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c337:Chemical {IUPAC: "N-dodecylbutanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c338:Chemical {IUPAC: "N-methylpentanamide", molecularFormula: "C₆H₁₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c339:Chemical {IUPAC: "N-ethylpentanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c340:Chemical {IUPAC: "N-propylpentanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c341:Chemical {IUPAC: "N-butylpentanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c342:Chemical {IUPAC: "N-pentylpentanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c343:Chemical {IUPAC: "N-hexylpentanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c344:Chemical {IUPAC: "N-heptylpentanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c345:Chemical {IUPAC: "N-octylpentanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c346:Chemical {IUPAC: "N-nonylpentanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c347:Chemical {IUPAC: "N-decylpentanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c348:Chemical {IUPAC: "N-undecylpentanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c349:Chemical {IUPAC: "N-dodecylpentanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c350:Chemical {IUPAC: "N-methylhexanamide", molecularFormula: "C₇H₁₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c351:Chemical {IUPAC: "N-ethylhexanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c352:Chemical {IUPAC: "N-propylhexanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c353:Chemical {IUPAC: "N-butylhexanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c354:Chemical {IUPAC: "N-pentylhexanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c355:Chemical {IUPAC: "N-hexylhexanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c356:Chemical {IUPAC: "N-heptylhexanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c357:Chemical {IUPAC: "N-octylhexanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c358:Chemical {IUPAC: "N-nonylhexanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c359:Chemical {IUPAC: "N-decylhexanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c360:Chemical {IUPAC: "N-undecylhexanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c361:Chemical {IUPAC: "N-dodecylhexanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c362:Chemical {IUPAC: "N-methylheptanamide", molecularFormula: "C₈H₁₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c363:Chemical {IUPAC: "N-ethylheptanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c364:Chemical {IUPAC: "N-propylheptanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c365:Chemical {IUPAC: "N-butylheptanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c366:Chemical {IUPAC: "N-pentylheptanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c367:Chemical {IUPAC: "N-hexylheptanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c368:Chemical {IUPAC: "N-heptylheptanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c369:Chemical {IUPAC: "N-octylheptanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c370:Chemical {IUPAC: "N-nonylheptanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c371:Chemical {IUPAC: "N-decylheptanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c372:Chemical {IUPAC: "N-undecylheptanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c373:Chemical {IUPAC: "N-dodecylheptanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c374:Chemical {IUPAC: "N-methyloctanamide", molecularFormula: "C₉H₁₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c375:Chemical {IUPAC: "N-ethyloctanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c376:Chemical {IUPAC: "N-propyloctanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c377:Chemical {IUPAC: "N-butyloctanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c378:Chemical {IUPAC: "N-pentyloctanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c379:Chemical {IUPAC: "N-hexyloctanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c380:Chemical {IUPAC: "N-heptyloctanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c381:Chemical {IUPAC: "N-octyloctanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c382:Chemical {IUPAC: "N-nonyloctanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c383:Chemical {IUPAC: "N-decyloctanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c384:Chemical {IUPAC: "N-undecyloctanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c385:Chemical {IUPAC: "N-dodecyloctanamide", molecularFormula: "C₂₀H₄₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c386:Chemical {IUPAC: "N-methylnonanamide", molecularFormula: "C₁₀H₂₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c387:Chemical {IUPAC: "N-ethylnonanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c388:Chemical {IUPAC: "N-propylnonanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c389:Chemical {IUPAC: "N-butylnonanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c390:Chemical {IUPAC: "N-pentylnonanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c391:Chemical {IUPAC: "N-hexylnonanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c392:Chemical {IUPAC: "N-heptylnonanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c393:Chemical {IUPAC: "N-octylnonanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c394:Chemical {IUPAC: "N-nonylnonanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c395:Chemical {IUPAC: "N-decylnonanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c396:Chemical {IUPAC: "N-undecylnonanamide", molecularFormula: "C₂₀H₄₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c397:Chemical {IUPAC: "N-dodecylnonanamide", molecularFormula: "C₂₁H₄₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c398:Chemical {IUPAC: "N-methyldecanamide", molecularFormula: "C₁₁H₂₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c399:Chemical {IUPAC: "N-ethyldecanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c400:Chemical {IUPAC: "N-propyldecanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c401:Chemical {IUPAC: "N-butyldecanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c402:Chemical {IUPAC: "N-pentyldecanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c403:Chemical {IUPAC: "N-hexyldecanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c404:Chemical {IUPAC: "N-heptyldecanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c405:Chemical {IUPAC: "N-octyldecanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c406:Chemical {IUPAC: "N-nonyldecanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c407:Chemical {IUPAC: "N-decyldecanamide", molecularFormula: "C₂₀H₄₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c408:Chemical {IUPAC: "N-undecyldecanamide", molecularFormula: "C₂₁H₄₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c409:Chemical {IUPAC: "N-dodecyldecanamide", molecularFormula: "C₂₂H₄₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c410:Chemical {IUPAC: "N-methylundecanamide", molecularFormula: "C₁₂H₂₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c411:Chemical {IUPAC: "N-ethylundecanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c412:Chemical {IUPAC: "N-propylundecanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c413:Chemical {IUPAC: "N-butylundecanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c414:Chemical {IUPAC: "N-pentylundecanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c415:Chemical {IUPAC: "N-hexylundecanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c416:Chemical {IUPAC: "N-heptylundecanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c417:Chemical {IUPAC: "N-octylundecanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c418:Chemical {IUPAC: "N-nonylundecanamide", molecularFormula: "C₂₀H₄₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c419:Chemical {IUPAC: "N-decylundecanamide", molecularFormula: "C₂₁H₄₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c420:Chemical {IUPAC: "N-undecylundecanamide", molecularFormula: "C₂₂H₄₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c421:Chemical {IUPAC: "N-dodecylundecanamide", molecularFormula: "C₂₃H₄₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c422:Chemical {IUPAC: "N-methyldodecanamide", molecularFormula: "C₁₃H₂₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c423:Chemical {IUPAC: "N-ethyldodecanamide", molecularFormula: "C₁₄H₂₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c424:Chemical {IUPAC: "N-propyldodecanamide", molecularFormula: "C₁₅H₃₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c425:Chemical {IUPAC: "N-butyldodecanamide", molecularFormula: "C₁₆H₃₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c426:Chemical {IUPAC: "N-pentyldodecanamide", molecularFormula: "C₁₇H₃₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c427:Chemical {IUPAC: "N-hexyldodecanamide", molecularFormula: "C₁₈H₃₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c428:Chemical {IUPAC: "N-heptyldodecanamide", molecularFormula: "C₁₉H₃₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c429:Chemical {IUPAC: "N-octyldodecanamide", molecularFormula: "C₂₀H₄₁NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c430:Chemical {IUPAC: "N-nonyldodecanamide", molecularFormula: "C₂₁H₄₃NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c431:Chemical {IUPAC: "N-decyldodecanamide", molecularFormula: "C₂₂H₄₅NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c432:Chemical {IUPAC: "N-undecyldodecanamide", molecularFormula: "C₂₃H₄₇NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c433:Chemical {IUPAC: "N-dodecyldodecanamide", molecularFormula: "C₂₄H₄₉NO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c434:Chemical {IUPAC: "Conc.Sulfuric acid", molecularFormula: "H₂SO₄ ", createdAt: datetime({timezone: '+07:00'})}),<br>
(c435:Chemical {IUPAC: "Dilute sulfuric acid", molecularFormula: "H₂SO₄ ", createdAt: datetime({timezone: '+07:00'})}),<br>
(c436:Chemical {IUPAC: "Water", molecularFormula: "H₂O", createdAt: datetime({timezone: '+07:00'})}),<br>
(c437:Chemical {IUPAC: "sodium hydroxide ", molecularFormula: "NaOH", createdAt: datetime({timezone: '+07:00'})}),<br>
(c438:Chemical {IUPAC: "Sodium methanoate", molecularFormula: "C HNaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c439:Chemical {IUPAC: "Sodium ethanoate", molecularFormula: "C₂H₃NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c440:Chemical {IUPAC: "Sodium propanoate", molecularFormula: "C₃H₅NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c441:Chemical {IUPAC: "Sodium butanoate", molecularFormula: "C₄H₇NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c442:Chemical {IUPAC: "Sodium pentanoate", molecularFormula: "C₅H₉NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c443:Chemical {IUPAC: "Sodium hexanoate", molecularFormula: "C₆H₁₁NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c444:Chemical {IUPAC: "Sodium heptanoate", molecularFormula: "C₇H₁₃NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c445:Chemical {IUPAC: "Sodium octanoate", molecularFormula: "C₈H₁₅NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c446:Chemical {IUPAC: "Sodium nonanoate", molecularFormula: "C₉H₁₇NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c447:Chemical {IUPAC: "Sodium decanoate", molecularFormula: "C₁₀H₁₉NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c448:Chemical {IUPAC: "Sodium undecanoate", molecularFormula: "C₁₁H₂₁NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c449:Chemical {IUPAC: "Sodium dodecanoate", molecularFormula: "C₁₂H₂₃NaO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c450:Chemical {IUPAC: "Ammonia", molecularFormula: "NH₃", createdAt: datetime({timezone: '+07:00'})}),<br>
(c451:Chemical {IUPAC: "Dicyclohexylcarbodiimide (DCC)", molecularFormula: "C13H22N2", createdAt: datetime({timezone: '+07:00'})}),<br>
(c452:Chemical {IUPAC: "Hydrochloric acid", molecularFormula: "HCl", createdAt: datetime({timezone: '+07:00'})}),<br>
(c453:Chemical {IUPAC: "Methanaminium chloride", molecularFormula: "CH₆ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c454:Chemical {IUPAC: "Ethanaminium chloride", molecularFormula: "C₂H₈ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c455:Chemical {IUPAC: "Propan-1-aminium chloride", molecularFormula: "C₃H₁₀ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c456:Chemical {IUPAC: "Butan-1-aminium chloride", molecularFormula: "C₄H₁₂ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c457:Chemical {IUPAC: "Pentan-1-aminium chloride", molecularFormula: "C₅H₁₄ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c458:Chemical {IUPAC: "Hexan-1-aminium chloride", molecularFormula: "C₆H₁₆ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c459:Chemical {IUPAC: "Heptan-1-aminium chloride", molecularFormula: "C₇H₁₈ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c460:Chemical {IUPAC: "Octan-1-aminium chloride", molecularFormula: "C₈H₂₀ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c461:Chemical {IUPAC: "Nonan-1-aminium chloride", molecularFormula: "C₉H₂₂ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c462:Chemical {IUPAC: "Decan-1-aminium chloride", molecularFormula: "C₁₀H₂₄ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c463:Chemical {IUPAC: "Undecan-1-aminium chloride", molecularFormula: "C₁₁H₂₆ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c464:Chemical {IUPAC: "Dodecan-1-aminium chloride", molecularFormula: "C₁₂H₂₈ClN", createdAt: datetime({timezone: '+07:00'})}),<br>
(c465:Chemical {IUPAC: "Bromine", molecularFormula: "Br₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c466:Chemical {IUPAC: "Hydrogen bromide", molecularFormula: "HBr", createdAt: datetime({timezone: '+07:00'})}),<br>
(c467:Chemical {IUPAC: "Oxygen", molecularFormula: "O₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c468:Chemical {IUPAC: "Carbon dioxide", molecularFormula: "CO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c469:Chemical {IUPAC: "Carbon monoxide", molecularFormula: "CO", createdAt: datetime({timezone: '+07:00'})}),<br>
(c470:Chemical {IUPAC: "Carbon", molecularFormula: "C", createdAt: datetime({timezone: '+07:00'})}),<br>
(c471:Chemical {IUPAC: "Potassium permanganate", molecularFormula: "KMnO₄", createdAt: datetime({timezone: '+07:00'})}),<br>
(c472:Chemical {IUPAC: "Manganese dioxide ", molecularFormula: "MnO₂", createdAt: datetime({timezone: '+07:00'})}),<br>
(c473:Chemical {IUPAC: "Potassium hydroxide ", molecularFormula: "KOH", createdAt: datetime({timezone: '+07:00'})})<br>

## Chemical TYPE_OF FunctionGroup
MATCH (f:FunctionalGroup {name_en: "Alcohol"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methanol", "Ethanol", "Propan-1-ol", "Butan-1-ol", "Pentan-1-ol", "Hexan-1-ol", "Heptan-1-ol", "Octan-1-ol", "Nonan-1-ol", "Decan-1-ol", "Undecan-1-ol", "Dodecan-1-ol", "Ethane-1,2-diol", "Propane-1,2-diol", "Butane-1,2-diol", "Pentane-1,2-diol", "Hexane-1,2-diol", "Heptane-1,2-diol", "Octane-1,2-diol", "Nonane-1,2-diol", "Decane-1,2-diol", "Undecane-1,2-diol", "Dodecane-1,2-diol"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Alkane"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methane", "Ethane", "Propane", "Butane", "Pentane", "Hexane", "Heptane", "Octane", "Nonane", "Decane", "Undecane", "Dodecane", "Bromomethane", "Bromoethane", "2-Bromopropane", "2-Bromobutane", "2-Bromopentane", "2-Bromohexane", "2-Bromoheptane", "2-Bromooctane", "2-Bromononane", "2-Bromodecane", "2-Bromoundecane", "2-Bromododecane", "1,2-Dibromoethane", "1,2-Dibromopropane", "1,2-Dibromobutane", "1,2-Dibromopentane", "1,2-Dibromohexane", "1,2-Dibromoheptane", "1,2-Dibromooctane", "1,2-Dibromononane", "1,2-Dibromodecane", "1,2-Dibromoundecane", "1,2-Dibromododecane", "1,1,2,2-Tetrabromoethane", "1,1,2,2-Tetrabromopropane", "1,1,2,2-Tetrabromobutane", "1,1,2,2-Tetrabromopentane", "1,1,2,2-Tetrabromohexane", "1,1,2,2-Tetrabromoheptane", "1,1,2,2-Tetrabromooctane", "1,1,2,2-Tetrabromononane", "1,1,2,2-Tetrabromodecane", "1,1,2,2-Tetrabromoundecane", "1,1,2,2-Tetrabromododecane"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Alkene"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["1,2-Dibromoethene", "1,2-Dibromopropene", "1,2-Dibromobut-1-ene", "1,2-Dibromopent-1-ene", "1,2-Dibromohex-1-ene", "1,2-Dibromohept-1-ene", "1,2-Dibromooct-1-ene", "1,2-Dibromonon-1-ene", "1,2-Dibromodec-1-ene", "1,2-Dibromoundec-1-ene", "1,2-Dibromododec-1-ene", "Ethene", "Propene", "Butene", "Pentene", "Hexene", "Heptene", "Octene", "Nonene", "Decene", "Undecene", "Dodecene"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Alkyne"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Ethyne", "Propyne", "Butyne", "Pentyne", "Hexyne", "Heptyne", "Octyne", "Nonyne", "Decyne", "Undecyne", "Dodecyne"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Amide"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methanamide", "Ethanamide", "Propanamide", "Butanamide", "Pentanamide", "Hexanamide", "Heptanamide", "Octanamide", "Nonanamide", "Decanamide", "Undecanamide", "Dodecanamide", "N-methylmethanamide", "N-ethylmethanamide", "N-propylmethanamide", "N-butylmethanamide", "N-pentylmethanamide", "N-hexylmethanamide", "N-heptylmethanamide", "N-octylmethanamide", "N-nonylmethanamide", "N-decylmethanamide", "N-undecylmethanamide", "N-dodecylmethanamide", "N-methylethanamide", "N-ethylethanamide", "N-propylethanamide", "N-butylethanamide", "N-pentylethanamide", "N-hexylethanamide", "N-heptylethanamide", "N-octylethanamide", "N-nonylethanamide", "N-decylethanamide", "N-undecylethanamide", "N-dodecylethanamide", "N-methylpropanamide", "N-ethylpropanamide", "N-propylpropanamide", "N-butylpropanamide", "N-pentylpropanamide", "N-hexylpropanamide", "N-heptylpropanamide", "N-octylpropanamide", "N-nonylpropanamide", "N-decylpropanamide", "N-undecylpropanamide", "N-dodecylpropanamide", "N-methylbutanamide", "N-ethylbutanamide", "N-propylbutanamide", "N-butylbutanamide", "N-pentylbutanamide", "N-hexylbutanamide", "N-heptylbutanamide", "N-octylbutanamide", "N-nonylbutanamide", "N-decylbutanamide", "N-undecylbutanamide", "N-dodecylbutanamide", "N-methylpentanamide", "N-ethylpentanamide", "N-propylpentanamide", "N-butylpentanamide", "N-pentylpentanamide", "N-hexylpentanamide", "N-heptylpentanamide", "N-octylpentanamide", "N-nonylpentanamide", "N-decylpentanamide", "N-undecylpentanamide", "N-dodecylpentanamide", "N-methylhexanamide", "N-ethylhexanamide", "N-propylhexanamide", "N-butylhexanamide", "N-pentylhexanamide", "N-hexylhexanamide", "N-heptylhexanamide", "N-octylhexanamide", "N-nonylhexanamide", "N-decylhexanamide", "N-undecylhexanamide", "N-dodecylhexanamide", "N-methylheptanamide", "N-ethylheptanamide", "N-propylheptanamide", "N-butylheptanamide", "N-pentylheptanamide", "N-hexylheptanamide", "N-heptylheptanamide", "N-octylheptanamide", "N-nonylheptanamide", "N-decylheptanamide", "N-undecylheptanamide", "N-dodecylheptanamide", "N-methyloctanamide", "N-ethyloctanamide", "N-propyloctanamide", "N-butyloctanamide", "N-pentyloctanamide", "N-hexyloctanamide", "N-heptyloctanamide", "N-octyloctanamide", "N-nonyloctanamide", "N-decyloctanamide", "N-undecyloctanamide", "N-dodecyloctanamide", "N-methylnonanamide", "N-ethylnonanamide", "N-propylnonanamide", "N-butylnonanamide", "N-pentylnonanamide", "N-hexylnonanamide", "N-heptylnonanamide", "N-octylnonanamide", "N-nonylnonanamide", "N-decylnonanamide", "N-undecylnonanamide", "N-dodecylnonanamide", "N-methyldecanamide", "N-ethyldecanamide", "N-propyldecanamide", "N-butyldecanamide", "N-pentyldecanamide", "N-hexyldecanamide", "N-heptyldecanamide", "N-octyldecanamide", "N-nonyldecanamide", "N-decyldecanamide", "N-undecyldecanamide", "N-dodecyldecanamide", "N-methylundecanamide", "N-ethylundecanamide", "N-propylundecanamide", "N-butylundecanamide", "N-pentylundecanamide", "N-hexylundecanamide", "N-heptylundecanamide", "N-octylundecanamide", "N-nonylundecanamide", "N-decylundecanamide", "N-undecylundecanamide", "N-dodecylundecanamide", "N-methyldodecanamide", "N-ethyldodecanamide", "N-propyldodecanamide", "N-butyldodecanamide", "N-pentyldodecanamide", "N-hexyldodecanamide", "N-heptyldodecanamide", "N-octyldodecanamide", "N-nonyldodecanamide", "N-decyldodecanamide", "N-undecyldodecanamide", "N-dodecyldodecanamide"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Amine"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methanamine", "Ethanamine", "Propan-1-amine", "Butan-1-amine", "Pentan-1-amine", "Hexan-1-amine", "Heptan-1-amine", "Octan-1-amine", "Nonan-1-amine", "Decan-1-amine", "Undecan-1-amine", "Dodecan-1-amine"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Aromatic"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Benzene", "Bromobenzene "]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Carboxylic_acid"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methanoic acid", "Ethanoic acid", "Propanoic acid", "Butanoic acid", "Pentanoic acid", "Hexanoic acid", "Heptanoic acid", "Octanoic acid", "Nonanoic acid", "Decanoic acid", "Undecanoic acid", "Dodecanoic acid"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Ester"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Methyl methanoate", "Methyl ethanoate", "Methyl propanoate", "Methyl butanoate", "Methyl pentanoate", "Methyl hexanoate", "Methyl heptanoate", "Methyl octanoate", "Methyl nonanoate", "Methyl decanoate", "Methyl undecanoate", "Methyl dodecanoate", "Ethyl methanoate", "Ethyl ethanoate", "Ethyl propanoate", "Ethyl butanoate", "Ethyl pentanoate", "Ethyl hexanoate", "Ethyl heptanoate", "Ethyl octanoate", "Ethyl nonanoate", "Ethyl decanoate", "Ethyl undecanoate", "Ethyl dodecanoate", "Propyl methanoate", "Propyl ethanoate", "Propyl propanoate", "Propyl butanoate", "Propyl pentanoate", "Propyl hexanoate", "Propyl heptanoate", "Propyl octanoate", "Propyl nonanoate", "Propyl decanoate", "Propyl undecanoate", "Propyl dodecanoate", "Butyl methanoate", "Butyl ethanoate", "Butyl propanoate", "Butyl butanoate", "Butyl pentanoate", "Butyl hexanoate", "Butyl heptanoate", "Butyl octanoate", "Butyl nonanoate", "Butyl decanoate", "Butyl undecanoate", "Butyl dodecanoate", "Pentyl methanoate", "Pentyl ethanoate", "Pentyl propanoate", "Pentyl butanoate", "Pentyl pentanoate", "Pentyl hexanoate", "Pentyl heptanoate", "Pentyl octanoate", "Pentyl nonanoate", "Pentyl decanoate", "Pentyl undecanoate", "Pentyl dodecanoate", "Hexyl methanoate", "Hexyl ethanoate", "Hexyl propanoate", "Hexyl butanoate", "Hexyl pentanoate", "Hexyl hexanoate", "Hexyl heptanoate", "Hexyl octanoate", "Hexyl nonanoate", "Hexyl decanoate", "Hexyl undecanoate", "Hexyl dodecanoate", "Heptyl methanoate", "Heptyl ethanoate", "Heptyl propanoate", "Heptyl butanoate", "Heptyl pentanoate", "Heptyl hexanoate", "Heptyl heptanoate", "Heptyl octanoate", "Heptyl nonanoate", "Heptyl decanoate", "Heptyl undecanoate", "Heptyl dodecanoate", "Octyl methanoate", "Octyl ethanoate", "Octyl propanoate", "Octyl butanoate", "Octyl pentanoate", "Octyl hexanoate", "Octyl heptanoate", "Octyl octanoate", "Octyl nonanoate", "Octyl decanoate", "Octyl undecanoate", "Octyl dodecanoate", "Nonyl methanoate", "Nonyl ethanoate", "Nonyl propanoate", "Nonyl butanoate", "Nonyl pentanoate", "Nonyl hexanoate", "Nonyl heptanoate", "Nonyl octanoate", "Nonyl nonanoate", "Nonyl decanoate", "Nonyl undecanoate", "Nonyl dodecanoate", "Decyl methanoate", "Decyl ethanoate", "Decyl propanoate", "Decyl butanoate", "Decyl pentanoate", "Decyl hexanoate", "Decyl heptanoate", "Decyl octanoate", "Decyl nonanoate", "Decyl decanoate", "Decyl undecanoate", "Decyl dodecanoate", "Undecyl methanoate", "Undecyl ethanoate", "Undecyl propanoate", "Undecyl butanoate", "Undecyl pentanoate", "Undecyl hexanoate", "Undecyl heptanoate", "Undecyl octanoate", "Undecyl nonanoate", "Undecyl decanoate", "Undecyl undecanoate", "Undecyl dodecanoate", "Dodecyl methanoate", "Dodecyl ethanoate", "Dodecyl propanoate", "Dodecyl butanoate", "Dodecyl pentanoate", "Dodecyl hexanoate", "Dodecyl heptanoate", "Dodecyl octanoate", "Dodecyl nonanoate", "Dodecyl decanoate", "Dodecyl undecanoate", "Dodecyl dodecanoate"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>
MATCH (f:FunctionalGroup {name_en: "Ketone"})<br>
MATCH (c:Chemical) WHERE c.IUPAC IN ["Butane-2,3-dione", "Pentane-2,3-dione", "Hexane-2,3-dione", "Heptane-2,3-dione", "Octane-2,3-dione"]<br>
CREATE (c)-[:TYPE_OF]->(f);<br>

## Reaction General
MATCH (r:Reaction)<br>
DETACH DELETE r<br><br>
CREATE<br>
(r1:Reaction {name_en: "Combustion reaction", name_th: "ปฏิกิริยาการเผาไหม้", createdAt: datetime({timezone: '+07:00'})}),<br>

## Condition
MATCH (con:Condition)<br>
DETACH DELETE con<br><br>
CREATE<br>
(con1:Condition {name_en: "Heat", name_th: "ความร้อน", symbol: "Δ", createdAt: datetime({timezone: '+07:00'})}),<br>

## Reaction FunctionGroup Relation 
#### [:REACTANT_IN] [:REQUIRED_FOR] [:MAIN_PRODUCT] [:BY_PRODUCT]
##### ===== Combustion reaction (Alkane) =====
MATCH (f:FunctionalGroup {name_en: "Alkane"})<br>
MATCH (c:Chemical {IUPAC: "Oxygen"})<br>
MATCH (c1:Chemical {IUPAC: "Carbon dioxide"})<br>
MATCH (c2:Chemical {IUPAC: "Water"})<br>
MATCH (c3:Chemical {IUPAC: "Carbon monoxide"})<br>
MATCH (c4:Chemical {IUPAC: "Carbon"})<br>
MATCH (con:Condition {name_en: "Heat"})<br>
CREATE (r:Reaction {name_en: "Combustion reaction Alkane", description: "แอลเคนถ้าออกซิเจนเพียงพอจะเผาแล้วไม่มีเขม่า", createdAt: datetime({timezone: '+07:00'})})<br>
MATCH (rm:Reaction {name_en: "Combustion reaction"})<br>
CREATE (r)-[:TYPE_OF]->(rm)<br>
CREATE (f)-[:REACTANT_IN]->(r)<br>
CREATE (c)-[:REACTANT_IN]->(r)<br>
CREATE (con)-[:REQUIRED_FOR]->(r)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c1)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c2)<br>
CREATE (r)-[:BY_PRODUCT]->(c3)<br>
CREATE (r)-[:BY_PRODUCT]->(c4);<br>
##### ===== Combustion reaction (Alkene) =====
MATCH (f:FunctionalGroup {name_en: "Alkene"})<br>
MATCH (c:Chemical {IUPAC: "Oxygen"})<br>
MATCH (c1:Chemical {IUPAC: "Carbon dioxide"})<br>
MATCH (c2:Chemical {IUPAC: "Water"})<br>
MATCH (c3:Chemical {IUPAC: "Carbon monoxide"})<br>
MATCH (c4:Chemical {IUPAC: "Carbon"})<br>
MATCH (con:Condition {name_en: "Heat"})<br>
CREATE (r:Reaction {name_en: "Combustion reaction Alkene", createdAt: datetime({timezone: '+07:00'})})<br>
MATCH (rm:Reaction {name_en: "Combustion reaction"})<br>
CREATE (r)-[:TYPE_OF]->(rm)<br>
CREATE (f)-[:REACTANT_IN]->(r)<br>
CREATE (c)-[:REACTANT_IN]->(r)<br>
CREATE (con)-[:REQUIRED_FOR]->(r)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c1)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c2)<br>
CREATE (r)-[:BY_PRODUCT]->(c3)<br>
CREATE (r)-[:BY_PRODUCT]->(c4);<br>
##### ===== Combustion reaction (Alkyne) =====
MATCH (f:FunctionalGroup {name_en: "Alkyne"})<br>
MATCH (c:Chemical {IUPAC: "Oxygen"})<br>
MATCH (c1:Chemical {IUPAC: "Carbon dioxide"})<br>
MATCH (c2:Chemical {IUPAC: "Water"})<br>
MATCH (c3:Chemical {IUPAC: "Carbon monoxide"})<br>
MATCH (c4:Chemical {IUPAC: "Carbon"})<br>
MATCH (con:Condition {name_en: "Heat"})<br>
CREATE (r:Reaction {name_en: "Combustion reaction Alkyne", createdAt: datetime({timezone: '+07:00'})})<br>
MATCH (rm:Reaction {name_en: "Combustion reaction"})<br>
CREATE (r)-[:TYPE_OF]->(rm)<br>
CREATE (f)-[:REACTANT_IN]->(r)<br>
CREATE (c)-[:REACTANT_IN]->(r)<br>
CREATE (con)-[:REQUIRED_FOR]->(r)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c1)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c2)<br>
CREATE (r)-[:BY_PRODUCT]->(c3)<br>
CREATE (r)-[:BY_PRODUCT]->(c4);<br>
##### ===== Combustion reaction (Aromatic) =====
MATCH (f:FunctionalGroup {name_en: "Aromatic"})<br>
MATCH (c:Chemical {IUPAC: "Oxygen"})<br>
MATCH (c1:Chemical {IUPAC: "Carbon dioxide"})<br>
MATCH (c2:Chemical {IUPAC: "Water"})<br>
MATCH (c3:Chemical {IUPAC: "Carbon monoxide"})<br>
MATCH (c4:Chemical {IUPAC: "Carbon"})<br>
MATCH (con:Condition {name_en: "Heat"})<br>
CREATE (r:Reaction {name_en: "Combustion reaction Aromatic", createdAt: datetime({timezone: '+07:00'})})<br>
MATCH (rm:Reaction {name_en: "Combustion reaction"})<br>
CREATE (r)-[:TYPE_OF]->(rm)<br>
CREATE (f)-[:REACTANT_IN]->(r)<br>
CREATE (c)-[:REACTANT_IN]->(r)<br>
CREATE (con)-[:REQUIRED_FOR]->(r)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c1)<br>
CREATE (r)-[:MAIN_PRODUCT]->(c2)<br>
CREATE (r)-[:BY_PRODUCT]->(c3)<br>
CREATE (r)-[:BY_PRODUCT]->(c4);<br>

## User
MATCH (u:User)<br>
DETACH DELETE u<br><br>
MATCH (s:Session)<br>
DETACH DELETE s<br><br>
CREATE<br>
(u1:User {username: "admin", password: "scrypt:32768:8:1$VcR9FHBOnXCQr7Pq$b603fbe4516f8922888e3d16398af7bfb0c70d4a40283eddbb184e9314d6ef9a474b13619579112edabf5cd10d7cc855fb2c7056a949fe016206fff69e6ebd54", role: "admin", name: "admin1", createdAt: datetime({timezone: '+07:00'})}),<br>