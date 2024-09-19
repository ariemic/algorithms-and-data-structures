'''
Dany jest graf nieskierowany G zawierajacy n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składajacy sie z dokładnie 4 wierzchołków. Zakładamy, ze
graf reprezentowany jest przez macierz sasiedztwa A.


Sposób działa tylko dla grafu nieskierowanego!
Szukam w macierzy prostokąta czyli dwóch kolumn w których dla obu wierszy są 1-dynki.


'''

def is_4_cycle(G):
    n = len(G)
    for i in range(n-1):
        for j in range(1, n):
            cnt = 0
            for k in range(n):
                if G[i][k] == 1 and G[j][k] == 1:
                    cnt += 1
                if cnt == 2: return True
    return False


