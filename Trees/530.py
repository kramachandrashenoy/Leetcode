530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=[]
        def func(root):
            if not root:
                return 
            else:
                func(root.left)
                l.append(root.val)
                func(root.right)
        func(root)
        d=float('inf')
        for i in range(len(l)-1):
            if abs(l[i+1]-l[i])<d:
                d=abs(l[i]-l[i+1])
        return d
