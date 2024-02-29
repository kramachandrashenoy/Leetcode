1609. Even Odd Tree

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Solution:

from collections import deque

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lvl = 0
        queue = deque([root])

        while queue:
            n = len(queue)
            l = []

            for i in range(n):
                current = queue.popleft()

                if (lvl + current.val) % 2 == 0:
                    return False
                else:
                    if current.val in l:
                        return False
                    else:
                        l.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if lvl % 2 == 0:
                if l != sorted(l):
                    return False
            else:
                if l != sorted(l, reverse=True):
                    return False

            lvl += 1

        return True
