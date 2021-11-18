
def reverse(exp):
	stackList = []
	x=""
	i=0
	while i < len(exp):		
		#while numbers
		if (ord(exp[i]) > 47 and ord(exp[i]) < 58) or (ord(exp[i])==46):
			x= ""
			while (ord(exp[i])> 47 and ord(exp[i]) < 58) or (ord(exp[i])==46):
				x = x + exp[i]
				i =i+1
				if i >= len(exp):
					break
			stackList.append(x)
			continue
		else:
			stackList.append(exp[i])
			i=i+1
			continue
	y=""
	for i in range(len(stackList)):
		y=y+stackList.pop()
	return y

def main():
	str1 = input().strip()
	print(reverse(str1))

if __name__ == '__main__':
	main()

