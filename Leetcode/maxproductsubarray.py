class Solution:
    def maxProduct(self, a: List[int]) -> int:
        maxProdPos=nums[1]
        minProdNeg=nums[1]
        overallMax=nums[1]
        atleast1Posval=0
        for i in nums:
            #max out of the current element, currentelem*maxpositiveproduct, minproductending here*a[i] (assign it to temp as we need to calculate minProdNeg before the assignment)
            temp=max(max(maxProdPos*a[i],a[i]),a[i]*minProdNeg)
            #negative product so far here
            minProdNeg=min(min(a[i],a[i]*minProdNeg),a[i]*maxProdPos)

            maxProdPos=temp
            
            overallMax=max(overallMax,maxProdPos)
        return overallMax