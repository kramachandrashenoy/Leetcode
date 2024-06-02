3110. Score of a String

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.

Solution:

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(1,len(s)):
            ans+=abs(ord(s[i])-ord(s[i-1]))
        return ans
        
