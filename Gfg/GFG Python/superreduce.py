import os
import sys
'''
Written in python3
Hackerrank problem on strings named SuperReduce
@author reg1reg1_1
In a for loop each time the iterator is assigned a new value from range
hence any modification to the 'i' value wont work
We need to use a freakin while loop instead
What secrets does python have in store for us , still?
'''

def superReduce(x):
	i = 1
	while i <=len(x)-1:
		#print("current comparisons ",i,i-1)
		if x[i]==x[i-1]:
			x = x[0:i-1]+x[i+1:]
			i=0
		i=i+1
		#print("modified as i,string", i,x)
	if len(x)==0:
		print("Empty String")
	else:
		print(x)



def main():
	string = str(input().strip())
	superReduce(string)

if __name__ == '__main__':
	main()