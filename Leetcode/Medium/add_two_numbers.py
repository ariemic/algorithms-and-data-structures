class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(arr):
    n = len(arr)
    p = ListNode(arr[0])
    h = p
    for i in range(1, n):
        p.next = ListNode(arr[i])
        p = p.next
    return h

def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next
            
def addTwoNumbers(l1, l2):
    l3 = ListNode(0)
    h = l3
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if l1 != None else 0
        l2VAl = l2.val if l2 != None else 0
        suma = l1Val + l2VAl + carry
        carry = suma//10     
        newNode = ListNode(suma%10)
        l3.next = newNode
        l3 = newNode
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    return h.next

l1 = createLinkedList([2,4,3])
l2 = createLinkedList([5,6,4])
wypisz(addTwoNumbers(l1, l2))