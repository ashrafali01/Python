'''
6) define a function which accepts a character and return toggle of it.
'''
def character(a):
    
    if a == a.upper():
        print(a)
        return a.lower()
    else:
        print(a)
        return a.upper()
    
#i= input("enter a character")
c=character("l")
print(c)