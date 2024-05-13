import pandas, os
df = pandas.read_csv("Exam_Table_Graded.csv")
mean = df.groupby("Stage")["Cry1Ac,ppmDW"].mean().reset_index()
mean.to_csv("b2_output.csv", index=False)