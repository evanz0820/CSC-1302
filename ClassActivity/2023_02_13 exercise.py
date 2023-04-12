import numpy as np

# First Exercise
arr1 = np.arange(0, 10)
odd = arr1[arr1 % 2 == 1]
print(odd)
greater2 = arr1[2:]
print(greater2)

# Second Exercise
arr2 = np.arange(100, 200, 10).reshape(5,2)
print(arr2)

# Third Exercise
arr3 = np.array([[11,22,33],[44,55,66],[77,88,99]])
print(arr3[0:,2:])

# Fourth Exercise
sampleArray = np.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])
print(sampleArray[0:3, 1:4])

# Fifth Exercise
print(sampleArray[::2,1::2])

# Sixth Exercise
sampleArray1 = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(np.sort(sampleArray1))
# sort by columns
sortedRow = np.sort(sampleArray1, axis = 1)
print(sortedRow)
# sort by rows
sortedCol = np.sort(sampleArray1, axis = 0)
print(sortedCol)

# Seventh Exercise
grades = np.array([[79, 95, 60], [95, 60, 61], [99, 67, 84], [76, 76, 97], [91, 84, 98], [70, 69, 96], [88, 65, 76], [67, 73, 80], [82, 89, 61], [94, 67, 88]])
female = [ True, False, True, True, False, True, False, False, False, False]
female_grades = grades[female, :]
print(female_grades)