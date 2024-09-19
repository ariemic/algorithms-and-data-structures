from zad3testy import runtests
import math

'''
Mamy w poleceniou równomierne rozłożenie to zazwyczaj chodzi o bucketSorta.
Tworze listę tupli w któej zapamiętuje orginalną wartość razem z jej wykładnikiem.
(wartość pierwotna, wykładnik), następnie wyciągamy z tupli tylko pierwszy element.
'''

def insertionSort(A, idx):
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            if A[i][idx] < A[j][idx]:
                A[i], A[j] = A[j], A[i]
                
def BucketSort(T, idx, id_out):
    #idx - indeks po którym mam sortować tablice, id_out - indeks tablicy którym chce zwracać w tablicy bez tupli
    #dla liczb z przedziału od [0, 1)
    n = len(T)
    B = [[]for _ in range(n)] #create buckets for numbers 
    
    for i in range(n):
        buck_ind = int(n*T[i][idx]) #int round down
        B[buck_ind].append(T[i]) #put number into suitable bucket
    for bucket in B:
        insertionSort(bucket, idx)
    i = 0
    for bucket in B:
        for x in bucket:
            T[i] = x[id_out]
            i += 1
    
    
def fast_sort(tab, a):
    '''
    Funkcja dostąje tablice z wynikiami eksperymetnu w postaci a^x, gdzie x nalezy do przedziału [0, 1)
    Tworze nową tablice zawierającą tuple gdzie na pierwszym indeskcie będzie wynik eksperymentu w postaci loga(a^x) = x, a na drugiej wynik w postacji zwykłej.
    Sortuje bucketSortem po 0-owej wspórzędnej. Zwracam posortowaną tablice z wynikami w postaci jak na wejściu.
    '''
    n = len(tab)
    
    for i in range(n):
        tab[i] = (math.log(tab[i], a), tab[i])
    BucketSort(tab, 0, 1)
    return tab



runtests( fast_sort )
