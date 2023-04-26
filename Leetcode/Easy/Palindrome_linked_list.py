

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

def wypisz(p):
    while p != None:
        print(p.val, end=" ")
        p = p.next

# Działanie odwracanie
# 1. Jeśli nasza lista składa się tylko z jednego elementu to ją zwróc
# 2. W.p.p odwróć listę zaczynającą się w następnym elemencie
# 3. Na koniec odwróconej listy z kolejnego elementu doczep element aktualny        

def reverseLinkedList(p):
    if p.next == None:
        return p
    q = p
    curr = q.next #potrzebuje tej zmiennej żeby móc przerzucać q na następny element, jednocześnie tworzą odseparowaną odwróconą liste res
    res = None #bedzie wskazywać na odwróconą listę
    while q != None:
        q.next = res
        res = q
        q = curr
        if curr != None:
            curr = curr.next
    return res
            
    
def isPalindrome(head):
    cnt = 0
    q = head
    while q != None:
        cnt += 1
        q = q.next
    q = head
    cnt1 = 0
    while cnt1 < cnt//2 - 1:
        cnt1 += 1
        q = q.next
    rev = q.next
    q.next = None
    
    rev = reverseLinkedList(rev)
    while head != None:
        if head.val != rev.val: return False
        head = head.next
        rev = rev.next
    return True
 
 
 


 
   
p = createLinkedList([1,2,2,2,1])

# wypisz(p)
# wypisz(reverseLinkedList(p))
# head, curr = (isPalindrome(p))
# wypisz(head)
# print()
# wypisz(curr)
print(isPalindrome(p))