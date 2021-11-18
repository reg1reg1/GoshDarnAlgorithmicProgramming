'''
Count the no of pallindromic substrings in 
the given string

'''

class Solution:
	def countSubstrings(self, s: str) -> int:
		#pallindromic substring of length 1
		n=len(s)
		count=0
		optim=[[False]*len(s) for x in range(len(s))]
		for i in range(len(s)):
			optim[i][i]=True
			count+=1
		#pallindromic substring of length 2
		for i in range(n-1):
			if s[i]==s[i+1]:
				count+=1
				optim[i][i+1]=True
		#length 3 onwards
		k=3
		
		while k<=n:
			#print("K ",k)
			for i in range(n-k+1):
				j=i+k-1
				#print("i ",i," j",j)
				if s[i]==s[j] and optim[i+1][j-1]:
					optim[i][j]=True
					count+=1
				else:
					optim[i][j]=False
			#print("=-------------")
			k+=1
		#print(start,fin)
		return count




def main():
	t= Solution()
	print(t.countSubstrings("abaab"))

if __name__ == '__main__':
	main()