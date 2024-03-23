143. Reorder List
Solved
Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # The slow pointer is pointing to the middle element
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        
        # From the middle of the linked list we reverse the linked list
        # The prev pointer contains the last element

        current=head
        last=prev
        while last.next:
            next_cur=current.next
            next_last=last.next

            current.next=last
            last.next=next_cur

            current=next_cur
            last=next_last
        
        #Merge the first half and reversed second half alternately and
        #Traverse until the last node of the reversed part

        last.next=None
        # Set the next of the last node to None to avoid cycles



        
