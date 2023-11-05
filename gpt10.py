"""
Question: You are given a list of integers. Write a Python function that finds the largest and the second-largest integers in the list without using built-in sorting functions. Your function should return both values. How would you approach this problem?

Feel free to attempt to solve it, and I can provide you with a solution and explanation if needed.
"""
""" list=[1,205,0,5,650,654,65,8,5,600,8979,888,6000]


def checkmax(list):   
    max=1 
    secondmax=1
    for i in list:
        if i>max:
            max=i
    for j in list:
        if j!=max and j>secondmax:
            secondmax=j

    print("largest is- {} and second largest is {}".format(max,secondmax))

checkmax(list)
 """
list1=[10,20,30,109,60,50,100,110,105,70]
second=0
first=0
for i in list1:
    if i > first:
        second=first
        first=i
    elif i >second:
        second=i
print(first,second)
