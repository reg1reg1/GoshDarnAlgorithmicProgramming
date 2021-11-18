'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
from collections import defaultdict
from typing import List
class Graph():
	def __init__(self):
		self.adjList=defaultdict(set)
		self.visited=set()
	def addVertex(self,u):
		self.adjList[u]=set()
	def addEdge(self,u,v):
		self.adjList[u].add(v)

	def DFSUtil(self,u):
		visited=self.visited
		visited.add(u)
		for v in self.adjList[u]:
			if v not in visited:
				self.DFSUtil(v)

	def DFS(self):
		visited=self.visited
		count=0
		for u in self.adjList:
			if u not in visited:
				self.DFSUtil(u)
				count+=1
		return count

		

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		rows=len(grid)
		if rows <=0:
			return 0
		cols=len(grid[0])

		
		g= Graph()

		#build graph
		for i in range(rows):
			for j in range(cols):
				if grid[i][j]=="1":
					g.addVertex((i,j))
					if i>0:
						g.addEdge((i,j),(i-1,j))
					if j>0:
						g.addEdge((i,j),(i,j-1))
					if i<rows-1:
						g.addEdge((i,j),(i+1,j))
					if j<cols-1:
						g.addEdge((i,j),(i,j+1))
				else:
					g.visited.add((i,j))

		return g.DFS()
def main():	
	nRows=int(input().strip())
	inp=[]*nRows
	for i in range(nRows):
		inp.append(list(map(str,input().strip())))
	print(inp)
	s = Solution()
	print(s.numIslands(inp))

if __name__ == '__main__':
	main()