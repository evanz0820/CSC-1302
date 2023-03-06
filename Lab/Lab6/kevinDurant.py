import pandas as pd

# create the series for each column
profession = pd.Series(['basketball', 'American football', 'soccer'], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])
age = pd.Series([38, 45, 35], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])
salary = pd.Series(['45 million', '15 million', '41 million'], index=['lebron_James', 'Tom_Brady', 'Leo_Messi'])

# create the dataframe
df = pd.DataFrame({'profession': profession, 'age': age, 'salary': salary})
print(df)

# kevin durant
kevin = pd.DataFrame({

    'profession': 'basketball',
    'age': 34,
    'salary': '43 million'

}, index = ['Kevin_Durant'])
df = pd.concat([df, kevin])
print(df)

# adding weight
weight = [250,225,148,240]
df.insert(3, 'weight', weight)
print(df)