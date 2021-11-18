from typing import List
class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
		#people.sort(key=lambda x:x[1])
		#people.sort(key=lambda x: x[0], reverse=True)
		#people.sort(key=lambda x:x[1])
		people.sort(key=lambda x:x[0],reverse=True)
		
		ans=[]
		#insertion of sorted elements
		#insert function takes care of duplicates.
		#If the index is higher it will simply place it at the first lower index
		for x in people:
			ans.insert(x[1],x)

		return ans



def main():
	s = Solution()
	x = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
	print(s.reconstructQueue(x))


if __name__ == '__main__':
	main()

