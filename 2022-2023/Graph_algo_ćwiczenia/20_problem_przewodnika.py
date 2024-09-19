'''
po kolei dodajemy KRAWEDZIE w kolejnosi MALEJACY WAG i jesli w ktoryms momencie mozemy dojsc do konca,
do celu, to ilosc grup jakie musimy stworzyc jest rowna: liczbie uczestnikow / waga ostatniej krawedzi jaka dodalismy
to jest ta minimalna pojemnosc autobusu 
'''

from collections import deque
from math import ceil

def max_vertex(Edges):
    return max(Edges[i][1] for i in range(len(Edges)))+1

def sort_edges_by_wieghts(Edges):
    #insertion sort in decreasing order -> first element has the largest weight
    n = len(Edges)
    for i in range(1, n):
        for j in range(i):
            if Edges[i][2] > Edges[j][2]:
                Edges[i], Edges[j] = Edges[j], Edges[i]
            else:
                continue
    return Edges

def add_edge(G, edge):
    u, v = edge[0], edge[1]
    G[u].append(v)
    G[v].append(u)
    

def bfs(G, A, B, n):
    #function return True if path exist else False
    q = deque()
    visited = [False]*n
    parent = [None]*n
    q.append(A)
    visited[A] = True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
            if v == B:
                return True
    return False

def turist_guide_problem(Edges, A, B, K):
    n = max_vertex(Edges)
    group_cnt = 0
    G = [[] for _ in range(n)]
    Edges = sort_edges_by_wieghts(Edges)
    for edge in Edges:
        add_edge(G, edge)
        if bfs(G, A, B, n):
            bus_capacity = edge[2]
            group_cnt= ceil(K//bus_capacity)
            return group_cnt
            

Edges = [
    (0, 1, 50),
    (0, 3, 25),
    (1, 2, 75),
    (2, 3, 20),
    (3, 5, 50),
    (5, 6, 2),
    (4, 6, 10),
    (6, 7, 20),
    (7, 8, 70),
    (1, 5, 75),
    (2, 5, 30),
    (3, 4, 50)
]

print(turist_guide_problem(Edges, 0, 8, 100))   
    
    
