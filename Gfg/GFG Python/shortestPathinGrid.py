'''
Given a grid
find shortest path between 2 cells
Some cells cannot be traversed (marked with 0)
Input : ['0', '*', '0', 's'],
		['*', '0', '*', '*'],
		['0', '*', '*', '*'],
		['d', '*', '*', '*']
Output : 6
If no path exists print -1
'''

import sys
from collections import deque
from collections import defaultdict
class Graph():
	def __init__(self,adjList=None):
		self.adjList=defaultdict(set)

	def addEdge(self,tuple1,tuple2):
		self.adjList[tuple1].add(tuple2)

	def bfs(self,source,destination,matrix):
		Q = deque()
		visited={}
		
		#marking blocking cells as already visited
		for v in self.adjList:
			if matrix[v[0]][v[1]]=='0':
				visited[v]=1
			else:
				visited[v]=0

		Q.append(source)
		visited[source]=1
		while len(Q)!=0:
			tup = Q.popleft()
			for v in self.adjList[tup]:
				if visited[v]==0:
					Q.append(v)
					visited[v]=visited[tup]+1
				if v==destination:
					return visited[v]-1


def findPath(matrix):
	G = Graph()
	cols = len(matrix[0])
	rows = len(matrix)
	source=tuple()
	dest=tuple()
	#populate the graph
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j]!='0':
				if j>0 and matrix[i][j-1]!='0':
					G.addEdge((i,j),(i,j-1))
				if j<cols-1 and matrix[i][j+1]!='0':
					G.addEdge((i,j),(i,j+1))
				if i>0 and matrix[i-1][j]!='0':
					G.addEdge((i,j),(i-1,j))	
				if i< rows-1 and matrix[i+1][j]!='0':
					G.addEdge((i,j),(i+1,j))
			if matrix[i][j]=='s':
				source=(i,j)
			if matrix[i][j]=='d':
				dest=(i,j)
	return G.bfs(source,dest,matrix)		


def main():
	pair=list(map(int,input().strip().split(" ")))
	cols=pair[1]
	rows=pair[0]
	matrix = [['0']*(cols+1) for x in range(rows+1)]
	i=0
	while i < rows:
		matrix[i] = list(map(str,input().strip().split(" ")))
		i+=1
	print(matrix)
	print(findPath(matrix))

if __name__ == '__main__':
	main()