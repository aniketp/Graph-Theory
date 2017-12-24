def bfs(graph, S):
    visited = set()
    Q.enqueue(S)

    while Q:
        vertex = Q.dequeue()
        
        for neighbor in graph[vertex].neighbors 
        	if neighbor not in visited:
            	visited.add(neighbor)
            	Q.enqueue(neighbor)
    
    return visited
