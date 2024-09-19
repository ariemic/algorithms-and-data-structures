'''
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
'''

#Posortuje tablice, sprawdzaj od najmniejszej liczby czy jej suma znajduje sie w tablice korzystając z binary searcha

from random import randint

def partition(A, left, right):
    x = randint(left, right)
    A[right], A[x] = A[x], A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] < A[right]:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i


def quickSort(A, left, right):
    while left < right:
        pivot = partition(A, left, right)
        if (pivot-1) - left > right - (pivot+1):
            #lewa tablica jest większa zatem sortuje prawą tablice
            quickSort(A, pivot+1, right)
            right = pivot - 1
        else:
            quickSort(A, left, pivot-1)
            left = pivot + 1
            


            
A = [34, -234, -122, 2, 12, 22, -1, 4534, 21323, 22, 90]
n = len(A)
quickSort(A, 0, n-1)
print(A)