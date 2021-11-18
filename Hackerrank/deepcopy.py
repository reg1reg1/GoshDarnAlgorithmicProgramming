def clone(head):
    temp = head 
    while temp != None: 
        new = ALNode(temp.data) 
        new.next = temp.next
        temp.next = new 
        temp = temp.next.next

    temp = head 
    while temp != None: 
        temp.next.random = temp.random.next
        temp = temp.next.next

    temp = head 
    deepcopy = head.next
    while temp.next != None: 
        tmp = temp.next
        temp.next = temp.next.next
        temp = tmp 

    return deepcopy