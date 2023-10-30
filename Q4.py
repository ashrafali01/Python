"""
4) accept 5 values in a Series and perform the following operations:
	a) display their sum
	b) add the value accepted from the user
	c) subtract the value accepted from the user
	d) multiply the value accepted from the user
	e) add the value accepted from the user

"""

import pandas as pd
Dict4={}

for i in range(5):
    Name=input("Enter name - ")
    marks=int(input("Enter your marks - "))
    Dict4[Name]=marks
ser=pd.Series(Dict4)
print("the sum of marks is - ",ser.sum())
x=int(input("Enter a number you want to add in each element - "))
print("edited series - ", ser.add(x))
print("after substraction - ", ser.subtract(2))
print("after multiplication - ",ser.mul(2))

"""
import pandas as pd

temp= pd.Series({'name':'jack','name1':'john'})
print(temp)"""