1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Solution:

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        l1={}
        l2={}
        for i in range(len(word1)):
            if word1[i] in l1:
                l1[word1[i]]+=1
            else:
                l1[word1[i]]=1
        for j in range(len(word2)):
            if word2[j] in l2:
                l2[word2[j]]+=1
            else:
                l2[word2[j]]=1
        s_l1=sorted(word1)
        s_l2=sorted(word2)
        if s_l1==s_l2:
            return True
        s_key1=sorted(list(l1.keys()))
        s_key2=sorted(list(l2.keys()))
        s_val1=sorted(list(l1.values()))
        s_val2=sorted(list(l2.values()))
        if s_key1==s_key2:
            if s_val1==s_val2:
                return True
        return False



        

