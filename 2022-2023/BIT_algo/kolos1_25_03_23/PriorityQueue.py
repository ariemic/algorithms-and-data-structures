from queue import PriorityQueue
# https://docs.python.org/3/library/queue.html
class Solution():
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next

# Aby zrobić kopiec maximum z priority queueu - mnoże wartości przez -1
q = PriorityQueue()

q.put((2*(-1), 'code'))
q.put((1*(-1), 'eat'))
q.put((3*(-1), 'sleep'))
while not q.empty():
    next_item = q.get()
    print(next_item)