#Dijikstra's algorithm for finding the shortest paths in weighted graph on adjancency list. 

from queue import PriorityQueue
# The lowest valued entries are retrieved first (the lowest valued entry is the one that would be returned by min(entries)). 
# A typical pattern for entries is a tuple in the form: (priority_number, data).

def max_vertex(E):
    n = len(E)
    return max(E[i][1] for i in range(n))+1


def build_graph(E, n):
    n = len(E)
    G = [[]for _ in range(n)] #create graph with proper size
    for edge in E:
        u, v, val = edge[0], edge[1], edge[2]
        G[u].append((v, val))
        G[v].append((u, val))
    return G

def relax(u, v, weight, d, parent):
    if d[v] > d[u] + weight:
        #distance to v vertex is longer then from d[u]+wieght what that exists shorter path from 
        #source to v vertex and we need to update it
        d[v] = d[u]+weight
        parent[v] = u
        return True
    return False
        
        
def dijkstra(Edges, s):
    G = build_graph(Edges)
    n = len(G)
    parent = [None]*n
    d = [float('inf')]*n
    visited = [False]*n
    d[s] = 0
    q = PriorityQueue()
    q.put((d[s], s))
    while not q.empty():
        d_u, u = q.get()
        for v, weight in G[u]:
            if not visited[v] and relax(u, v, weight, d, parent):
                q.put((d[v], v))
        visited[u] = True
    return d, parent


s = 0
Edges = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]

print(build_graph(Edges))

d, parent = dijkstra(Edges, s)
print(d, parent)