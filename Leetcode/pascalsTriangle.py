class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		output= []
		for i in range(numRows):
			row=[]
			for j in range(i+1):
				#surrounded by 1 on each level of triangle
				if j==0 or j==i:
					row.append(1)
				else:
					row.append(output[i-1][j]+output[i-1][j-1])
			output.append(row)
		return output
