def partition(A, left, right):
    i = left - 1
    for j in range(left, right):
        if A[j] <= A[right]:
            i += 1
            A[j], A[i] = A[i], A[j] 
    i += 1
    A[i], A[right] = A[right], A[i]
    return i

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def push(self, data):
        self.items.append(data)


def quickSortStack(A, l, r):
    '''
    Mój stos przechowuje krotke z granicami nowej tablicy(indeks początkowy i końcowy)
    która ma ulec partycji, do momentu aż wielkość tej tablicy będzie 1 lub 2, 
    będziemy mieć poprawną kolejność elementów.
    
    Funckja wrzuca na stos nowe krotki w kolejnośći lewe prawe i z każdym przejściem, zabiera
    elementy ze stosu dostając nowe partycje, najepierw będzie posortowana tablica bardziej
    prawa później lewo ze wględu na własności stosu first in last out. 
    
    Stos pozwala nam przechowywać indeksy nowych (left, right) w pamięci, bez potrzeby do
    odwoływania się do nich rekurencyjnie. Z tego powodu nie ma tu wywoływań rekurencyjnych 
    funkcji quicksort, gdyż krotki do partycji będą pobierane bezpośrednio ze stosu.
    '''
    S = Stack()
    S.push((l, r))
    while not S.is_empty():
        left, right = S.pop()
        if left < right:
            pivot = partition(A, left, right)
            S.push((left, pivot-1))
            S.push((pivot+1, right))

A = [2, 4, 2, 1, 9, 10, 23, 21]
quickSortStack(A, 0, len(A)-1)
print(A)