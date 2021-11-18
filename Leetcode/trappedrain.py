from typing import List
def mmax(x,y):
	if x>y:
		return x
	return y
def mmin(x,y):
	if x<y:
		return x
	return y

class Solution:
	def trap(self, height: List[int]) -> int:
		n = len(height)
		if(n<3):
			return 0
		else:
			water=0
			#creating 2 arrays for storing maxleft and maxright
			maxleft=[0]*(n-2)
			#print(maxleft)
			maxright= [0]*(n-2)
			mleft=height[0]
			mright=height[n-1]

			for i in range(1,n-1):
				#print(i,end=" ")
				mleft=mmax(mleft,height[i])
				maxleft[i-1]=mleft
			#print()
			for i in range(n-2,0,-1):
				#print(i,end=" ")
				mright=mmax(mright,height[i])
				maxright[i-1]=mright
			#print()
			#Summing up the water collected
			#print(maxleft)
			#print(maxright)
			for i in range(n-2):
				#print(i,end="")
				varx=mmin(maxleft[i],maxright[i])
				if varx>height[i+1]:
					water+=varx-height[i+1]
			return water
def main():
	l = list(map(int,input().strip().split(" ")))
	s = Solution()
	print(s.trap(l))

if __name__ == '__main__':
	main()