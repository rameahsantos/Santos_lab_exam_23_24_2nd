import pandas as pd
df = pd.read_csv("Exam_Table_Graded.csv")
transposed_df = df.T
transposed_df.to_csv('b4_output1.csv', header=False)
