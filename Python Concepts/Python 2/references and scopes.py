'''
Python 2 
Extension of lists and sets
Shallow vs deep copy
What can be changed and what cant be
Call by value or call by reference ?
'''
import copy

#Primitive object Will never be changed
x=10
y=x
y+=20
#shallow copy on a primitive object
#shallowcopy creates a new object
z=copy.copy(x)
z+=20
print x



#Mutable objects Lists
l1 = ['a','b','c','d','e']
l2 = l1
l2.append('f')
print l1 #f will get appended as both point to same object

#performing a shallowcopy

l3 = ['a','b','c']
l4 = l3[:] #one way of creating a shallow copy(using slice operation)
#above is same as l4 = copy.copy(l3)
l4.append('d')
print l3

#what will happen if we have sublist(or some non primitive object in the list), 
#the lists will have the reference to the object

l5 = ['a','b','c',['a','b']]
l6 = copy.copy(l5)

#will not reflect in l5
l6.append('g')
print "first print",l5


#3rd element is a list
#shallow copy copies reference to that list in l6
#all other elements (primitives) are same
#will reflect in l5
l6[3].append('x')
print "second print",l5

#How do python functions treat arguments?







