def solve(arr):
	val = arr[0]%2
	for i in arr:
		if i%2!=val:
			arr.sort()
			return arr
	return arr
	



def main():
	t= int(input().strip())
	lineinp=input().strip()
	arr= list(map(int,lineinp.split()))
	gp=solve(arr)
	for i in gp:
		print("{} ".format(i),end="")
main()