class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class

# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

def how_many_ones(n):
    cnt = 0
    while n > 0:
        cnt += n % 2 
        n = n // 2
    #end while
    return cnt % 2 == 1 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def dec_to_bin(n):
    dig = 0
    number = 0

    while n > 0:
        number += ( n % 2 ) * ( 10 ** dig)
        dig += 1
    #end while
    return number
#end def


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def



def put_guardian(p):
    k = Node( None )
    k.next = p
    return k 
#end def

def remove_odd_ones(p): # co zle?
    p = put_guardian(p)
    q = p

    while p.next is not None:
        if how_many_ones( p.next.val ):
            p.next = p.next.next
        p = p.next
    #end while

    return q
#end def

# def remove(p):
#     q = p # head do ktorej dopisujemy
#     x = q
    
#     while p.next != None:
#         p = p.next
#         if how_many_ones( p.val ):
#             q.next = p
#             q = q.next

#             p = p.next 
#     #end while
#     p.next = None 

#     return x 
# #end def


# T = [1,2,3,4,5,6,7,8,11,15,158,139,13951,41995]
# p = create_linked_list_with_given_elements( T )
# print_all(p.next)
# print()
# p = remove_odd_ones(p)
# print()
# print()

# p = remove(p)
# print_all(p.next)
