def main():
	t = int(input().strip())
	stack=[]
	S=""
	stack.append(S)
	for i in range(t):
		line=input().strip()
		elem= line.split()
		operation = int(elem[0])
		if operation==1:
			string = elem[1]
			S+=string
			stack.append(S)
		elif operation==2:
			num = int(elem[1])
			S = S[:-num]
			print("After deletion ",S)
			stack.append(S)
		elif operation ==3:
			num = int(elem[1])
			print(S[num-1])
		else:
			stack.pop()
			S=stack[len(stack)-1]
if __name__ == '__main__':
	main()