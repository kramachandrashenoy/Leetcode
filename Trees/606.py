606. Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def func(root):
            if not root:
                return

            result.append(str(root.val))

            if root.left or root.right:
                result.append('(')
                func(root.left)
                result.append(')')

            if root.right:  
                result.append('(')
                func(root.right)
                result.append(')')

        func(root)
        return ''.join(result)


