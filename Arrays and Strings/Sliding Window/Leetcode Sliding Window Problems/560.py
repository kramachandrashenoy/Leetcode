560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Solution:

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summ=0
        c=0
        l={0:1}
        for num in nums:
            summ+=num
            diff=summ-k
            c+=l.get(diff,0)
            l[summ]=1+l.get(summ,0)
        return c
