#Edit string modifying question (levenshtein's) distance on leetcode


class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m = len(word1)
		n = len(word2)
		mCost=1
		#here n is the no of columns which is length of 2nd word +1 
		#m is the no of rows which size of the first word plus 1
		dp = [[0]*(n+1) for i in range(m+1)]
		#print(dp)

		for i in range(0,m+1):
			for j in range(0,n+1):
				if i==0:
					dp[i][j]=j
				elif j==0:
					dp[i][j]=i
				elif word1[i-1]==word2[j-1]:
					dp[i][j]=dp[i-1][j-1]
				else:
					dp[i][j]=mCost+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
		return dp[m][n]
 



def main():
	x = input().strip()
	y = input().strip()
	s = Solution()
	print(s.minDistance(x,y))
if __name__ == '__main__':
	main()
