def main():
	t = int(input().strip())
	for i in range(t):
		ans=0
		inp = input().strip()
		alist = list(map(float,inp.split(" ")))
		a=alist[0]
		b=alist[1]
		c=alist[2]
		x=0
		y=0
		x += min(int(b/2),a)*3
		remb=b-2*min(int(b/2),a)
		if(remb>0):
			x+=min(int(c/2),remb)*3
		
		y+=min(int(c/2),b)*3
		remb=b-min(int(c/2),b)
		if(remb>0):
			y+=min(int(remb/2),a)*3
		print(int(x)," ",int(y))
		ans=max(int(x),int(y))
		print(ans)
if __name__ == '__main__':
	main()