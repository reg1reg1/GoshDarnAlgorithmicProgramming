def main():
	arr = list(map(int,input().strip(" ").split()))
	
	d1= arr[0]
	d2= arr[1]
	ans=-1
	

	if d1==9 and d2==1:
		d1=d1*10+9
		d2=d1+1
		print(d1,d2)
		return

	if d1>d2 or d2-d1>1:
		print(-1)
		return

	if d1==d2:
		d1=d1*10+1
		d2=d1+1
	else:
		d1=d1*10+9
		d2=d1+1

	print(d1,d2)
if __name__ == '__main__':
	main()
