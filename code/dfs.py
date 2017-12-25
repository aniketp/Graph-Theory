def dfs(graph, S, visited = ()):
  visited.push(S)
     
  for neighbor in graph[S].neighbors:
    if neighbor not in visited:
      dfs(graph, neighbor)

  return visited
