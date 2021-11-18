import sys

'''
Array can have all real numbers 
Special care is to be taken when encountering negative numbers or fractional numbers
mpos to the max value that was found till there
mneg refers to the least value that could be found
mmax refers to the maximum product 

It is to be noted that for input where array has only a negative number or zero ourput is 0
If there is only 1 negative number in array , output is that negative number

Logic is that at each position we can either carry on the subsequence by taking the number 
or break the ongoing subsequence by ignoring the number and start a new subsequence with 
that number as the first element
'''

def smax(x,y):
	if x>y:
		return x
	return y
def smin(x,y):
	if x<y:
		return x
	return y

def main():
	t = int(input().strip())
	for i in range(t):
		inp = input().strip()
		alist = list(map(float,inp.split(" ")))
		print(alist)
		mpos=float(sys.maxsize*(-1))
		mneg=float(1)
		mmax=float(sys.maxsize*(-1)) #(Any large negative number (use some library in python))
		print(mpos,mneg,mmax)
		for i in range(0,len(alist)):
			#print('POSITION',i)
			if alist[i]>0:
				mpos=smax(alist[i],mpos*alist[i])
				mneg=smin(mneg,smin(1.0,mneg*alist[i]))
			
			elif alist[i]==0:
				mpos=0.0
				mneg=1.0
			else:
				temp = mpos
				mpos = smax(alist[i],alist[i]*mneg)
				mneg = smin(alist[i],temp*alist[i])
				#print("mpos changed to",mpos)
				#print("mneg changed to",mneg)
			mmax = smax(mpos,mmax)
			if mpos<=0:
				mpos=1
			#print("Max now",mmax)
			#print("----------------------------")
		print(mmax)

if __name__ == '__main__':
	main() 