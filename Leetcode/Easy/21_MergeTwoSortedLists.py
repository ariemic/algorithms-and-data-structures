
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1, list2):
        # res = ListNode()
        def merge(self, list1, list2, res):
            if list1 == None: return list2
            if list2 == None: return list1
            if list1.val < list2.val:
                res = list1
                res.next = merge(self,list1.next, list2, res.next)
            else:
                res = list2 #z każdym przejsciem rekurencyjnym przesuwamy wskaznik res
                res.next = merge(self, list1, list2.next, res.next)
            return res
        return merge(self, list1, list2, res = ListNode())
    