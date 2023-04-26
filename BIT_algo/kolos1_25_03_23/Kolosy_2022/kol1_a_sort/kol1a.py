from kol1atesty import runtests
from math import floor
#tworze kupełki ze względu na długość napisu O(n), sortuje wewnątrz kubła i wyliczam liczbe wystąpień najczęstrzego elementu O(klogn). Porównuje z maxami z innych kubełków O(n)


def merge_sort(S):
    n = len(S)
    if n > 1:
        left = merge_sort(S[:n//2])
        right = merge_sort(S[n//2:])
        
        #merge
        nl, nr = len(left), len(right)
        i = j = k = 0
        while i < nl and j < nr:
            if left[i] <= right[j]:
                S[k] = left[i]
                i += 1
            else:
                S[k] = right[j]
                j += 1
            k +=1
        while i != nl:
            S[k] = left[i]
            i += 1
            k += 1;
        while j != nr:
            S[k] = right[j]
            j += 1
            k += 1
    return S
    

def Buckets(T):
    #dla liczb z przedziału od [0, 1)
    n = len(T)
    B = [[]for _ in range(n)] #create buckets for numbers # tu jest problem jeśli chodzi o długość napisu
    for i in range(n):
        buck_ind = min(n-1, floor(len(T[i])/n)) #indeksem kosza będzie długość napisu
        B[buck_ind].append(T[i]) #put number into suitable bucket
    maxi = 0
    for bucket in B:
        merge_sort(bucket)
        k = len(bucket)
        i =  0
        j = 1
        while j < k:
            cnt = 0
            while j < k and bucket[i] == bucket[j]: 
                j += 1
                cnt += 1
            maxi = max(cnt, maxi)
            i = j
            j += 1
    return maxi+1
    
def g(T):
    n = len(T)
    for i in range(n):
        if T[i] > T[i][::-1]:
            T[i] = T[i][::-1]
        #wypieram zawsze opcje mniejszą leksykograficznie
    maxi = Buckets(T)
    return maxi


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
