'''
Minimum no of jumps
Dynamic Programming
'''
INT_MAX=9999999
def minJump(jumpArray):
	n=len(jumpArray)
	dp=[0]*(n)
	
	for j in range(n-2,-1,-1):
		#print("VALUE",jumpArray[j],"index ",j)
		x=jumpArray[j]
		if x==0:
			dp[j]=INT_MAX
		else:	
			if x>=n-j-1:
				dp[j]=1
			else:
				ans=INT_MAX
				for m in range(j+1,j+1+jumpArray[j]):
					#print(m,end=" ")
					ans = min(ans,dp[m])
				if dp[j]<INT_MAX:
					dp[j]=1+ans
				else:
					dp[j]=ans
	if dp[0]<INT_MAX:
		return dp[0]
	return -1

def main():
	
	t= int(input().strip())
	i=0
	while i<t:
		n=int(input().strip())
		astr = input().strip()
		jump= list(map(int,astr.split(" ")))
		print(minJump(jump))
		i=i+1

if __name__ == '__main__':
	main()