977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Solution:

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        start,end=0,n-1
        l=[0]*n
        i=n-1
        while(i>-1):
            if nums[start]**2>nums[end]**2:
                l[i]=nums[start]**2
                i-=1
                start+=1
            else:
                l[i]=nums[end]**2
                i-=1
                end-=1
        return l

            
        
            
        

        
