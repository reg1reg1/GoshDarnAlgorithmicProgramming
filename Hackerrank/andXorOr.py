def stackTop(x):
	return x[len(x)-1]
def andXorOr(a):
	stack=[]
	currXor=-1
	i=0
	#len atleast 2
	for i in range(len(a)):
		while len(stack)!=0 and a[i]<=stackTop(stack):
			x=stack.pop()
			xor = x^a[i]
			currXor=max(currXor,xor)
		if len(stack)!=0:
			xor=stackTop(stack)^a[i]
			currXor= max(currXor,xor)
		stack.append(a[i])
	return currXor


def main():
	t=int(input().strip())
	for i in range(t):
		xarr= list(map(int,input().strip().split(" ")))
		print(andXorOr(xarr))
if __name__ == '__main__':
	main()