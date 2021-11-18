import sys
import os


'''
@Stack
General implementation of stack in python
functions
top()
pop()
push()
empty()
size()
'''
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
	count=0
	answer = []
	p=int(input())
	stack = Stack()
	array = input().strip()
	inplist = list(map(int, array.split(" ")))
	answer.append(1)
	stack.push(0)
	for i in range(1,len(inplist)):
		#print("At value:",inplist[i])
		while(inplist[stack.top()]  <= inplist[i] and stack.empty() is False):
			#print("POPPED",stack.top())
			stack.pop()

		if stack.empty() is True:
			#print("IF:added",i+1)
			answer.append(i+1)
		else:
			#print("ELSE:added",i-stack.top())
			answer.append(i-stack.top())
			
		#print("PUSHED",i)
		stack.push(i)
		#print()
	for i in range (0,len(answer)):
		print(answer[i],end=" ")
	print(" ")










