from typing import List

class Solution:
	def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
		colsOrig=len(mat[0])
		rowsOrig=len(mat)
		if r*c!=colsOrig*rowsOrig:
			return mat
		newMat = [[0]*c for x in range(r)]
		print(newMat)
		r1=1
		c1=1
		r2=1
		c2=1
		print(r,c,rowsOrig,colsOrig)
		while r2<=r:
			print("(",r1,c1,") (",r2,c2," )")
			newMat[r2-1][c2-1]=mat[r1-1][c1-1]

			if c1%(colsOrig)==0:
				r1+=1
				c1=0
			if c2%(c)==0:
				r2+=1
				c2=0
			c1+=1
			c2+=1
		return newMat




def main():
	inpMat=[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
	s=Solution()
	print(s.matrixReshape(inpMat,4,3))
	

if __name__ == '__main__':
	main()