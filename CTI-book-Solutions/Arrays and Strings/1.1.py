'''
Language: Python 3.x
Program Statement:
Print Yes if string has all Unique characters
Mod: Do it without extra space
For extra space allowed just use a simple hash
'''

import os
import sys
def main():
	t = int(input().strip())
	for i in range(t):
		inputstring= input().strip()
		strsize = len(inputstring)
		sortedstring = sorted(inputstring)
		flag = True
		for i in range(1,strsize):
			if sortedstring[i]==sortedstring[i-1]:
				print("FALSE")
				flag = False
				break
		if flag is True:
			print("TRUE")
if __name__ == '__main__':
	main()


