#3 Dany jest graf G jako macierz sąsiedztwa, czy w tym grafie istnieje cykl o długości 4

G = [[0, 1, 0, 0, 1], #G - graf nieskierowany z cyklem długości 4
     [1, 0, 1, 1, 1],
     [0, 1, 0, 1, 0], 
     [0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0]]

G1 = [[0, 0, 0, 1], 
      [0, 0, 0, 1], 
      [0, 0, 0, 1], 
      [1, 1, 1, 0]]

from collections import deque

# szukasz kwadratu na macierzy; najpierw wybierasz 2 wiersze a potem sprawdzasz 
# każdą kolumnę jak są 2 kolumny gdzie obie przecinające się mają krawędź to zwracasz True

def cykl4(G):
    '''
    Tworze dwie for loopy które mają przechodzić po kazdym z wierszy pierwsza petla ustawia sie na wierszu 0, a kolejna petla przechodzi 
    wszystkie pozostałe wiersze. Trzecia pętla przechodzi przez kolumny, jeśli znajde z i-tym wierszu i k-tej kolumnie krawędz (ozn. 1 w macierzy)
    to sprawdzam czy krawędz wystepuje, także w j-tym wierszu i k-tej kolumnie, jesli tak to zwiekszam cnt++; jesli znajde takie dwie kolumny
    dla wiersza i oraz j że w obu z nich są krawedzie oznacza to ze znalazlem 4 wierzchołki ktore mają połączenia z 2 innymi - znalazłem 
    4 wierzchołkowy cykl.
    '''
    n = len(G)
    for i in range(n-1):
        for j in range(i+1, n):
            cnt = 0
            for k in range(n):
                if G[i][k] and G[j][k]:  #czy to jest poprawne czy Doroty jest poprawne a może oba są? Dla moich przykladow oba dzialaja
                    cnt += 1
                if cnt == 2:
                    return True
    return False


print(cykl4(G1))

def is_cycle4(G, s=0):
    #za pomoca bfs'a, jak znajde cykl w grafie to sprawdzam jakiej jest długości?
    #trzeba sprawdzić czy działa ale to dla list sąsiedztwa
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    d = [-1]*n
    q = deque()
    q.append(s)
    visited[s], d[s]=True, 0
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u]+1
                q.append(v)
            elif parent[u] != v and d[v] == 3:#mamy cykl trzeba sprawdzic czy wynosi 4
                return True



