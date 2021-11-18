#https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings/0/?ref=self
#https://practice.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string/0
#
#geeks considers string candidates only with minLen=2
def countPallinDromicSubstring(s):
	slen= len(s)
	dist=set()
	memoiz = [[False]*slen for i in range(slen)]
	tot=0
	if(slen>=1):
	 	i=0
	 	while i<slen:
	 		memoiz[i][i]=True
	 		dist.add(s[i:i+1])
	 		tot+=1
	 		i+=1
	#print(tot)
	if(slen>=2):
		i=0
		while i<slen-1:
			if s[i]==s[i+1]:
				memoiz[i][i+1]=True
				dist.add(s[i:i+2])
				tot+=1
			i+=1
	#print(tot)
	strLen=3
	#counting how many pallindromes exist of this size.

	while strLen<=slen:
		i = 0
		while i<slen-strLen+1:
			j=i+strLen-1
			#print(i,"<>",j)
			if s[i]==s[j] and memoiz[i+1][j-1]:
				tot+=1
				memoiz[i][j]=True
				dist.add(s[i:j+1])
			else:
				memoiz[i][j]=False
			i+=1
		strLen+=1
	return len(dist)

def main():
	t = int(input().strip())
	for i in range(t):
		lenstr = int(input().strip())
		inpstr = input().strip()
		print(countPallinDromicSubstring(inpstr))


if __name__ == '__main__':
	main()