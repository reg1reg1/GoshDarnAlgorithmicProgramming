import copy
class DirectedGraph():
	
	def __init__(self,adjList=None):
		self.__adjacencylist__={}
		self.cycle=False

	def topoSort(self):
		self.topoStack=[]
		self.color={}
		for v,v_adj in self.__adjacencylist__.items():
			self.color[v]="white"

		for v,adj_v in self.__adjacencylist__.items():
			if self.color[v]=="white":
				self.__DFSMain(v,True)
		return self.topoStack

	#Returns a DirectedGrph instance which is a transpose
	def returnTranspose(self):
		#transPose of adjacencylist
		transposeSelf= DirectedGraph()
		for v,uList in self.__adjacencylist__.items():
			for u in uList:
				transposeSelf.addEdge(u,v)
		return transposeSelf

	def sccKosaraju(self):
		localStack=[]
		visited={}

		def kosarajuDFS(G,v):
			visited[v]=True
			print(v,end=" ")
			for u in G.__adjacencylist__[v]:
				if visited[u]==False:
					kosarajuDFS(G,u)
			localStack.append(v)
			print("\n")

		#beginDfsKosaraju
		for v in self.__adjacencylist__:
			visited[v]=False
		#Traversing graph to fill the stack
		for v,uList in sorted(self.__adjacencylist__.items()):
			if visited[v]==False:
				 kosarajuDFS(self,v)

		print(localStack)



		#Prepare for the second dfs on transpose of the graph		 
		visited={}
		gtranspose = self.returnTranspose()
		print(localStack)
		for v in gtranspose.__adjacencylist__:
			visited[v]=False
		
		print("SCC as follows:")
		while len(localStack)>0:
			u=localStack.pop()
			if visited[u]==False:
				kosarajuDFS(gtranspose,u)
				print("SCC-------BOUNDARY")
		


	def isCycle(self):
		self.DFStraversal()
		return self.cycle

	def bfsTraversal(self,u):
		pass

	#Is there a path from u to v
	def isRoute(self,u,v):
		if self.DFStraversal(u,v)=="white":
			return False
		return True

	def addEdges(self,v,u):
		if v not in self.__adjacencylist__:
			self.__adjacencylist__[v]=[]
		for x in u:
			if x not in self.__adjacencylist__:
				self.__adjacencylist__[x]=[]
			if x not in self.__adjacencylist__[v]:
				self.__adjacencylist__[v].append(x)	


	def addEdge(self,v,u):
		if v not in self.__adjacencylist__:
			self.__adjacencylist__[v]=[]
		if u not in self.__adjacencylist__:
			self.__adjacencylist__[u]=[]
		self.__adjacencylist__[v].append(u)

	def sortAdjacencyList(self):
		for v in self.__adjacencylist__:
			self.__adjacencylist__[v].sort()

		
	
	def printAdjacencyList(self):
		for key,value in sorted(self.__adjacencylist__.items()):
			print(key,":",value)

	def DFStraversal(self,a=None,b=None):
		self.color={}
		self.timeTuple={}
		self.time=0
		#Initialization
		
		for v,v_adj in sorted(self.__adjacencylist__.items()):
			self.color[v]="white"
			self.timeTuple[v]=[0,0]

		if a is None and b is None:
			for v,v_adj in sorted(self.__adjacencylist__.items()):
				if self.color[v]=="white":
					self.__DFSMain(v)
		elif b is None:
			self.__DFSMain(a)

		else:
			self.__DFSMain(a)
			return self.color[b]


		print("END")
		print("---------Finishing and Discovery times---------")
		for key,value in sorted(self.timeTuple.items()):
			print("Key ",key,value)
	

	def __DFSMain(self,v,topo=False):

		#These things are not required by topological sort
		if topo is False:
			print(v,"--> ",end=" ")
			self.time=self.time+1
			self.timeTuple[v][0]=self.time
		
		self.color[v]="grey"
		

		for u in sorted(self.__adjacencylist__[v]):
			if self.color[u]=="white":
				self.__DFSMain(u,topo)
			#checking for cycle( or backedge)
			if self.color[u]=="grey":
				self.cycle=True
		
		
		if topo:
			self.topoStack.insert(0,v)
		else:
			self.time=self.time+1
			self.timeTuple[v][1]=self.time
		self.color[v]="black"
		

def main():
	print("GRAPH-----------------------G2")
	G1= DirectedGraph()
	G1.addEdge("q","w")
	G1.addEdge("q","t")
	G1.addEdge("q","s")
	G1.addEdge("r","y")
	G1.addEdge("r","u")
	G1.addEdge("s","v")
	G1.addEdge("t","y")
	G1.addEdge("t","x")
	G1.addEdge("u","y")
	G1.addEdge("v","w")
	G1.addEdge("w","s")
	G1.addEdge("x","z")
	G1.addEdge("y","q")
	G1.addEdge("z","x")

	G1.sortAdjacencyList()
	G1.printAdjacencyList()
	G1.DFStraversal("q")
	print(G1.isCycle())
	print("Path ?",G1.isRoute("z","t"))

	print("GRAPH-----------------------G2")
	G2= DirectedGraph()
	G2.addEdges("m",["q","r","x"])
	G2.addEdges("n",["o","q","u"])
	G2.addEdges("o",["r","s","v"])
	G2.addEdges("p",["o","s","z"])
	G2.addEdges("q",["t"])
	G2.addEdges("r",["u","y"])
	G2.addEdges("s",["r"])
	G2.addEdges("u",["t"])
	G2.addEdges("v",["w","x"])
	G2.addEdges("w",["z"])
	G2.addEdges("y",["v"])

	#G2.DFStraversal("m")
	print("G2 Topologicalsort ",G2.topoSort())

	print("GRAPH---------------------------g3")

	G3= DirectedGraph()

	G3.addEdges("a",["i","h"])
	G3.addEdges("b",["c","a"])
	G3.addEdge("c","m")
	G3.addEdge("d","i")
	G3.addEdges("e",["a","m"])
	G3.addEdge("f","d")
	G3.addEdge("g","f")
	G3.addEdges("h",["f","c"])
	G3.addEdge("i","g")
	G3.addEdge("m","h")
	G3.sortAdjacencyList()
	G3.printAdjacencyList()
	G3.sccKosaraju()
	G4 = G3.returnTranspose()
	G4.printAdjacencyList()



if __name__ == '__main__':
	main()
		