'''
Stacje nadawcze
#2) Stacje nadawcze - chcemy je wylaczac tak, by miec ciagle spojny graf -> z uzyciem BFS -> po kolei zapisujemy elementy w liście, na koniec odwracamy v


stacje - wierzchołki; Cel: Wyłączenie wszystkich nadajników bez przerwania spójności połączenia utrzymywanego przez stacje, czyli innymi słowy bez rozspójnienia grafu.

G - dane jako lista sąsiedztwa

Plan działania:
1. Wykonuje bfs i dochodzę do najdalszych stacji w grafie (takie wierzchołki z ktorych juz dalej nie wychodza krawedzi)
2. Jesli jakis wierzchołek jest jeszcze nie odwiedzony dodaje go do listy przetworzone ktore w czytane odwrotnej kolejnosci pozwoli mi na usuwanie wierzcholków
bez rospójnienia grafu
'''
from collections import deque

def stacje(G, s):
    n = len(G)
    q = deque()
    visited = [False]*n
    przetworzone = [s]
    q.append(s)
    visited[s] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                przetworzone.append(v)
                q.append(v)
    # przetworzone[::-1]
    print(przetworzone)
    #w mojej tablicy przetworzone bede usuwac z grafu wierzcholki od samego tylu listy, bo sa tam ostatnio dołączone wierzcholki z najwyzszym numerem fali
    while przetworzone:
        x = przetworzone.pop()
        print(G)
        for arr in G:
            try:
                arr.remove(x)
            except ValueError:
                pass #do nothing

G = [[3, 4], [4, 2], [4,1],[4,0], [1,3,0,2]]
print(stacje(G, 0))