from queue import PriorityQueue


def relax(u, v, edge_weight, parent, d):
    if d[v] > d[u]+edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False


def Dijkstra(G, s, t):
    n = len(G)
    q = PriorityQueue()
    d = [float('inf')]*n
    visited = [False]*n
    parent = [None]*n
    d[s[0]] = 0
    q.put((0, s[0]))
    
    while not q.empty():
        du, u = q.get()
        for v in range(n):
            if not visited[v] and G[u][v] != -1 and relax(u, v, G[u][v], parent, d):
                q.put((d[v], v))
        visited[u] = True #zapobiega cofaniu się w tył (takie cofanie wydłuża ścieżke) ten wierzchołek jest już przetworzony
        if t == (u,v):
            return d[u]
        
G = [[-1, 7, 5, 2, -1, -1],
     [7, -1, -1, -1, 3, 8 ],
     [5, -1, -1, 10, 4, -1],
     [2, -1, 10, -1, -1, 2], 
     [-1, 3, 4, -1, -1, 6],
     [-1, 8, -1, 2, 6, -1]]

print(Dijkstra(G, (0, 0), (5, 5)))
