'''
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
'''
#modified b search to find first elem >=K in the array
from typing import List

class Solution:
	def hIndex(self, citations: List[int]) -> int:
    	lsize=len(citations)
    	low=0
    	high=lsize
    	while low<high:
    		mid = int((low+high+1)/2)
    		if citations[lsize-mid]>=mid:
    			low = mid
    		else:
    			high = mid-1

    	return low

def main():
	l = list(map(int,input().strip().split(" ")))
	s=Solution()
	print(s.hIndex(l))

if __name__ == '__main__':
	main()