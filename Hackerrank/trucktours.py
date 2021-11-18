def trucktours(pumps):
	start =0
	end=start+1
	fuel =0
	fuel+=pumps[start][0]
	fuel-=pumps[start][1]
	while start!=end or fuel<0:
		
		while fuel< 0 and start!=end:
			fuel-=pumps[start][0]
			fuel+=pumps[start][1]
			start=(start+1)%len(pumps)
			if start==0:
				return -1
		
		fuel+=pumps[end][0]
		fuel-=pumps[end][1]
		end = (end+1)%len(pumps)

	return start



def main():
	t= int(input())
	
	pumps=[]
	while t!=0:
		size=int(input())
		while size!=0:
			xinp=input()
			tuple1 = tuple(map(int,xinp.split(" ")))
			pumps.append(tuple1)
			size-=1
		print(trucktours(pumps))
		t-=1

if __name__ == '__main__':
	main()