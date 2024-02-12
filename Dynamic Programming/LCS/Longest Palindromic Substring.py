5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Solution:

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = n = len(s)
        r = s[::-1]
        res=0
        t = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == r[j-1]:
                        t[i][j] = 1+t[i-1][j-1]
                else:
                        t[i][j] = 0
                if t[i][j] > res:
                    temp=s[i-t[i][j]:i]
                    temp2=temp[::-1]
                    if temp==temp2:
                        ans=temp
                        res=t[i][j]
        return ans
                

        
