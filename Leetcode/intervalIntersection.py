from typing import List
class Solution:
	def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
		aL = len(A)
		bL = len(B)
		i=0
		j=0
		ans=[]
		iStart=-1
		iFin=-1
		#Assuming x1<y1 and x2<y2
		while i < aL and j< bL:

			iStart=max(A[i][0],B[j][0])
			iFin=min(A[i][1],B[j][1])
			#print(iStart,iFin)
			#no interval may be pushed
			if iStart<=iFin:
				ans.append([iStart,iFin])
			
			if iFin==A[i][1]:
				i+=1
			else:
				j+=1
		return ans

def main():
	s = Solution()
	l1 =[[1,5]]
	l2= [[7,9],[10,13],[11,18]]
	print(s.intervalIntersection(l1,l2))



if __name__ == '__main__':
	main()