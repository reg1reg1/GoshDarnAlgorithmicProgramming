
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


t=int(input().strip())
for i in range(0,t):
	stackobj = Stack()
	inpstring=input().strip()
	flag = True
	for i in range(0,len(inpstring)):
		
		if inpstring[i] in ('[','(','{'):
			#print("PUSHED:",inpstring[i])
			stackobj.push(inpstring[i])
			continue

		if inpstring[i] in (']',')','}') and stackobj.empty() is True:
			#print("Stack empty and brace came along")
			flag=False
			break
		elif (']',')','}').index(inpstring[i]) != ('[','(','{').index(stackobj.top()):
			#print("stack non empty, non matching brace")
			flag=False
			break
		else:
			#print("POPPED ",stackobj.top())
			stackobj.pop()

	if not stackobj.empty():
		flag=False
	if flag:
		print("balanced")
	else:
		print("not balanced")






