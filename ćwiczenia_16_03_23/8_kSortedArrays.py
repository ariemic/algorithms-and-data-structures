#merge k sorted array into one array

def parent(i):
    return (i-1)//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

def heapify_min(A, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    if l < n and A[l].val < A[min_ind].val: min_ind = l
    if r < n and A[r].val < A[min_ind].val: min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify_min(A, min_ind, n) #kopiec zepsuł się niżej trzeba go naprawić
    return A

def buildheap(A,n):
    for i in range(parent(n-1), -1, -1):
        heapify_min(A, i, n)

class Node:
    def __init__(self, val, idx, leng, list_num):
        self.val = val
        self.idx = idx
        self.leng = leng
        self.list_num = list_num
        
def insert(arr, heap):
    if heap[0].idx + 1 < heap[0].leng:
        #moja tablica z której biore wartość jeszcze się nie skończyla mogę wstawić kolejną wartość do kopca
        id = heap[0].idx + 1
        nr = heap[0].list_num
        heap[0].val, heap[0].idx = arr[nr][id], id
        # heap[0] = Node(arr[nr][id], id, heap[0].leng, nr)
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
    heapify_min(heap, 0, len(heap))
    # return heap
    
    
    
def MergeKArrays(arr):
    k = len(arr)
    heap = []
    res = []
    for i in range(k):#utwórz kopiec wielkości k
        heap.append(Node(arr[i][0], 0, len(arr[i]), i)) #dodaje do kopca strukture z wartością pierwszego elementu każdej z k tablic
    buildheap(heap, k)
    while heap:
        res.append(heap[0].val)
        insert(arr, heap)
    return res

arr = [[1, 5, 21, 45], [12, 23, 24, 90], [1, 2, 19, 19, 20]]
res = MergeKArrays(arr)
print(res)