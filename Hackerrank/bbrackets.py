
def returnType(x):
	if x=="{" or x=="}":
		return 1
	elif x=="(" or x==")":
		return 2
	else:
		return 3

def balancedBrackets(string):
	stack = []
	n = len(string)
	for i in range(n):
		#print(string[i])
		if string[i]=="(" or string[i]=="{" or string[i]=="[":
			stack.append(string[i])
			#print("PUSHED ",string[i])
		else:
			if len(stack)==0:
				return "NO"
			s= stack.pop()
			#print("POPPED ",s)
			if returnType(s)!=returnType(string[i]):
				return "NO"
	if len(stack)!=0:
		return "NO"
	return "YES"

def main():
	l1= ["[]","{{}}[][](){{(())}}","{","[[[[","[]]]]]]"]
	for i in l1:
		print(i)
		print(balancedBrackets(i))

if __name__ == '__main__':
	main()