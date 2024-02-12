1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Solution:

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=n=len(s)
        r=s[::-1]
        t=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==r[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return m-t[m][n]
