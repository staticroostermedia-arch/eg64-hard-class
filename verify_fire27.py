#!/usr/bin/env python3
"""Property tests for Fire 27 U2b/pure-f C8 laws."""
import networkx as nx

def cycles(G, L):
    return [c for c in nx.simple_cycles(G) if len(c) == L]

core = [
    ("e", "T2"), ("e", "f"),
    ("T2", "e_prime"),
    ("f", "g"), ("f", "g_prime"),
    ("e_prime", "r1"), ("e_prime", "pa"),
    ("g", "r1"), ("g", "ug"),
    ("g_prime", "pa"), ("g_prime", "pb"),
    ("r1", "q"),
    ("ug", "y"),
    ("pa", "w"),
    ("pb", "s"), ("pb", "s2"),
    ("q", "c1"), ("q", "cs"),
    ("a_star", "c1"), ("a_star", "c2"),
]

def G_with(*extra):
    G = nx.Graph()
    G.add_edges_from(core + list(extra))
    return G

# H384
c8 = cycles(G_with(("s", "c1")), 8)
assert any(set(c) >= {"s", "c1", "q", "r1"} for c in c8), c8
print("H384 PASS", len(c8), "C8s")

# H387
c8 = cycles(G_with(("w", "c1"), ("s", "c2")), 8)
assert len(c8) >= 1, c8
print("H387 PASS", len(c8), "C8s")

# H375
c8 = cycles(G_with(("y", "Lsh"), ("s", "Lsh")), 8)
assert len(c8) >= 1, c8
print("H375 PASS", len(c8), "C8s")

# H371
c4 = cycles(G_with(("s", "c2"), ("s2", "c2")), 4)
assert len(c4) >= 1, c4
print("H371 PASS", len(c4), "C4s")

# H391
c4 = cycles(G_with(("y", "c1"), ("y", "cs")), 4)
assert len(c4) >= 1, c4
print("H391 PASS", len(c4), "C4s")

# H399 pure f
pf = [
    ("e", "f"), ("f", "g"), ("f", "g_prime"),
    ("g", "r1"), ("g", "ug"),
    ("g_prime", "pb"),
    ("r1", "q"),
    ("pb", "s"),
    ("q", "c1"),
    ("s", "c1"),
]
c8 = cycles(nx.Graph(pf), 8)
assert len(c8) >= 1, c8
print("H399 PASS", len(c8), "C8s")
print("ALL Fire 27 property tests PASS")
