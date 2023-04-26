#znajdz jednoczesnie max i min tak aby bylo 3/2 porównań

from random import randrange

#1 Sortowanie tablicy O(n^2)
tab = [randrange(1, 100) for _ in range(20)]
print(tab)
            
def insertion_sort(tab):
    n = len(tab)
    for i in range(1, n):
        for j in range(i):
            if tab[i] < tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
            else: continue
    return tab
print(insertion_sort(tab))

#2 Sortowanie listy odsyłaczowej
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        
#a wstawianie do posortowanej listy        
def extract_max(L): 
    M = L 
    while L.next != None:
        if L.next.val > M.next.val:
            M = L
    R = M.next
    M.next = R.next
    R.next = None
    return R

#b wyciąganie maksimum z listy
def insert(head, node):
    
    while head.next != None and head.next.val <= node.val:
        head = head.next
    node.next = head.next
    head.next = node

#c sortowanie listy przez wstawianie
def insertion_sort(head): #DOKOŃCZYĆ
    A = Node(None)
    while head.next:
        temp = head.next
        head.next = temp.next
        insert(f, temp)
        
def selection_sort(head):
    new_list = Node(None)
    while head.next != None:
        curr_max = extract_max(head)
        curr_max.next = new_list.next
        new_list = curr_max
    return new_list

#3 Algorytm znajdujązy jednocześnie minimum i maximum używając około 3/2n porównań
# 3 porw na 2 indeksy
def f(T):
    n = len(T)
    mini = T[-1]
    maxi = T[-1]
    for i in range(1, n-2):#patrzmy na drugi elem z pary dlatego start na indx = 1
        if T[i] < T[i-1]:
            mi, ma = T[i], T[i -1]
        else:
            mi, ma = T[i-1], T[i]
        
        
#4 T - posortowana tablica liczb; x - liczba; sprawdz czy istnieją indeksy i, j, takie że T[j] - T[i]=x

def sortowacz(tab, x):
    i = 0
    j = i+1
    while i < len(tab):
        if tab[j] - tab[i] == x:
            return True
        if tab[j] - tab[i] < x:
            j += 1
        else:
            i += 1
    return False 

        
