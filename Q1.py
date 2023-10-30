"""
1) store marks of 5 subjects
	here use marks as actual data and subject names as indexes.
accept both marks and subjects from the user.
"""
import pandas as pd

dict = {}

for i in range(5):
    subject=input("Enter your Subject Name - ")
    marks=int(input("Enter marks you got - " ))

    dict[subject]=marks

print(dict)

marksheet=pd.Series(dict)
print(marksheet)