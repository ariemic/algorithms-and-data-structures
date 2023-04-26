
#6) Dana jest szachownica n x n, każde pole ma koszt {1...5}, król w lewym górnym rogu, ma przejść w prawy dolny z jak najmniejszym kosztem -> return min koszt
# -> do kolejki BFS wrzucamy pare wiezcholek, wartosc/zmniejszamy wart

from collections import deque

def convert(G):
    n = len(G)
    res = []
    for i in range(n):
        for j in range(n):
            

def kingWalk(G, s=0):
    n = len(G)
    k = n-1 
    q = deque()
    q.append(s)
    visited = [False]*n 
    parent = [None]*n
    visited[s] = 1
    
        
    
    