import pandas as pd
df = pd.read_csv("Exam_Table_Graded.csv")
df['CPEID'] = df['Entry'] + '-' + df['Replication'].astype(str) + '-' + df['Stage']
df['CPEID'] = df['CPEID'].str.replace(',', '-')
df.to_csv('b3_output1.csv')