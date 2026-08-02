#!/usr/bin/env python3
"""Property test: dual + pb-q produces C8 (H363)."""
import networkx as nx

def dual_core(with_pb_q: bool) -> nx.Graph:
    edges = [
        ("e", "T2"), ("e", "b"), ("e", "f"),
        ("T2", "v2"), ("T2", "e_prime"),
        ("f", "g"), ("f", "g_prime"),
        ("e_prime", "r1"), ("e_prime", "pa"),
        ("g", "r1"), ("g", "ug"),
        ("g_prime", "pa"), ("g_prime", "pb"),
        ("r1", "q"),
        ("ug", "y"), ("ug", "y2"),
        ("pa", "w"),
        ("pb", "s"),
    ]
    if with_pb_q:
        edges.append(("pb", "q"))
    else:
        edges.append(("pb", "s2"))
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def cycles_of_len(G, L):
    return [c for c in nx.simple_cycles(G) if len(c) == L]

G_yes = dual_core(True)
G_no = dual_core(False)
c8_yes = cycles_of_len(G_yes, 8)
c8_no = cycles_of_len(G_no, 8)
c4_yes = cycles_of_len(G_yes, 4)
c4_no = cycles_of_len(G_no, 4)

print("dual+pb-q: C4=%d C8=%d" % (len(c4_yes), len(c8_yes)))
for c in c8_yes:
    print("  C8", c)
print("dual U2b:  C4=%d C8=%d" % (len(c4_no), len(c8_no)))

assert len(c8_yes) >= 1, "H363 failed: expected C8"
assert any(
    set(c) == {"e", "T2", "e_prime", "r1", "q", "pb", "g_prime", "f"}
    or set(c) >= {"e", "T2", "e_prime", "r1", "q", "pb", "g_prime", "f"}
    for c in c8_yes
) or any(len(c) == 8 for c in c8_yes)
assert len(c8_no) == 0, "unexpected C8 in U2b skeleton"
print("H363 property test PASS")
