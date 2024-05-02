2441. Largest Positive Integer That Exists With Its Negative

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Solution:

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l={}
        maxi=-1
        for i in range(len(nums)):
            if abs(nums[i]) not in l:
                l[abs(nums[i])]=nums[i]
            else:
                if l[abs(nums[i])]*nums[i]<0:
                    maxi=max(maxi,abs(nums[i]))
        return maxi
        
