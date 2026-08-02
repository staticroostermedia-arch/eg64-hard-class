#!/usr/bin/env python3
"""Fire 33: B1 C16/C8 seeds; double-stretch closure property tests."""
import networkx as nx

residual = [
    ("v0", "v1"), ("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v5"), ("v5", "v0"),
    ("s", "v0"), ("s", "delta"), ("s", "a_star"),
    ("delta", "eps"), ("eps", "T5"), ("T5", "v5"),
    ("v1", "t"), ("t", "b1"), ("t", "b2"),
    ("T2", "v2"), ("T2", "e1"), ("T2", "e2"),
    ("a_star", "c1"), ("a_star", "c2"),
]
F = [("e1", "f1"), ("e1", "f2"), ("e2", "f3"), ("e2", "f4")]

def Gx(*extra):
    G = nx.Graph()
    G.add_edges_from(residual + F + list(extra))
    return G

def has_c(G, L):
    return any(len(c) == L for c in nx.simple_cycles(G))

# residual dist(a*,f1)=7
assert nx.shortest_path_length(Gx(), "a_star", "f1") == 7
print("H567 residual dist(a*,f1)=7 PASS")

# H566 dist5 C16
G = Gx(("c1", "p"), ("p", "q"), ("q", "r"), ("r", "f1"))
hand = ["a_star","c1","p","q","r","f1","e1","T2","v2","v3","v4","v5","T5","eps","delta","s"]
assert all(G.has_edge(hand[i], hand[(i+1)%16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H566 dist5 C16 PASS")

# H571 L7 free-gate
G = Gx(
    ("c1", "u"), ("u", "u1"), ("u1", "u2"), ("u2", "y1"),
    ("y1", "yf"), ("yf", "f1"),
)
hand = ["a_star","s","v0","v5","v4","v3","v2","T2","e1","f1","yf","y1","u2","u1","u","c1"]
assert all(G.has_edge(hand[i], hand[(i+1)%16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H571 L7 free-gate C16 PASS")

# H570 7+9
G = Gx(
    ("c1", "u"), ("u", "u1"), ("u1", "u2"), ("u2", "u3"), ("u3", "u4"),
    ("u4", "y1"), ("y1", "yf"), ("yf", "f1"),
)
hand = ["a_star","s","v0","v1","v2","T2","e1","f1","yf","y1","u4","u3","u2","u1","u","c1"]
assert all(G.has_edge(hand[i], hand[(i+1)%16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H570 7+9 C16 PASS")

# H572 dist3 + L5 third => C8
G = Gx(
    ("c1", "y"), ("y", "f1"),
    ("c2", "w"), ("w", "w1"), ("w1", "z"), ("z", "f1"),
)
hand = ["a_star", "c1", "y", "f1", "z", "w1", "w", "c2"]
assert all(G.has_edge(hand[i], hand[(i+1)%8]) for i in range(8))
assert has_c(G, 8)
print("H572 dist3 L5 C8 PASS")

# H573 dist3 + L7 third => C16
G = Gx(
    ("c1", "y"), ("y", "f1"),
    ("c2", "w"), ("w", "w1"), ("w1", "w2"), ("w2", "w3"),
    ("w3", "z"), ("z", "f1"),
)
hand = ["a_star","s","v0","v5","v4","v3","v2","T2","e1","f1","z","w3","w2","w1","w","c2"]
assert all(G.has_edge(hand[i], hand[(i+1)%16]) for i in range(16))
assert has_c(G, 16) and not has_c(G, 4) and not has_c(G, 8)
print("H573 dist3 L7 C16 PASS")

print("ALL Fire 33 tests PASS")
