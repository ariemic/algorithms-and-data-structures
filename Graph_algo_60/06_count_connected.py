'''
2. Policzyc liczbe spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)
'''

def DFS(G):
    n = len(G)
    visited = [False]*n
    
    def dfs_visit(G, u):
        
        visited[u] = True
        for v in G[u]:
            if not visited[v]:              
                dfs_visit(G, v)
    cnt = 0
    for u in range(n):
        if not visited[u]:
            cnt += 1
            dfs_visit(G, u)
    return cnt

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1], [8], [7]] #graf ma dwie spójne składowe
print(DFS(G))