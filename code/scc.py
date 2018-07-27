def isSCC(Graph):
    bool Visited(V, false)
    traverseDFS(0, visited)

    if visited.len() != V:
        return false

    revGraph = Graph.reverse()
    Visited(V, false)
    revGraph.traverseDFS(0, visited)

    if visited.len() != V:
        return false
    return true
