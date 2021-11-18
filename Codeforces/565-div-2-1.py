import os
import sys


x = dict()
def solve(n):
	c=0
	while n!=1:
		if(n%2==0):
			n=int(n/2)
			c+=1
			
		elif (n%3==0):
			n=2*int(n/3)
			c+=1
		elif (n%5==0):
			n=4*int(n/5)
			c+=1
		else:
			c=-1
			break
	return c

def main():
	global x
	q= int(input())
	
	while q!=0:
		n = int(input())
		print(solve(n))
		q-=1

if __name__ == '__main__':
	main()