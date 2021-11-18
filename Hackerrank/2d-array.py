import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# array is 6x6
def hourglassSum(arr):
	X= arr[1][1]+arr[0][0]+arr[0][1]+arr[0][2]+arr[2][0]+arr[2][1]+arr[2][2]
	maxsum = X
	solve=[[-1]*6 for x in range(6)]
	solve[1][1]=X
	for i in range(1,5):
		for j in range(1,5):
			hourglasssum = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
			maxsum=max(maxsum,hourglasssum)
	return maxsum


def main():
	arr=[]
	for i in range(6):
		arr.append(list(map(int, input().rstrip().split())))
	print(hourglassSum(arr))

if __name__ == '__main__':
	main()