'''
Language: Python 3.x
Program Statement:
Print if a string can be compressed with the following format
ababbcdee=> a2b3c1d1e2

Print 2nd string unless the first string is shorter in length

We need character count, so either we sort or we use a space time tradeoff

Crux:
Find count difference len of compressed string - len of new string
Count difference must be negative
'''
def calcdigits(x):
	i = 0
	while x > 0:
		x = int(x/10)
		i=i+1
	return i

def main():
	t = int(input().strip())
	for i in range(t):
		count=0
		#calculatelettercount
		strinp = input().strip()
		n = len(strinp)
		hashtable = [0]*52
		for i in range(n):
			z=ord(strinp[i])
			if z>90:
				z=z-6
			z=z-65
			hashtable[z]+=1
		index=0
		#print(hashtable)
		while index < 52:
			if hashtable[index]>0:
				#print(calcdigits(hashtable[index]),hashtable[index])
				count=count - hashtable[index] + calcdigits(hashtable[index]) + 1
			index+=1
		#print("COUNT ",count)
		if count >=0:
			print(strinp)
		else:
			i=0
			while i < 52:
				val=0
				if i < 26:
					val = i+65
				else:
					val = i+71
				if hashtable[i]>0:
					print("%c%d"%(chr(val),hashtable[i]),end='')
				i=i+1
			print('')

if __name__ == '__main__':
	main()
