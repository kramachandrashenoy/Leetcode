872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1=[]
        l2=[]
        def func(root,l):
            if root is None:
                return l
            if root.left is None and root.right is None:
                l.append(root.val)
                return l
            l=func(root.left,l)
            l=func(root.right,l)
            return l
        l1=func(root1,l1)
        l2=func(root2,l2)
        if l1==l2:
            return True
        return False
        
