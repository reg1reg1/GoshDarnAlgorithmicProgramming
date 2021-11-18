
import os
import math
l = ['123','455','897']
print "Hello World@ysingh.fastenal.co"
print l[1:2]
x = 120
def mymethod(y):
    y = 90
num1 = 45
num2 = 56
class myclass:
    print "This is my class, pretty normal"
    
    global num1
    global num2
    num1 = 75
    num2 = 90
    print("Value of stat var num4 set")
    num4 = 56
    def myfunction(self,num1):
        num1 = num1 +20 
        print 'Called self.num',num1
        print 'Functional Variable',num1
        print 'Called local',num1
    def __init__(self,num1,num2):
        print 'Constructor was called'
        self.num1=num1
        self.num2=num2
    def setStatic(self,val):
        print("Value of num4 modified")
        #access function variable
        num4=val
        myclass.num4 = val
        print("as ",num4)

    
   
obj1 = myclass(100,200)
obj2 = myclass(100,300)
#myclass.num1->Compiler error as num1 in scope of class has been defined as global
obj2.setStatic(34)
obj1.setStatic(31)
print(obj1.num1,obj1.num2,num1,num2,obj2.num1,obj2.num2,obj1.num4,obj2.num4,myclass.num4)

mymethod(x)
print "The value of x is ", x
