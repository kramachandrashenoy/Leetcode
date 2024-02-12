938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        l=[]
        def sumbst(root,l,low,high):
            if root is None:
                return l
            if root.val>=low and root.val<=high:
                l.append(root.val)
            l=sumbst(root.left,l,low,high)
            l=sumbst(root.right,l,low,high)
            return l
        l=sumbst(root,l,low,high)
        sum=0
        for num in l:
            sum+=num
        return sum
