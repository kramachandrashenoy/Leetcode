https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        temp=dummy
        nums_set=set(nums)

        while head:
            if head.val not in nums_set:
                temp.next=head
                temp=temp.next
            head=head.next
        temp.next=None
        return dummy.next

        
