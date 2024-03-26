442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

Solution:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def cyclicsort(nums):
            i=0
            while i<len(nums):
                check=nums[i]-1
                if nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[check]:
                    nums[i],nums[check]=nums[check],nums[i]
                else:
                    i+=1
        cyclicsort(nums)
        l=[]
        for i in range(len(nums)):
            if i+1!=nums[i]:
                l.append(nums[i])
        return l
                
        
