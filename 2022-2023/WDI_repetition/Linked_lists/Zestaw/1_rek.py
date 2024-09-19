
class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val
    
def wypisz(zb):
    while zb != None:
        print(zb.val)
        zb = zb.next

#uwaga lista jest posortowna rosnąco
    
def czy_nalezy_rek(el, zb):
    #rekurencyjnie
    if zb.next is None: 
        return False
    if zb.next.val == el:
        return True
    elif zb.next.val > el:
        return False
    else:
        return(el, zb.next)

def czy_nalezy(el, zb):
    while zb.next != None:
        if zb.val == el:
            return True
        zb = zb.next
    return False

def wstaw_rek(el, zb): #przy rekurencji dawanie wartownika nie ma sensu
    #CZY PRZY REKURENCYJNYM WSTAWIANIU TRAKTUJEMY PIERWSZY ELEMENT ZB JAK WARTOWNIK?
    #1 jesli w zb jest jeden element
    if zb.next == None:
        q = Node(el)
        zb.next = q
        #nic nie trzeba zwracać bo zmieniamy wskaźniki w pamięci, zbior przy wyswietlaniu ma
        #zmienione wartości
        return 
    else:
        if zb.next.val == el:
            return
        elif zb.next.val < el:
            wstaw_rek(el, zb.next)
        else:
            #wstawiam na początku listy element
            q = Node(el)
            q.next = zb.next
            zb.next = q #wstawiam sklejony dalszy ciąg zb i element dodany na poczatku

def wstaw_rek1(el, zb):
    #wstawiam na koniec
    if zb.next == None:
        q = Node(el)
        zb.next = q
        return 
    else:
        #PROBLEM JEZELI EL == WARTOSCI PIERWSZEGO ELEM ZBIORU BEDZIEMY MIEC POWTORZENIE
        if zb.next.val == el:
            return 
        elif zb.next.val < el:
            wstaw_rek1(el, zb.next)
        else:
            q = Node(el)
            q.next = zb.next
            zb.next = q
            
def create_linked(tab):
    p = Node(tab[0])
    p_cp = p
    n = len(tab)
    for i in range(1,n):
        q = Node(tab[i])
        p.next = q
        p = p.next
    return p_cp

# tab = [1, 2, 4, 5]
# p = create_linked(tab)
# wypisz(p)

def wstaw(el, zb):
    r = None
    p = zb
    while p.next != None and p.val < el:
        r = p
        p = p.next
    if p.next != None and p.val == el:
        return zb
    #wstaw el na początek
    q = Node(el)
    if r == None:
        q.next = zb
        return q
    #wstaw po środku
    if p.val < el:
        #wstawiam el pomiedzy r i p
        r.next = q
        q.next = p
        return zb
    
def remove_rek(el, zb):
    #nie usuwa pierwszego elementu z listy
    if zb.next == None:
        return 
    else:
        if zb.next.val == el:
            zb.next = zb.next.next
        else:
            remove_rek(el, zb.next)

zb = Node(1)
zb.next = Node(2)
zb.next.next = Node(8)
wstaw_rek1(7, zb)
wstaw_rek(4, zb)
remove_rek(1, zb)
wypisz(zb)
