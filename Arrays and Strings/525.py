525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number 

Solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        count=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if count not in d:
                d[count]=i
            if count==0:
                res=max(res,i+1)
            else:
                res=max(res,i-d[count])
        return res
        
