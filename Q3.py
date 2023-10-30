"""
Q. accept 10 values and store them in the Series. Now perform following operations:
a) display the entire Series
b) extract 3rd element
c) extract elements from 4 to 7
d) extract elements from fourth last till the last element
e) extract first 3 elements
f) extract elements from the 5th position
"""

import pandas as pd
Dict3={}

for i in range(10):
    Name=input("Enter name - ")
    rank=int(input("Enter your rank - "))
    Dict3[rank]=Name

Rankings=pd.Series(Dict3)

print(Rankings)
print("\n", "3rd Element")
print(Rankings[2])
print("\n","for 3rd to 7")
print(Rankings[3:7])
print(Rankings[-4:])
print(Rankings[0:2])
print(Rankings[0:5])