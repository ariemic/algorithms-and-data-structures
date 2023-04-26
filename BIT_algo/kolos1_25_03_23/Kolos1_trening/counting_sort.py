def CountingSort(A,k):
    #k - przedzial z jakiego są wartości
    n = len(A)
    B = [0]*k
    for val in A:
        B[val] += 1
    #make >= statement
    for i in range(1,k):
        B[i] = B[i] + B[i-1]
    C = [0]*n
    for i in range(n-1, -1, -1):
        C[B[A[i]]-1] = A[i]
        B[A[i]] -= 1
    return C

A = [3, 5, 2, 1, 2, 5, 1]
print(CountingSort(A, 6))