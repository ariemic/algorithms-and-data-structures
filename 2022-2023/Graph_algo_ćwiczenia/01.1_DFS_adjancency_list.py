
def DFS(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)
        time += 1
    #end dfs_visit
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
    

def DFS(G):
    n = len(G)
    visited = [False]*n
    
    def dfs_visit(G, u):
        
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
              
                dfs_visit(G, v)
   
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)