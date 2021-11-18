import math
import os
import random
import re
import sys

def main():
	nd = input().split()
	n = int(nd[0])
	d = int(nd[1])
	a = list(map(int, input().rstrip().split()))
	b = a+a
	d= n-d%n
	c = b[len(a)-d:len(a)-d+len(a)]
	for i in c:
		print("{}".format(i),end=" ")

if __name__ == '__main__':
	main()

