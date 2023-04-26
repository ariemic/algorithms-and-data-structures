
def DFS_spojneSkadowe(G, s=0):
    n = len(G)
    visited = [False]*n
    
    def dfsVisit(G, u):
        nonlocal visited
        visited[u] = True
        #oznacza wierzcholki jesli zostana odwiedzona dopoki dfs nie przejdzie najdalej w głąb jak może
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
    
    cnt = 0 #licznik spojnych skladowych grafu
    for u in range(n):
        if not visited[u]:
            cnt += 1 #jedna z skladowych grafu
            dfsVisit(G, u) 
    return cnt

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1], [8], [7]] #graf ma dwie spójne składowe
print(DFS_spojneSkadowe(G))