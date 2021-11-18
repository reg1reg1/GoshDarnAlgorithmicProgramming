from typing import List
class Solution:
	# take second element for sort
	
	def twoCitySchedCost(self, costs: List[List[int]]) -> int:
		x= len(costs)
		#print(x)
		aCost =0
		def takeSecond(elem):
			return elem[1]
		for i in range(x):
			aCost+=costs[i][0]
			costs[i][1]=costs[i][1]-costs[i][0]
		#print(costs)
		#print(aCost)
		costs.sort(key=takeSecond)
		ref=0
		for i in range(x//2):
			ref+=costs[i][1]

		aCost+=ref
		
		return aCost
def main():
	s= Solution()
	x= [[10,20],[30,200],[400,50],[30,20]]
	print(s.twoCitySchedCost(x))

if __name__ == '__main__':
	main()