import pandas as pd
df = pd.read_csv("Exam_Table_Graded.csv")
average = df.groupby ("Stage") ["Cry1Ac,ppmDW"].mean()
output = pd.DataFrame({"Stage": ["Vegetative"], "Cry1Ac,ppmDW" : average["Vegetative"]})

average = df.groupby ("Stage") ["Cry1Ac,ppmDW"].mean()
output = pd.DataFrame({"Stage": ["Reproductive"], "Cry1Ac,ppmDW" : average["Reproductive"]})


output.to_csv("./Santos_B2.csv")
             
                               
                               