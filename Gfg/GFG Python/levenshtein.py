def levenshtein(x,y):
	m=len(x)
	n=len(y)
	#n is the no of columns
	#m is the no of rows
	
	Ac=1
	Sc=1
	Dc=1

	#Transforming String x to String y
	dp=[[0]*(n+1) for j in range(m+1)]
	
	for i in range(0,m+1):
		for j in range(0,n+1):

			#important case
			if i==0:
				dp[i][j] = j
			elif j==0:
				dp[i][j]= i
			elif x[i-1]==y[j-1]:
				dp[i][j]=dp[i-1][j-1]
			else:
				dp[i][j]=min(Ac+dp[i][j-1],Sc+dp[i-1][j-1],Dc+dp[i-1][j])
	
	for i in range(0,m+1):
		for j in range(0,n+1):
			print(dp[i][j],end=" ")
		print()
	return dp[m][n]

def main():
	x="sunday"
	y="saturday"
	print(levenshtein(x,y))

if __name__ == '__main__':
	main()