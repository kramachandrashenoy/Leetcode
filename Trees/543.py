543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def func(root:Optional[TreeNode]) -> int:
            nonlocal diameter
            if not root:
                return 0
            left=func(root.left)
            right=func(root.right)
            diameter=max(diameter,left+right)
            return 1+max(left,right)
        func(root)
        return diameter
