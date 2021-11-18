'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''
import sys
from typing import List
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		coinNum = len(coins)
		solve= [0 for i in range(amount+1)]
		solve[0]=0 #base case

		for i in range(1,amount+1):
			solve[i]=sys.maxsize

		for i in range(1,amount+1):
			for j in range(coinNum):
				if coins[j]<=i:
					ans=solve[i-coins[j]]
					if ans!=sys.maxsize and ans+1<solve[i]:
						solve[i]=ans+1

		if solve[amount]==sys.maxsize:
			return -1		
		return solve[amount]
def main():
	amount = int(input().strip())
	l = list(map(int,input().strip().split(" ")))
	s = Solution()
	print(s.coinChange(l,amount))

if __name__ == '__main__':
	main()