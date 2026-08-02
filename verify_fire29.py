#!/usr/bin/env python3
"""Fire 29 property tests: chords + PF4."""
import networkx as nx

def cyc(G, L):
    return [c for c in nx.simple_cycles(G) if len(c) == L]

# Dual H390 core for chords
dual = [
    ("e", "T2"), ("e", "f"),
    ("T2", "e_prime"),
    ("f", "g"), ("f", "g_prime"),
    ("e_prime", "r1"), ("e_prime", "pa"),
    ("g", "r1"), ("g", "ug"),
    ("g_prime", "pa"), ("g_prime", "pb"),
    ("r1", "q"),
    ("ug", "y"),
    ("pb", "s"),
    ("q", "c1"),
    ("a_star", "c1"), ("a_star", "c2"),
    ("s", "c2"),
    ("y", "c1"),
]

def Gd(*extra):
    G = nx.Graph()
    G.add_edges_from(dual + list(extra))
    return G

assert cyc(Gd(("s", "f")), 4)
print("H435 s-f PASS")
assert cyc(Gd(("c2", "g_prime")), 4)
print("H436 c2-g' PASS")
assert cyc(Gd(("pb", "e")), 4)
print("H437 pb-e PASS")
assert cyc(Gd(("a_star", "pb")), 4)
print("H438 a*-pb PASS")
assert cyc(Gd(("y", "f")), 4)
print("H439 y-f PASS")

# PF4
pf4 = [
    ("e", "T2"), ("e", "f"),
    ("T2", "e_prime"),
    ("f", "g"), ("f", "g_prime"),
    ("e_prime", "pa"), ("e_prime", "ug"),
    ("g", "r1"), ("g", "ug"),
    ("g_prime", "pa"), ("g_prime", "pb"),
    ("r1", "q"), ("r1", "x"),
    ("ug", "y"),
    ("pa", "w"),
    ("pb", "s"),
    ("q", "c1"), ("q", "cs"),
    ("a_star", "c1"), ("a_star", "c2"),
]

def Gp(*extra):
    G = nx.Graph()
    G.add_edges_from(pf4 + list(extra))
    return G

assert cyc(Gp(("x", "c1")), 4)
print("H453 x-c1 PASS")
assert cyc(Gp(("y", "c2")), 8)
print("H454 y-c2 PASS")
assert cyc(Gp(("y", "c1"), ("w", "c2")), 8)
print("H455 y-c1+w-c2 PASS")
assert cyc(Gp(("s", "c1")), 8)
print("H399 PF4 s-c1 PASS")
print("ALL Fire 29 tests PASS")
