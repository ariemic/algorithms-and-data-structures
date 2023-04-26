''''
1)Sprawdzanie czy graf jest dwudzielny (BFS) - zakladamy ze graf jest spojny
2) Liczba spójnych składaowych w grafie (DFS)
'''
from collections import deque
def dwudzielny(G, start_v):
    n = len(G)
    colors = [-1]*n
    
    q = deque()
    q.append(start_v)
    colors[start_v]=1
    while q:
        v = q.popleft()
        for u in G[v]:
            if colors[u] == -1:
                colors[u] = (colors[v]+1)%2
                q.append(u)
            else:
                if colors[u] == colors[v]: return False
    return True

#2
def ccs(G):
    n = len(G)
    vis = [0]*n
    def dfs(v):
        vis[v]=1
        for x in G[v]:
            if vis[x]: continue
            dfs(x)
    l = 0
    for i in range(n):
        if not vis[i]:
            l += 1
            dfs(i)
    return l

#3)Dany jest graf jako macierz sąsiedztwa. Czy istnieje cykl o długości 4?
#   a)O(v^4) -> sprawdzamy wszystkie czwórki wierchołków czy są połączone v 
#   b)O(v^3) -> 1) Rozważamy wszystkie pary wierzcholkow -> jesli x i y maja wspolnych dwoch sasiadow -> 
# przechodzimy po macierzy sąsiedztwa/BFS dla każdego wierzchołka v

G1 = [[0, 0, 0, 1], 
      [0, 0, 0, 1], 
      [0, 0, 0, 1], 
      [1, 1, 1, 0]]

def cykl4(G):
    n = len(G)
    for i in range(n-1):
        for j in range(i+1, n):
            cnt = 0
            for k in range(n): 
                if G[i][k] and G[j][i]:
                   cnt += 1
                if cnt >= 2:
                    return True
    return False

print(cykl4(G1))
'''
4) Znaleźć uniwersalne ujścia t - czy istnieje wierzchołke (ujście) do którego wchodzą wszystkie pozostałe i on do żadnego nie wchodzi
a) dla każdego v istnieje krawędź a v
b) t nie posiada krawędzi wychodzących
Dane: G - graf skierowany jako macierz sąsiedztwa

5) Znaleźć najkrótszą ścieżke w grafie używając BFS'a w grafie nieskierowanym. 
'''
def spath(G, s, k):
    n = len(G)
    vis = [0]*n
    parent = [-1]*n
    q = deque()
    vis[s] = 1
    q.append()
    while q:
        v = q.popleft()
        for x in G[v]:
            if vis[x]: continue
            parent[x] = v
            q.append(x)
            vis[x]=1
    t = [k] #tablica t przetrzymuje najkrótszą ściezke od wierzcholka koncowego do początkowego
    while parent[k] != -1:#bo wierzchołek startowy zawsze nie ma rodzica więc jego wartość jest zawsze -1
        t.append(parent[k])#dodajemy rodzica k
        k = parent(k)#zamieniamy k ze swoim rodzicem dopoki rodzica nie zabraknie czyli nie dotarlismy do startowego wierzchołka
    return 



'''
6. Dana jest szachownica nxn. Każde pole ma koszt {1, 2, 3, 4, 5}
Szukaj: minimlany koszt przejścia
Konwertujemy do listy sąsiedztwa z modyfiacją, ktora uwzględnia te wagi

7. malejące krawędzie, mamy graf nieskierowany takei, że każda krawędz ma inny koszt.
Znaleźć algortym, którey przejdzie z wierzchołka z s do t i ma najmniejsze wagi. 
Trzeba sprawdzać czy jest spójny.

8. Mamy graf G=(V, E), to mapa drogowa kraju. Koszt przejazdu przez krawędz to 0 lub 1. Chcemy z s do z tak żeby koszt ścieżki był najmniejszy.
Kolejka do której na początek wrzuacamy 0, a dopiero poźniej z kosztem 1. bfs
'''











 







            
                