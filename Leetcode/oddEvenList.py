#https://leetcode.com/problems/odd-even-linked-list/
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:
		if head is None or head.next is None:
			return head
		
		hOdd = head
		
		hEven = head.next
		#print("HEADS",hOdd.val,hEven.val)
		currOdd = hOdd
		currEven = hEven
		#base check

		tail = currOdd
		while currOdd is not None and currOdd.next is not None:
			tail = currOdd
			currOdd.next=currOdd.next.next
			currOdd = currOdd.next

			if currEven.next is not None:
				currEven.next=currEven.next.next
				currEven = currEven.next
		
		if currEven:
			currEven.next = None
		else:
			tail = tail.next
		tail.next=hEven
		return hOdd


def main():
	#Initialize List
	
	count=4
	i=0
	head=None
	while i<count:
		
		if i == 0:
			curr = ListNode(i)
			head=curr
			curr.next=None
			i+=1
			continue
		curr.next = ListNode(i)
		curr=curr.next	
		i+=1
	curr.next=None
	temp = head
	while temp is not None:
		print(temp.val,end="-->")
		temp=temp.next

	sol=Solution()
	temp=sol.oddEvenList(head)
	
	while temp is not None:
		print(temp.val,end="-->")
		temp=temp.next


	



if __name__ == '__main__':
	main()