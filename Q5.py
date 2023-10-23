'''
5) define a function to accept a number. This function should return 1 if a number passed is more than 0
return -1 if a number passed is less than 0 , else it should return 0.
'''
def inp():
    x=int(input("enter a number"))
    if x>0:
       print("1")
    elif x<0:
        print("-1")
    else:
        print("0")
inp()