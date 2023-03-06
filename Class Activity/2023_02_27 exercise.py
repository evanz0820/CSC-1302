import pandas as pd

excel_path = "/Users/zhang/Projects/CSC1302/Class Activity/example_exel.xlsx"
df = pd.read_excel(excel_path)
print(df)

df1 = df.sort_values(by = ['final exam', 'midterm'], ascending = False)
print(df1)

df1 = df1.nlargest(6, 'midterm')
print(df1)