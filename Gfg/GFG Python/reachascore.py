#Dynamic programming question based on counting the no of unique solutions
#It is a different wording of the coin change problem involving counting unique solutions
#The trick is to include a coin more than once, but once excluded we move over to the next coin
#Hence it is a 2-state dp
choice=[3,5,10]



	


def main():
	global choice
	t = int(input().strip())
	while t>0:
		n = int(input().strip())
		mem= [[0]* (len(choice)) for x in range(n+1)]

		for i in range(len(choice)):
			mem[0][i]=1

		for i in range(1,n+1):
			for j in range(len(choice)):
				if i>=choice[j]:
					x=mem[i-choice[j]][j]
				else:
					x=0
				if j>=1:
					y=mem[i][j-1]
				else:
					y=0
				mem[i][j]=x+y
		t-=1
		print(mem[n][len(choice)-1])

if __name__ == '__main__':
	main()