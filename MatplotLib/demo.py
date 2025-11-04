import pandas as pd
import numpy as np

# arr = np.array([10,15,18,22])
# s = pd.Series(arr)
# print(s)

# arr = np.array(['a', 'b', 'c', 'd'])
# s = pd.Series(arr,
#               index=['first', 'second', 'third', 'fourth'])
# print(s)

# d={1:["yo",12],2:["hphp",12],3:["123",231]}
# s=pd.Series(d)
# print(s)

# s=pd.Series([1,2,3,4,5])
# print(s*2)
# print(s**2)
# print(s[s>2])

s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s3=pd.Series([22,10,32,41],index=['a','b','c','d'])
print(s1+s2)
print(s2+s3)
print(s2.add(s3,fill_value=0))

