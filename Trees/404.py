404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s=0
        def func(root,s):
            if root:
                if root.left:
                    if root.left.left is None and root.left.right is None:
                        s=s+int(root.left.val)
                s=func(root.left,s)
                s=func(root.right,s)
            return s
        s=func(root,s)
        return s
