import pandas as pd
import numpy as np

technologies = ({
    'Courses':['Spark', 'PySpark', 'Hadoop', 'Python', 'Pandas', 'Hadoop', 'Spark', 'Python', 'NA'],
    'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration(days)':[30,50,55,40,60,35,30,50,30],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
})
exer = pd.DataFrame(technologies)
print(exer)
exer1 = exer.groupby('Courses')
print(list(exer1))
print(exer1.get_group('Python').agg({'Fee':np.median,'Discount':np.mean,'Duration(days)':np.std}))

boolean=[True,False]
gender=["male","female"]
color=["white","black","yellow"]
data=pd.DataFrame({
"height":np.random.randint(150,190,50),
"weight":np.random.randint(40,90,50),
"gender":[gender[x] for x in np.random.randint(0,2,50)],
"age":np.random.randint(15,90,50),
"color":[color[x] for x in np.random.randint(0,len(color),50)],
"salary":np.random.randint(100000,500000,50)
})

colorData = {'black':0,'white':1,'yellow':2}
ColorMap = data['color'].map(colorData)
data['color'] = ColorMap

print(ColorMap)

print(data[['height', 'weight', 'age']].apply(np.mean, axis=1))