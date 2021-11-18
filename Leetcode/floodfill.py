from typing import List
class Solution:

	def DFS(self,image,sr,sc):
		#We do not need to traverse the forest
		#Assuming grid is rectangular
		self.visited.add((sr,sc))
		image[sr][sc]=self.newColor
		
		if sr<self.rowlen-1:
			if image[sr+1][sc]==self.color and (sr+1,sc) not in self.visited:
				self.DFS(image,sr+1,sc)
		
		if sc<self.collen-1:
			if image[sr][sc+1]==self.color and (sr,sc+1) not in self.visited:
				self.DFS(image,sr,sc+1)

		if sr>0:
			if image[sr-1][sc]==self.color and (sr-1,sc) not in self.visited:
				self.DFS(image,sr-1,sc)
		if sc>0:
			if image[sr][sc-1]==self.color and (sr,sc-1) not in self.visited:
				self.DFS(image,sr,sc-1)


			

	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		

		self.visited=set()
		self.color=image[sr][sc]
		self.newColor=newColor

		image[sr][sc]=newColor
		
		
		self.rowlen=len(image)
		self.collen=len(image[0])
		
		self.DFS(image,sr,sc)
		return image

def main():
	x= [[0,0,0],[0,0,1]]
	c = 2
	s= Solution()
	print(s.floodFill(x,0,0,2))

if __name__ == '__main__':
	main()





		
