41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Solution:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def cyclicsort(nums):
            i=0
            while i<len(nums):
                check=nums[i]-1
                if nums[i]<len(nums) and nums[i]>0 and nums[i]!=nums[check]:
                    nums[i],nums[check]=nums[check],nums[i]
                else:
                    i+=1
        cyclicsort(nums)
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1


