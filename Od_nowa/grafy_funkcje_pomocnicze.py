from collections import deque

def createG(edges, n, directed=False):
    #mam tablice krotek (vertex 1, vertex 2) reprezentujące krawędzie
    # z których chce stworzyć graf w reprezentacji listy sąsiedztwa
    G = [[] for _ in range(n)]
    for edge in edges:
        a, b = edge[0], edge[1]
        G[a].append(b)
        if not directed:
            G[b].append(a)
    return G

def find_n(edges):
    maxi = 0
    for arr in edges:
        for i in arr:
            maxi = max(i, maxi)
    return maxi+1
    
edges = [[0, 1], [1, 2], [2, 0]]
n = find_n(edges) #liczba wewnetrznych tablic ktore potrzebuje miec reprezentacja grafu
print(createG(edges, n ))


def DFS(G, visited, post_visited, u, time):
    visited[u] = True
    time += 1
    for v in G[u]:
        if not visited[v]:
            visited[v]=True
            DFS(G, visited, u)
    time += 1
    post_visited.appendleft((u, time)) #kolejnosc od najwyzszego czasu przetworzenia 