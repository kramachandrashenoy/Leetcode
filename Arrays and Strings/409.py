409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Solution:

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l={}

        for ch in s:
            l[ch]=l.get(ch,0)+1
        odd=False
        ans=0

        for val in l.values():
            if val%2==0:
                ans+=val
            else:
                ans+=val-1
                odd=True
        if odd:
            ans+=1
        return ans
