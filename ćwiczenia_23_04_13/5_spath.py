# 5) Znaleźć najkrótszą ścieżke w grafie nieskierowanym używając BFS'a 
#graf dany jako lista sąsiedztwa; funkcja przyjmuje graf, wierchołek poczatkowy od którego wychodzi, wierzchołek końcowy do którego ma dotrzeć

from collections import deque

def shortestPath(G, s, k): #s - start vertex, k - end vertex
    q = deque()
    q.append(s)
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    visited[s] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
            if v == k: #juz nic wiecej mnie nie interesuje doszedlem do koncowego wierzcholka, teraz bede musiał odtworzyć tą trase 
                q = deque()
                break
    res = [k]
    while parent[k] != None:
        res.append(parent[k])
        k = parent[k]
    return res

# G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
# print(shortestPath(G, 3, 0))
G = [[1,2,3], [0,3], [0], [0,1,5], [], [3]]
s = 0
t = 5
print(shortestPath(G, s, t))