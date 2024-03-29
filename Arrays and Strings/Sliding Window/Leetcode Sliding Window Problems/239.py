239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Solution::

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = j = 0
        l=deque()
        ans = []
        n = len(nums)

        while j < n:
            while l and l[-1]<nums[j]:
                l.pop()
            l.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if nums[i]==l[0]:
                    ans.append(l.popleft())
                else:
                    ans.append(l[0])
                i += 1
                j += 1

        return ans
