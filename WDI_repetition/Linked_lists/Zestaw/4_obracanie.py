class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val

# Działanie odwracanie
# 1. Jeśli nasza lista składa się tylko z jednego elementu to ją zwróc
# 2. W.p.p odwróć listę zaczynającą się w następnym elemencie
# 3. Na koniec odwróconej listy z kolejnego elementu doczep element aktualny

def print_all(p):
    while p is not None:
        print(p.val, end="")
        p = p.next
        
def reverse(p): 
    if p.next == None:
        return p
    else:
        prev = reverse(p.next) #dojde do ostatniego elementu w ten sposob
        q = prev
        #ODTĄD NIE ROZUMIEM TEGO PROGRAMU
        while q.next != None:
            q = q.next 
        q.next = p #dodaje liste p do pierwszego elementu nowej odwrc listy
        p.next = None 
        return prev

def reverse_iter(p):
    if p.next == None:
        return p
    
    q = p
    r = None
    curr = q.next #kolejny el w liscie
    
    while q != None:
        q.next = r
        r = q
        q = curr
        if curr != None:
            curr = curr.next
    return r    
            
            
a = Node(2, None)
b = Node(1,a)
c = Node(3,b)
d = Node(7,c)

print_all(d)
x = reverse_iter(d)
print()
print_all(x)