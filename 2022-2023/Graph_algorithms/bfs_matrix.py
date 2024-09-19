
from collections import deque

def bfs(G, s=0):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    q = deque()
    q.append((0,0))
    while q:
        u = q.popleft()
        for i in range(1, n):
            for j in range(n):
                pass