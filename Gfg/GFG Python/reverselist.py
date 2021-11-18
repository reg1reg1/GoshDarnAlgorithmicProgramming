import os
import sys
from ysinglinked import *





llist = LinkedList()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

llist.Insert(a)
llist.Insert(b)
llist.Insert(c)
llist.Insert(d)
llist.Insert(e)
llist.display()

llist.ReverseList()
llist.display()
head = llist.getHead()
llist.ReverseRecursion(head)
llist.display()




	



