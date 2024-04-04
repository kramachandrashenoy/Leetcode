1614. Maximum Nesting Depth of the Parentheses

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Solution:

class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxi=0
        for char in s:
            if char=="(":
                count+=1
                if count>maxi:
                    maxi=count
            elif char==")":
                count-=1
        return maxi
