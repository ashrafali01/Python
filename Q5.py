#5) accept 5 names,designations and salaries and display them with DataFrame.
import pandas as pd
"""
Name=['Jack','John','Ezekiel','Johnson','Maverick']
desg=['Captain','Boxer','Shooter','Spy','Veteran']
wlth=[100,45,55,65,75]"""

#DF= pd.DataFrame([[Name,desg,wlth]])
DF=pd.DataFrame({"Name":['Jack','John','Ezekiel','Johnson','Maverick'],"desg":['Captain','Boxer','Shooter','Spy','Veteran'],"wlth":[100,45,55,65,75]})
print(DF)