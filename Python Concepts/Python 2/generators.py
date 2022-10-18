
'''
Python 2 Demonstrating Generators
In python 3 more functionalities are added to decorators
'''


#generators are defined in the same way as functions 
def infinityStones():
	print "Reality Stone"
	yield()
	print "Mind Stone"
	yield()
	print "Time Stone"
	yield()
	print "Soul Stone"
	yield()
	print "Power Stone"
	yield()
	print "Space Stone"
c=0
x = infinityStones()
#generators can be looped through

for i in x:
	print "Stone number ",c," ",i

# yield works same way as return in afunction,
# It pauses execution and resumes it from the same place once the generator is called again
#Once all items are iterated the next() methgod fails

