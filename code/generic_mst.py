GENERIC-MST(G(V,E),w)
A = {}

# Loop till A connects all vertices
while A.len != (V - 1):
    edge = min((u,v))
    A = A.append(edge)
return A
