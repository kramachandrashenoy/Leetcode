1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

Solution:

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l={}
        
        for i in range(len(arr)):
            if arr[i] not in l:
                l[arr[i]]=1
                
            else:
                l[arr[i]]+=1
        for key in l.keys():
            if (l[key])>int(0.25*len(arr)):
                return key
        return arr[0]


