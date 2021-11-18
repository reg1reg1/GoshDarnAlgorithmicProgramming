from collections import defaultdict
class Solution:
	# prerequisites 
	def DFS(self,node):
		self.visited[node]="grey"

		for i in self.adjacencyList[node]:
			if self.visited[i]=="white":
				self.DFS(i)
			if self.visited[i]=="grey":
				self.cycle=True
				break

		self.visited[node]="black"

	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		
		def defaultvalue():
			return "white"

		self.cycle=False
		self.visited=defaultdict(defaultvalue)
		self.adjacencyList={}

		#Build the adjacency List
		for i in prerequisites:
			if i[0] not in self.adjacencyList:
				self.adjacencyList[i[0]]=[]
			if i[1] not in self.adjacencyList:
				self.adjacencyList[i[1]]=[]

			self.adjacencyList[i[0]].append(i[1])


		#The DFS begins
		for node,adjList in self.adjacencyList.items():
			if self.visited[node]=="white":
				self.DFS(node)

		return not self.cycle