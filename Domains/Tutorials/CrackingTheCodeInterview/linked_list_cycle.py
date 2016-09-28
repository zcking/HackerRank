"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    # Use two pointers moving at different speeds. SlowPtr moves one pointer at a time and fastPtr moves two pointers at a time.
    # Once they enter the loop, they are expected to meet.
    
    fastPtr = head
    slowPtr = head
    
    while(fastPtr and slowPtr):
        fastPtr = fastPtr.next   # move fastPtr one pointer
        
        
        if fastPtr == slowPtr:
            return 1
            
        if fastPtr == None:
            return 0
        
        fastPtr = fastPtr.next         # move fastPtr one pointer again
        if fastPtr == slowPtr:
            return 1
        
        slowPtr = slowPtr.next         # move slowPtr one pointer
    
