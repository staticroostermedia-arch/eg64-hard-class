#!/usr/bin/env python3
"""Fire 31 Arm B property tests."""
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

def dist_v1_T2(G):
    H = G.copy()
    H.remove_node("v2")
    return nx.shortest_path_length(H, "v1", "T2")

# H493
assert has_c(Gx(("T3", "c1")), 8)
print("H493 T3-c1 C8 PASS")

# H475
assert dist_v1_T2(Gx(("f1", "b1"))) < 8
print("H475 f1-b1 short PASS")

# H491 dist1 kill
assert dist_v1_T2(Gx(("a_star", "f1"))) < 8
print("H491 a*-f1 short PASS")

# H490 dist5 C16
edges = [
    ("a_star", "p1"), ("p1", "p2"), ("p2", "p3"), ("p3", "p4"), ("p4", "f1"),
]
G = Gx(*edges)
assert has_c(G, 16)
assert not has_c(G, 4) and not has_c(G, 8)
hand = ["a_star","p1","p2","p3","p4","f1","e1","T2","v2","v3","v4","v5","T5","eps","delta","s"]
assert all(G.has_edge(hand[i], hand[(i + 1) % 16]) for i in range(16))
print("H490 dist5 C16 PASS")

# B2 core dist=8
assert dist_v1_T2(Gx()) == 8
print("B2 core dist=8 PASS")

print("ALL Fire 31 tests PASS")
