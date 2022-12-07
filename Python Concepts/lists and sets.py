'''
Python 2 Lists,sets, comprehensions
Comprehensions can be used in place of Lambda , Map reduce

Sets are like lists but do not have order, also sets cannot have duplicates
'''
#Python list slicing :-> https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
'''
>>> seq[:]                # [seq[0],   seq[1],          ..., seq[-1]    ]
>>> seq[low:]             # [seq[low], seq[low+1],      ..., seq[-1]    ]
>>> seq[:high]            # [seq[0],   seq[1],          ..., seq[high-1]]
>>> seq[low:high]         # [seq[low], seq[low+1],      ..., seq[high-1]]
>>> seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
>>> seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
>>> seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
>>> seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
'''
#List comprehension
# List comprehension are surrounded by square braces

b = [1,2,3,4,5,6]
a = [(x*x) for x in b]

for y in a:
  print y

#Cross product of 2 sets using List comprehension

z = [(x,y) for x in a for y in b]
for i in z:
  print i

#Declaring a 2-d list 
my2dlist = [[0]*10 for x in range(5)]

for j in range(len(my2dlist)):
  print my2dlist[x]
#{} stands for set comprehension
#[] stands for list comprehension
#If we use [] then we will have duplicates in noprimes 6 will be present once for 2, and 
#once for 3
#Hence we use curly braces 
noprimes = {j for i in range(2,8) for j in range (i*2,100,i)}
primes = [i for i in range(0,100) if i not in noprimes]
print primes


#Set in python 
#an unordered collection of unique and immutable objects
#Sets cannot have mutable objects,Why?
#Sets have to maintain unique values, objects need to be hashable


#Sets are mutable, but the objects they contain cannot be mutable
#Here the set contains strings
#Eg:
#the following will fail, as here list is passed as an element to a set
# guns = set((["ak-47","mp5-carbine","rpg","eagle","glock"],["g9"]))


'''
Instances of Set and ImmutableSet both provide the following operations:
As they generate a new set and not modify the older set
Operation Equivalent  Result
len(s)    number of elements in set s (cardinality)
x in s    test x for membership in s
x not in s    test x for non-membership in s
s.issubset(t) s <= t  test whether every element in s is in t
s.issuperset(t) s >= t  test whether every element in t is in s
s.union(t)  s | t new set with elements from both s and t
s.intersection(t) s & t new set with elements common to s and t
s.difference(t) s - t new set with elements in s but not in t
s.symmetric_difference(t) s ^ t new set with elements in either s or t but not both
s.copy()    new set with a shallow copy of s

The following table lists operations available in Set but not found in ImmutableSet:

Operation Equivalent  Result
s.update(t) s |= t  return set s with elements added from t
s.intersection_update(t)  s &= t  return set s keeping only elements also found in t
s.difference_update(t)  s -= t  return set s after removing elements found in t
s.symmetric_difference_update(t)  s ^= t  return set s with elements from s or t but not both
s.add(x)    add element x to set s
s.remove(x)   remove x from set s; raises KeyError if not present
s.discard(x)    removes x from set s if present
s.pop()   remove and return an arbitrary element from s; raises KeyError if empty
s.clear()   remove all elements from set s

'''

#set function ->converts<- resulting sequence or iterable object into a set
fruits = set(["apple","oranges","mangoes","apple"])
#The duplicate value will be automatically removed
print fruits

def modifySet(x):
  x.discard("apple")
  x.update(["banana"])
  print "Within the function",x

modifySet(fruits)
print "Modified set",fruits


#And then there are frozen sets
stubbornFruits = ImmutableSet(["apple","oranges","mangoes"])
#There are no update instructions supported on this set and hence it is immutable

#sets must contain immutable objects , hence a list as an element of the set is not allowed
#in the previous example the list was converted to a set, 
#it was not a set with one element as a list



#Tuples 
#Immutable and fixed in size unlike lists

t = 12345,16,90,29080
#t is a tuple
#t[0] = 123456 will throw an error as tuples immutable
#immutable objects do not support assignment

v = ([1,2,3,4],[2,3,4])
#v is a tuple





