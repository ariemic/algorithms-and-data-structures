from random import randint

def partition(A, left, right):
    # x = randint(left, right)
    x = right
    i = left - 1
    for j in range(left, right):
        if A[j] <= A[x]:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[x] = A[x], A[i]
    return i

def quicksort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
        quicksort(A, left, pivot-1)
        quicksort(A, pivot+1, right)

def strong_string(T):
    '''
    Porównuje każde słowo ze swoją odwrotnością i zostawiam wersje mniejszą według porządku leksykograficznego.
    '''
    n = len(T)
    # S = [0]*n
    for i in range(n):
        word = T[i] 
        mirror, m = word[::-1], len(word)
        for j in range(m):
            if ord(word[j]) > ord(mirror[j]):
                T[i] = mirror
                break
            elif ord(word[j]) < ord(mirror[j]):
                break
        # S[i] = sum([ord(T[i][j]) for j in range(m)])
    quickSort(T, 0, n-1)  
    print(T)
    '''
    sortuje leksykograficznie słowa, po pierwszej literze, pozniej po drugiej, pozniej po trzeciej -> jakies sortowanie stabilne - trzeba jakoś zmienić quicksorta żeby sortował alfabetycznie
    
    '''
    # nadaj wartości słowom tak żeby każde miało jakiś kod
    i = maxi =  0
    while i < n:
        j, cnt = i+1, 1 
        while j < n and T[i] == T[j]:
            cnt += 1
            j += 1
        maxi = max(cnt, maxi)
        if maxi > n//2 + 1: return maxi
        i = j
    return maxi
    
T = ["pies", "mysz", "kot", "kogut", "tok", "siep", "kot"]
print(strong_string(T))

# A = [433, 467, 334, 554, 334, 433, 334]
# quickSort(A, 0, len(A)-1)
# print(A)

print("mysz" > "kot")