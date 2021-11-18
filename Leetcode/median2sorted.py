def median(nums1,nums2):
	#making nums1 as the shorter list
	if(len(nums1)>len(nums2)):
		temp=nums1
		nums1=nums2
		nums2=temp
	xlen=len(nums1)
	ylen=len(nums2)
	#x has to be the shorter list
	
	'''
	xpart is xpartition (which will be in the shorter list)
	ypart is the larger partition controlled by the position of xpart
	xpart and ypart must be integer values, and valid index positions at all point within the loops
	xpart ranges from 0 -> i+1 (i being the last position in the x array)
	ypart ranges from 0-> j+1 (j being the last position in the y array)

	'''

	totleft=int((xlen+ylen+1)/2)
	#xpart+ypart=totleft
	low=0
	high=xlen
	#do a conditional binary search on the array
	while low<=high:
		xpart=int((low+high)/2)
		print("XPART ",xpart)
		#Experimental, approach(Needs verification)
		xrightpos = xpart
		xleftpos = xrightpos-1

		#Case where xleft does not exist
		if xpart==0:
			xrightpos=xpart
			yrightpos=totleft-xpart
			yleftpos=yrightpos-1
			xleft=nums2[yleftpos]
			if yrightpos >= ylen:
				yright=nums1[xrightpos]
			else:
				yright=nums2[yrightpos]
			xright=nums1[xrightpos]
			yleft=nums2[yleftpos]
			break

		#Case where xright does not exist
		if xpart == xlen:
			xleftpos = xpart-1
			yrightpos =totleft-xpart
			yleftpos=yrightpos-1
			xright =  nums2[yrightpos]
			if yleftpos <= 0:
				yleft = nums1[xleftpos]
			else:
				yleft = nums2[yleftpos]
			yright=nums2[yrightpos]
			xleft= nums1[xleftpos]
			break

		yrightpos=totleft-xpart
		yleftpos=yrightpos-1

		#Defining the variables
		xright=nums1[xrightpos]
		xleft=nums1[xleftpos]
		yleft=nums2[yleftpos]
		yright=nums2[yrightpos]


		print(xleftpos,xrightpos,yleftpos,yrightpos)
		print("x1,x2,y1,y2")
		print(xleft,xright,yleft,yright)
		
		if(xleft<=yright and yleft <= xright):
			flag=1
			break

		if xleft>yright:
			high=xpart-1
		else:
			low=xpart+1
	print("AT LOOP TERMINATION")			
	print(xleftpos,xrightpos,yleftpos,yrightpos)
	print("x1,x2,y1,y2")
	print(xleft,xright,yleft,yright)
	
	if((xlen+ylen)%2==0):
		ans=(max(xleft,yleft)+min(xright,yright))/2
	else:
		ans=max(xleft,yleft)
	return ans

def main():
	t = int(input().strip())
	for i in range(t):
		ainp = input().strip()
		binp= input().strip()
		a= list(map(int,ainp.split(" ")))
		b= list(map(int,binp.split(" ")))
		x=median(a,b)
		print(x)

if __name__ == '__main__':
	main()
