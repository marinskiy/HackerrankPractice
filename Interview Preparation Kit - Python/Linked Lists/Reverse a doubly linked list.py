

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if(head==None or head.next==None):
        return head
    else:
        temp=head
        temp1=None
        while temp is not None:  
            temp1 = temp.prev;  
            temp.prev = temp.next;  
            temp.next = temp1;              
            temp = temp.prev;    
    head1=temp1.prev
    return head1

