def main():
	t= int(input().strip())
	while t>0:
		n = int(input().strip())
		arr = list(map(int,input().strip().split()))
		dep = list(map(int,input().strip().split()))
		xarr=[]

		for i in range(len(dep)):
			xarr.append((arr[i],1))
			xarr.append((dep[i],-1))
		#print(xarr)
		sortarr=sorted(xarr,key= lambda x : x[0])[::]
		#print(sortarr)
		mmax=-1
		q=0
		for i in sortarr:
			q+=i[1]
			if q>mmax:
				mmax=q
		print(mmax)
		t-=1
if __name__ == '__main__':
	main()