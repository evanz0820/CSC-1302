import pandas as pd

# create the series for each column
profession = pd.Series(['basketball', 'American football', 'soccer'], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])
age = pd.Series([38, 45, 35], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])
salary = pd.Series(['45 million', '15 million', '41 million'], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])

# create the dataframe
df = pd.DataFrame({'profession': profession, 'age': age, 'salary': salary})

# display the dataframe
print(df)
