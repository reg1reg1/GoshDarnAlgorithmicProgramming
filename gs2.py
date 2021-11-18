import math
def playlist(A):
	X = [0]*(61)
	C = [0]*(1001)
	count = 0
	cb=0
	for i in range(len(A)):
		if(A[i]%60!=0):
			diff = 60 - A[i]%60
			X[diff]=X[diff]+1
			C[A[i]]=C[A[i]]+1
		else:
			cb=cb+1
	if cb>2:
		cb= int(((cb) * (cb-1))/2)
	else:
		cb = int(cb/2)
	
	for i in range(len(C)):
		if C[i]!=0:
			count=count+C[i]*X[i]
	ans=0
	ans=ans+count+cb
	return ans
def main():
	A = [3,60,60,60]
	B = [5,30,20,150,100,40]
	C = [10,10,50,50 ]
	D = [60,60,60,60]

	print(playlist(A))
	print(playlist(B))
	print(playlist(C))
	print(playlist(D))
if __name__ == '__main__':
	main()
