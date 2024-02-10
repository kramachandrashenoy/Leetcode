416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Solution:

DP approach

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def subset(arr,target,n):
            t=[[False for i in range(target+1)]for j in range(n+1)]
            for i in range(n+1):
                for j in range(target+1):
                    if i==0:
                        t[i][j]=False
                    elif j==0:
                        t[i][j]=True
                    elif arr[i-1]<=j:
                        t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n][target]
        n=len(nums)
        s=0
        for i in range(n):
            s+=nums[i]
        if s%2 !=0:
            return False
        else:
            return subset(nums,s/2,n)
        
