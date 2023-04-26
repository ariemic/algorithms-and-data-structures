# 102. Binary Tree Level Order Traversal
#Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def levelOrder(root):
    #we have root of the binary tree we need to return the array
    #with lists represents every level of the tree and contains
    #nodes on that level
    res = []
    q = collections.deque() #import queue
    q.append(root)
    #from that start runing bfs
    while q: #while queue is not empty
        n = len(q) #ansurring us that we iterate over one level at the time
        level = [] #we adding here nodes from the same level
        for i in range(n):
            node = q.popleft() #first in first out
            if node:
                level.append(node.val)
                q.append(node.left) #we adding children of that node to the list
                q.append(node.right)
        if level: #if the level isn't empty add it to the res array
            res.append(level)
    return res
    
    
def levelOrder(root):
    '''
    algorytm na wejściu dostaje node'a z korzeniem drzewa, ma zwrócić liste z listami nodów na każdym poziomie drzewa
    tworzymy kolejke q w której będziemy przechowywać jeszcze nie dołączone do żadnej listy level node'y
    dopóki w kolejce coś będzie, będzemy przechodzić pętlą for po danym poziomie - zapewnimy nam to że w danym forze wszystkie node'y są na tej samej wysokości.
    Dalej będziemy usuwać z kolejki pierwszy node i przypisaywać go pod zmieną node, jeżeli nie jest on Nonem to sprawdzamy czy ma dzieci jeśli tak to dołączamy je do kolejki.
    Wracamy forem do kolejnego node'a na tym samym poziomie i sprawdzamy tak samo czy ma potomstwo. Po wyjściu z fora sprawdzamy czy lista level jest nie pusta jeśli tak do appendujemy do res.
    Co ważne po sprawdzeniu czy q != None obliczamy rozmiar kolejki ZAWSZE WSAZUJE ON na ilość nodeow na tym samym poziomie ponieważ przechodza przez fora dzieci są dodawane a każdy rodzic usuwany i dołączny do levelu.
    
    
    '''
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        n = len(q)
        level = []
        for i in range(n):
            node = q.popleft() #nody na tym samym poziomie
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res