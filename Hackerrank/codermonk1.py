'''
coderMonk Hacker Earth
'''

def main():
	t = int(input().strip())
	for i in range (t):
		n = int(input().strip())
		tmp1 = input().strip()
		tmp2 = input().strip()
		cp = list(map(int, tmp1.split(" ")))
		lp = list(map(int, tmp2.split(" ")))
		mmin = cp[0]
		prod=0
		for i in range (n):
			if mmin > cp[i]:
				mmin=cp[i]
			prod += lp[i]*mmin	
		print(prod)

if __name__ == '__main__':
	main()