class Solution:
	def longestPalindromeSubseq(self, s: str) -> int:
		n = len(s)
		cache = [[0]*n for x in range(n) ]
		#init
		for i in range(n):
			cache[i][i]=1
		i=1
		j=1
		while j<n:
			k=j
			i=0
			while i<n and k<n:
				if s[i]==s[k]:
					cache[i][k]=2+cache[i+1][k-1]
				else:
					cache[i][k]=max(cache[i][k-1],cache[i+1][k])
				i+=1
				k+=1
			j=j+1
		#print(cache[0][n-1])
		'''
		for i in cache:
			print(i)
		'''
		i=0
		j=n-1
		value=cache[0][n-1]
		xlist=[]
		flag=-1
		centre="a"
		while i<n and j>=0 and cache[i][j]>0:
			
			if i+1<n and cache[i+1][j]==value:
				i+=1
				#print("Down ",i)
				value=cache[i][j]
				continue
			if j-1>=0 and cache[i][j-1]==value:
				j-=1
				#print("left ",j)
				value=cache[i][j]
				continue
			if i+1>=n or j-1<=0:
				mod=0
			else:
				mod=cache[i+1][j-1]
			if abs(value-mod)%2==0:
				xlist.append(s[i])
			else:
				flag=0
				centre=s[i]
			if i+1>=n or j-1<=0:
				break 
			value=cache[i+1][j-1]
			i+=1
			j-=1
		
		#print("XLIST",xlist)
		str1=""
		for i in xlist:
			str1+=i
		#print(str1,centre)
		str2=str1[::-1]
		if flag!=-1:
			str1+=centre
		str3=str1+str2
		return len(str3)
		#calculate which letters were chosen for the solution


def main():
	t= Solution()
	print(t.longestPalindromeSubseq("aabcdebaz"))
if __name__ == '__main__':
	main()
