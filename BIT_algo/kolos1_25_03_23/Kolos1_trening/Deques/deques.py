from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        return self._items.popleft()

from queue import PriorityQueue
q = PriorityQueue()
'''
put() Puts an item into the queue.
get()  Removes and returns an item from the queue.
qsize()  Returns the current queue size.
empty()  Returns True if the queue is empty, False otherwise. It is equivalent to qsize()==0.
full()  Returns True if the queue is full, False otherwise. It is equivalent to qsize()>=maxsize.
'''
q.put((2, 'g'))
q.put((3, 'e'))
q.put((4, 'k'))
q.put((5, 's'))
q.put((1, 'e'))

