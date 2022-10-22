class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l=len(nums)
        totsum=nums[0]
        mmax=nums[0]
        currmax=nums[0]
        #Basic Kadane, candidate 1
        for i in range(1,l):
            currmax=max(nums[i],nums[i]+currmax)
            mmax=max(currmax,mmax)
            totsum+=nums[i]
        a1=mmax
        currmax=-1*nums[0]
        mmax=currmax
        #Calculate 2nd candidate, calculate what is left out in circarray. Flip sign, kadane
        # The numbers not taken in by kadane is 2nd candidate
        for i in range(1,l):
            currmax=max(nums[i]*(-1),nums[i]*(-1)+currmax)
            mmax=max(currmax,mmax)
            
        #Case where entire array might get ignored. 
        if mmax!=0 and mmax!= (-1)*totsum:
            a2=totsum + mmax
        else:
            a2=a1
        
        #print(a2,a1)
        return max(a2,a1)