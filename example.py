import pandas as pd
import numpy as np

a_dic = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5}
ser= pd.Series(a_dic)

print(ser)
print(ser[0:3])
print(ser['2nd'])
print(ser[1])
