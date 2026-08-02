#!/usr/bin/env python3
"""Fire 30: Arm A geodesic + residual forces C16 (H470)."""
import networkx as nx

residual = [
    ("v0", "v1"), ("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v5"), ("v5", "v0"),
    ("s", "v0"), ("s", "delta"), ("s", "a_star"),
    ("delta", "eps"), ("eps", "T5"), ("T5", "v5"),
    ("v1", "t"),
    ("T2", "v2"),
    ("a_star", "c1"), ("a_star", "c2"),
]
ebset = [
    ("e", "T2"), ("e", "b"), ("e", "f"),
    ("b", "t"),
    ("T2", "e_prime"),
    ("f", "g"), ("f", "g_prime"),
]

def cycles(G):
    c4 = c8 = c16 = 0
    examples = []
    for c in nx.simple_cycles(G):
        L = len(c)
        if L == 4: c4 += 1
        elif L == 8: c8 += 1
        elif L == 16:
            c16 += 1
            if len(examples) < 3: examples.append(c)
    return c4, c8, c16, examples

def check(edges, name, want_c16=True):
    G = nx.Graph()
    G.add_edges_from(edges)
    c4, c8, c16, ex = cycles(G)
    print(f"{name}: C4={c4} C8={c8} C16={c16}")
    if want_c16:
        assert c16 >= 1, (name, ex)
        assert c4 == 0 and c8 == 0, (name, c4, c8)
    else:
        assert c16 == 0, (name, ex)
    return ex

# baseline: no geodesic ⇒ no C16
check(residual + ebset, "residual+ebset only", want_c16=False)

# f-ending geodesic
f_geo = [("c1", "q"), ("q", "u"), ("u", "g"), ("g", "f"), ("f", "e")]
ex = check(residual + ebset + f_geo, "f-ending H470")
# hand cycle
hand = ["v0","v1","v2","T2","e","f","g","u","q","c1","a_star","s","delta","eps","T5","v5"]
G = nx.Graph(residual + ebset + f_geo)
assert all(G.has_edge(hand[i], hand[(i+1)%16]) for i in range(16))
print("  hand f-C16 OK", hand)

# T2-ending geodesic
t2_geo = [("c1", "q"), ("q", "u"), ("u", "e_prime"), ("e_prime", "T2"), ("T2", "e")]
ex = check(residual + ebset + t2_geo, "T2-ending H470")
hand2 = ["v0","v1","t","b","e","T2","e_prime","u","q","c1","a_star","s","delta","eps","T5","v5"]
G2 = nx.Graph(residual + ebset + t2_geo)
assert all(G2.has_edge(hand2[i], hand2[(i+1)%16]) for i in range(16))
print("  hand T2-C16 OK", hand2)

print("ALL Fire 30 / H470 property tests PASS")
