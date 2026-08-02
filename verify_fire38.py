#!/usr/bin/env python3
"""Fire 38: residual-good chain seeds (S590)."""
import networkx as nx

def test_H9():
    G = nx.cycle_graph(6)
    nodes = [f"p{i}" for i in range(10)]
    G.add_edge(0, nodes[0])
    for i in range(9):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[9], 1)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("H9 exclusive path11 C16 PASS")

def test_H13_H9():
    G = nx.Graph()
    for i in range(6):
        G.add_edge(f"v{i}", f"v{(i+1)%6}")
    G.add_edge("v0", "s")
    G.add_edge("v1", "t")
    nodes = [f"h{i}" for i in range(8)]
    G.add_edge("s", nodes[0])
    for i in range(7):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[7], "t")
    lens = {len(c) for c in nx.simple_cycles(G)}
    assert 12 in lens and 16 in lens
    print("H13 path9 => C12+C16 PASS")

def test_Cstar():
    G = nx.Graph()
    G.add_edges_from(
        [
            ("s", "a1"),
            ("a1", "b1"),
            ("b1", "t"),
            ("a1", "x"),
            ("b1", "y"),
            ("x", "p"),
            ("p", "q"),
            ("q", "y"),
        ]
    )
    assert any(len(c) == 6 for c in nx.simple_cycles(G))
    print("H853 C* C6 PASS")

def test_H36_logic():
    """dist 2 => C4, dist 6 => C8 with the vertex."""
    # C4 from second common neighbour
    G = nx.Graph()
    G.add_edges_from([("v", "x"), ("v", "y"), ("x", "c"), ("y", "c")])
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    # C8 from path6 + x-v-y
    G2 = nx.Graph()
    G2.add_edges_from([("v", "x"), ("v", "y")])
    nodes = [f"q{i}" for i in range(5)]
    G2.add_edge("x", nodes[0])
    for i in range(4):
        G2.add_edge(nodes[i], nodes[i + 1])
    G2.add_edge(nodes[4], "y")
    assert any(len(c) == 8 for c in nx.simple_cycles(G2))
    print("H36 C4/C8 gap logic PASS")

def test_length4_path_is_good():
    """d0=4 configuration smoke: path s-p1-p2-t-v1 style exists as graph."""
    G = nx.Graph()
    G.add_edges_from(
        [
            ("v0", "s"),
            ("v0", "v1"),
            ("v0", "v5"),
            ("s", "p1"),
            ("p1", "p2"),
            ("p2", "t"),
            ("t", "v1"),
            ("v1", "v2"),
        ]
    )
    assert nx.shortest_path_length(G, "s", "v1") <= 4
    # path in G-v0
    H = G.copy()
    H.remove_node("v0")
    assert nx.has_path(H, "s", "v1")
    assert nx.shortest_path_length(H, "s", "v1") == 4
    print("H850 residual-good path4 smoke PASS")

def test_chain_regression():
    """Prior arm kills still pass."""
    import subprocess, sys
    for s in ["verify_fire30.py", "verify_fire33.py", "verify_fire37.py"]:
        r = subprocess.run(
            [sys.executable, f"/workspace/engram-math-campaign/{s}"],
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, (s, r.stdout, r.stderr)
    print("regression fire30/33/37 PASS")

if __name__ == "__main__":
    test_H9()
    test_H13_H9()
    test_Cstar()
    test_H36_logic()
    test_length4_path_is_good()
    test_chain_regression()
    print("ALL Fire 38 tests PASS")
