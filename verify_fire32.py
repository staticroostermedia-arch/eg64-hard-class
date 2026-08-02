#!/usr/bin/env python3
"""Fire 32: B2 dist 3/7 C16 seeds and H547/H541."""
import networkx as nx

residual = [
    ("v0", "v1"), ("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v5"), ("v5", "v0"),
    ("s", "v0"), ("s", "delta"), ("s", "a_star"),
    ("delta", "eps"), ("eps", "T5"), ("T5", "v5"),
    ("v1", "t"), ("t", "b1"), ("t", "b2"),
    ("T2", "v2"), ("T2", "e1"), ("T2", "e2"),
    ("a_star", "c1"), ("a_star", "c2"),
]
b2 = [
    ("e1", "f1"), ("f1", "T3"), ("T3", "v3"),
    ("e1", "f1b"), ("e2", "f2a"), ("e2", "f2b"),
]

def Gx(*extra):
    G = nx.Graph()
    G.add_edges_from(residual + b2 + list(extra))
    return G

def has_c(G, L):
    return any(len(c) == L for c in nx.simple_cycles(G))

# residual length 7
G0 = Gx()
assert nx.shortest_path_length(G0, "a_star", "f1") == 7
print("residual dist(a*,f1)=7 PASS")

# H539 u-f1b C16
G = Gx(("c1", "u"), ("u", "f1b"), ("f1", "y"), ("y", "y1"), ("y", "y2"))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H539 u-f1b C16 PASS")

# H539 u-v1 C16
G = Gx(("c1", "u"), ("u", "v1"), ("f1", "y"), ("y", "y1"), ("y", "y2"))
assert has_c(G, 16) and not has_c(G, 8)
print("H539 u-v1 C16 PASS")

# H547: Py length 7
G = Gx(
    ("c1", "u"), ("u", "u1"), ("u1", "u2"), ("u2", "y1"),
    ("y1", "y"), ("y", "f1"),
)
hand = ["a_star","s","delta","eps","T5","v5","v4","v3","T3","f1","y","y1","u2","u1","u","c1"]
assert all(G.has_edge(hand[i], hand[(i + 1) % 16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H547 Py L7 C16 PASS")

# H541: P* L7 + Q L9
G = Gx(
    ("c1", "u"), ("u", "u1"), ("u1", "u2"), ("u2", "u3"), ("u3", "u4"),
    ("u4", "y1"), ("y1", "y"), ("y", "f1"),
)
hand = ["a_star","s","v0","v1","v2","T2","e1","f1","y","y1","u4","u3","u2","u1","u","c1"]
assert all(G.has_edge(hand[i], hand[(i + 1) % 16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H541 7+9 C16 PASS")

# H541 T3 entry L9
G = Gx(
    ("c1", "u"), ("u", "u1"), ("u1", "u2"), ("u2", "u3"), ("u3", "u4"),
    ("u4", "x"), ("T3", "x"),
)
hand = ["a_star","s","v0","v1","v2","T2","e1","f1","T3","x","u4","u3","u2","u1","u","c1"]
assert all(G.has_edge(hand[i], hand[(i + 1) % 16]) for i in range(16))
assert has_c(G, 16)
print("H541 T3 L9 C16 PASS")

print("ALL Fire 32 tests PASS")
