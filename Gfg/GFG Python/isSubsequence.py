class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		slen=len(s)
		tlen=len(t)
		if tlen<slen:
			return False

		i,j,k=0,0,0
		while i < slen and j< tlen:
			if s[i]==t[j]:
				i+=1
			
			j+=1
		
		return i==slen

def main():
	a="axc"
	b="azcdddac"
	s=Solution()
	print(s.isSubsequence(a,b))


if __name__ == '__main__':
	main()