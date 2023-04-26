#merge two linked lists using recursion
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

def insert_next(inputt, output):
    node = inputt
    inputt = inputt.next
    node.next = None
    output.next = node
    output = output.next


def mergeRek(a, b, res):
    if a == None: return b
    if b == None: return a
    if a.val < b.val:
        res = a
        res.next = mergeRek(a.next, b, res.next) #przypisanie jest bardzo wazne 
        #inczaej sie wykrzaczy
    else:
        res = b
        res.next = mergeRek(a, b.next, res.next)
    return res

a = create_linked([1, 3, 5, 21])
b = create_linked([2, 5, 6, 21, 22])
c = mergeRek(a, b, Node())
wypisz(c)
