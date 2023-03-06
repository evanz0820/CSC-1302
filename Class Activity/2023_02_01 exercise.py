import numpy as np

arr1 = np.random.randint(20, size = (4,4))
print(arr1)

arr2 = np.sum(arr1)
print(arr2)

arr3 = np.argmin(arr1, axis = 0)
print(arr3)

arr4 = np.cumsum(arr1)
print(arr4)