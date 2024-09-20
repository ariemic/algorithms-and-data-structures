def dfs(G):
  time = 0
  n = len(G)
  visited = [False]*n
  parent = [None]*n

  def dfs_visit(G, u):
    nonlocal time
    time += 1 #visitng time
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        parent[v]= u
        dfs_visit(G, v)
    time += 1 #processing time  

  for u in range(n):
    if not visited[u]:
      dfs_visit(G, u)


G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
