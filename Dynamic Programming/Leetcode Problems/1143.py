1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Solution:

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m=len(text1)
        n=len(text2)
        t=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    t[i][j]=0
                else:
                    if text1[i-1]==text2[j-1]:
                        t[i][j]=1+t[i-1][j-1]
                    else:
                        t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[m][n]
