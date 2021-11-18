#https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
consider
0. abcdef
1. aa
2. ababa
3. abcdefgcbd
4. a
5. abcdabcd
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	letterDict={}
    	maxLen=0
    	currLen=0
    	st=0
    	fin=0
    	while(fin < len(s)):
    		if s[fin] not in letterDict:
    			letterDict[s[fin]]=fin
    			currLen+=1
    			if maxLen<currLen:
    				maxLen=currLen
    		else:
    			temp = st
    			st = letterDict[s[fin]]+1
    			currLen=currLen-(st-temp)+1
    			j=temp
    			k=st
    			while(j!=k):
    				del letterDict[s[j]]
    				j+=1
    			letterDict[s[fin]]=fin
    			#print(currLen,fin)	
    		fin+=1
    	return maxLen


def main():
	sol =  Solution()
	print(sol.lengthOfLongestSubstring("a"))
	print(sol.lengthOfLongestSubstring("abcdefa"))
	print(sol.lengthOfLongestSubstring("aaa"))
	print(sol.lengthOfLongestSubstring("pwwkew"))
	print(sol.lengthOfLongestSubstring("tmmzuxt"))

if __name__ == '__main__':
	main()