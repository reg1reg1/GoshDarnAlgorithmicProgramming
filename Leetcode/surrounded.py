from collections import deque
from collections import defaultdict
from typing import List
class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""

		
		#Put all the hero O's
		rowNum=len(board)
		if rowNum<=0:
			return
		colNum=len(board[0])
		


		#print("Row and col",rowNum," ",colNum)
		oQ= []
		#Traverse the top,left,right and bottom borders
		
		

		visited=set()
		#top and bottom rows

		
		for j in range(colNum):
			if board[0][j]=='O':
				oQ.append((0,j))

			if board[rowNum-1][j]=='O':
				oQ.append((rowNum-1,j))


		#left and right columns
		for i in range(1,rowNum-1):
			if board[i][0]=='O':
				oQ.append((i,0))

			if board[i][colNum-1]=='O':
				oQ.append((i,colNum-1))


		#print("Initial oQ",oQ)

		#BFS over Forest
		bfsQ= deque()
		
		for i in range(len(oQ)):
			if oQ[i] not in visited:
				bfsQ.append(oQ[i])
				visited.add(oQ[i])

			while len(bfsQ)!=0:
				src = bfsQ.popleft()

				srcR=src[0]
				srcC=src[1]

				#traverse 4 adjacent dirns

				#bottom
				if srcR<rowNum-1:
					if board[srcR+1][srcC]=='O' and (srcR+1,srcC) not in visited:
						bfsQ.append((srcR+1,srcC))
						visited.add((srcR+1,srcC))
				#top
				if srcR>0:
					if board[srcR-1][srcC]=='O' and (srcR-1,srcC) not in visited:
						bfsQ.append((srcR-1,srcC))
						visited.add((srcR-1,srcC))
				#left
				if srcC>0:
					if board[srcR][srcC-1]=='O' and (srcR,srcC-1) not in visited:
						bfsQ.append((srcR,srcC-1))
						visited.add((srcR,srcC-1))

				if srcC<colNum-1:
					if board[srcR][srcC+1]=='O' and (srcR,srcC+1) not in visited:
						bfsQ.append((srcR,srcC+1))
						visited.add((srcR,srcC+1))
		'''
		print("contents of visited")
		for val in visited:
			print(val)
		print(">>")
		'''
		for i in range(rowNum):
			for j in range(colNum):
				if board[i][j]=='O' and (i,j) not in visited:
					board[i][j]='X'

def main():
	x=[['X' ,'X', 'X', 'X'],['X', 'O', 'O' ,'X'],['X', 'X' ,'O', 'X'],['X' ,'O' ,'X' ,'X']]
	s= Solution()
	s.solve(x)
	for i in x:
		print(i)



if __name__ == '__main__':
	main()