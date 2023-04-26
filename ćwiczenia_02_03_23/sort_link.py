'''
1.
a) Wstaw element do posortowanej link listy.
b) Wyciągnij maksimum z listy jako wskaznik na ten element


'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def wypisz(p):
    while p != None:
        print(p.val, end=" ")
        p = p.next

def create_linked(tab):
    p, n = Node(tab[0]), len(tab)
    q = p
    for i in range(1, n):
        p.next = Node(tab[i])
        p = p.next
    return q
#a)
def insert(p, x):
    q = p
    t = None
    while q != None and q.val < x:
        t = q
        q = q.next
    w = Node(x)
    if t == None: #insert x as first element
        w.next = p
        return w
    else:#insert x after tail but before q
        t.next = w
        t = t.next
        t.next = q
    return p
        

# a = create_linked([2, 4, 5, 7, 9])
# wypisz(insert(a, 1))
# print()

#b)

def extract_max(q): #returns only value
    p = q
    maxi = 0
    while p != None:
        maxi = max(p.val, maxi)
        p = p.next
    return maxi

def extract_max(q):
    m = q
    while q.next != None:
        if q.next.val > m.next.val:
            m = q
        q = q.next
    res = m.next
    m.next = res.next
    res.next = None
    return res


# wypisz(extract_max(a))


b = create_linked([2, 4, 9, 2, 3, 5, 7, 11, 10])

    


             
            
            
    









