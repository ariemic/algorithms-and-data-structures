from random import randrange
import time
t0 = time.time()

#dla k = 20
def CountingSort(A, k):
    n = len(A)
    C , B = [0]*k, [0]*n
    for i in range(n): #count values in A array and add them to equal them index at C array
        C[A[i]] += 1
    # print(C)
    for i in range(1, k): #make <= order for elements
        C[i] = C[i] + C[i-1]
    # print(C)
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    # print(C)
    # print(B)
    return B


k = int(input("Enter the range value:  "))
A = [randrange(k)for _ in range(15)]
print(A)
# A = [6, 8, 11, 7, 18, 7, 17, 18, 4, 9, 3, 17, 12]
print(CountingSort(A, k))

t1 = time.time()
total = t1 - t0
print(total)