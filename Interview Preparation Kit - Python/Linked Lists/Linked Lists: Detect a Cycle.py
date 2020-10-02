"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    temp=[]
    travel=head
    while(travel!=None):
        if(travel in temp):
            return True
        else:
            temp.append(travel)
            travel=travel.next
    return False
    
