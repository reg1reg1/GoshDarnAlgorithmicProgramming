


#Divided by 1000
suffix=["","Thousand","Million","Billion"]
num = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens= ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
teens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

'''
test cases : 
Divide the number in groups of 3
1
11,12,13
20,45,34
234
245
1000
1234
1003
12,456
234,689
100000
102034234

'''


class Solution:
	def convtonum(self, numbers: str) -> str:
		global num
		global tens
		global teens

		#Converting to number and back to string to remove leading 0's example from the triplet 056
		gnum=int(numbers)
		numbers=str(gnum)
		
		if gnum==0:
			return ""
		#100-999
		str1=""
		if len(numbers)==3:
			str1+=num[int(gnum/100)]+" Hundred "

		tnum=gnum%100
		#100,109,119,219 (singles, teens)
		#100,200,300
		if tnum==0:
			return str1.strip()
		#101,102,109,110,119,219
		if tnum>0 and tnum<=19:
			ttnum=int(tnum/10)
			
			#100------109
			if ttnum==0:
				sing=tnum%10
				str1+=num[sing]+" "
			#10--------19
			else:
				teen=tnum%10
				str1+=teens[teen]+" "
				
		else:
			ttnum=int(tnum/10)
			modn=tnum%10
			str1+=tens[ttnum]+" "
			str1+=num[modn]+" "
		return str1.strip()


	def numberToWords(self, num: int) -> str:
		global suffix
		numt=str(num)
		if num==0:
			return "Zero"
		wordStr=[]
		ct=0
		while numt!="":

			if len(numt)>=3:
				numw=numt[-3:]
				#print("numconv ",numw)

				numt=numt[:-3]
				#print("numt ",numt)
			else:
				numw=numt
				numt=""
				#print("numt ",numt)
			if int(numw)!=0:
				strw=self.convtonum(numw)+" "+suffix[ct]
			else:
				strw=self.convtonum(numw)
			#print("strw ",strw)
			wordStr.append(strw.strip())
			ct+=1

		
		str1=""
		#print(wordStr)	
		while wordStr:
			str1=str1+wordStr.pop()+" "

		return " ".join(str1.split())

def main():
	num = int(input().strip())
	s = Solution().numberToWords(num)
	print(s)


if __name__ == '__main__':
	main()