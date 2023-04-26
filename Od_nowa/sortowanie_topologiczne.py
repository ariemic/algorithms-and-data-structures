'''
1. Uruchomić DFS
2. po przetworzeniu każdego wierchołka dopisać go na początek tworzonej listy

Moment przetworzenia wierzchołka traktujemy jak jego usunięcie po czym się cofamy, następny przetwarzamy cofamy się przetwarzamy jest to 
to samo co znalezienia ostatniego wierzchołka usunięcie go tylko że dfs robi to w jednym przebiegu.
'''

def sort_topologiczne(G, s=0):
    time = 0
    n = len(G)
    visited = [False]*n 
    res = []
    
    def dfsVisit(G, u):
        nonlocal time
        time += 1
        visited[u] = True 
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
        time += 1
        res.append(u)
        
    for u in range(n):
        if not visited[u]:
            dfsVisit(G, u)
        
    return res[::-1]

G=[[3], [0, 2], [], [4, 2], [5, 6], [], [], [4]]

print(sort_topologiczne(G))
