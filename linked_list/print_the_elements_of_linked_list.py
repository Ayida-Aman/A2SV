def printLinkedList(head):
    if not head:
        return
    
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next