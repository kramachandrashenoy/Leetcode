1669. Merge In Between Linked Lists
'''
re given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:
'''
Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        prev=list1
        after=list1
        for i in range(a-1):
            prev=prev.next
        for i in range(b):
            after=after.next
        prev.next=list2
        temp=list2
        while temp.next:
            temp=temp.next
        temp.next=after.next

        return list1


        
