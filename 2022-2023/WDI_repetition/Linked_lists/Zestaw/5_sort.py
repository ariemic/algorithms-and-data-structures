# Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej cyfry pola val. 
# W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową,  która jest posortowana niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val
    
def wypisz(p):
    while p != None:
        print(p.val, end="-")
        p = p.next

def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q

def rozdziel(p):
    #zakladam ze lista p ma 10 elementow
    tab = [0]*10
    for i in range(10):
        tab[i] = Node(p.val%10)
        p = p.next
    #mam tablice z nodami, musze je posortować i połączyć w liste odsyławcza
    q = Node()
    r = q
    for i in range(10):
        prev = tab[i]
        for j in range(i+1, 10):
            curr = tab[j]
            if curr.val < prev.val:
                tab[j] = Node(prev.val)
                prev.val = curr.val
                
        q.next = tab[i]
        q = q.next
    return r.next 

    #DA SIE ŁATWIEJ ZROBIĆ TO ZADANIE ZAMIAST TWORZYĆ TABLICE Z NODAMI, STWORZYĆ TABLICE Z WARTOŚCIAMI A PÓŹNIEJ TWORZYĆ LISTE ODSYŁACZOWĄ Z TEGO
    #ALE TREŚĆ ZADANIA ZABRANIA TAKEIGO SPOSOBU

def rozdziel_sort(p):
    '''
    funkcja przekształaca liste p na liste q złożoną ostatnich cyfr każdego elementu, następnie ją sortuje niemalejąco
    '''
    q = p
    cnt = 0
    while p != None:
        p.val = p.val%10
        p = p.next
        cnt += 1
    p = q
    #sortuj niemalejąco linked liste NAPISAĆ SORTOWANIE
    for i in range(cnt-1):
        if p.val > p.next.val:
            r = p.val
            p.val = p.next.val
            p.next.val = r
        p = p.next
    return q       
    
p = create_linked([112, 98, 4, 72, 34, 23, 4, 12, 24, 19])
wypisz(p)
print()
q = rozdziel(p)
wypisz(q)
print()
r = rozdziel_sort(p)
wypisz(r)