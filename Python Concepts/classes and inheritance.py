'''
Discussing classes and inheritance
new vs init
and metaclasses
staticmethod vs classmethod vs normalmethod
Static methods are similar to class methods in the way that they are common to instances

However, there is no way of tracing them back to the classes either
They are just defined inside classes


Classmethods are traceable to the classes, class information can be derived from them
and they are not dependent on class instances
'''


'''
static and non-static variable access
overriding and overloading in python
old style classes vs new style classes (python 2 only)
old style classes inherit from type
new style classes inherit from object
Better to avoid using old style classes
Link-->https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
Inheriting from old-style classes https://stackoverflow.com/questions/11527921/python-inheriting-from-old-style-classes
'''


'''
Importance of self
In python unlike Java we cannot use this from any method to refer to the object that called it
we need to explicitly pass the instance of the object using self to be able to use it

'''

'''
Constructors of super or base classes are not automatically called unlike Java,
base classes must call them explicitly to initialize them
'''
import sys
import os

class classA():
  
  def inc(self,x):
    print("Method of class A called")
    x = x+10
    return x
  def __init__(self):
    print("Class A constructor")

class classB():

  def __init__(self):
    print("Class B constructor")

  def inc(self,x):
    print("Method of class B called")
    x = x+100
    return x
'''
When 2 classes are inherited with conflicting method names,
The one placed earlier takes precedence if classA were to be placed before classB
the output will change
'''
class classC(classB,classA):
  x = 100
  def __init__(self):
    print("Object  initialized")
    print(self.inc(classC.x))
    super(classC,self).__init__(self,classB)
    #(Changed in Python3)In python 2 this way of class calling require you to explicitly 
    # specify 
  def printX():
    print(x)


#main 
cobj = classC()
