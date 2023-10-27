# Exception class has following "__init__()" method:

""" 
def __init__(self,message=None)
	self.message=message
"""


class wrongvalue(Exception):
	pass

def double(var):
	if var<=0:
		raise wrongvalue("Number cannot be negative or zero")
		# raise wrongvalue()
	return var*var

def fun():
	try:
		print(double(-4))
	except Exception as e:
		print("error is\t",e.__str__())
	print("Done")
fun()


