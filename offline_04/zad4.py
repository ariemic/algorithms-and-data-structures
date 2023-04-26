'''
Ariel Michalik
Złożoność: O(|V|^2 + |V|*|E|)
Algorytm początkowo wyszukuje najkrótszą ścieżke w grafie danym na wejściu, zapisuje ją w tablicy path oraz jej długość pod zmienną n. Następnie wycinam n razy krawedz z grafu G, modyfikując go po czym 
sprawdzam długość nowej najkrótszej ścieżki jeśli jest ona dłuższa to zwracam krotkę z wierzchołkami usuniętej krawędzi, jeśli nie to dołączam do grafu usunięte wcześniej krawędzie, przywracając go do
stanu wyjściowego i powtarzam proces. Jeśli nie znajde takie ścieżki zwrazam None.

'''
from zad4testy import runtests
from collections import deque

def shortestPath(G, s, t, arr=False):
    #function search for shortest path from s to t vertex
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    d = [0]*n
    visited[s], d[s] = True, 1
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u]+1
                q.append(v)
            if v == t:#I found shortest path from s to t
                q = deque()
                break
    m = d[t] #dlugosc sciezki, jesli sciezka nie istnieje zwraca 0
    if not arr: return m
    else:
        res = [t]
        while parent[t] != None:
            res.append(parent[t])
            t = parent[t]
        return res, m

def longer( G, s, t ):
    path, n = shortestPath(G, s, t, True)
    for i in range(n-1): 
        G[path[i]].remove(path[i+1])
        G[path[i+1]].remove(path[i]) #usuwam krawedz z grafu
        
        leng = shortestPath(G, s, t, False) 
        if leng > n or leng == 0: #leng == 0 oznacza ze sciezka nie istnieje zatem na dlugosc inf wiec zwracam wsp krawedzi
            return (path[i], path[i+1]) 
        
        G[path[i]].append(path[i+1])
        G[path[i+1]].append(path[i])
        
    return None         
    

    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )


