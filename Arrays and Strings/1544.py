1544. Make The String Great

Given a string s of lower and upper case English letters.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
Return the string after making it good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Solution:

class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        i=0
        n=len(s)
        while i<n:
            if stack and abs(ord(stack[-1])-ord(s[i]))==32:
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)

        
