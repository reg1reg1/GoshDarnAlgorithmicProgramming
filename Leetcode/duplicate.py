from typing import List
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		s=0
		f=0
		t = 0
		
		#If there is no duplicate, this will cause this loop to run into infinite
		#Solution is to check the sum or prod of array and if it is equal to fact(n) or Summation(n)
		#not to proceed with below
		while True:
			s = nums[s]
			f = nums[nums[f]]
			
			if s == f:
				break
		#Detect where the cycle begins in a LL
		while True:
			
			s = nums[s]
			t = nums[t]
			
			if s == t:
				break
		
		return t
		
def main():
	x = list(map(int,input().strip().split(" ")))
	s = Solution()
	print(s.findDuplicate(x))

if __name__ == '__main__':
	main()