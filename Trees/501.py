501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l={}
        def func(root):
            if not root:
                return 
            else:
                if root.val in l:
                    l[root.val]+=1
                else:
                    l[root.val]=1
                func(root.left)
                func(root.right)
        func(root)
        a=[]
        a=list(l.values())
        maxi=max(a)
        res=[]
        for key,val in l.items():
            if val==maxi:
                res.append(key)
        return res
        
