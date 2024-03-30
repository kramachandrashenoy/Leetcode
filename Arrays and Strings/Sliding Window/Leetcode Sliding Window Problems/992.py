992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Solution:

from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0

        def atMostK(nums, k):
            count = 0
            left = 0
            frequency = {}
            for right in range(len(nums)):
                if nums[right] not in frequency:
                    frequency[nums[right]] = 0
                frequency[nums[right]] += 1

                while len(frequency) > k:
                    frequency[nums[left]] -= 1
                    if frequency[nums[left]] == 0:
                        del frequency[nums[left]]
                    left += 1

                count += right - left + 1
            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)

