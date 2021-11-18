'''
Program to reverse a stack using recursion
'''
from ysinghStack import *
#Utility function to hold members in the function stack
def reverseStack(stack):
	if stack.empty() is False:
		temp = stack.top()
		stack.pop()
		reverseStack(stack)
		insertatEnd(stack,temp)




def insertatEnd(stack,data):
	if stack.empty() is True:
		stack.push(data)
	else:
		temp = stack.top()
		stack.pop()
		insertatEnd(stack,data)
		stack.push(temp)

def main():
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	reverseStack(stack)


if __name__ == '__main__':
	main()