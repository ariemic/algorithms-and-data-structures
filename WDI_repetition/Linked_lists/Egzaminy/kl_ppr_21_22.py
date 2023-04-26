# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# Zbiór mnogościowy liczb naturalnych reprezentowanych jest przez listę o uporządkowanych rosnąco
# elementach. Proszę napisać funkcję iloczyn(z1, z2, z3), która przekształca 3 listy (zbiory) z1, z2,
# z3 w jedną listę (zbiór) zawierającą elementy będące częścią wspólną zbiorów z1, z2, z3. Funkcja
# powinna zwrócić wskazanie do listy wynikowej.
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def print_all(p):
  if p is not None:
    print(p.val)
    print_all(p.next)


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next

def iloczyn2(p, q):
  if p == None or q == None:
    return None
  
  if p.val == q.val:
    x = p
    p, q = p.next, q.next
    x.next = iloczyn2(p, q)
    return x
  else:
    if p.val < q.val:
      return iloczyn2(p.next, q)
    else:
      return iloczyn2(p, q.next)


def iloczyn(z1, z2, z3):
  return iloczyn2(z1, iloczyn2(z2, z3))


a = create_linked_list_with_given_elements([1, 2, 3, 5, 7, 8])
b = create_linked_list_with_given_elements([2, 4, 5, 7, 8])
c = create_linked_list_with_given_elements([0, 2, 5, 8, 12, 24])

i = iloczyn(a, b, c)

print_all(i)