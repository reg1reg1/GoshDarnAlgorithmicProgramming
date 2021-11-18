'''
Author: reg1reg1
Longest common subsequence
'''

def LCS(str1,str2):
	x=len(str1)
	y=len(str2)

	#x is the no of columns
	#y is the no of rows
	dp = [[0]*(x+1) for i in range(y+1)]

	for i in range(1,y+1):
		for j in range(1,x+1):
			if str1[j-1]!=str2[i-1]:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
			else:
				dp[i][j]=1+dp[i-1][j-1]
	
	#For printing the computation matrix
	for i in range(1,y+1):
		for j in range(1,x+1):
			print(dp[i][j],end=" ")
		print()
	
	
	#which letters were chosen
	i=y
	j=x
	value=dp[y][x]
	#move towards the top left
	chars=[]
	while i!=0 and j!=0:
		if dp[i-1][j]==value:
			i=i-1
			continue
		if dp[i][j-1]==value:
			j=j-1
			continue
		chars.append(str2[i-1])
		i=i-1
		j=j-1
		value=dp[i][j]
	
	#print chars
	while chars:
		print(chars.pop(),end=">")
	print()
	return dp[y][x]

def main():
	x="ENCIRCLE"
	y="NOTICE"
	print("Length of LCS is ",LCS(x,y))


if __name__ == '__main__':
	main()





		