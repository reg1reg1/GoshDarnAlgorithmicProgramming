'''
How python variables are handled when passed to
functions
'''
def myfunction(x):
	x.append('z')
	x = ['a','b','c'];
	return x


h = ['d','e','f']

z=myfunction(h)

print(h) 
print(z)