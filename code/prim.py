def prim(G, w, src):
    mst_set = {}
    for u in G.V:
        u.key = INFY

    src.key = 0
    mst_set.append(src)

    Q = G.V
    while Q is not None:
        u = Extract-Min(Q)
        for v in G.Adj[u]:
            if (v in Q) and w(u,v) < v.key:
                v.key = w(u,v)
                mst_set.append(v)
    return mst_set

