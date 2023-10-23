'''
7) define a function which accepts a string , toggle and return it.
	[ hint :  use "swapcase()" function of string ]
'''
def str(a):
    '''
   # print(a==a.upper())
    if a == a.upper():
        b =a.lower()
        print(b)
    else:
        b=a.upper()
        print(b)
        '''
    
    return a.swapcase()
    
p=str("JacK")
print(p)

