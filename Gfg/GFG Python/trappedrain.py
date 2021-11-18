'''
Trapped rainwater
Solution 1: With O(2n) extra space
'''
def mmax(x,y):
	if x>y:
		return x
	return y
def mmin(x,y):
	if x>y:
		return y
	return x

def main():
	t=int(input().strip())
	for i in range(t):
		n = int(input().strip())
		arrinp = input().strip()
		a = list(map(int,arrinp.split(" ")))
		if(n<3):
			print("0")
		else:
			water=0
			#creating 2 arrays for storing maxleft and maxright
			maxleft=[0]*(n-2)
			#print(maxleft)
			maxright= [0]*(n-2)
			mleft=a[0]
			mright=a[n-1]

			for i in range(1,n-1):
				#print(i,end=" ")
				mleft=mmax(mleft,a[i])
				maxleft[i-1]=mleft
			#print()
			for i in range(n-2,0,-1):
				#print(i,end=" ")
				mright=mmax(mright,a[i])
				maxright[i-1]=mright
			#print()
			#Summing up the water collected
			#print(maxleft)
			#print(maxright)
			for i in range(n-2):
				#print(i,end="")
				varx=mmin(maxleft[i],maxright[i])
				if varx>a[i+1]:
					water+=varx-a[i+1]
			print(water)
if __name__ == '__main__':
	main()




