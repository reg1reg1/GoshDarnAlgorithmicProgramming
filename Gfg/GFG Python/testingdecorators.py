'''
Testing the decorator functionality
class decorators

'''

print("Start")

class myDecorator():
	print("Inside the class mydecorator")
	def __init__(self, f):
		print("inside myDecorator.__init__()")
		self.f = f

	def __call__(self):
		print("Beginning of a function")
		print(self.f(1,8,9))
		print("End of function")



print("In the middle, instantiating decorator")
@myDecorator
def aFunction(var1,var2,var3):
	print("inside aFunction()")
	return var1 * var2 * var3

print("First function Finished decorating aFunction()")

# def myfunction(value):
# 	print("Entered",format(value))
print("End of compilation")
print("calling aFunction()......")
aFunction()

#myfunction(4)