'''
Mutable vs Immutable types
Important link: https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types
Lists,sets,dictionaries,Strings, primitive data types
'''

'''
Mutable : primitive vars, lists, sets
Immutable: frozen sets,dictionaries ,strings
'''


def Mutator(x,y,z,a):
  #reassignment holds meaning within function as arguments are just variables pointing to
  x=y #original variables, hence not changed
  x[1]=900 #changed as temp copies point to the same memory location
  y=y[::-1] #will not reflect as value of y changed within function scope
  z = z/2 #Same as above
  a = "str12345"  
  #a[0]= "x" #will throw a error as we are trying to mutate a string

x= [10,20,25,30]
y= [11,12,13,14,15]
z= 50
str1 = "bggzzzzzz"
set1 = {"red","blue","green","yellow","red"}
Mutator(x,y,z,str1)

print x," ",y," ",z