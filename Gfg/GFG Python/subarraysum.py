'''
First subarray with given sum
We could have done by storing inplace the sum array instead of the input array
GFG status: Accepted
Programmed in a tricky way which must be avoided in timed contests
(Took a lot of time to figure out the edge cases and index increment to get the prog to work as expected)
In a timed contest, do not hesitate to repeat lines of code to cover edge cases.
'''

def main():
	t = int(input().strip())
	for i in range(t):
		numinp  = input().strip()
		numlist = list(map(int,numinp.split(" ")))
		num = numlist[1]
		n = numlist[0]
		arrayinp = input().strip()
		arraylist = list(map(int,arrayinp.split(" ")))
		start = 0
		fin = 0
		ssum = arraylist[0]
		while True:
			if ssum ==  num:
				#print("FOUND")
				break
			if ssum < num:
				#last element reached but sum still less
				if fin == n-1:
					break
				fin+=1
				ssum = ssum+arraylist[fin]
				#print("Sum has become ",ssum)
				continue
			if ssum > num:
				if start == fin:
					if start == n-1:
						break
					start+=1
					fin+=1
					ssum=arraylist[start]
					#print("Sum has become ",ssum)
					continue
				ssum=ssum-arraylist[start]
				#print("Sum has become ",ssum)
				start+=1



		if ssum == num:
			print(start+1,fin+1)
		else:
			print("-1")

if __name__=="__main__":
	main()