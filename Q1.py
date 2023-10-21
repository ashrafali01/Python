'''
1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
'''
def add():
    print("in add")
def modify():
    print("in modify")
def delete():
    print("in delete")

x=int(input("enter a number"))

if x==1:
    add()
elif x==2:
    modify()
elif x==3:
    delete()
else:
    print("enter 1 to 3")