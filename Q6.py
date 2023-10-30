#6) create a csv file (with whatever columns and rows you want) manually and then read using pandas.

import pandas as pd

DF=pd.DataFrame({"Name":['Jack','John','Ezekiel','Johnson','Maverick'],"desg":['Captain','Boxer','Shooter','Spy','Veteran'],"wlth":[100,45,55,65,75]})

DF.to_csv("MyCSV.csv")

dff=pd.read_csv("MyCSV.csv")

print(dff)