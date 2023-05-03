
from collections import deque
import math

def createGraph(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
        G[b].append(a)
    #
#

def addEdge(G, a, b):
    G[a].append(b)
    G[b].append(a)
#


def BFS(G, n, source, destination):
    visited = [ False for _ in range(n) ] 
    queue = deque()

    visited[source] = True 
    queue.append(source)

    while queue:
        s = queue.popleft()

        for vertex in G[s]:
            if visited[vertex] == False:
                visited[vertex] = True 
                queue.append(vertex)
            
                if vertex == destination:
                    return visited
            #
        #
    #end while

    return visited
#end def ^^^


def getVertices(edges):
    maxVertex = 0
    for edge in edges:
        a = edge[0]
        b = edge[1]
        maxVertex = max( maxVertex, a )
        maxVertex = max( maxVertex, b)
    #
    return maxVertex + 1
#end def ^^^


def TouristGuide(K, edges, A, B):
    #
    n = getVertices(edges)
    edges.sort( key = lambda x: x[2], reverse = True )
    # print(edges)
    numberGroups = 0

    G = [ [] for _ in range(n) ]

    for edge in edges:
        #
        a = edge[0]
        b = edge[1] 
        value = edge[2]

        addEdge(G, a, b)
        # numberGroups = max( numberGroups, math.ceil( K / value) )

        visited = BFS(G, n, A, B)
        if visited[B] == True: return math.ceil( K / value ) # return numberGroups
    #end for 

#end def ^^^

edges = [
    (0, 1, 50),
    (0, 3, 25),
    (1, 2, 75),
    (2, 3, 20),
    (3, 5, 50),
    (5, 6, 2),
    (4, 6, 10),
    (6, 7, 20),
    (7, 8, 70),
    (1, 5, 75),
    (2, 5, 30),
    (3, 4, 50)
]
# Edges = [(0, 1, 20),(0, 1, 30), (1, 4, 25), (0, 4, 10), (0, 2, 30), (2, 3, 21), (3, 4, 22)]
# print(TouristGuide(80, Edges, 0, 4))

print( TouristGuide(100, edges, 0, 8) )