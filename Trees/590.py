590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Solution:

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        l=[]
        for child in root.children:
            l.extend(self.postorder(child))
        l.append(root.val)
        return l
