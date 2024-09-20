def dfs(G):
    time = 0
    n = len(G)
    visited = [False]*n
    parent = [None]*n             
    
    def dfs_visit(G, u):
        nonlocal time #saying when the search finishs examining v's adjacency list (and makes v black)
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)
        time += 1 #czas przetworzenia tego wierzchołka
    
    #sprawdza od indeksu 0, zatem pokolei od 0 wierzchołka, nie mogę ustalić żeby przeszukiwanie ustalać od innego w tej wersji algorytmu
    for u in range(n): #w ten sposób przejdze przez wyszyskie wierzchołki grafu, nawet jezeli z niczym nie maja płączenia 
        if not visited[u]:
            dfs_visit(G, u)
        
            