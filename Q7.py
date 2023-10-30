"""
7) create "Vita.xlsx" using pandas. In this Excel file you have to create 2 sheets "DBDA", and "DAC". 
in each sheet you have to write name,address and age of all the team leaders.
make sure Excel file gets created successfully.
"""

import pandas as pd

vita=pd.DataFrame({"Name":['Jack','John','Ezekiel','Johnson','Maverick'],"desg":['Captain','Boxer','Shooter','Spy','Veteran'],"wlth":[100,45,55,65,75]})

mydataframe=pd.DataFrame({"proid":range(5,9),"proname":['soap','perfume','deo','powder'],"price":[120,400,280,160]})


with pd.ExcelWriter('vita.xlsx') as mywriter:
    vita.to_excel(mywriter, sheet_name='Pirates',index=False)
    mydataframe.to_excel(mywriter, sheet_name='Employee',index=False)

