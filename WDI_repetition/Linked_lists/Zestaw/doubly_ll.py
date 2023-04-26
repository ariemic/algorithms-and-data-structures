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
        
        