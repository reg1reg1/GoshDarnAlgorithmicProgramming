'''
Time of start:11:29am
'''
def largestRectangle(a):
	n = len(a)
	stack= []
	area = a[0]
	i =0
	while i < n:
		if not stack or a[stack[len(stack)-1]] < a[i]:
			stack.append(i)
			i=i+1
		else:
			index = stack.pop()
			#print("Popped ", a[index])
			#stack not empty case: 
			if stack:
				left = stack[len(stack)-1]
				area= max(area,(i-left-1)*a[index])
			else:
				area=max(area,(i)*a[index])
			#print("AREA ",area)

	#i now stores size of array
	while stack:
		index = stack.pop()
		#stack not empty case
		if stack:
			left=stack[len(stack)-1]
			area= max(area, (i - left-1)*a[index])
		else:
			area= max(area, i*a[index])
		
		#print(area," ",index)
	
	return area

def main():
	xstr = input().strip()
	arr = list(map(int,xstr.split()))
	print(largestRectangle(arr))

if __name__ == '__main__':
	main()