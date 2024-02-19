438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Solution:

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l={}
        count=0
        ans=0
        i=j=0
        m=len(s)
        n=len(p)
        c=[]
        for char in p:
            if char in l:
                l[char]+=1
            else:
                l[char]=1
        count=len(l)
        while j<m:
            if j-i+1<n:
                if s[j] in l:
                    l[s[j]]-=1
                    if l[s[j]]==0:
                        count-=1
                j+=1
            if j-i+1==n:
                if s[j] in l:
                    l[s[j]]-=1
                    if l[s[j]]==0:
                        count-=1
                if count==0:
                    c.append(i)
                if s[i] in p:
                    l[s[i]]+=1
                    if l[s[i]]==1:
                        count+=1
                i+=1
                j+=1
        return c

                

