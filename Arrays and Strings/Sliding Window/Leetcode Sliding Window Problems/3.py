3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        n=len(s)
        d=set()
        ans=0
        while j<n:
            while s[j] in d:
                d.remove(s[i])
                i+=1
            else:
                d.add(s[j])
            ans=max(ans,j-i+1)
            j+=1
        return ans




        
