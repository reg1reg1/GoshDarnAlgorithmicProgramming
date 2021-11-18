class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		x=len(text1)
		y=len(text2)
		dp = [[0]*(y+1) for i in range(x+1)]
		for i in range(1,x+1):
			for j in range(1,y+1):
				if text1[i-1]==text2[j-1]:
					dp[i][j]=1+dp[i-1][j-1]
				else:
					dp[i][j]=max(dp[i-1][j],dp[i][j-1])
		return dp[x][y]
def main():
	x = input().strip()
	y = input().strip()
	s = Solution()
	print(s.longestCommonSubsequence(x,y))
if __name__ == '__main__':
	main()
