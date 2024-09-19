class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(0)
    q.next = p 
    return q 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def

def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def



def solve(l):
    l = put_guardian(l) # Wartownik
    
    last_val = l.val

    while l.next.next != None:
        curr_val = l.next.val

        if curr_val < last_val:
            curr_val = l.next.next.val
            l.next = l.next.next
        

        last_val = curr_val
        l = l.next  

    if l.next.val < last_val:
        l.next = None

    # print()


a = create_linked_list_with_given_elements([11,2,1,5,2,7,6,5,4,9,8])
solve(a)
print_all(a)