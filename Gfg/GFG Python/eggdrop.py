import os
import sys
'''
Program to find out the min no of trials needed in a worst case outcome,
for n eggs and k floors
'''
def eggdrop(n,k):
	pass
def main():
	t = int(input().strip())
	while t!=0:
		array = input().strip()
		inplist = list(map(int, array.split(" ")))
		n =inplist[0]
		k =inplist[1]
		#Initializing a 2d matrix of dimensions n+1xk+1
		#k is no of columns
		solve=[[0 for x in range(k+1)] for y in range(n+1)]
		'''
		Terminal conditions of problems
		k=1->return 1 (1 trial required if 1 floor)
		k=0 o trials required
		n=1 if one egg and k floors , then k trials required in the worst case
		'''
		for i in range (1,n+1):
			solve[i][0]=0
			solve[i][1]=1
		for j in range(1,k+1):
			solve[1][j]=j
		'''
		Display for assurity of initialization
		'''
		for i in range (2,n+1):
			for j in range(2,k+1):
				solve[i][j]=float("inf")
				for x in range (1,j+1):
					res = 1+max(solve[i-1][x-1],solve[i][j-x])
					if res<solve[i][j]:
						solve[i][j]=res

		print(solve[n][k])
		t=t-1
if __name__ == '__main__':
	main()

