import time
t0 = time.time()

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):#nowe karty, jeszcze nie przełożone
        for j in range(i):#wczesniejesze karty w tali
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
            else: #if A[j] < A[i] we can stop comparing because card before has less value then the next one
                continue
    return A


A = [1, 5, 3, 2, 9, 13, 12, 11, 7, 2]
print(insertion_sort(A))
t1 = time.time()
print(t1-t0)