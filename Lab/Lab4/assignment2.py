import numpy as np
import time

#Creates and calculate the time it takes to sum up the array
arr1 = np.arange(0,100000)
start = time.time()
arr2 = np.sum(arr1, dtype = np.float64)
end = time.time()
array_Time = end - start

#Creates and calculate the time it takes to sum up the list
list1 = [*range(0,100000)]
list2 = 0
start = time.time()
for i in list1:
    list2 += i
end = time.time()
list_Time = end - start

# print results
print("Sum of Array: ", arr2)
print("Time taken to calculate sum of Array: ", array_Time)
print("Sum of List: ", list2)
print("Time taken to calculate sum of List: ", list_Time)

#Calculate the difference
difference = list_Time - array_Time
print("Difference in time taken to calculate sum: ", difference)