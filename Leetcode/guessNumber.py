class Solution:
	def guessNumber(self, n: int) -> int:
		
		num=n//2
		
		while guess(num)!=0:
			
			if guess(num)==-1:
				num=num-num//2-1
			if guess(num)==1:
				num=num+num//2+1
		return num
