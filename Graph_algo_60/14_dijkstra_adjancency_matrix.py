from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(G, s):
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n
    visited = [False]*n
    
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    
    while not q.empty():
        d_u, u = q.get()
        for v in range(n):
            #co robi warunke G[u][v] ?
            if not visited[v] and G[u][v] != 0 and relax(u, v, G[u][v], d, parent):
                q.put((d[v], v))
        visited[u] = True
        
    return d, parent


graph = [[0, 1, 5, 0, 0],
         [1, 0, 2, 8, 7],
         [5, 2, 0, 3, 0],
         [0, 8, 3, 0, 1],
         [0, 7, 0, 1, 0]]

parent, distance = dijkstra(graph, 0)
print(parent, distance)
# [None, 0, 1, 2, 3] [0, 1, 3, 6, 7]