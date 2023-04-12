import pandas as pd
import numpy as np

# Exercise 1
arr = np.random.randint(0,100,(10,1))
print(arr)
new_index = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj']
s1 = pd.Series(arr, index = new_index, name = "series practice")
print(s1)
average = s1.mean()
print(average)
below = s1[s1<average]
print(below)
above = s1[s1>average]
print(above)

# Exercise 2
songs = {
    1:"one", 
    2:"two", 
    3:"three", 
    4:"four",
    5:"five"}
s2 = pd.Series(songs)
print(s2)
second = s2[2]
print("My second song is", second)