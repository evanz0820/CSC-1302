import pandas as pd
import numpy as np

# create series based on a list
my_list = [10, 20, 30, 40, 50]
series_list = pd.Series(my_list, name='panda list')
print(series_list)

# create series based on an array
my_array = np.array([100, 200, 300, 400, 500])
series_array = pd.Series(my_array, index=list('abcde'))
print(series_array)

# create series based on a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_dict = pd.Series(my_dict)
print(series_dict)

# change the index of the series of array into alphabet
series_array.index = list('vwxyz')
print(series_array)

# change the name of the series of the list with panda lab5
series_list.name = 'panda lab5'
print(series_list)