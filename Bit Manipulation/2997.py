2997. Minimum Number of Operations to Make Array XOR Equal to K

You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Solution:

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        for num in nums:
            ans^=num
        ans=ans^k
        return bin(ans).count('1')
        
