'''
Python 2 Iterators 
Iterators are any kind of objects that implement the iter and the next method
effectively making them iterable
Note that the syntax varies slightly in Python 3 with the methods being renamed as
__next__ and __iter__ instead.
https://www.datacamp.com/community/tutorials/python-iterator-tutorial
'''

#Note that list are not iterators , they just behave like one.


'''
The for loop is actually implemented in the following way making it able
to loop through any iterable object

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop (Implementation of for loop)
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
'''

#Crux of the matter, Create your own Iterator?
#written in python 3 syntax 
class PowTwo:
    """Class to implement an iterator
    of powers of two"""
    
    def __init__(self, max = 0):
        self.max = max

    ##this is called when iteration is initialized
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
        	raise StopIteration
#StopIteration is raised when we do not want to do any more iterations
#The max value is defined here for exactly that purpose.


#if we do not raise the StopIteration exception at any point then we would have created
#an Infinite iterator
#the following iterator generates all the odd numbers , infinitely until exited or
#stopped


class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

powerObject = PowTwo(10) #max is 0 if not initialized
print(list(powerObject))


# iterable. the Iter function is always called when the powerObject is interacted with as an iterable
for i in powerObject:
    print(i)





