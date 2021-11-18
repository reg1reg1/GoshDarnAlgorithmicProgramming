def main():
	t = int(input().strip())
	col=[[0]*t for x in range(t)]
	k=0
	num=1
	for i in range(t):
		if(k%2==0):
			for j in range(t):
				col[i][j]=num
				num+=1
		else:
			for j in range(t-1,-1,-1):
				col[i][j]=num
				num+=1
		k+=1
	#print transpose
	for j in range(t):	
		for i in range(t):
			print(col[i][j],end=" ")
		print()
if __name__ == '__main__':
	main()