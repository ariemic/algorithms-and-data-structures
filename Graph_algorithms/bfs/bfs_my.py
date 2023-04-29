from collections import deque

def bfs(G, s=0):
    #s - first vertex
    #we keep our Graph as adjencenty list
    #take into consideration that vertex s don't have a parent so in parent array for will be assigned None value
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    d = [-1]*n #distance
    q = deque()
    q.append(s)
    visited[s], d[s] = True, 0 #mark root vertex as visited and distance as 0 
    while q:
        u = q.popleft() #u - parent vertex for their neighbours
        for v in G[u]: #iterate over u vertex children
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                q.append(v)
    return parent, visited, d

# G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G = [[2, 6], [4, 3], [1], [], [], [1], [5]]         
parent, visited, d = bfs(G)
print(parent, visited, d)