'''
Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algortym, który podzieli te liczby na n par
w taki sposób, że podział będzie miał najmniejsza maksymalna sumę liczb w parze.
Przykładowo, dla liczb (1,3, 5, 9) możemy mieć podziały ((1,3), (5,9)), ((1,5), (3,9)) oraz ((1,9), (3, 5))
Sumy par dla tych podziałow to (4, 14), (6, 12) oraz (10,8) w związku z tym maksylamne sumy 
to 14, 12, 10. Wynika z tego, że ostatni podziął ma najmniejszą sumę.
'''
def partition(A, left, right):
    x = A[right]
    i = left -1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i

def quickSort(A, left,right):
    while left < right:
        pivot = partition(A, left, right)
        quickSort(A, left, pivot-1)
        left = pivot+1
    return A

def find(A, n):
    #mamy n par ktore sumuja sie do sumy liczb z całej tablicy
    #parujemy najbardziej skrajne elementy tablicy, dostaniemy tak możliwe najmniejszą maksymalną
    A = quickSort(A, 0, n//2)
    return [(A[i],A[-i-1])for i in range(n//2)]

    
print(find([1, 3, 5, 9], 4))
    