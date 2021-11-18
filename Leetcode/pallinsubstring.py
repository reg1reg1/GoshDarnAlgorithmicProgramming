'''
Longest pallindromic substring in a given strin
Problem Class: Dynamic Programming, Strings

'''

class Solution:
	def __init__(self):
		self.optim=[[False]*1000 for x in range(1000)]

	def longestPalindrome(self, s: str) -> str:
		#pallindromic substring of length 1
		n=len(s)
		start=-1
		fin=-1
		for i in range(len(s)):
			self.optim[i][i]=True
			start=i
			fin=i
		maxlen=1
		#pallindromic substring of length 2
		for i in range(n-1):
			if s[i]==s[i+1]:
				maxlen=2
				start =i
				fin=i+1
				self.optim[i][i+1]=True
		#length 3 onwards
		k=3
		
		while k<=n:
			#print("K ",k)
			for i in range(n-k+1):
				j=i+k-1
				#print("i ",i," j",j)
				if s[i]==s[j] and self.optim[i+1][j-1]:
					self.optim[i][j]=True
					if k>maxlen:
						start = i
						fin = j
						maxlen=k
				else:
					self.optim[i][j]=False
			#print("=-------------")
			k+=1
		#print(start,fin)
		return s[start:fin+1]





def main():
	t= Solution()
	print(t.longestPalindrome("a"))

if __name__ == '__main__':
	main()

