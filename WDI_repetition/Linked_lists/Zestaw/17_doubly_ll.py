# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej, 
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, val):
        #adding new elements
        p = Node(val)
        p.next = self.head
        if self.head is not None:
            self.head.prev = p
        self.head = p

    def wypisz(self, p):
        while p != None:
            print(p.val, end=" ")    
            last = p
            p = p.next
    
    def delete_by_value(self, el):
        if self.head is None:
            return 
        if self.head.next is None:
            if self.head.val == el:
                self.head = None
        if self.head.val == el:
            #niedokonczone
            pass
        
        
        
        
def is_odd_ones(n):
    cnt = 0
    while n != 0:
        if n%2 == 1: cnt +=1
        n //= 2
    return cnt%2 == 1 

#dla listy jednokierunkowej
def remove(head):
    #dla listy dwukierunkowej trzeba zrobić przepięcia w obie strony
    p = head
    q = head
    while p.next != None:
        p = p.next
        if is_odd_ones(p.val) == False:
            q.next = p
            q = q.next
    p.next = None
    #usuwam element p z listy
            
        
p = doubly_linked_list()
p.push(12)
p.push(8)
p.push(62)
p.wypisz(p.head)