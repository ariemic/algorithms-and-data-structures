def DFS(G, s=0):
    n = len(G)
    visited, res = [False]*n, []
    
    def dfs_visit(G, i, n):
        visited[i] = True
        res.append(i)
        for j in range(n):
            if not visited[j] and G[i][j] == 1:
                dfs_visit(G, j, n)

    dfs_visit(G, s, n)
   
            
    return res
            




# [2, 4, 0, 1, 3]
G = [[0, 0, 1, 0], 
     [1, 0, 0, 0], 
     [0, 1, 0, 0], 
     [1, 0, 0, 0]]

print(DFS(G, 3))
