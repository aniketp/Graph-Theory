def dijkstra(Graph, source):
  dist[source] = 0           
  for node in Graph:
    if not node = source:
      dist[node] = infinity
    Q.push(node)

  while Q:
    v = vertex in Q with min dist[v]
    Q.pop(v) 
    for u in Graph[v].neighbors:
      alt = dist[v] + len(v, u)
      if alt < dist[u]:
        dist[u] = alt
        
  return dist[]