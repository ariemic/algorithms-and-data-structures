'''
Sprawdz czy w grafie występuje cykl - jesli wejdziemy do wierzchołka który jest już oznaczony w tablicy visited na True oraz nie jest dzieckiem swojego rodzica, 
warunek z rodzicem jesk konieczny przy grafach nieskierowanych.
'''
from collections import deque   

def is_cycle(G, s=0):
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    q = deque()
    q.append(s)
    visited[s]= True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
            #jesli parent[rodzica] != dziecka to znaczy nie sa to na przemian rodzic-dziecko - nie przechodzimy w drugą strone po tej samej krawedzi co oznacza 
            #że mamy połączenie z jakimś wierzchołkiem dla którego wczesniej jeszcze nie istniała krawedź
            elif parent[u] != v: return True
    return False

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]
print(is_cycle(G))
        