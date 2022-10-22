class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax=nums[0]
        mmax=nums[0]
        #start=0,end=0
        for i in range(1,len(nums)):
            #update start and end indexes here
            #if nums[i]>currmax+nums[i], update start=i,end=i
            #else end=i 
            currmax=max(nums[i],currmax+nums[i])
            
            #update max start and max end here (storing the start and beginning of max contiguoous subarray if currmax>mmax)
            #update both maxStart and maxEnd
            mmax=max(currmax,mmax)
            
           # print(currmax,mmax)
        return mmax