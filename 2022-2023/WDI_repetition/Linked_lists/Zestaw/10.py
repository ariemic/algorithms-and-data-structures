# Liczby naturalne reprezentowane jak poprzednim zadaniu. 
# Proszę napisać funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next
        
def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q

def reverse(p):
    if p.next == None:
        return p
    else:
        prev = reverse(p.next) #tworzymy odwrocony liste tutaj korzystajac z rekurencji
        q = prev
        while q.next != None:
            q = q.next 
        q.next = p
        p.next = None 
        return prev
        
def rozmiar(p):
    cnt = 0
    while p != None:
        cnt += 1
    return cnt

def add(p, q):
    #wstawiam do funkcji juz obrocone listy
    #DZIALA TYLKO DLA NAJPROSTSZEGO PRZYPADKU
    r = Node()
    cr = r
    #musze zrobić ten sam rozmiar list dodając zera, inczej operujac na odwroc listach 
    #mamy duzy problem bo nie rozrozniamy co jest cześcią dziesiętną a co jednością 
    size_p, size_q = rozmiar(p), rozmiar(q)
    while p != None and q != None:
        value = p.val + q.val 
        if value < 9:
            r.next = Node(value)
            r = r.next
        p = p.next
        q = q.next
    
        
    return reverse(cr.next)

p = create_linked([1, 2, 3])
q = create_linked([2, 3])
p = reverse(p)
q = reverse(q)
r = add(p, q)
wypisz(r)
print()
        
        