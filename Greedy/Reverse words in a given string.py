https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i

Example 2:
Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr

Solution:

#Function to reverse words in a given string.
def reverseWords(self,S):
    # code here 
    l=S.split(".")
    l=l[::-1]
    return ".".join(l)
