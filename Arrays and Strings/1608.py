1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there 
are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Solution:

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for num in range(len(nums)+1):
            count=0
            for item in nums:
                if item>=num:
                    count+=1
            if count==num:
                return num
        return -1
