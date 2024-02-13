118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

Solution:

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        new=[]
        for _ in range(numRows):
            new.append([])
        new[0].append(1)
        for i in range(1,numRows):
            new[i].append(1)
            for j in range(len(new[i-1])-1):
                new[i].append(new[i-1][j]+new[i-1][j+1])
            new[i].append(1)
        return new
