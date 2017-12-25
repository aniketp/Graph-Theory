def bellmanFord(Graph, Egde, S):
  for node in Graph:
    dist[node] = infinity
    node.prev = nil
  dist[S] = 0

  for node in Graph:
    for (u,v) in Edge:
      if dist[v] > dist[u] + len(u,v):
        dist[v] = dist[u] + len(u,v)

  for (u, v) in Edge:
    if dist[v] > dist[u] + len(u,v):
      print "A negative weight cycle exists"

  return dist[], Graph.prev[]