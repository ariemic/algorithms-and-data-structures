""" 
Maksymalna liczba odwiedzonych komnat
F(x, y)- maksymalna liczba odwieczonych komnat po dojściu do (x,y) komnaty w F[(0,0)] trzymam krotke
pierwsza wartość krotki trzyma wynik idąc od lewj lub dołu 
a druga idąc od lewej lub góry

"""


from zad7testy import runtests

def print_matrix(F):
    n = len(F)
    for i in range(n):
        print(F[i])


def maze( L ):
    n = len(L)
    if L[0][0] == "#" or L[n-1][n-1] == "#":return -1

    #! undone 
    F = [[(0,0) for _ in range(n)]for _ in range(n)]

    for i in range(1, n):
        
        if L[i][0] != "#":
            F[i][0] = F[i-1][0] + 1
        
        if L[0][i] != "#":
            F[0][i] = F[0][i-1] + 1

    
    for col in range(1, n):
        
        for row in range(n):
            if L[row][col] != "#":
                F[row][col] = max(F[row][col],  F[row][col-1] + 1 )
                if row - 1 >= 0 and F[row-1][col] + 1 > F[row][col]:
                    F[row][col] = F[row-1][col] + 1
                    
        for row in range(n-1, -1, -1):
            if L[row][col] != "#":
                F[row][col] = max(F[row][col],  F[row][col-1] + 1 )
                if row + 1 <= n-1:
                    # napisuje wartości przechodze dwa razy po tych samym komnatach
                    F[row][col] = max(F[row+1][col] + 1, F[row][col])

            

    # print_matrix(F)
    return F[row][col] if F[row][col] != 0 else -1



L = ['....', 
     '..#.', 
     '..#.', 
     '....']


maze(L)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
