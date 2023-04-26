class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



tab = [1,2,3,5,7,8,11]
p = Node( tab[0] )
q = p

def print_all(q):
    while q is not None:
        print(q.val, end=" ")
        q = q.next


def add(q, tab): # laczenie tablicy w link liste
    for i in range(1, len(tab) ):
        k = Node( tab[i] )
        q.next = k
        q = q.next # lub ( q = k )
    #end for
#end def

add(q, tab)


def is_present(p, number): # sprawdzanie czy element nalezy do zbiorow
    q = p
    while q is not None:
        if q.val == number: return True
        q = q.next
    #end while
    return False
#end def



def add_element(p, element):

    if p is None:
        k = Node(element)
        return k 
    #end if

    q = p
    tail = None 
    while q is not None:
        tail = q
        q = q.next
    #end while
    k = Node(element)
    tail.next = k

    return p


add_element(p, 100)
# print_all(p)


def insert_sort(p, tab):
    q = p

    tail = None 
    while q is not None and tab < q.val:
        q = q.next 
    #end while

    if q == None and tail == None:
        k = Node(tab)
        q.next = k 
        q = k 
        return p
    #end if

    
p = Node(None) # guardian !!!!
add_element(p,3)
add_element(p,4)
add_element(p,5)
add_element(p,6)
    
def add(p, new_val): #dodawanie rekurencyjne

    if p.next is None:
        q = Node(new_val)
        p.next = q
        return 

    if p.next is not None:

        if p.next.val == new_val:
            return

        elif p.next.val > new_val:
            q = Node(new_val)
            q.next = p.next 
            p.next = q
        else:
            add(p.next, new_val)
    #end if 
#end def    

def present_rek(p, el):

    if p is None:
        return False 

    if p.val == el: 
        return True 
    else:
        return present_rek(p.next, el)
    

# print( present_rek(p,6) )

def is_present(g, val):

    if g.next is None:
        return False
    
    if g.next.val == val:
        return True
    elif g.next.val > val:
        return False
    else:
        return is_present(g.next, val)

        
def remove_rek(p, el):

    if p.next is None:
        return
    
    if p.next.val > el: 
        return
    
    if p.next.val == el:
        p.next = p.next.next
        return 
    else:
        delete(p.next,el)

        
def delete(g, val):
    if g.next is None:
        return 
    
    if g.next.val == val:
        g.next = g.next.next
    
    elif g.next.val < val:
        delete(g.next, val)
    

# remove_rek(p, 5)
# print_all(p.next)
# print()

print_all(p.next)
delete(p,5)
print()
print_all(p.next)