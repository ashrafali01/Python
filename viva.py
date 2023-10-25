"""  # lamda with default arguements
a= lambda x,y=10: print(x+y)
a(10)
 """
""" for i in range(0,8):
    for j in range(1,i):
        for s in range(8-i,1,-1):
            print(end=" ")
        print("*",end=" ")
    print()
 """

# create a list and delete elements

""" list1=[10,20,30,40,50,60,70]
print(list1)
i=int(input("enter index of number you want to delete"))
list1.pop(i)
print(list1)

list1.remove(40)
print(list1) """

# store list elements till enter zero

#list2=[]
#i=1

""" while (1):
    i = int(input("enter"))
    if (i==0):
        break
    else:
        list2.append(i)
print(list2) 
while(i!=0):
    i=int(input("enter"))
    if(i!=0):
        list2.append(i)
print(list2)

"""

#
from multipledispatch import dispatch

@dispatch(int)
def fun1(a):
    print("in int",a)
@dispatch(str)
def fun1(b):
    print("in sttring",b)

fun1(10)
fun1("any")