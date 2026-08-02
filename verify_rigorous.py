#!/usr/bin/env python3
"""Seeds for PROOF_RIGOROUS.md — fully proved theorems only."""
import networkx as nx
from pathlib import Path
import subprocess
import sys

def test_thm1_exclusive_C16():
    G = nx.cycle_graph(6)
    nodes = [f"p{i}" for i in range(10)]
    G.add_edge(0, nodes[0])
    for i in range(9):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[9], 1)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("Thm1 exclusive C12=>C16 PASS")

def test_thm3_path9():
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
    assert 12 in {len(c) for c in nx.simple_cycles(G)}
    assert 16 in {len(c) for c in nx.simple_cycles(G)}
    print("Thm3 path9 => C12+C16 PASS")

def test_thm8_unions():
    for L1, L2 in [(8, 8), (4, 12), (7, 9)]:
        G = nx.Graph()
        for i in range(L1):
            G.add_edge(i, i + 1)
        q = [f"q{i}" for i in range(L2 - 1)]
        G.add_edge(0, q[0])
        for i in range(L2 - 2):
            G.add_edge(q[i], q[i + 1])
        G.add_edge(q[-1], L1)
        assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("Thm8 path unions PASS")

def test_thm12_A2_C8():
    """A2 p2=T2 long cycle length 8 seed."""
    G = nx.Graph()
    for i in range(6):
        G.add_edge(i, (i + 1) % 6)
    G.add_edge(0, "s")
    G.add_edge(2, "T2")
    G.add_edge("s", "p1")
    G.add_edge("p1", "T2")
    # cycle s-p1-T2-v2-v3-v4-v5-v0-s
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("Thm12 A2 C8 PASS")

def test_thm19_chord_flip():
    """Legal chord on length-7 path: span 5 => C6, flip => length 3 path ends."""
    # s-a2-x2-x3-x4-x5-b2-t with chord a2-x5 (A to A? a2 in A, x5 in A — same part, no edge)
    # chord x2-b2: x2 in B, b2 in B — same part no
    # chord a2-x4: a2 A, x4 B — path a2-x2-x3-x4 length 3, chord => C4 forbidden
    # legal: a2-b2? a2 A b2 B, path a2-x2-x3-x4-x5-b2 length 5, chord => C6
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edge("a2", "b2")  # chord span 5
    assert any(len(c) == 6 for c in nx.simple_cycles(G))
    # flipped path s-a2-b2-t length 3
    assert nx.shortest_path_length(G, "s", "t") == 3
    print("Thm19.1 chord flip PASS")

def test_thm27_shared_third_C16():
    G = nx.cycle_graph(18)
    G.add_edges_from([(0, "t"), (4, "t")])
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("Thm27 L=18 d=4 shared third C16 PASS")

def test_thm34_triangle():
    G = nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0),(0,3),(1,4)])
    G.add_edges_from([(3,6),(6,7),(7,8),(8,4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    G2 = nx.Graph()
    G2.add_edges_from([(0,1),(1,2),(2,0),(0,3),(1,4)])
    G2.add_edges_from([(3,6),(6,7),(7,8),(8,9),(9,4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G2))
    print("Thm34 triangle L=4,5 C8 PASS")

def test_thm40_C7():
    G = nx.Graph()
    for i in range(7):
        G.add_edge(i, (i + 1) % 7)
        G.add_edge(i, 7 + i)
    nodes = [14 + i for i in range(10)]
    G.add_edge(7, nodes[0])
    for i in range(9):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[9], 10)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("Thm40 C7 L=10 C16 PASS")

def test_portable_closed():
    root = Path(__file__).resolve().parent
    r = subprocess.run([sys.executable, str(root / "verify_closed.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("verify_closed portable PASS")

if __name__ == "__main__":
    test_thm1_exclusive_C16()
    test_thm3_path9()
    test_thm8_unions()
    test_thm12_A2_C8()
    test_thm19_chord_flip()
    test_thm27_shared_third_C16()
    test_thm34_triangle()
    test_thm40_C7()
    test_portable_closed()
    print("ALL verify_rigorous PASS")
