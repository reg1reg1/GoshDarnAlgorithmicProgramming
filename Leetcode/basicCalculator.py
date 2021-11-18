class Solution:
	def __init__(self):
		self.__expr__=[]
		self.__tokens__=[]
	
	@staticmethod
	def isNumber(x)->bool:
		#print("CHECK ",x,"VALUE:",ord(x))
		if ord(x)<48 or ord(x)>57:
			return False
		return True

	def whiteSpaceTokenize(self,str1):
		x=list(map(str,str1.split()))
		#print(x)
		for item in range(len(x)):
			if Solution.isNumber(x[item][0]):
				x[item]=int(x[item]) 
		return x

	def tokenize(self,str1):
		x = 0
		while x < len(str1):
			#print(x)
			if Solution.isNumber(str1[x]):
				i=x
				#print("st: ",i)
				str2=""
				while i<len(str1) and Solution.isNumber(str1[i]):
					str2+=str1[i]
					i=i+1
					#print(str2)
				#print("en: ",i)
				x=i
				self.__tokens__.append(int(str2))
			else:
				self.__tokens__.append(str1[x])
				x=x+1
		return self.__tokens__
	
	@staticmethod
	def getPriority(x):
		if x=="+" or x=="-":
			return 0
		if x=="*":
			return 1
		if x=="/":
			return 2
		return -9

	def infixToPostfix(self,list1):
		#For storing the answer
		expr=[]
		#tempstack
		stack=[]
		for token in list1:
			if type(token) is int:
				expr.append(token)
			elif len(stack)==0:
				stack.append(token)	
			else:
				if token=="(":
					stack.append(token)
				elif token ==")":
					#expression is assummed to be valid
					while stack[len(stack)-1]!="(" and len(stack)!=0:
						val=stack.pop()
						if(Solution.getPriority(val)>=0):
							expr.append(val)
					stack.pop()
				else:
					'''
					Handle the normal operator case
					'''
					priority=Solution.getPriority(token)
					priorityTop=Solution.getPriority(stack[len(stack)-1])
					if priorityTop>=0:
						while len(stack)!=0 and priority<=priorityTop:
							val = stack.pop()
							expr.append(val)
							if len(stack)==0:
								break
							priorityTop=Solution.getPriority(stack[len(stack)-1])
						stack.append(token)
					else:
						stack.append(token)


		while len(stack)!=0:
			val=stack.pop()
			if(Solution.getPriority(val)>=0):
				expr.append(val)
		return expr
	@staticmethod
	def resolve(b1,expr,b2):
		if expr=="+":
			return b2+b1
		if expr=="-":
			return b2-b1
		if expr=="*":
			return b2*b1
		if expr=="/":
			return b2/b1
	@staticmethod
	def solveEq(list1):
		#stack based
		stack=[]
		for items in list1:
			if type(items) is int:
				stack.append(items)
			else:
				b1=stack.pop()
				b2=stack.pop()
				stack.append(Solution.resolve(b1,items,b2))
			#print(stack)
		return stack.pop()



	def calculate(self, s: str) -> int:
		#print("".join(s.split()))
		l1=self.tokenize("".join(s.split()))
		#print(l1)
		l2=self.infixToPostfix(l1)
		#print(l2)
		return Solution.solveEq(l2)

def main():
	x1="(1+1)"
	x= Solution()
	print(x.calculate(x1))

if __name__ == '__main__':
	main()