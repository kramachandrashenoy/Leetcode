https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/


Solution:

class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            a=int(s[i])
            b=int(s[i+1])

            if (a%2==b%2) and a>b:
                s=s[:i]+s[i+1]+s[i]+s[i+2:]
                return s
        return s
        
