from zad5testy import runtests
from queue import PriorityQueue


def Singularity(n, S):
    isSingularity = [False for _ in range(n)]
    for v in S:
        isSingularity[v] = True
    #
    return isSingularity
# end def ^^^


def createG(n, E, isSingularity):
    G = [[] for _ in range(n + 1)]

    for edge in E:
        a, b, value = edge

        if isSingularity[a] == True and isSingularity[b] == False:
            G[n].append((b, value))
            G[b].append((n, value))

        elif isSingularity[a] == False and isSingularity[b] == True:
            G[n].append((a, value))
            G[a].append((n, value))

        elif isSingularity[a] == False and isSingularity[b] == False:
            G[a].append((b, value))
            G[b].append((a, value))
    # end for
    return G
# end def ^^^


def Dijkstra(G, n, source, destination):

    # distance to each vertex from starting vertex
    distance = [float('inf') for _ in range(n)]
    done = [False for _ in range(n)]

    queue = PriorityQueue()
    distance[source] = 0
    queue.put((0, source))

    while not queue.empty():
        value, vertex = queue.get()

        if done[vertex] == False:
            for (neighbour, weight) in G[vertex]:

                if (distance[vertex] + weight) < distance[neighbour]:

                    distance[neighbour] = distance[vertex] + weight
                    queue.put((distance[neighbour], neighbour))
                #

            # end for
        done[vertex] = True

        if vertex == destination:
            return distance
    # end while

    return distance
# end def ^^^


def spacetravel(n, E, S, a, b):
    #
    isSingularity = Singularity(n, S)
    G = createG(n, E, isSingularity)
    #
    if isSingularity[a]:
        a = n
    if isSingularity[b]:
        b = n
    #
    distance = Dijkstra(G, n + 1, a, b)
    #
    
    if distance[b] == float('inf'):
        return None
    return distance[b]

# end def ^^^


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
