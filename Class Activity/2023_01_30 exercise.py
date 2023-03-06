import numpy as np
# create a 3 dimensional array with all zeros
# create a array within the range of 20 with step size 3
# create a random array within range of 20 and shape of 3*3

arr1 = np.zeros((3, 3, 3), dtype = 'i')
print(arr1)
print()
arr2 = np.arange(1, 20, 3)
print(arr2)
print()
arr3 = np.random.randint(20, size = (3,3))
print(arr3)
