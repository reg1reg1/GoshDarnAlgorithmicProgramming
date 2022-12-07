'''
Written
Same output in both python languages
'''
import os
import math
l = ['123','455','897']
#declared 2 variables in global scope
num1 = 1000 #keep an eye on this variable's value
num2 = 2000

class myclass:
    num1=3600 #causes syntax warning as num1 called before declaring it as global, but 
    print "In and between"
    # if global declaration is removed and then num1 = 100 is written
    # num1 acts as a class variable, and causes no warning and will be treated as class variable 
    # if global exists , then we cannot have a class variable by the name of num1
    # we will be just modifying the global variable
    numtest=numtest+num1
    global num1
    numtest=numtest+num1
    print("Inside class num1 value is",num1)# This will print 3600 if top line is not commented
    print("Inside class ,What will be the value of numtest?",numtest)
    #The above print line takes the class value of num1?
    global num2
    num2 = 200000# as global is mentioned these are global variables
    num3 = 500 #these are not specified as global , hence class variables 
    num4 = 800 #class variable
    def myfunction(self,num1):
        #global num2
        # global num1 if uncommented 
        #will throw error(not warning error) as num1 is passed in func argument, cannot be both local and global
        num1 = num1 +100  # will refer to the function (passed in argument variable)
        #will not acceess global variable
        print('Inside function Value of num1 ',num1) #will not take global value for num1, but the passed value
        print('Inside function value of num2 ',num2) #will take global value
        print('Inside function Value of self.num1 ',self.num1)
        #In the print statement below num3 refers to one outside the class
        print('Inside function value of num3 ',num3,myclass.num3)

    def __init__(self):
        #print("(Insidde init->)Num1's:",num1,myclass.num3,myclass.num4)
        # 225 500 800
        #to access global variable here mention global
        print('Constructor was called')
        self.num1 = 45 #object variable valid for the object Instance
        num1 = 6666 #variable local to the function _init_, will not affect global
        # Access to class variables must be done using <classname>.label  (Vimp)        
        print("(init->)Num1's:",num1,self.num1,myclass.num3,myclass.num4)
    
obj1 = myclass()
#myclass.num1 will give error if there is a global declaration that overshadows the class declaration
print("Outside class Value of the num1's",num1,obj1.num1,myclass.num3,myclass.num4)#,myclass.num1) #Will give error as no static variables exist
# num2 = input("Input a number") #will change the global value of num2
num3 = int(input("Outside class Input a number into num3 ")) 
obj1.myfunction(num3)
print("Outside class Value of the num1's",num1,obj1.num1,num2,num3,myclass.num3)

#To sum up the scope, we must understand the four variable scope
#Local(inside function of defined in a scope has highest preference)
#Global just resolves the conflict in favor of the global variable, which would be considered as class
#or local variable if there was a name related conflict in the class scope
#Local, global, class, instance, arument are five of the scopes a variable can have

#See the case of num3 on Line 39 print statement,
#The num3 is being called inside a function myfunction
#This function when uses num3  it refers to the global variable outside the function and class scope 
#Inside a function we have to call class variables explicitly via <classname>.<variablename>

#If we comment out global num2 what will happen?
'''
num2 =20000 will be treated as a class variable initialization
Then if we access num2 inside myfunction via num2? We still access the global variable of num2
We use classname.variable to access the classvariable num2
However if we uncomment the global num2 line, then we never created a num2 in classscope
we were just assigning a new value to the global num2 in the class scope

'''
