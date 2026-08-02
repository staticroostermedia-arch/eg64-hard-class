#!/usr/bin/env python3
"""Fire 28 L6-bridge property tests."""
import networkx as nx

def cyc(G, L):
    return [c for c in nx.simple_cycles(G) if len(c) == L]

base = [
    ("e", "T2"), ("e", "f"),
    ("T2", "e_prime"),
    ("f", "g"), ("f", "g_prime"),
    ("e_prime", "r1"), ("e_prime", "pa"),
    ("g", "r1"), ("g", "ug"),
    ("g_prime", "pa"), ("g_prime", "pb"),
    ("r1", "q"),
    ("ug", "y"), ("ug", "y2"),
    ("pa", "w"),
    ("pb", "s"), ("pb", "s2"),
    ("q", "c1"), ("q", "cs"),
    ("a_star", "c1"), ("a_star", "c2"),
    ("y", "c1"), ("s", "c2"),
    ("y", "alpha"),
    ("y2", "beta"), ("y2", "gamma"),
    ("w", "delta"), ("w", "eps"),
    ("s", "sigma"),
    ("s2", "mu"), ("s2", "nu"),
]

def Gx(*extra):
    G = nx.Graph()
    G.add_edges_from(base + list(extra))
    return G

# H404
assert cyc(Gx(("c2", "tau"), ("tau", "sigma")), 4)
print("H404 PASS")

# H413 tau-delta C8
assert cyc(Gx(("c2", "tau"), ("tau", "delta")), 8)
print("H413 tau-delta PASS")

# H413 alpha-sigma L6
assert cyc(Gx(("Lbr", "alpha"), ("Lbr", "sigma")), 8)
print("H413 alpha-sigma PASS")

# H413 delta-mu L6
assert cyc(Gx(("Lbr", "delta"), ("Lbr", "mu")), 8)
print("H413 delta-mu PASS")

# Private L6 free
G = Gx()
for v in ["alpha", "beta", "gamma", "delta", "eps", "sigma", "mu", "nu", "cs"]:
    for i in range(2):
        lam = f"L6_{v}_{i}"
        G.add_edge(v, lam)
        G.add_edge(lam, f"P_{v}_{i}a")
        G.add_edge(lam, f"P_{v}_{i}b")
G.add_edge("c2", "tau")
G.add_edge("tau", "Pta")
G.add_edge("tau", "Ptb")
assert not cyc(G, 4) and not cyc(G, 8)
print("H424 private L6 C48-free PASS")
print("ALL Fire 28 tests PASS")
