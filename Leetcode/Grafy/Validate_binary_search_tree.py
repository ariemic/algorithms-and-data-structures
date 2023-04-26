import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
'''
Każdy node w prawej części drzewa musi być wiekszy od swojego korzenia jak i każdego wczesniejszego, analog dla lewej częsci tylko mniejszy.
Nie patrzymy tylko na wartość samego rodzica, ale na kazdego wcześniejszego także.
'''
#nie dziala narazie
def isValidBST(root) -> bool:
    q = collections.deque()
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if node:
                if node.left:
                    if node.left.val >= node.val: return False
                    q.append(node.left)
                if node.right:
                    if node.right.val <= node.val: return False
                    q.append(node.right)
    return True