'''
Algorytm Bellmana-Forda z def. graf musi być skierowany
Najkrótsze ścieżki gdy dopuszczamy ujemne wagi
Złożoność: O(V*E)

1. Inicjalizacja
    for v { V:
        v.d = inf
        v.parent = None
    s.d = 0
    
2. Relaksacje
    for i in range(|V|-1):
        for (u, v) { E:
            Relax(u,v)
            
3. Weryfikacja
    czy dla każdego (u, v) { E:
        v.d <= u.d + w(u, v)?
        jeśli nie zachodzi przynajmniej dla jednego wierzchołka to mamy gdzieś w grafie cykl o ujemnej wartości
        
Czemu kroki 1 + 2 dają dobry wynik, jeśli nie ma cykli o ujemnej wadze?
Każda iteracji relaksuje co najmniej jedną dalej krawędź najkrótszej ścieżki

Czemu kork 3 wykrywa ujemne cykle wtedy suma[i=0, k-1](vi, v(i+1) ) < 0
Zał: weryfikacja nie wykryła ujemnego cyklu to dla każdego i:
    vi.d <= v(i-1).d + w(v(i-1), vi)
    Po zsumowaniu tych nierówności:
    suma[i=1, k](vi.d) <= suma[i=1, k]( v(i-1).d + w( v(i-1), vi) )
        x                       x                       < 0        sprzeczność
               
'''

def max_vertex(E):
    return max(E[i][1] for i in range(len(E)))+1


def relax(u, v, weight_edge, d, parent):
    if d[v] > d[u] + weight_edge:
        d[v] = d[u] + weight_edge
        parent[v] = u
        
def BellmanFord(Edges, s, t):
    #for adjencency graph representation
    n = max_vertex(Edges) 
    d = [float('inf')]*n
    parent = [None]*n
    d[s]=0
    
    for _ in range(n-1):
        for edge in Edges: #przechodze po kazdej krawedzi
            u, v, val = edge[0], edge[1], edge[2]
            relax(u, v, val, d, parent)
    is_negative_cycle = False
    for edge in Edges:
        u, v, val = edge[0], edge[1], edge[2]
        if d[v] > d[u] + val:
            is_negative_cycle = True #pojawił sie cykl o ujemnej wadze - bellman ford nie radzi sobie - bo takie cykle dają -inf
    
    if is_negative_cycle:
        return None
    else:
        return d[t]
    

Edges = [[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4], [2, 3, -3],
         [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]]
    
print(BellmanFord(Edges, 0, 4))    

    
    
    
    
    
    
    
    
   
        