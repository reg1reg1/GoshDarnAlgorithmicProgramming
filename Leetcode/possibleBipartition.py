from typing import List
from collections import defaultdict
from collections import deque
class Solution:
	def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
		if len(dislikes)==0:
			return True
		self.adjList={}
		self.ans=True
		def coldef():
			return -1
		self.color=defaultdict(coldef)
		self.visited=set()
		for j in range(1,N):
			self.adjList[j]=[]
		for j in dislikes:
			if j[0] not in self.adjList:
				self.adjList[j[0]]=[]
			if j[1] not in self.adjList:
				self.adjList[j[1]]=[]
			self.adjList[j[0]].append(j[1])
			self.adjList[j[1]].append(j[0])
		

		dQ = deque()
		#Case of disjoint forest
		for k in range(1,N):
			if k not in self.visited:
				dQ.append(k)
			#coloring the start node
			self.color[k]=0
			self.visited.add(k)

			while len(dQ)!=0:
			
				node = dQ.popleft()
				for i in self.adjList[node]:
					if i not in self.visited and self.color[i]==-1:
						self.visited.add(i)
						dQ.append(i)
						#print("Visiting ",i)
						self.color[i]=self.color[node]^1
						#print("Coloring ",i," ",self.color[i])
						continue

					if self.color[i]^self.color[node]==0:
						return False
					
		return True				


def main():
	s=Solution()
	n=5
	x=[[1,2],[3,4],[4,5],[3,5]]
	print(s.possibleBipartition(5,x))
if __name__ == '__main__':
	main()


