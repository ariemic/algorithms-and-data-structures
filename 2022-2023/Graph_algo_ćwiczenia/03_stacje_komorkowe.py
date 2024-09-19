#Algorytm ma zwracać kolejność stacji w jakiej będziemy odłączać je tak aby graf pozostał spójny

# Plan działania:
# 1. Wykonuje bfs i dochodzę do najdalszych stacji w grafie (takie wierzchołki z ktorych juz dalej nie wychodza krawedzi)
# 2. Jesli jakis wierzchołek jest jeszcze nie odwiedzony dodaje go do listy przetworzone ktore w czytane odwrotnej kolejnosci pozwoli mi na usuwanie wierzcholków
# bez rospójnienia grafu


from collections import deque

def stations(G, s=0):
    q = deque()
    n = len(G)
    visited, parent = [False]*n, [None]*n
    res = []
    visited[s] = True 
    q.append(s)
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                parent[v] = u
        res.append(u)
    return res[::-1]


G = [[3, 4], [4, 2], [4,1],[4,0], [1,3,0,2]]
print(stations(G))