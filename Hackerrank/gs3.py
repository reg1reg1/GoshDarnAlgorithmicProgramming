def gridGame(grid, k, rules):

	colNum=len(grid[0])
	rowNum=len(grid)

	#print("No of rows ",rowNum)
	#print("No of columns ",colNum)

	boolRules=[0]*len(rules)
	#print(boolRules)
	liveNeighbours=[[0]*(colNum) for x in range(rowNum)]
	#print("init liveNeighbours ",liveNeighbours)
	#print(liveNeighbours)
	#print(len(rules))
	for i in range(len(rules)):
		#print("I",i)
		if rules[i]=="alive":
			boolRules[i]=1
		else:
			boolRules[i]=0
	#print(boolRules,end=" ")
	
	#initlive
	count=0
	for i in range(rowNum):
			for j in range(colNum):
				count=0			
				if i-1>=0:
					if grid[i-1][j]==1:
						count+=1
				if j+1<colNum:
					if grid[i][j+1]==1:
						count+=1
				if j-1>=0:
					if grid[i][j-1]==1:
						count+=1
				if i+1<rowNum:
					if grid[i+1][j]==1:
						count+=1
				if i-1>=0 and j-1>=0:
					if grid[i-1][j-1]==1:
						count+=1
				if i-1>=0 and j+1<colNum:
					if grid[i-1][j+1]==1:
						count+=1
				if i+1<rowNum and j-1>=0:
					if grid[i+1][j-1]==1:
						count+=1
				if i+1<rowNum and j+1<colNum:
					if grid[i+1][j+1]==1:
						count+=1
				#print("I",i,"J",j,"Count",count)
				liveNeighbours[i][j]=count
	#print("BEGIN LIVE ")
	#for i in liveNeighbours:
		#print(i)
	#print()


	while(k!=0):
		for i in range(rowNum):
			for j in range(colNum):
				#checklive neighbours:
				if boolRules[liveNeighbours[i][j]]==0:
					grid[i][j]=0
				else:
					grid[i][j]=1

		#update live neighbours			
		for i in range(rowNum):
			for j in range(colNum):
				count=0				
				if i-1>=0:
					if grid[i-1][j]==1:
						count+=1
				if j+1<colNum:
					if grid[i][j+1]==1:
						count+=1
				if j-1>=0:
					if grid[i][j-1]==1:
						count+=1
				if i+1<rowNum:
					if grid[i+1][j]==1:
						count+=1
				if i-1>=0 and j-1>=0:
					if grid[i-1][j-1]==1:
						count+=1
				if i-1>=0 and j+1<colNum:
					if grid[i-1][j+1]==1:
						count+=1
				if i+1<rowNum and j-1>=0:
					if grid[i+1][j-1]==1:
						count+=1
				if i+1<rowNum and j+1<colNum:
					if grid[i+1][j+1]==1:
						count+=1
				#print(i,j)
				liveNeighbours[i][j]=count			
		#Update live neighbours		

		k-=1
	return grid
			

def main():
	arr=[
			[0],
			[0],
			[0],
			[1]
		]
	rules=["dead","alive","dead","dead","dead","dead","dead","dead","dead"]
	print(gridGame(arr,5,rules))
if __name__ == '__main__':
	main()
