import pandas as pd
df = pd.read_csv("Exam_Table_Graded.csv")
output = df[df["Entry"] == "M4"]
print(output)
output.to_csv("./Santos_B1.csv") 