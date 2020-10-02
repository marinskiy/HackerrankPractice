

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    prev=None
    node1=DoublyLinkedListNode(data)
    if(node1.data<head.data):
        node1.next=head
        head.previous=node1
        head=node1
        return head
    temp=head.next
    while(temp!=None):
            if(temp.prev.data<=node1.data and node1.data<=temp.data):
                break
            else:
                prev=temp
                temp=temp.next
    if(temp!=None):
        node1.prev=temp.prev
        node1.next=temp
        temp.prev.next=node1
        temp.prev=node1
    else:
        prev.next=node1
        node1.prev=prev
    return head


