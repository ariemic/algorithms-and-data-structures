class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next

def czy_nalezy(el, zb):
    r = zb
    while r != None:
        if r.val == el: return True
        r = r.next
    return False
    
def insert(el, zb):
    #wstawianie elementu do zbioru
    q = zb #WSKAZANIE NA PIERWSZY ELEMENT LISTY
    r = None #tail 
    while q != None and q.val < el:
        r = q
        q = q.next
    #element jest już w liście, nic nie musimy robić
    if q != None and q.val == el:
        return zb
    #przypadki gdy elementu nie ma w liście musimy tworzyć nowy element
    #wstawianie na początek, zbiór był pusty
    p = Node(el)
    
    
    #w liście są już jakieś elementy, ja wstawiam na początek
    if r == None:
        p.next = zb
        return p #zwracam wskazanie na pierwszy element łańcucha
    else:
        r.next = p
        p.next = q
        return zb
    

def insert1(el, zb):
    r = None #tail
    q = zb
    while q.next != None and q.val < el:
        r = q
        q = q.next
    #1 sprawdz czy ten el nie jest juz w zbiorze
    if q.next != None and q.val == el:
        return zb
    #2 el nie jest w zbiorze, trzeba go dodać
    #tworze obiekt  klasy node z przypisaną wartościa elementu
    p = Node()
    p.val = el
    
    #3 Wstawiam na początku listy
    if r == None:
        p.next = zb
        return p
    else:
        #Wstawiam na środku lub na końcu, czyli po ogonie ale
        #przed wskazaniem na większy element zbioru - q
        r.next = p
        p.next = q #po ogonie z nowym elemencie będzie reszta zb czyli q
        return zb
    
    
def remove(el, zb):
    r = None
    q = zb
    while q != None and q.val < el:
        r = q
        q = q.next
    
    if q == None: return zb
    if r == None: #usuwam pierwszy element
        #zwracam zbiór bo na q przesuwałem liste
        zb = zb.next
        return zb
    else:
        #usuwamy el z środka lub końca -> robimy przepięcie
        r.next = q.next
        return zb
    

def remove1(el, zb):
    #nie dziala usuwanie pierwszego elementu
    r = None
    q = zb
    while q != None and q.val < el:
        r = q
        q = q.next
    if q == None: #zb pusty
        return zb
    if r == None: #usun pierwszy element
        zb = zb.next
        return zb
    else:
        r.next = q.next
        return zb
         
    
    
def create_linked_list(tab):
    p = Node(tab[0])
    zb = p
    for i in range(1, len(tab)):
        q = Node(tab[i])
        p.next = q
        p = p.next
    return zb

tab = [1, 2, 5, 7]
zb = create_linked_list(tab)
insert(8, zb)
insert(3, zb)
wypisz(zb)
print()

# zb = remove1(1, zb)
wypisz(remove1(1, zb))
# wypisz(zb)
    

    