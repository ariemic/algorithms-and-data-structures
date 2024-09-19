'''
Oblicz liczbe spoójnych składowych w grafie(dfs)
'''
def dfs(G):
    #dla grafu zapisanego przy pomocy list sąsiedztwa
    def dfs_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
               dfs_visit(G, v)
    
    n = len(G)
    visited = [False]*n
    cnt = 0
    for u in range(n):#dla każdego wierzchołka w drzewie
        if not visited[u]:
            cnt += 1 #wchodzimy do tego wierzchołka i do wszystkich połączeń które tworzy czyli go grafu spójnego (spójnej składowej)
            dfs_visit(G, u)
    return cnt        

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1], [8], [7]] #graf ma dwie spójne składowe
print(dfs(G))


def skladowe(G):
    
    def dfs_visit(G, u):
        #wyjdziemy z tej fukncji gdy dany las sie skonczy, nie bedziemy mieli gdzie głębiej dojść
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
    
    n = len(G)
    visited = [False]*n
    cnt = 0
    for u in range(n):
        if not visited[u]:
            cnt += 1 #kazdorazowe wejscie do spójnej składowej
            dfs_visit(G, u)
    return cnt