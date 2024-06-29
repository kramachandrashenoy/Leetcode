escription/?envType=daily-question&envId=2024-06-29

Solution:

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj=[[]for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
        ancestors=[[] for _ in range(n)]

        def dfs(cur,orig):
            for neighbor in adj[cur]:
                if neighbor in ancestors[orig]:
                    continue
                else:
                    dfs(neighbor,orig)
                    ancestors[orig].append(neighbor)

                

        for i in range(n):
            dfs(i,i)
        for num in ancestors:
            num.sort()
        return ancestors
        
