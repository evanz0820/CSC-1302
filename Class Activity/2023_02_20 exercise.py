import numpy as np
import pandas as pd

grades = {
    'Student1' : [10,10,10],
    'Student2' : [9,7,9],
    'Student3' : [9,6,6]
}

df = pd.DataFrame(grades, index = ('Homework', 'Activity', 'Attendance'))
df.index.name = 'Grades'
print(df)

student1 = df['Student1']
print(student1)

allAttend = df.loc['Attendance']
print(allAttend)

df['Student4'] = [6,8,9]
print(df)

examGrades = {'Student1':10, 'Student2':9, 'Student3':7, 'Student4':8}
df = df.append(pd.Series(examGrades, index=df.columns, name='Exams'))
print(df)
