'''
Language: Python 3.x
Program Statement:
Print if given 2 strings one string is permutation of the other

Possible Algos: 
Count the characters and if the characters have same count, 2 strings are same O(n) with O(C)
space(Constant space of 256)
If the strings can be modified sort both of them  O(Nlog(N))
'''

t = int(input().strip())
for i in range(t):
	flag = True
	str1 = input().strip()
	str2 = input().strip()
	hashmap = [0]*256
	hashmap2= [0]*256
	n =len(str1)
	if n!= len(str2):
		print("FALSE")
		continue
	else:
		for i in range(n):
			z1 = ord(str1[i])-ord('0')
			z2 = ord(str2[i])-ord('0')
			hashmap[z1]+=1
			hashmap2[z2]+=1
		for i in range(256):
			if hashmap[i]!=hashmap2[i]:
				print("FALSE")
				flag=False
				break
		if flag:
			print("TRUE")
		else:
			print("FALSE")
