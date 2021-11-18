'''
Program to maximise profit given an array of stock prices
You can buy sell, multiple times 
Print the output as buy sell day tuple

'''

t = int(input().strip())
for i in range(t):
	n = int(input().strip())
	arinp = input().strip()
	alist  = list(map(int,arinp.split(" ")))
	j=0
	buy =0
	sell=0
	count=0
	if n == 1:
		print("No Profit")
	else:
		#main condition
		while j<n-1:


			#find an element to buy(a place where we find the decreasing sequence breaks 100 180 for eg)
			#then sequence breaks at 100 i.e j a[j] is less than a[j+1], we buy j as
			while j<n-1 and alist[j]>=alist[j+1]:	
				j+=1

			#if j==n-1 it means we failed to find an element to buy, so exit
			if(j==n-1):
				break
			buy=j
			#print("Bought ",buy)
			#Once j is bought it cannot be sold, so increment j
			j+=1
			print("J inc to ",j)
			#find the first element that is less than next element
			#for 100 180 260 300 40
			#we bought 0
			#j is at 1 now
			#so we compare j and j-1 and do it till we find something that breaks the increasing seq
			#This happens at j=4 as j =40 , so we sell our product if array ends before we find such a num
			#we sell it at the last day
			#we sell at the point just before stocks dip
			#since we are not selling at the dip, the dipping day can be buy day so no need to inc j
			#after selling
			while j<n and alist[j-1]<=alist[j]:
				j+=1
			sell = j-1
			print("Sold ",sell)

			
			print(("({} {})").format(buy,sell),end=" ")
			count+=1
		if(count==0):
			print("No Profit")
		else:
			print()
