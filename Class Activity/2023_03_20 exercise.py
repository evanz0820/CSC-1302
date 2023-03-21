import pandas as pd
import numpy as np

# Exercise 1
ser1 = pd.Series(np.random.randint(0,100,10))
ser2 = pd.Series(np.random.randint(0,25,10))
dic = {
    "Score": ser1,
    "Age": ser2
}

df = pd.DataFrame(dic)
print(df)
print(df.tail())
print(df.describe())

# Exercise 2
df.sort_values(by='Score')
# Write the file to a new csv file
df.to_csv('2023_03_20 exercise.csv', index = False)
# Read from the csv file and store it into an array
df = pd.read_csv('2023_03_20 exercise.csv')
print(df)

# Exercise 3
row1 = pd.DataFrame({'Age': 22, 'Score': 95}, index = [10])
df = pd.concat([df,row1])

company = ['Baidu', 'Alibaba', 'Tencent', 'Tencent', 'Baidu', 'Alibaba', 'Alibaba', 'Tencent', 'Baidu', 'Tencent', 'Baidu']
df.insert(0,'Company', company)

# Exercise 4
score50 = df[df['Score'] > 50]
age20 = score50[score50['Age'] > 20]

# Exercise 5
grouped = df.groupby('Company')
print(grouped.get_group('Tencent').agg({'Age':np.median, 'Score':np.mean}))

# Exercise 6
map = df['Company'].map({'Baidu':'b', 'Alibaba':'a', 'Tencent':'t'})
print(map)
df[['Score', 'Age']].apply(np.mean, axis = 1)
df.to_csv('2023_03_20 exercise.csv',index=False)