from typing import List
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		cnt=1
		ch = nums[0]
		n=len(nums)
		for i in range(1,n):
			if nums[i]==ch:
				cnt+=1
			else:
				cnt-=1
				if cnt==0:
					ch=nums[i]
					cnt=1
			#print(cnt,i)

		cnt=0
		for i in nums:
			if ch==i:
				cnt+=1
		
		if cnt>n//2:
			return ch
		return -1

def main():
	s=Solution()
	x=[1,2,4,1,1,1]
	print(s.majorityElement(x))

if __name__ == '__main__':
	main()
