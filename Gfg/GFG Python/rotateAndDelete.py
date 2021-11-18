def main():
	t = int(input().strip())
	for i in range(t):
		size = int(input().strip())
		arr = list(map(int,input().strip().split()))
		if len(arr)%2==0:
			print(arr[(len(arr)//2)-1])
		else:
			print(arr[len(arr)//2])

if __name__ == '__main__':
	main()