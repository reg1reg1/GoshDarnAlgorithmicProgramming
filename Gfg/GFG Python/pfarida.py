

'''
input:
1
5
10 2 3 4 5 1 10 100
'''

def maxval(a,b):
	if a>b:
		return a
	return b





t = int(input().strip())
for i in range(0,t):
	n = int(input().strip())
	dp=[0]*n
	array=input().strip()
	a = list(map(int, array.split()))
	if(n > 1):
		dp[0]=a[0]
		dp[1]=maxval(a[0],a[1])
		for i in range (2,n):
			dp[i]=maxval(dp[i-1],dp[i-2]+a[i])
		print("Case %d:%d"%(t,dp[n-1]))
	else:
		print("Case %d:%d"%(t,a[0]))