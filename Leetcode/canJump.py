'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p=nums[0] #index of farthest potion can reach for now
        for i in range(1,len(nums)):
            if p>=i:
                p = max(p, nums[i]+i)
        return p>=len(nums)-1



def main():
	n = list(map(int,input().strip().split(" ")))
	s = Solution()
	print(s.canJump(n))

if __name__ == '__main__':
	main()