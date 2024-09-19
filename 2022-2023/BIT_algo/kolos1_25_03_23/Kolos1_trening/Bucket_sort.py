def insertion_sort(A):
    n = len(A)
    for i in range(1, n):#nowe karty, jeszcze nie przełożone
        for j in range(i):#wczesniejesze karty w tali
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
            else: #if A[j] < A[i] we can stop comparing because card before has less value then the next one
                continue
    return A


def Bucket_Sort(A, n):
    B = [0]*n
    for i in range(n):
        B[n*A[i]].append(A[i])
    for i in range(n):
        insertion_sort(B[i])
    