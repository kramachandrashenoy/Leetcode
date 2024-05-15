https://www.naukri.com/code360/problems/bfs-in-graph_973002?leftPanelTabValue=PROBLEM

Solution:

from typing import List
from collections import deque


def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
    queue=deque()
    traversed=set()
    res=[]
    starting_node=0

    queue.append(starting_node)
    traversed.add(starting_node)

    while(queue):
        node=queue.popleft()
        res.append(node)

        for neighbour in adj[node]:
            if neighbour not in traversed:
                queue.append(neighbour)
                traversed.add(neighbour)
    return res
