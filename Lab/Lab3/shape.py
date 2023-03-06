import numpy as np
#Create a new array with range from 0 to 100 with shaep (30,3)
arr1 = np.random.randint(100, size = (30,3))
#Change the shape to (18,5)
arr2 = np.reshape(arr1, (18,5))
print(arr2)
#Extract the information after the second column include the second column
arr3 = arr2[:,1:]
print()
print(arr3)
#Also extract the information from fifth row second column to eighth row second column(include fifth and eighth row)
arr4 = arr2[4:8, 1:]
print()
print(arr4)