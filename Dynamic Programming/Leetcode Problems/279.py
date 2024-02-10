279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Solution:

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[i**2 for i in range(1,int(n**0.5)+1)]
        N=len(arr)

        t=[[10005 for i in range(n+1)]for j in range(N+1)]
        for i in range(n+1):
            t[0][i]=10005
        for j in range(1,N+1):
            t[j][0]=0
        for i in range(1,n+1):
            if i%arr[0]==0:
                t[1][i]=int(i/arr[0])
            else:
                t[1][i]=10005
        for i in range(2,N+1):
            for j in range(1,n+1):
                if arr[i-1]<=j:
                    t[i][j]=min(1+t[i][j-arr[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return t[N][n]
        
