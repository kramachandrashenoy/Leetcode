392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Solution:

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m=len(t)
        n=len(s)
        dp=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        if dp[m][n]==n:
            return True 
        else:
            return False

BETTER CODE:

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        n=len(s)
        m=len(t)
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
