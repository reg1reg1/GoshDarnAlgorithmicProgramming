'''
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Verdict : TLE ( Building the graph can be time consuming) O(n2). Our path may not even touch all
         words in the dictionary whose size may be huge. 
Solution: use BFS on the go
'''
from collections import defaultdict
from collections import deque
from typing import List
def isEdge(str1,str2):
	#constraint all words have same length
	strSize=len(str1)
	c=0
	for i in range(strSize):
		if str1[i]!=str2[i]:
			c+=1
	#c cannot be zero as there are no duplicate words in the dictionary
	return c==1 

class Graph():
	def __init__(self,adj=None):
		if adj is None:
			self.adjlist=defaultdict(set)
		else:
			self.adjlist=adj	
	def addEdge(self,u,v):
		self.adjlist[u].add(v)
		self.adjlist[v].add(u)

	def bfs(self,source,destination):
		visited = {}
		for v in self.adjlist:
			visited[v]=0
		if destination not in self.adjlist:
			return 0
		if source not in self.adjlist:
			return 0
		aQ = deque()
		aQ.append(source)
		visited[source]=1
		while len(aQ)!=0:
			vertex = aQ.popleft()
			for u in self.adjlist[vertex]:
				if visited[u]==0:
					visited[u]=visited[vertex]+1
					aQ.append(u)
				if u==destination:
					return visited[u]
		#There was no path from source to destination
		if visited[destination]==0:
			return 0

class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		wSize=len(wordList)
		found=0
		g = Graph()
		for i in range(wSize):
			if wordList[i]==endWord:
				found=1

		if found==0:
			return found
		wordList.append(beginWord)
		wSize+=1
		for i in range(wSize):
			for j in range (i,wSize):
				if isEdge(wordList[i],wordList[j]):
					#print("Adding edge ",wordList[i],wordList[j])
					g.addEdge(wordList[i],wordList[j])
		return g.bfs(beginWord,endWord)

def main():
	beginWord= input().strip()
	endWord = input().strip()
	wordList = list(map(str,input().strip().split(" ")))
	s = Solution()
	print(s.ladderLength(beginWord,endWord,wordList))

if __name__ == '__main__':
	main()


