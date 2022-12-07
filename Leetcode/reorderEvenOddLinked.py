# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head.next
        tail=None
        if p2 is None:
            return p1
        tail=p2    
        while p1 is not None and p2 is not None:
            #p2 exists, so p1.next will exist here
            if p2.next:
                p1.next=p2.next
                p2.next=p2.next.next
                p1=p1.next
                p2=p2.next
            else:
                p1.next=tail
                break
        x=head
        j=0#inf loop debug
        while x and j<20:
            print(x.val)
            x=x.next
            j+=1
