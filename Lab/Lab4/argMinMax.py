import numpy as np

# Generate 5x5 array with random values
arr = np.random.rand(5,5)

# Calculate the sum of the array
arr1 = np.sum(arr)
print(arr1)

# Calculate the index of the minimum value in each column
arr2 = np.argmin(arr, axis=0)
print(arr2)

# Calculate the index of the maximum value in each row
arr3 = np.argmax(arr, axis=1)
print(arr3)