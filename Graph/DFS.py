https://www.naukri.com/code360/problems/dfs-traversal_630462?leftPanelTabValue=PROBLEM

Solution:

from typing import *

def dfsearch(adj,ver,visited,ans):

    if(visited[ver]!=0):

        return

    else:

        ans.append(ver)

        visited[ver]=1

        for i in adj[ver]:

            dfsearch(adj,i,visited,ans)

 

def depthFirstSearch(V: int, E: int, edges: List[List[int]]):

    adj={}

    for i in range(V):

        adj[i]=[]

    visited=[0]*(V+1)

    for i in edges:

        i=list(i)

        adj[i[0]].append(i[1])

        adj[i[1]].append(i[0])

    ans=[]

    for i in range(V):

        if(visited[i]==0):

            l=[]

            dfsearch(adj,i,visited,l)

            ans.append(sorted(l))

    return(ans)
