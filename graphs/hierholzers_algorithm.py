from collections import *
from typing import *


def euler_path_directed(adj: Dict[int, List[int]]):
    '''
    Modifies adj in place
    adj should be of type dict
    '''
    def dfs(u):
        while adj[u]:
            v = adj[u].pop()
            dfs(v)
        res.append(u)

    c = Counter()
    for u, vs in adj.items():
        for v in vs:
            c[u] += 1
            c[v] -= 1
    start = u # pick any start
    flag = False # used to check if there is more than 1 node with degree = 1
    for u, d in c.items():
        if d > 1:
            return []
        if d == 1:
            if flag:
                return []
            start = u
            flag = True
    res = []
    dfs(start)
    if any(len(v) for v in adj.values()):
        return [] # Graph not sufficiently connected
    res.reverse()
    return res


# Example: https://leetcode.com/submissions/detail/1124703223/
