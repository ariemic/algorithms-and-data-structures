'''
Dobry początek
Znajdz wyszystkie silnie spojne skladowe, zamien je na jeden wierzcholek
Silna spojna skladowa to taki podzbior wierzcholkow ze istnieje sciezka pomiedzy kazda para wierzcholkow w tej silnie spojnej skladowej
Wszystkie wiercholki w cyklu sa dobrymi poczatkami

DFS:
-dfs na grafie
-zapisujemy kolejnosc przetwarzania (postorder - wychodzac z dfs na danym wierzcholku zapisuje go)
-znajdujemy wierzcholek z najwyzsza wartoscia i z znalezionego wierzcholka urachamiam dfs/ bfs i patrze czy dojde z niego do wszystkich pozostalych wierzcholkow

Urachamiam dfs na calym grafie, zapisuje kolejnosc przetwarzania w tablicy, ten wierzcholek ktory jest przetworzony jako ostatni moze być
jedynie dobrym poczatkiem, z znalezionego wierzcholka urachamiam dfs/ bfs i patrze czy dojde z niego do wszystkich pozostalych wierzcholkow
'''
def dfsVisit(G, v, time, time_completed, visited):
    #time - ile juz wierzcholkow prztworzylismy
    visited[v] = True
    for v in G[v]:
        if not visited[v]:
            time = dfsVisit(G, v, time, time_completed, visited)
    time_completed[v] = time #wpisujemy tutaj czas przetworzenia wierzcholka (post-order)
    time += 1
    return time

def good_beginning(G):
    n = len(G)
    time_visited = [-1]*n #zapisuje czas przetworzenia dla kazdego wierzcholka
    visited = [False]*n
    time = 1
    
    for v in range(n):
        if not visited[v]:
            time = dfsVisit(G, v, time, time_visited, visited)
            
    max_v = time_visited.index(n-1) #sztuczka do znalezienia wierzcholka o najwyzszym czasie przetworzenia
    visited = [False]*n
    time_visited = [-1]*n
    time = dfsVisit(G, max_v, time, time_visited, visited)
    
    #finish it
    
    
    