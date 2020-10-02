

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    temp1=head1
    temp2=head2
    while(temp1!=temp2):
        if(temp1.next==None):
            temp1=head2
        else:
            temp1=temp1.next
        if(temp2.next==None):
            temp2=head1
        else:
            temp2=temp2.next
    return temp2.data

