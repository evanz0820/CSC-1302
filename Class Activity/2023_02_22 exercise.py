import numpy as np
import pandas as pd

grades = {

    'Student1' : [10,10,10],
    'Student2' : [9,7,9],
    'Student3' : [9,6,6]

}

df = pd.DataFrame(grades, index = ('Homework', 'Activity', 'Attendance'))
df.index.name = 'Grades'

midterm1 = pd.DataFrame({

    'Student1':10, 
    'Student2':10, 
    'Student3':10
}, index=['Midterm 1'])

# df = pd.concat([df, midterm1])
# print(df)

student4 = [9,7,8,8]
df.insert(3, 'Student4', student4)
# print(df)

# df.drop(columns = ['Student1'], inplace=True)
# df.drop(['Midterm 1'], inplace = True)
# print(df)

print(df['Student2'])
print(df.loc[['Attendance'], ['Student3', 'Student4']])

