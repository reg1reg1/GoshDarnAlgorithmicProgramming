'''
Print the integer that occurs only once
'''

def lonelyinteger(x):
	S = set()
	R= set()
	'''
	Set.add() only works on sets and not on dictionaries
	'''
	for i in x:
		if i not in S:
			S.add(i)
		else:
			R.add(i)
	G = S - R
 
	return next(iter(G))









def main():
	t = int(input().strip())
	while(t>0):
		arr =  input().strip()
		xarr = list(map(int,arr.split()))
		print(lonelyinteger(xarr))
		t-=1

if __name__ == '__main__':
	main()