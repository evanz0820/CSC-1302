import numpy as np
import pandas as pd

technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
}
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)
technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
}
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)

dfInner = pd.merge(df1, df2, on='Courses', how='inner')
dfOutter = pd.merge(df1, df2, on='Courses', how='outer')
dfLeft = pd.merge(df1, df2, on='Courses', how='left')
print(dfInner)
print(dfOutter)
print(dfLeft)