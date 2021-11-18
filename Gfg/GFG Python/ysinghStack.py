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


