def minimumBribes(q):
	ans=0
	for i in range(len(q)):
		if q[i]-(i+1)>2:
			return "Too chaotic"

	#bubble sort, calculate how many swaps were performed (Reverse sorted is the initial state)
	for i in range(len(q)-1):
		for j in range(len(q)-1):
			if q[j] > q[j+1]:
				q[j],q[j+1] = q[j+1],q[j]
				sw = True
				ans+=1
		#Reset swp bool for the next inner loop.
		#If there were no swaps performed, you can simply exit the entire loop as the   array will be already sorted.
		if sw:
			sw = False
		else:
			break
	print(ans)
	return ans

def main():
	t = int(input().strip())
	while t!=0:
		size = int(input().strip())
		arr = list(map(int,input().strip().split()))
		print(arr)
		print(minimumBribes(arr))
		t-=1
if __name__ == '__main__':
	main()