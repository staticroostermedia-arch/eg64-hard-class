#!/usr/bin/env python3
"""Property tests for PROOF_CLOSED.md theorems C1–C16 seeds."""
import networkx as nx
import random
import subprocess
import sys
from pathlib import Path

def test_H9_H13():
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
    print("C3/H13 path9 C16 PASS")

def test_L4_triangle_C8():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3), (1, 4)])
    G.add_edges_from([(3, 6), (6, 7), (7, 8), (8, 4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("C12 L=4 triangle C8 PASS")

def test_L5_triangle_C8():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3), (1, 4)])
    G.add_edges_from([(3, 6), (6, 7), (7, 8), (8, 9), (9, 4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("C12 L=5 triangle C8 PASS")

def test_universal_common_C4():
    G = nx.Graph()
    G.add_edges_from(
        [
            (0, 1), (1, 2), (2, 0), (0, 3), (1, 4), (2, 5),
            (3, "x"), (4, "x"), (5, "x"),
            (3, "w"), (4, "w"), (5, "w"),
        ]
    )
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    print("C12 universal common C4 PASS")

def test_C7_L10():
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
    print("C15/H682 C7 L10 C16 PASS")

def test_smooth_d14():
    G = nx.Graph()
    G.add_edges_from([("a", "t"), ("t", "b"), ("t", "v")])
    nodes = [f"p{i}" for i in range(13)]
    G.add_edge("a", nodes[0])
    for i in range(12):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[12], "b")
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("C15 d=14 C16 PASS")

def test_C10_antipodal():
    G = nx.cycle_graph(10)
    for i in range(10):
        G.add_edge(i, 10 + i)
    nodes = [30 + i for i in range(8)]
    G.add_edge(10, nodes[0])
    for i in range(7):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[7], 15)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("C16/H840 C10 C16 PASS")

def test_path_union():
    for L1, L2 in [(8, 8), (4, 12), (6, 10)]:
        G = nx.Graph()
        for i in range(L1):
            G.add_edge(i, i + 1)
        nodes = [f"q{i}" for i in range(L2 - 1)]
        G.add_edge(0, nodes[0])
        for i in range(L2 - 2):
            G.add_edge(nodes[i], nodes[i + 1])
        G.add_edge(nodes[-1], L1)
        assert any(len(c) == L1 + L2 for c in nx.simple_cycles(G))
    print("H811-812 path union PASS")

def test_chord_L18_d5():
    """L=18 chord at d=5 creates C6 and C14 — C6 exists."""
    G = nx.cycle_graph(18)
    G.add_edge(0, 5)  # chord d=5
    lens = {len(c) for c in nx.simple_cycles(G)}
    assert 6 in lens
    print("C9 L=18 chord d=5 gives C6 PASS")

def test_shared_third_L18_d4():
    """Shared third at d=4 on C18: lengths 6 and 16."""
    G = nx.cycle_graph(18)
    G.add_edges_from([(0, "t"), (4, "t")])
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("C9 L=18 shared third d=4 C16 PASS")

def test_og5_L4():
    """C5 thirds L=4 => C8."""
    G = nx.cycle_graph(5)
    for i in range(5):
        G.add_edge(i, 10 + i)
    # path between t0=10 and t2=12 length 4
    G.add_edges_from([(10, 20), (20, 21), (21, 22), (22, 12)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("C14 og5 L=4 C8 PASS")

def test_regression():
    root = Path(__file__).resolve().parent
    for s in [
        "verify_fire30.py",
        "verify_fire33.py",
        "verify_fire36.py",
        "verify_fire37.py",
        "verify_fire38.py",
        "verify_fire39.py",
    ]:
        r = subprocess.run(
            [sys.executable, str(root / s)],
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, (s, r.stdout[-500:], r.stderr[-500:])
    print("full regression PASS")

if __name__ == "__main__":
    test_H9_H13()
    test_L4_triangle_C8()
    test_L5_triangle_C8()
    test_universal_common_C4()
    test_C7_L10()
    test_smooth_d14()
    test_C10_antipodal()
    test_path_union()
    test_chord_L18_d5()
    test_shared_third_L18_d4()
    test_og5_L4()
    test_regression()
    print("ALL verify_closed PASS — Theorems A/B seeds green")
