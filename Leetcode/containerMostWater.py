'''
Slightly different variation of the trapped rainwater problem
'''
from typing import List

def mmax(x,y):
	if x>y:
		return x
	return y

def mmin(x,y):
	if x>y:
		return y
	return x



class Solution:
	def maxArea(self, height: List[int]) -> int:
		fin=len(height)-1
		start = 0
		mProd=0
		while start < fin:
			prod=mmin(height[start],height[fin])*(fin - start)
			mProd=mmax(mProd,prod)

			if height[start]>height[fin]:
				fin-=1
			else:
				start+=1
		return mProd


def main():
	num = list(map(int,input().strip().split(" ")))
	#print(num)
	s = Solution()
	print(s.maxArea(num))


if __name__ == '__main__':
	main()