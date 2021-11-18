'''
Problem Statement:
You're given an array a of length 2n. Is it possible to reorder it in such way so that the sum of the first n elements isn't equal to the sum of the last n elements?

Input
The first line contains an integer n (1≤n≤1000), where 2n is the number of elements in the array a.

The second line contains 2n space-separated integers a1, a2, …, a2n (1≤ai≤106) — the elements of the array a.

Output
If there's no solution, print "-1" (without quotes). Otherwise, print a single line containing 2n space-separated integers. They must form a reordering of a. You are allowed to not change the order.
'''
def printList(x):
	for i in x:
		print("{} ".format(i),end="")

def boolPossible(x):
	flag=x[0]
	for i in x:
		if i!=flag:
			x.sort()
			printList(x)
			return
	print("-1")





def main():
	t= int(input().strip())
	lineinp=input().strip()
	arr= list(map(int,lineinp.split()))
	boolPossible(arr)

main()