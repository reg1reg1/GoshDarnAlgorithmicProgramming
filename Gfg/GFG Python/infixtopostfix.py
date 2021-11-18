'''
Problem statement
Convert an infix expression to a postfix expression
Expression will have single digit numbers and paranthesis
Significance of postfix is that compiler avoids multiple scanning of expression in this form.
and it becomes much easier to evaluate
'''

from ysinghStack import *
def isNumber(x):
	if ord(x) in range(48,58):
		return True
	return False

def getPriority(x):
	if x == '(':
		return 0
	if x =='+' or x == '-':
		return 1
	if x == '*':
		return 2
	if x == '/':
		return 3
	if x == ')':
		return 4
def main():
	t= int(input().strip())
	for i in range(t):
		stack=Stack()
		str1= input().strip()
		n = len(str1)
		for i in range(n):
			if isNumber(str1[i]):
				print(str1[i],end="")
				continue
			else:
				if stack.empty():
					#push char if stack empty
					#print("PUSHED",str1[i])
					stack.push(str1[i])
					continue

				priority = getPriority(str1[i])
				priorTop = getPriority(stack.top())
				if priority > priorTop:
					stack.push(str1[i])
					#print("Pushed high prior ",str[i])
				else:
					while priority <= priorTop and stack.empty() is False:
						if(stack.top()!='(' and stack.top()!=')'):
							print(stack.top(),end="")
						stack.pop()
						priorTop = getPriority(stack.top())
					stack.push(str1[i])
		while stack.empty() is False:
			#print("Emptying out the stack")
			if(stack.top()!='(' and stack.top()!=')'):
				print(stack.top(),end="")
			stack.pop()
			print()

if __name__ == '__main__':
	main()





