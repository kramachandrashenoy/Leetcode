260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Solution:

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        right_bit = xor & -xor
        n1, n2 = 0, 0
        for num in nums:
            if num & right_bit:
                n1 ^= num
            else:
                n2 ^= num
        return[n1,n2]
