1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

Solution:

class Solution:
    def numSteps(self, s: str) -> int:
        n=int(s,2)
        ans=0
        while n!=1:
            if n%2:
                n+=1
            else:
                n=n//2
            ans+=1
        return ans
        
