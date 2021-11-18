'''
DP-13
GeeksforGeeks Dynamic Programming Rod cutting problem


'''
def retMin(price):
	n=len(price)
	cost=1
	dp=[[0]*(n+1) for i in range(n+1)]
	s=[]
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i<j:
				dp[i][j]=dp[i][j-1]
			else:
				if i==j:
					dp[i][j]=max(price[j-1]+dp[i-j][j],dp[i][j-1])
				else:
					dp[i][j]=max(price[j-1]+dp[i-j][j]-cost,dp[i][j-1])
			if dp[i][j]!=dp[i][j-1]:# indicates that a cut was made
				s.append(j)
	for i in range(0,n+1):
		for j in range(0,n+1):
			print(dp[i][j],end=" ")
		print()
	print(s)
	return dp[n][n]
def main():
	price=[1,6,8,9,10]
	t = int(input().strip())
	i = 0
	while i<t:
		u=input().strip()
		price=list(map(int,u.split(" ")))
		print(retMin(price))
		i=i+1

if __name__ == '__main__':
	main()