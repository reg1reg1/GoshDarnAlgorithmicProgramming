import heapq
import math
from typing import List


class Solution:
	def calcdistance(self,x1,x2):
		return math.sqrt(x1*x1+x2*x2)
	def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
		arr=[]
		distpoints =[(self.calcdistance(x[0],x[1]),[x[0],x[1]]) for x in points]
		#Build Heap takes O(n)
		heapq.heapify(distpoints)
		ans=[]
		for i in range(K):
			ans.append(heapq.heappop(distpoints)[1])
		return ans


		
				

def main():
	s= Solution()
	print(s.kClosest([[1,2],[2,3],[4,3],[0,-1]],2))

if __name__ == '__main__':
	main()
			