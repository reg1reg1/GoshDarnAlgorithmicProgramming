'''
Recursive inefficient solution
'''
def cost(val):
	if val == 1:
		return 2
	if val == 7:
		return 7
mem= [0]*30
#print(mem)

count = 0
def CalcCost(x,ptr,val):
	if ptr == len(x):
		return 0
	if x[ptr]  < val:
		print("IF: index ",x[ptr],"value ",val)
		mem[x[ptr]]=min(CalcCost(x,ptr+1,val),25)
		return mem[x[ptr]]
	else:
		print("ELSE: index ",x[ptr],"value ",val)
		mem[x[ptr]]=min(CalcCost(x,ptr+1,x[ptr]+6)+cost(7),CalcCost(x,ptr+1,x[ptr])+cost(1),25)	
		return mem[x[ptr]]
	



def main():
	a = [1,2,3,4,5,6,7]
	CalcCost(a,0,0)
	print(mem)

if __name__ == '__main__':
	main()