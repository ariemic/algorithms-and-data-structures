# Proszę napisać funkcję, która rozdziela listę na dwie listy. 
# Pierwsza powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. 
# Do funkcji należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. 
# Funkcja powinna zwrócić liczbę usuniętych elementów.

#USUNIECIE Z PAMIECI OZNACZA USUNIECIE REFERENCJI


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

def wypisz(zb):
    while zb != None:
        print(zb.val, end=" ")
        zb = zb.next
        
def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q

def split(head, res_n, res_p):
    #zwraca liczbe usuniętych elementów
    p = head
    cnt = 0
    #listy wynikowe zawierają wartowniki
    while p != None:
        if p.val%2 == 0 and p.val > 0:
            res_p.next = p
            res_p = res_p.next
            # p = p.next
        elif p.val%2 == 1 and p.val < 0:
            res_n.next = p
            res_n = res_n.next
            # p = p.next
        else:#remove
            cnt += 1
        temp = p
        p = p.next
        temp.next = None #likwiduje połaczenia w liscie przyjmowanej, 
        #gwarantuje to rozdzielenie listy tak aby została zlikwidowana w pamięci
        #PROBLEM ZOSTANIE W PAMIECI PIERWSZY ELEMENT LISTY
    res_n.next = None
    res_p.next = None
    return cnt

res_n = Node()
res_p = Node()
p = create_linked([1, 2, 4, 5, -2, -5, -8, 12, -49])
a = split(p, res_n, res_p)
wypisz(res_n) #wypisuje z wartownikami -> jak wypisać bez nich?
print()
wypisz(res_p)#same problem what above
print()
print(a)
wypisz(p)