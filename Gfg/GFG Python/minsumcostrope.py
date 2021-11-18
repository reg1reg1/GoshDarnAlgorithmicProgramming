
import heapq
def minCostSumRope(x):
	heapq.heapify(x)
	sumv=0
	while len(x)!=0:
		a1=heapq.heappop(x)
		#print("a1",a1)
		
		a2=heapq.heappop(x)
		#print("a2",a2)
		c=a1+a2
		
		sumv+=c
		if len(x)==0:
			break
		#print("SUMV",sumv)
		heapq.heappush(x,c)
		#print("HEAP",x)
	#print("sumv",sumv)
	return sumv


def main():
	t = int(input().strip())
	
	while t>0:
		n = int(input().strip())
		arr = list(map(int,input().strip().split()))
		print(minCostSumRope(arr))
		t-=1

if __name__ == '__main__':
	main()