from collections import deque
'''
Dnia pierwszego osoba 0 przekazuje wiadomość wszystkim swoim znajomym, dnia drugiego znajomi przekazują swoim znajomym i tak dalej...
Zwróc dzień w który najwięcej osób poznało wiadomość oraz liczbe znajomych
Stosujemy algorytm bfs, zliczamy ilość wierzchołków objętą daną falą, mamy zwrócić liczbe tych osób oraz numer tej fali
'''
def message(G, s):
    '''
    algorytm przyjmuje Graf w postaci listy krawędzi (lista krotek (skad dokąd połączenie))
    jak ktoś zna wiadomość to juz nie otrzyma drugi raz, juz ma przypisany jakis numer fali
    '''
    n = len(G)
    d = [0]*n
    visited = [False]*n
    q = deque()
    for i in range(n): #przez to ze graf w postaci listy krawedzi decyduje sie na zapelnienie kolejki na samym początku
        q.append(G[i])
    visited[s[0]], d[s[0]] = True, 1
    while q:
        u, v = q.popleft()
        if not visited[v]:
            visited[v] = True
            d[v] = d[u]+1
    return d
            
def messageQ(G, s):
    '''
    algorytm przyjmuje Graf w postaci listy krawędzi (lista krotek (skad dokąd połączenie))
    W kolejce przetrzymujemy krotki (nr wierzchołka, nr fali), dopóki nr fali jest bez zmian to powiekszamy zmienna maxi ktora szuka najdluzszej kolejki do przetworzenia  - 
    kiedy najwiecej osob poznalo wiadomosc
    '''
    n = len(G)
    visited = [False]*n
    q = deque()
    visited[s[0]] = True
    q.append((s, 1))
    maxi = 0
    while q:
        node, d = q.popleft()
            
        u, v = node[0], node[1]
        if not visited[v]:
            visited[v] = True
            q.append(())

    
G = [(0, 1), (0, 3), (3, 1), (3, 2)]
print(message(G, G[0]))
        
        
    
G = [(0, 1), (0, 3), (3, 1), (2, 3)]
print(message(G, G[0]))