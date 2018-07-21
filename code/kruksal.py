def kruksal(G(E,V)):
    A = {}
    Sorted_Edge(u,v) = sort(G.E(u,v))
    for v in G.V:
        MAKE-SET(v)

    for (u,v) in Sorted_Edge(u,v):
        # Check if u and v are in the same tree or not
        if FIND-SET(u) != FIND-SET(v):
            A = A.append({u,v})
            UNION(u,v)
    return A
