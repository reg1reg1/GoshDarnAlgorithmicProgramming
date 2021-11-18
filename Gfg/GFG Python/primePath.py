'''
Given 2 4 digit prime nos
Find the shortest prime path from one to another.
'''
primes=[]

from collections import defaultdict
from collections import deque
class Graph():
	def __init__(self,adjList=None):
		self.adjList=defaultdict(set)
	#Undirected graph
	def addEdge(self,u,v):
		# u and v are indexes in primeset
		#Adjacency list is a dictionary 
		#Each key is mapped to a set
		self.adjList[u].add(v)
		self.adjList[v].add(u)

	def bfs(self,u,v):
		#visited is a dictionary
		visited={}
		#queue will store nodes.
		q = deque()
		

		for x in self.adjList:
			visited[x]=0
		
		q.append(u)
		visited[u]=1
		while len(q)!=0:
			edge = q.popleft()
			#iterating over a set
			for x in self.adjList[edge]:
				if visited[x]==0:
					q.append(x)
					#print("visited",primes[x],end=" ")
					# We do this step to calculate path on the go
					visited[x]=visited[edge]+1
				if x==v:
					#already added in the last call
					return visited[x]-1
			#print("\n\n\n")		 


#Calculate all 4 digit prime numbers between n1 and n2
def sieveOfErastothenes():
	n=9999
	p=2
	pList = [True]*(10000)
	
	while p*p<=n:
		if pList[p]==True:
			for i in range(p*p,n+1,p):
				pList[i]=False
		p+=1
	pSet=[]
	for i in range(1000,10000):
		if pList[i]:
			pSet.append(i)
	return pSet

def isPath(n1,n2):
	nStr1= str(n1)
	nStr2= str(n2)
	c=0
	if nStr1[0]!=nStr2[0]:
		c+=1
	if nStr1[1]!=nStr2[1]:
		c+=1
	if nStr1[2]!=nStr2[2]:
		c+=1
	if nStr1[3]!=nStr2[3]:
		c+=1
	if c==1:
		return True
	return False

def shortPrimePath(n1,n2):
	global primes
	primes=sieveOfErastothenes()
	#print("Primes ",primes)
	graph = Graph()
	for i in range(len(primes)):
		for j in range(i+1,len(primes)):
			if isPath(primes[i],primes[j]):
				graph.addEdge(i,j)
	x1=0
	x2=0
	for i in range(len(primes)):
		if n1==primes[i]:
			x1=i
		if n2==primes[i]:
			x2=i
	print("indices",x1," ",x2)
	return graph.bfs(x1,x2)	

def main():
	n1 = int(input().strip())
	n2 = int(input().strip())
	print(shortPrimePath(n1,n2))
if __name__ == '__main__':
	main()