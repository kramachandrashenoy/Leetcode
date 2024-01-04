94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        stack=[]

        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            
            root=stack.pop()
            ans.append(root.val)
            root=root.right
        return ans

alternative:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    inorderHelper(root, result)
    return result

def inorderHelper(node, result):
    if node:
        inorderHelper(node.left, result)
        result.append(node.val)
        inorderHelper(node.right, result)
