'''
Language: Python 3.x
Program Statement:
Print True if a given string can be obtained by rotation of another given string
and false otherwise
Eg: water is a rotation of rwate
Initial intuition is to double up the string and see if the other string exists as a substing,
if Yes, then rotation can be done to obtain or else not
Eg: rwate+rwate=>rwaterwate
There is a catch that the length of both the strings should be verified as equal before going
for the above
And for string search, we have to know and USE KMP
Mod1: Use library funtion and solve
Mod2:Solve by using KMP from scratch (need to come back to this)
'''

#library pattern search
def mod1():
	t = int(input()).strip()
	for i in range(t):
		str1=input.strip()
		str2=input.strip()
		str1= str1.concat(str1)


#KMP (dynamic programming)
def mod2():