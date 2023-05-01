'''
Napisz algorytm wyodrębniający silnie spójne składowe z grafu. 
Zwróć tablice [[wierzcholki pierwszej spojnej skladowe], [2-iej], [i-tej]]

#mógłbym zapisywać czasy z wierzchołkiem i po nich po sortować counting sortem, 
#ale falisz mówił że tak się nie robi

#tworze liste w której zapisuje wierzcholki w kolejnoscie czasow przetworzenia w
#wyniku czego wierzchołek o najwyzszym czasie przetworzenia bede miec na początku listy
'''
from collections import deque

def StronglyConnectedComponents(G):
    time = 0
    n = len(G)
    visited = [False]*n
    components = []
    cnt = 0 #cnt of connected compomnents
    
    finish_times_order = deque() #wierzcholki po przejsciu pierwszego dfs'a beda w kolejnoscie malejacej czasow przetworzenia
    
    def dfsVisit(G, u, arr):
        nonlocal time
        time += 1
        visited[u] = True 
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v, arr)
        time += 1
        arr.appendleft(u)
        
    #pierwsze przejscie dfs'a
    for u in range(n):
        if not visited[u]:
            dfsVisit(G, u, finish_times_order)
    
    #odwracam kierunek krawędzi - PROBLEM JEŻELI CHCIAŁEM ROBIĆ TO NA TYM SAMYM GRAFIE PRZEZ JEDNOCZESNE USUWANIE I DODAWANIE KRAWĘDZI
    newG = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            newG[v].append(u)
    
            
    #drugie przejscie dfs'a
    visited = [False]*n
    for u in finish_times_order:
        if not visited[u]:
            cnt += 1
            #wierzchołki odwiedzone w danym dfs'ie tworzą spójną składową
            vertices=deque()
            dfsVisit(newG, u, vertices)
            components.append(vertices)
    
    return components, cnt

G = [[1], [2], [0, 3, 8], [4, 6], [5], [3], [5], [8], [9], [5, 10], [3, 7]]

print(StronglyConnectedComponents(G))