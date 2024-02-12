111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def func(root):
            if not root:
                return 0
            if root.left and not root.right:
                return 1+func(root.left)
            if not root.left and root.right:
                return 1+func(root.right)
            if not root.left and not root.right:
                return 1
            if root.left and root.right:
                return 1+min(func(root.left),func(root.right))
        return func(root)
