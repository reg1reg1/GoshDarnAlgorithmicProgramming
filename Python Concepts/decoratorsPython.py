'''
Decorators are similar in Python2  and Python3
'''



'''
We will now manually demonstrate what a decorator actually does behind the shadows
'''
def funcDecorator(funcObject):
	def funcWrap(x):
		print("Func Beginning")
		funcObject(x)
		print("Func End")
	return funcWrap

def foo(x):
	print("Func has been called with ",str(x))

x = "Hello World!"


#This will return the function object funcWrap with foo as internal object
#As we know in python function are first class objects
foo = funcDecorator(foo)


foo(x)

'''
To understand the above example,have a look at the following
Functions can return function references as well
'''

def f(x):
	x = x+100
	def g(y):
		return y + x + 3
	x =x+1000     
	return g
#When the f(1) is called, function reference g is returned after processing value of x
#g then uses this value of x when called with some value such as from within the print 
# statement as shown below, this value of x is remembered when nf1/nf2 is called


#This property of python to remember variables even when out of scope or the outside namespace
# is removed is termed as closure, and decorators make extensive use of closures.
nf1 = f(1)
nf2 = f(3)



print("Value of nf1 is ",nf1(1))
print("Value of nf2 is ",nf2(1))


def decoratingFoo(funcObj):
	def Helper(x):
		print("Function begins")
		funcObj(x)
		print("Function ends")
	return Helper

def fooBar(x):
	print("Printing ", str(x))

#defining argument
x = "HelloWorld" 






'''
Analysis:
RHS-> decoratingFoo(fooBar)
it will call decoratingFoo with fooBar as argument  and "Helper")
will be defined in this context and namespace which it will retain afterwards, "closure")

decoratingFoo will return a ref to this function Helper (defined in the context explained)
LHS->
Now fooBarOBject will be pointing to this Helper function
Now when we call fooBar(x), Helper(x) is being called with funcObj referring to the original 
fooBar function (as Helper was defined in this way and retained when decoratingFoo(foobar) was 
called)
so Helper(x):
  blah blah
  fooBar(x)#original fooBar 
  blah blah
is what the fooBar(x) will do
'''
fooBarObject = decoratingFoo(fooBar)
fooBarObject(x)



'''
Actually using decorators
Without manually writing all the above
We could use @ and the decorator will do it behind the scenes
'''

def checkArgtype(fRef):
	def wrapIt(x):
		if type(x) == int:
			print("begins")
			return fRef(x)
		else:
			return "Error, argument type not Integer"
	return wrapIt

@checkArgtype
def multiplyIntBy10(x):
	return x*10

print(str(multiplyIntBy10(100)))


class NewClass(object):
	def __init__(self):
		pass

	def __call__(self,funcRef): 
		def wrapperFunction(x):
			print("Need to execute the passed function")
			funcRef(x)
			print("Ending call to the function")
		return wrapperFunction

aFunc = NewClass()

@aFunc
def innocentFunction(x):
	print(x)

innocentFunction("I feel like, I am gonna be surrounded by someone")