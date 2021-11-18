

def minv(a,b):
	if a < b:
		return a
	return b

def maxv(a,b):
	if a > b:
		return a
	return b


class Stack():

	def __init__(self):
		self.__stacklist = list()
		self.__top=-1

	def top(self):
		return self.__stacklist[self.__top];

	def pop(self):
		if self.__top is not -1:
			self.__top = self.__top - 1
			#print("TOP pos val :",self.__top)
	
	def push(self,data):
		self.__top = self.__top + 1
		self.__stacklist.insert(self.__top,data)

	def empty(self):
		if self.__top is -1:
			return True
		else:
			return False
	
	def size(self):
		return self.__top+1

t=int(input())
for i in range(0,t):
	p=int(input())
	stack = Stack()
	array = input().strip()
	inplist = list(map(int, array.split(" ")))
	#stack.push(0)
	i=0
	maxarea=inplist[0]
	while i < len(inplist):
		if stack.empty() or inplist[stack.top()] < inplist[i]:
			stack.push(i)
			#print("Pushed :",inplist[i])
			i= i+1
		else:
			toppos = stack.top()
			stack.pop()
			#print("Popped :",inplist[toppos])
			if stack.empty():
				area = inplist[toppos] * i
				#print("area calculated as :",area)
			else:
				area = inplist[toppos] * (i-stack.top()-1)
				#print("area calculated as :",area)
			if area > maxarea:
				maxarea=area
	
	while stack.empty() is False:
			toppos = stack.top()
			#print("Popped end:",inplist[toppos])
			stack.pop()
			if stack.empty():
				area = inplist[toppos] * i
			else:
				area = inplist[toppos] * (i-stack.top()-1)
			if area > maxarea:
				maxarea=area

	print(maxarea)
	








		


