from collections import defaultdict


def def_value(): 
	return 0

class Solution:
	def frequencySort(self, s: str) -> str:
		alphaDict = defaultdict(def_value)
		for i in s:
			alphaDict[i]+=1
		sort_alpha = sorted(alphaDict.items(), key=lambda x: x[1], reverse=True)
		ans=""
		for i in sort_alpha:
			ans+=i[0]*i[1]
		return ans
def main():
	s = Solution()
	print(s.frequencySort("abcadabbcad"))

if __name__ == '__main__':
	main()