'''
na wejściu otrzymuje ciąg n liter oraz liczbę k i wypisuje najczęsciej powtarzający się podciąg dłguości k. 
Ciąg składa się z wyłącznie z liter a i b. To że wystąpienia na siebie nachodza nie jest istotne.
np. ababaaaabb, k = 3. rozwiązaniem jest aba

Tworze tablice w czasie liniowym z wszystami wyrazami długości k. Następnie sortuje to raddix sortem a jako algo sortującego w raddix sorcie uzywam counting sorta.
'''

def CountSort_binary(arr, p):
    new_arr = [[] for _ in range(2)]
    # base = 2**p
    for seq in arr: #moge tak zrobic bo napisy mają tą samą długość
        last = seq[p] #napis jest traktowany jak tablica w pythone biore ostatnią litere w napisie i po niej będę sortować
        idx = ord(last)-97
        new_arr[idx].append(seq)
    i = 0
    for bucket in new_arr:
        #nie musze sortować w buckecie po sortuje po pojedynczej literze, każda litera w koszu jest taka sama
        for x in bucket:
            arr[i] = x
            i += 1

def RaddixSort(arr, k):
    for i in range(k-1, -1, -1):
        CountSort_binary(arr, i)
    

def findLongestSubsequence(napis, k):
    n = len(napis)
    arr = []
    i = 0
    while i + k < n:  
        arr.append(napis[i:i+k])
        i += 1
    #sort by Raddix Sort
    RaddixSort(arr, k)
    print(arr)
    maxi, res = 0, ''
    m, i = len(arr), 0
    while i + 1 < m:
        cnt = 1
        j = i+1
        while arr[j] == arr[i]:
            cnt += 1
            j += 1
        if cnt > maxi:
            maxi = cnt
            res = arr[i]
        i = j
    return res

napis = 'ababaaabaabababbbb'
# print(napis[2])
# print(napis[0:3])
print(findLongestSubsequence(napis , 3))
