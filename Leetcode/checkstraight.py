from typing import List
class Solution:
	def slopeF(self,pt1,pt2) -> float:
		if pt1[0]-pt2[0]!=0:
			return (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
		return float('inf')

	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		if len(coordinates)<=2:
			return True
		p1=coordinates[0]
		p2=coordinates[1]
		if p1[0]-p2[0]!=0:
			slope=(p1[1]-p2[1])/(p1[0]-p2[0])
		else:
			slope=float('inf')
		flag = True
		for i in range(1,len(coordinates)-1):
			if slope!=self.slopeF(coordinates[i],coordinates[i+1]):
				flag=False
				break

		return flag

def main():
	s = Solution()
	coordinates=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

	print(s.checkStraightLine(coordinates))

if __name__ == '__main__':
	main()