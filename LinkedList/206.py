206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list

Solution:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        pointer1=None
        pointer2=head
        while pointer2:
            temp=pointer2.next
            pointer2.next=pointer1
            pointer1=pointer2
            pointer2=temp
        return pointer1
            
