1002. Find Common Characters
Solved
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Solution:

from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result=Counter(words[0])

        for word in words[1:]:
            new=Counter(word)
            result=result & new
        
        l=[]
        for char,count in result.items():
            l.extend([char]*count)

        return l
        
