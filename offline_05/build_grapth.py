from queue import PriorityQueue


def build_graph(E, singularities, s, n):
    #robi graf z niepotrzebnymi krawędziami
    
    G = [[]for _ in range(n)]
    
    for i in range(len(E)):
        u, v, val = E[i]
        if singularities[u] and not singularities[v]:
            G[v].append((s, val))
            G[s].append((v, val))
            
        if not singularities[u] and singularities[v]:
            G[u].append((s, val))
            G[s].append((u, val))
            
        if not singularities[u] and not singularities[v]:
            G[u].append((v, val))
            G[v].append((u, val))
                    
    return G



def build_graph(E, singularities, s, n):
    #szybsze ale brzydkie
    G = [[]for _ in range(n)]
    distance_from_s = [float('inf')]*n
    
    for i in range(len(E)):
        u, v, val = E[i]
        if singularities[u] and not singularities[v]:
            distance_from_s[v] = min(distance_from_s[v], val) 
            
        if not singularities[u] and singularities[v]:
            distance_from_s[u] = min(distance_from_s[u], val)
            
        if not singularities[u] and not singularities[v]:
            G[u].append((v, val))
            G[v].append((u, val))
            
    for i in range(n):
        if distance_from_s[i] != float('inf'):
            G[i].append((s, distance_from_s[i]))
            G[s].append((i, distance_from_s[i]))
            
    return G




def build_graph(E, singularities, s, n):
    #ładniejsze ale wolniejsze
    G = [[]for _ in range(n)]

    q = PriorityQueue()
    
    for i in range(len(E)):
        u, v, val = E[i]
        if singularities[u] and not singularities[v]:
            q.put((val, v)) 
            
        if not singularities[u] and singularities[v]:
            q.put((val, u))
            
        if not singularities[u] and not singularities[v]:
            G[u].append((v, val))
            G[v].append((u, val))
        
    visited = [False]*n        
    while not q.empty():
        val, u = q.get()
        if not visited[u]:
            G[u].append((s, val))
            G[s].append((u, val))
            visited[u] = True
        
    return G            