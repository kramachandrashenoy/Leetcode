2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse a linked list
        def reverse_list(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # Reverse the given linked list
        head = reverse_list(head)

        carry = 0
        curr = head
        prev = None
        while curr or carry:
            if not curr:
                curr = ListNode(0)
                prev.next = curr
            temp_sum = curr.val * 2 + carry
            curr.val = temp_sum % 10
            carry = temp_sum // 10
            prev = curr
            curr = curr.next

        # Reverse the list again to restore the original order
        head = reverse_list(head)

        return head



        
