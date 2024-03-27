https://www.codingninjas.com/studio/problems/interview-shuriken-42-detect-and-remove-loop_241049?leftPanelTabValue=SUBMISSION
Problem statement
Given a singly linked list, you have to detect the loop and remove the loop from the linked list, if present. You have to make changes
in the given linked list itself and return the updated linked list.
Expected Complexity: Try doing it in O(n) time complexity and O(1) space complexity. Here, n is the number of nodes in the linked list

Solution:
from typing import *

# Following is the structure of  Node
# Do not update or change the structure 

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def removeLoop(head :Node) -> Node :

    # Write your code
    slow=fast=head
    while fast and fast.next:
        slow=slow.next 
        fast=fast.next.next
        if slow==fast:
            break
    if slow!=fast:
        return head
    
    slow=head
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    fast.next=None
    return head

    pass
