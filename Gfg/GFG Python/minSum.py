import heapq

def main():
	t = int(input().strip())
	
	while t>0:
		n = int(input().strip())
		arr = list(map(int,input().strip().split()))
		heapq.heapify(arr)
		count=0
		str1=""
		str2=""
		while len(arr)!=0:
			if count%2==0:
				str1+=str(heapq.heappop(arr))
			else:
				str2+=str(heapq.heappop(arr))
			count+=1
		if str1=="":
			str1="0"
		if str2=="":
			str2="0"
		x=int(str1)
		y=int(str2)
		print(x+y)
		t-=1

if __name__ == '__main__':
	main()