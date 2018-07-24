def topological(graph(V)):
    list <int> L;
    bool mark[V];
    foreach mark[V]:
        mark[v] = false;

    for v in mark[]:
        if not mark[v]:
            dfs(graph, v, visited)
        
        L.insert(v);
    return L;

def dfs(graph, S, visited = ()):
  visited.push(S)
     
  for neighbor in graph[S].neighbors:
    if neighbor not in visited:
      dfs(graph, neighbor)

  return visited
