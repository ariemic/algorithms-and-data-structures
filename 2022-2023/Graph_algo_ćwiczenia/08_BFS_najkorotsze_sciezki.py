# Zadanie 3. (BFS i najkrótsze sciezki) Prosze zaimplementowac algorytm BFS tak, zeby znajdował
# najkrótsze sciezki w grafie i nastepnie, zeby dało sie wypisac najkrotsza sciezke z zadanego punktu startowego
# do wskazanego wierzchołka.

from collections import deque

def BFS_shortest_path(G, s, t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
            if v == t:
                q = deque()
                break
    path = [t]
    while parent[t] != None:
        t = parent[t]
        path.append(t)
    
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=" ")
                
                
                
G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
print(BFS_shortest_path(G, 3, 0))    