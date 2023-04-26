def length(T):
    maxLength = 0
    for i in range(len(T)):
        n = len(T[i])
        if n > maxLength: maxLength = n
    #
    return maxLength
# end def ^^^

def countingSort(A, p):
    n = len(A)
    B = [ 0 for _ in range(n) ]
    C = [ 0 for _ in range(27) ] # 27, bo indeks 0 bede zwiekszac, gdy dlugosc slowa jest mniejsza niz obecnie sortowana pozycja
    base = ord('a') - 1 # odejmuje -1 dla "dummy letter", patrz wyzej
    #
    for i in range(n):
        if len( A[i] ) > p:
            index = ord( A[i][p] ) - base 
        else:
            index = 0
        #
        C[ index ] += 1
    #
    for i in range(1,27):
        C[i] = C[i] + C[i-1]
    #
    for i in range(n - 1, -1, -1):
        if len( A[i] ) > p:
            index = ord( A[i][p] ) - base 
        else:
            index = 0
        #
        B[ C[index] - 1 ] = A[i]
        C[ index ] -= 1
    #
    return B
#end def ^^^

def radixSort(T):
    n = len(T)
    maxLength = length(T)
    #
    
    for i in range( maxLength - 1, -1, -1):
        print(T)
        T = countingSort(T, i)
    #
    return T

#end def ^^^

T = [ "ala", "kot", "zybaz", "grafa", "grafy", "matematyka", "alicja", "kraina", "czarow", "lubie", "campo", "di", "fiori"]
T = radixSort(T)
print(T)