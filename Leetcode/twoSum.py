from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        p=-1
        q=-1
        for i in range(len(nums)):
            if target-nums[i] in x:
                q=i
                p=x[target-nums[i]]
                break
            x[nums[i]]=i
        return [p,q]