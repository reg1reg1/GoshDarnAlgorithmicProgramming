class Solution:
	def isPalindrome(self, head):
		
		if head is None:
			return True
		#find middle
		#slowptr will be pointing to the head where we need to reverse
		slowptr=head
		fastptr=head
		count=0
		while fastptr.next is not None:
			fastptr=fastptr.next
			if(fastptr.next is None):
				slowptr=slowptr.next
				break
			slowptr=slowptr.next
			fastptr=fastptr.next
		
		# slowptr  unchanged will store middle
		# After reversal it will store the tail of the reversed list
		prev = None
		curr = slowptr
		while curr is not None:
			temp = curr.next
			curr.next=prev
			prev=curr
			curr=temp
		#new head
		h1=prev
		h2=head
		flag=1
		temp = h1
		while h1 is not None:
			if h1.val!=h2.val:
				flag=0
				break
			h1= h1.next
			h2= h2.next
		if flag ==1:
			return True
		return False
		#Reverse the list with slowptr as the head