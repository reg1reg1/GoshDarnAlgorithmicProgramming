from typing import List
import sys
#merge two sortted lists
def mergerTwo(A,B)->list:
	Y=[]
	sizeA=len(A)
	sizeB=len(B)
	if sizeA==0 and sizeB==0:
		return None
	elif sizeB==0:
		return A
	elif sizeA==0:
		return B
	else:
		p1=0
		p2=0
		while p1<sizeA or p2<sizeB:
			if p2>=sizeB: #append all of remaining A to Y
				while p1<sizeA:
					Y.append(A[p1])
					p1+=1
			elif p1>=sizeA:
				while p2<sizeB:
					Y.append(B[p2])
					p2+=1
			else:
				if A[p1]<B[p2]:
					Y.append(A[p1])
					p1+=1
				else:
					Y.append(B[p2])
					p2+=1
	return Y







def mergeSortUtil(X,low,high):
	#print(low,high)
	if low>=high:
		return [X[high]]#single-element list


	mid=int(low+((high-low)/2))
	#print(mid)
	#sys.exit(0)
	list_left=mergeSortUtil(X,low,mid)
	list_right=mergeSortUtil(X,mid+1,high)
	
	return mergerTwo(list_left,list_right)


def mergeSort(X)->list:
	
	arrSize=len(X)
	low=0
	high=arrSize-1
	#print("mergeSort:61 ",low,high)
	return mergeSortUtil(X,low,high)

def main():
	inpstring=input().strip()
	inpArr=list(map(int,inpstring.split(" ")))

	print("Input :",inpArr)
	x=mergeSort(inpArr)
	print("Output: ",x)

if __name__ == '__main__':
	main()