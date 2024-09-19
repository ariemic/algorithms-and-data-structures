# 1)Sprawdzanie czy graf jest dwudzielny (BFS) - zakladamy ze graf jest spojny
#Używam dwóch kolorów (cyfr), które na przemian będę przydzielać
from collections import deque

#pisane dla reprezentacji przez listy sąsiedztwa

def is_bipartite(G, s=0):
    #sprawdza czy graf jest dwudzielny, jesli jest w stanie kolorować rodzic - dziecko na inny kolor -> jest wpw nie jest
    n = len(G)
    visited = [-1]*n
    q = deque()
    q.append(s)
    visited[s]=0
    while q:
        u = q.leftpop()
        for v in G[u]:
            if visited[v] == -1:
                visited[v] = (visited[u]+1)%2 #zawsze 1%2 or 2%2
                q.append(v)
            elif visited[v] != (visited[u]+1)%2: return False #same as visited[v] == visited[u] polaczenie w tym samym grafie - banned
    return True    

def rek_solution(G, s=0):
    #za pomocą dfs'a
    n = len(G)
    colors = [-1]*n
    colors[s]=0
    
    def rek(G, u):
        nonlocal colors
        for v in G[u]:
            if colors[v] != -1 and colors[v] != colors[u]: return False
            
    for u in range(1, n):
        if colors[u] == -1:
            if not rek(G, u): return False
    return True
            
    
     