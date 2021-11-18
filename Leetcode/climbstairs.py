'''
Have to climb n stairs
Can climb only 1 or 2 steps 
Determine no of ways you can climb n stairs
'''

class Solution:
	def climbStairs(self, n: int) -> int:
		memoize=[(-1) for x in range(n+1)]
	
		def solve(n):
			if n<0:
				return 0

			if n==0:
				return 1
			
			if memoize[n]!=-1:
				return memoize[n]

			

			

			memoize[n]=solve(n-1)+solve(n-2)
			return memoize[n]
		return(solve(n))

def main():
	x = int(input().strip())
	s = Solution()
	print(s.climbStairs(x))

if __name__ == '__main__':
	main()