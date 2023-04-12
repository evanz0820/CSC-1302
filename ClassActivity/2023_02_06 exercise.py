import numpy as np

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
#print(x)

arr = np.arange(0,12).reshape(4,3)
print(arr)
corner = arr[[0,3,0,3],[0,2,0,2]]
print(corner)
row = np.array([[0,0],[3,3]])
col = np.array([[0,2],[0,2]])
print(row)
print(col)
new = arr[row,col]
print(new)