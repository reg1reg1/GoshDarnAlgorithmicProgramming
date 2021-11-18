#https://leetcode.com/problems/check-if-it-is-a-straight-line/
'''
Consider
1. [[0,0],[1,2],[2,4],[3,6]] y=2x
2. [[0,0],[1,2],[2,3],[3,4]] y = x+1
3. [[0,0],[1,-1],[2,-2],[3,-5]] invalid line
4. [[0,0],[1,-1],[2,-2],[-4,4],[2,-2],[3,-3]]
'''
from typing import List

class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    	if len(coordinates)<=2:
    		return True
    	else:
    		x1 = coordinates[0][0]
    		y1 = coordinates[0][1]
    		x2 = coordinates[1][0]
    		y2 = coordinates[1][1]

    		d= y1-y2
    		c= x1-x2

    		st=2
    		while st<len(coordinates):
    			if (coordinates[st][1]-y1)*(c) != (coordinates[st][0]-x1)*(d):
    				return False
    			st+=1
    		return True 



def main():
	sol =Solution()
	print(sol.checkStraightLine([[0,0],[1,2],[2,4],[3,6]]))
	print(sol.checkStraightLine([[0,1],[1,2],[2,3],[3,4]]))
	print(sol.checkStraightLine([[0,0],[1,-1],[2,-2],[3,-5]]))
	print(sol.checkStraightLine([[0,0],[1,-1],[2,-2],[-4,4],[2,-2],[3,-3]]))


if __name__ == '__main__':
	main()