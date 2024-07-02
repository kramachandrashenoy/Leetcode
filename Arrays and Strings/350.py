https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02


Solution:

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        ans=[]
        for num in nums1:
            if num in h:
                h[num]+=1
            else:
                h[num]=1
        for num in nums2:
            if num in h:
                ans.append(num)
                h[num]-=1
                if h[num]==0:
                    del h[num]
        return ans
        
