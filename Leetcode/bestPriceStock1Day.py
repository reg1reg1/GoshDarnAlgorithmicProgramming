class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        cp=prices[0]
        for i in range(1,len(prices)):
            #always take the minimum buy price so far (traversing from left 0->n)
            if cp > prices[i]:
                cp=prices[i]

            else:
                maxProf=max(maxProf,prices[i]-cp)
        return maxProf