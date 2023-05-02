
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
                low[u] = min(low[u], low[v]) #bierzemy paremetry low ponieważ visit_time nie ulega zmienie, interesuje nas tylko przy patrzeniu na krawedz wsteczna!
                
            elif v != parent[u]:
                low[u] = min(low[u], visit_time[v]) #patrze na krawedz wsteczną jeśli nie mogę wejść głębiej bo już wszystkie sąsiednie wierzchołki są odwiedzone
        
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
            
    for u in range(n):
        if visit_time[u] == low[u] and parent[u] != None:
            bridges.append((parent[u], u))
    return bridges




G = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
bridges = Bridges(G)
print(bridges)
