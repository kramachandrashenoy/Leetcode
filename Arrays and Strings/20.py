20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Solution:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        input_sym=['(','{','[']
        output_sym=[')','}',']']
        c=[]
        for i in range(len(s)):
            if s[i] in input_sym:
                c.append(s[i])
            elif s[i] in output_sym:
                if c:
                    temp=c.pop()
                    if temp =='(': 
                        if s[i]==')':
                            continue
                        else: 
                            return False
                    if temp =='[': 
                        if s[i]==']':
                            continue
                        else: 
                            return False
                    if temp =='{': 
                        if s[i]=='}':
                            continue
                        else: 
                            return False
                else:
                    return False
                    
        if len(c)>0:
            return False
        return True

Optimal solution:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapp={')':'(',']':'[','}':'{'}

        for i in range(len(s)):
            if s[i] in mapp:
                if stack:
                    if mapp[s[i]]!=stack.pop():
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) >0:
            return False
        else:
            return True
        
