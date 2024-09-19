
class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val


def scal_iter(p,q):
    '''
    p, q - wskazania na dwie posortowane listy, musze je połączyć w jedną i zwrócić wskazanie na posortowaną liste
    '''

    r = Node()
    res = r
    
    while p != None and q != None:
        if p.val <= q.val:
            # r = Node(p.val)
            res.next = p
            p = p.next
        else:
            # r = Node(q.val)
            res.next = q
            q = q.next
        res = res.next
    if p == None:
        res.next = q
    elif q == None:
        res.next = p
    return r.next #BARDZO SPRYTNE TAK ZEBY NIE ZWRACAC WARTOWNIKA

def create_ll(tab):
    p = Node(tab[0])
    zb = p
    for i in range(1, len(tab)):
        q = Node(tab[i])
        p.next = q
        p = p.next
    return zb

def wypisz(zb):
    while zb != None:
        print(zb.val, end="")#end=""nastepny element wyswietla odrazu przy poprzednim
        zb = zb.next

def scal_rek(p, q):#DUZO KROTSZE
    if p == None:
        return q
    if q == None:
        return p
    if p.val < q.val:
        p.next = scal_rek(p.next, q)
        return p
    else:
        q.next = scal_rek(p, q.next)
        return q
    
    
p = create_ll([1, 4, 7])
q = create_ll([2, 3, 8, 9])
wypisz(p)
print()
wypisz(q)
print()
# res = scal_iter(p, q)
res = scal_rek(p, q)
wypisz(res)