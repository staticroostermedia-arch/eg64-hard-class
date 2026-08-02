#!/usr/bin/env python3
"""Fire 34: connectivity facts + re-run chain integrity."""
import networkx as nx
import subprocess, sys

def is_cubic(G):
    return all(d == 3 for _, d in G.degree())

# H581 examples: cubic ⇒ κ=λ
graphs = {
    "K33": nx.complete_bipartite_graph(3, 3),
    "Q3": nx.hypercube_graph(3),
    "circ_ladder6": nx.circular_ladder_graph(6),
    "heawood": nx.heawood_graph(),
}
# λ=2 cubic bipartite with C4s
G = nx.Graph()
for a in [0, 1, 2]:
    for b in [3, 4, 5]:
        if (a, b) != (0, 3):
            G.add_edge(a, b)
for a in [6, 7, 8]:
    for b in [9, 10, 11]:
        if (a, b) != (6, 9):
            G.add_edge(a, b)
G.add_edge(0, 9)
G.add_edge(3, 6)
graphs["lambda2_c4"] = G

for name, H in graphs.items():
    assert is_cubic(H), name
    k, l = nx.node_connectivity(H), nx.edge_connectivity(H)
    assert k == l, (name, k, l)
    print(f"H581 {name}: kappa=lambda={k} PASS")

# Heawood is 3-connected hard-ish (has C6, has C8 actually)
H = nx.heawood_graph()
assert nx.node_connectivity(H) == 3
print("Heawood kappa=3 PASS")

# Chain scripts
for s in ["verify_fire30.py", "verify_fire32.py", "verify_fire33.py"]:
    r = subprocess.run([sys.executable, f"/workspace/engram-math-campaign/{s}"], capture_output=True, text=True)
    assert r.returncode == 0, (s, r.stdout, r.stderr)
    print(f"chain {s} PASS")

print("ALL Fire 34 tests PASS")
