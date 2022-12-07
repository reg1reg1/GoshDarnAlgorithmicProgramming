from typing import List
class Solution:
	def largestPerimeter(self, nums: List[int]) -> int:
		if len(nums)==3:
			g=max(nums)
			s=nums[0]+nums[1]+nums[2]
			if s-g<=g:
				return 0
		nums.sort()
		inpS=len(nums)
		j=inpS-1
		output=0
		while j>=2:
			print(j)
			if nums[j]>=nums[j-1]+nums[j-2]:
				j-=1
			else:
				output=nums[j]+nums[j-1]+nums[j-2]
				break
		return output

def main():
	s=Solution()
	x=[1,2,2,3,4,9,19]
	print(s.largestPerimeter(x))

if __name__ == '__main__':
	main()