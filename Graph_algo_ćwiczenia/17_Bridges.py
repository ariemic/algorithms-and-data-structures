
def Bridges(G):
    #algorytm zwraca liczbe mostów w grafie oraz wierzchołki je tworzące w postaci listy krotek
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    visit_time = [0]*n
    low = [float('inf')]*n
    bridges = []
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        
        time += 1
        visited[u] = True
        visit_time[u], low[u] = time, time #1 krok
        
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)
                low[u] = min(low[u], low[v])
                
            elif v != parent[u]:
                low[u] = min(low[u], visit_time[v])
        
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
            
    for u in range(n):
        if visit_time[u] == low[u] and parent[u] != None:
            bridges.append((parent[u], u))
    print(bridges)
    return bridges




# def Edge(G, u, v):
#     G[u].append(v)
#     G[v].append(u)
# #

# V = 6
# G = [ [] for _ in range(V) ]
# Edge(G, 0, 2)
# Edge(G, 1, 2)
# Edge(G, 2, 3)
# Edge(G, 2, 4)
# Edge(G, 3, 4)
# Edge(G, 3, 5)

# bridges = Bridges(G)
# print(bridges)
graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
Bridges(graph)
