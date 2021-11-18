'''
3 sum problem on leetcode																																																																																													`1
'''
from typing import List
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		#sort the array
		lsize= len(nums)
		nums.sort()

		ansList=set()
		for i in range(lsize):
			k=nums[i]
			reqd=0-k
			start = i+1
			fin = lsize-1
			while start<fin:
				if reqd<nums[start]+nums[fin]:
					fin-=1					
				elif reqd>nums[start]+nums[fin]:
					start+=1
				else:
					#print(k,nums[start],nums[fin] ,"::: ")
					ansList.add((k,nums[start],nums[fin]))
					start+=1
					fin-=1
		formAns=[]			
		for i in ansList:	
			x=[]
			x.append(i[0])
			x.append(i[1])
			x.append(i[2])
			formAns.append(x)
		return formAns

def main():
	x=list(map(int,input().split(" ")))
	s= Solution().threeSum(x)
	print(s)

if __name__ == '__main__':
	main()
