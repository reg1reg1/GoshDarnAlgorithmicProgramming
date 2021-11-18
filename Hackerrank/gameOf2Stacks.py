import os
import sys
fwrite = open("output.txt","w+")
def twoStacks(x,a,b):
	
	tsum=0
	count=0
	aSum=[]
	bSum=[]
	aSum.append(0)
	bSum.append(0)
	aTot=0
	bTot=0
	for i in range(len(a)):
		aTot+=a[i]
		aSum.append(aTot)
	for i in range(len(b)):
		bTot+=b[i]
		bSum.append(bTot)
	indexA = len(a)
	indexB = len(b)
	maxcount=-1
	bigArr=[]
	smallArr=[]
	right=0
	left=0
	llimit=-1
	print(aSum)
	print(bSum)
	while indexA!=0 and aSum[indexA]>x:
		indexA-=1
	while indexB!=0 and bSum[indexB]>x:
		indexB-=1
	if indexA>indexB:
		right=indexA
		llimit=indexB
		maxcount=indexA
		currSum= aSum[indexA]
		bigArr=aSum
		smallArr=bSum
	else:
		right=indexB
		llimit=indexA
		maxcount=indexB
		currSum=bSum[indexB]
		bigArr=bSum
		smallArr=aSum
	#print("INITIAL:left ",left,"INITIAL:right ",right)
	left =0
	initSum=0
	#print("llimit ",llimit)
	if right==0 and left ==0:
		return 0
	while left<=llimit or right>0:
		#print("left ",left," right ",right)
		#make sure right and left are valid indices when they hit this statement
		initsum = bigArr[right]+smallArr[left]
		#print("initsum ",initsum)
		if initsum<=x:
			count=left+right
			
			if count > maxcount:
				#print("UPDATED at ",left,"<<<<left:right>>>>",right)
				maxcount=count
			
			left+=1
			if left >llimit:
				break
		else:
			if right==0:
				break
			right-=1
	return maxcount

def main():
	g = int(input())

	for g_itr in range(g):
		nmx = input().split()

		n = int(nmx[0])

		m = int(nmx[1])

		x = int(nmx[2])

		a = list(map(int, input().rstrip().split()))

		b = list(map(int, input().rstrip().split()))

		result = twoStacks(x, a, b)
		#fwrite.write(str(result))
		#fwrite.write("\n")
		print(result)


if __name__ == '__main__':
	main()