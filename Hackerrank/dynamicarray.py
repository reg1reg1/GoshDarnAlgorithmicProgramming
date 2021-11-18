def dynamicArray(n, queries):
	answer=[]
	lastAnswer=0
	seq=[[]*n for x in range(n)]
	#print(queries)
	for i in range(len(queries)):
		qType = queries[i][0]
		x = queries[i][1]
		y = queries[i][2]
		#print(qType,)
		if qType==1:
			seq[(x^lastAnswer)%n].append(y)
		else:
			#print("ee")
			seqIndex = (x^lastAnswer)%n
			lastAnswer= seq[seqIndex][y%len(seq[seqIndex])]
			answer.append(lastAnswer)
	return answer

def main():
	line1 = input().strip()
	arr = list(map(int,line1.split()))
	n = arr[0]
	q = arr[1]
	queries=[]
	for i in range(q):
		queries.append(list(map(int, input().rstrip().split())))
	x=dynamicArray(n,queries)
	#print(x)
	for i in x:
		print(i)

if __name__ == '__main__':
	main()