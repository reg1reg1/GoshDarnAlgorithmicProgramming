
#minimize the no of unique elements in window of size d in array of size n
# n size of array
# d size of window
# k max limit of elem value in array
def main():
	t = int(input().strip())
	for i in range(t):
		inpLine1 = list(map(int,input().strip().split(" ")))
		n = inpLine1[0]
		k = inpLine1[1]
		d = inpLine1[2]
		a = list(map(int,input().strip().split(" ")))
		countHash = [0]*(k+1)
		#print("Initial ",countHash)
		#uniqCount = set()
		minLen=-1
		start=0
		fin=start+d-1
		#sliding window initial
		#print("start",start,"fin",fin)
		for i in range(fin+1):
				countHash[a[i]]+=1
		minLen=0
		#print(countHash)
		for i in range(1,k+1):
			if(countHash[i]!=0):
				#print(i," present in window")
				minLen+=1
		
		#print("Initial minLen ",minLen)
		
		#you cannot change size of window
		#print(uniqCount)
		ansLen=minLen
		start=start+1
		fin=fin+1
		#print(minLen)
		while fin < len(a):
			#print("start ",start,"fin ",fin)
			#print("vstart",a[start])
			if countHash[a[start]] >=1:
				countHash[a[start]]-=1
				if countHash[a[start]]==0:
					#print("removed ",a[start])
					minLen=minLen-1
			start+=1
			fin+=1
			if(fin<len(a)):
				
				if countHash[a[fin]]==0:
					#print("Added ",a[fin])
					minLen=minLen+1
				#countHash[a[start]]+=1
				countHash[a[fin]]+=1
				if ansLen>minLen:
					ansLen=minLen
			

		print(ansLen)




if __name__ == '__main__':
	main()



