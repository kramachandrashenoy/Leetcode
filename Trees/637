637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        l=[]
        que=deque([root])

        while que:
            l.append(sum([node.val for node in que])/float(len(que)))
            for _ in range(len(que)):
                new=que.popleft()
                if new.left:
                    que.append(new.left)
                if new.right:
                    que.append(new.right)
        return l
