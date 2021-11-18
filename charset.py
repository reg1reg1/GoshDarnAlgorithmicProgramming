#
def conv(x):
	ans=""
	if x== 0:
		return chr(65)
	while x > 0:
		x-=1
		y = chr(x % 26 + 65);
		x = int(x/26);
		ans+=y;
	return ans
    
def charset(x):
	row= int(x/702)
	if(x%702!=0):
		row+=1
	colnum = int(x%703)
	#print(row,colnum)
	colchar=conv(colnum)
	return(row,colchar)

x= [702,703,26,1,2,3,4,27]

for i in x:
	print(charset(i))