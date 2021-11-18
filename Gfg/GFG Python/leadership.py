import os
import sys

def solve(x):
	pass
def main():
	q= int(input().strip())
	while q!=0:
		size = int(input().strip())
		xarr= input().strip()
		arr = list(map(int,xarr.split(" ")))
		mmax=-1
		x=[]
		for i in range(len(arr)-1,-1,-1):
			#print("MMAX :",mmax,end=": ")
			if arr[i]>=mmax:
				mmax=arr[i]
				x.append(arr[i])
		x=x[::-1]
		for i in x:
			print(i,end=" ")
		print()
		q-=1

if __name__ == '__main__':
	main()

