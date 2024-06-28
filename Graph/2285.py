https://leetcode.com/problems/maximum-total-importance-of-roads/description/?envType=daily-question&envId=2024-06-28

Solution:

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree=[0]*n
        pair=[]
        value=[0]*n
        ans=0
        for u,v in roads:
            indegree[u]+=1
            indegree[v]+=1
        for i in range(n):
            pair.append((i,indegree[i]))
        pair.sort(key=lambda x:x[1],reverse=True)
        i=0
        while i<n:
            value[pair[i][0]]=n-i
            i+=1
        for u,v in roads:
            ans+=value[u]+value[v]
        return ans



        
        
