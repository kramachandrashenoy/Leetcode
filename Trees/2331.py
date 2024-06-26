2331. Evaluate Boolean Binary Tree

''' You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.'''

Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def func(root):
            if root.val==0:
                return False
            elif root.val==1:
                return True
            elif root.val==2:
                if root.left:
                    ans=func(root.left) or func(root.right)
                return ans
            elif root.val==3:
                if root.left:
                    ans=func(root.left) and func(root.right)
                return ans

        if not root.left:
            return root.val
        else:
            return func(root)
        
