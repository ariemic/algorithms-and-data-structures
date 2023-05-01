from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(G, s, t):
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
            #co robi warunke G[u][v] ? - jeśli krawędz istnieje to jej waga jest nie ujemna
            if not visited[v] and G[u][v] != -1 and relax(u, v, G[u][v], d, parent):
                q.put((d[v], v))
        visited[u] = True
        if t == (u, v):
            return d[t[0]]
        
    # return d, parent


graph = [[-1, 3, 1, 2],
         [3, -1, -1, -1], 
         [1, -1, -1, 0],
         [2, -1, 0, -1]]

print(dijkstra(graph, 0, (3, 3)))
# print(parent, distance)
# [None, 0, 1, 2, 3] [0, 1, 3, 6, 7]