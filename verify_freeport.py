#!/usr/bin/env python3
"""Explicit path-9 constructions for PROOF_FREEPORT_CLOSED.md"""
import networkx as nx
from pathlib import Path
import subprocess
import sys

def assert_path(G, nodes, name):
    for i in range(len(nodes) - 1):
        assert G.has_edge(nodes[i], nodes[i + 1]), f"{name}: missing {nodes[i]}-{nodes[i+1]}"
    assert len(nodes) - 1 == 9, f"{name}: len {len(nodes)-1} != 9"
    print(f"  {name} PASS")

def base_Pstar_PH():
    G = nx.Graph()
    G.add_edges_from(
        [("s", "a2"), ("a2", "x2"), ("x2", "x3"), ("x3", "x4"), ("x4", "x5"), ("x5", "b2"), ("b2", "t")]
    )
    G.add_edges_from([("s", "a1"), ("a1", "b1"), ("b1", "t")])
    return G

def test_I1a_wa_w4():
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("ua", "wa"), ("u4", "w4"), ("wa", "w4")])
    assert_path(G, ["s", "a2", "ua", "wa", "w4", "u4", "x4", "x5", "b2", "t"], "I.1.a")

def test_I1c_table():
    # e2 with e1
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("x3", "u3"), ("b2", "ub"), ("u3", "ub")])
    assert_path(G, ["s", "a2", "ua", "u4", "x4", "x3", "u3", "ub", "b2", "t"], "I.1.c e2")
    # u3-wa
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("ua", "wa"), ("x3", "u3"), ("u3", "wa")])
    assert_path(G, ["s", "a2", "ua", "wa", "u3", "x3", "x4", "x5", "b2", "t"], "I.1.c wa")
    # u3-a1
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("x3", "u3"), ("u3", "a1")])
    assert_path(G, ["s", "a2", "ua", "u4", "x4", "x3", "u3", "a1", "b1", "t"], "I.1.c a1")
    # n-ua
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("x3", "u3"), ("u3", "n"), ("n", "ua")])
    assert_path(G, ["s", "a2", "ua", "n", "u3", "x3", "x4", "x5", "b2", "t"], "I.1.c n-ua")
    # n-u5
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("x3", "u3"), ("x5", "u5"), ("u3", "n"), ("n", "u5")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "n", "u5", "x5", "b2", "t"], "I.1.c n-u5")
    # n-b1
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("x3", "u3"), ("u3", "n"), ("n", "b1")])
    assert_path(G, ["s", "a2", "ua", "u4", "x4", "x3", "u3", "n", "b1", "t"], "I.1.c n-b1")

def test_I3_ua_dist5_ub():
    G = base_Pstar_PH()
    G.add_edges_from([("x2", "u2"), ("x5", "u5"), ("u2", "u5")])  # e3
    G.add_edges_from([("a2", "ua"), ("b2", "ub")])
    nodes = ["ua"] + [f"m{i}" for i in range(4)] + ["ub"]
    G.add_edge("ua", nodes[1])
    for i in range(1, 4):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[4], "ub")
    # s-a2-ua-m0? nodes[0] is ua. path s-a2-ua-m1-m2-m3-m4-ub-b2-t
    p = ["s", "a2", "ua", "m1", "m2", "m3", "m4", "ub", "b2", "t"]
    # fix edges: ua-m1, m1-m2, m2-m3, m3-m4, m4-ub
    G = base_Pstar_PH()
    G.add_edges_from([("x2", "u2"), ("x5", "u5"), ("u2", "u5"), ("a2", "ua"), ("b2", "ub")])
    G.add_edges_from([("ua", "m1"), ("m1", "m2"), ("m2", "m3"), ("m3", "m4"), ("m4", "ub")])
    assert_path(G, ["s", "a2", "ua", "m1", "m2", "m3", "m4", "ub", "b2", "t"], "I.3 d=5")

def test_II_clean():
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "p"), ("p", "q"), ("q", "u4")])
    assert_path(G, ["s", "a2", "ua", "p", "q", "u4", "x4", "x5", "b2", "t"], "II.1 ua_u4")
    G = base_Pstar_PH()
    G.add_edges_from([("x3", "u3"), ("b2", "ub"), ("u3", "p"), ("p", "q"), ("q", "ub")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "p", "q", "ub", "b2", "t"], "II.1 u3_ub")
    G = base_Pstar_PH()
    G.add_edges_from([("x5", "u5"), ("x2", "u2"), ("u5", "p"), ("p", "q"), ("q", "u2")])
    assert_path(G, ["s", "a2", "x2", "u2", "q", "p", "u5", "x5", "b2", "t"], "II.1 u5_u2")

def test_II2_ua_ub():
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("b2", "ub"), ("ua", "p"), ("p", "q"), ("q", "ub"), ("x3", "u3"), ("u3", "p")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "p", "q", "ub", "b2", "t"], "II.2 u3-p")
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("b2", "ub"), ("ua", "p"), ("p", "q"), ("q", "ub"), ("x3", "u3"), ("u3", "n"), ("n", "q")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "n", "q", "ub", "b2", "t"], "II.2 n-q")
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("b2", "ub"), ("ua", "p"), ("p", "q"), ("q", "ub"), ("x3", "u3"), ("u3", "n"), ("n", "ua")])
    assert_path(G, ["s", "a2", "ua", "n", "u3", "x3", "x4", "x5", "b2", "t"], "II.2 n-ua")
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("b2", "ub"), ("ua", "p"), ("p", "q"), ("q", "ub"), ("x3", "u3"), ("u3", "n"), ("n", "b1")])
    assert_path(G, ["s", "a1", "b1", "n", "u3", "x3", "x4", "x5", "b2", "t"], "II.2 n-b1 via a1")

def test_II3_landings():
    # ua_u2 + u3-p
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x2", "u2"), ("ua", "p"), ("p", "q"), ("q", "u2"), ("x3", "u3"), ("u3", "p")])
    assert_path(G, ["s", "a2", "ua", "p", "u3", "x3", "x4", "x5", "b2", "t"], "II.3.1 u3-p")
    # ua_u2 + u4-q
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x2", "u2"), ("ua", "p"), ("p", "q"), ("q", "u2"), ("x4", "u4"), ("u4", "q")])
    assert_path(G, ["s", "a2", "ua", "p", "q", "u4", "x4", "x5", "b2", "t"], "II.3.1 u4-q")
    # ua_u2 + u4-n-p style (n in B free of u4, n~p): path9
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x2", "u2"), ("ua", "p"), ("p", "q"), ("q", "u2"), ("x4", "u4"), ("u4", "n"), ("n", "p")])
    assert_path(G, ["s", "a2", "ua", "p", "n", "u4", "x4", "x5", "b2", "t"], "II.3.1 u4-n-p")
    # u3_u4 + ua-p
    G = base_Pstar_PH()
    G.add_edges_from([("x3", "u3"), ("x4", "u4"), ("u3", "p"), ("p", "q"), ("q", "u4"), ("a2", "ua"), ("ua", "p")])
    assert_path(G, ["s", "a2", "ua", "p", "q", "u4", "x4", "x5", "b2", "t"], "II.3.3 ua-p")
    # u3_u4 + ub-q
    G = base_Pstar_PH()
    G.add_edges_from([("x3", "u3"), ("x4", "u4"), ("u3", "p"), ("p", "q"), ("q", "u4"), ("b2", "ub"), ("ub", "q")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "p", "q", "ub", "b2", "t"], "II.3.3 ub-q")
    # u5_ub + u3-p
    G = base_Pstar_PH()
    G.add_edges_from([("x5", "u5"), ("b2", "ub"), ("u5", "p"), ("p", "q"), ("q", "ub"), ("x3", "u3"), ("u3", "p")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "p", "q", "ub", "b2", "t"], "II.3.5 u3-p")
    # u5_ub + u2-q-p-u5
    G = base_Pstar_PH()
    G.add_edges_from([("x5", "u5"), ("b2", "ub"), ("u5", "p"), ("p", "q"), ("q", "ub"), ("x2", "u2"), ("u2", "q")])
    assert_path(G, ["s", "a2", "x2", "u2", "q", "p", "u5", "x5", "b2", "t"], "II.3.5 u2-q")

def test_III2_p3_x4():
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x3", "u3"), ("ua", "p1"), ("p1", "p2"), ("p2", "p3"), ("p3", "u3"), ("p3", "x4")])
    assert_path(G, ["s", "a2", "ua", "p1", "p2", "p3", "x4", "x5", "b2", "t"], "III.2 p3-x4")
    G = base_Pstar_PH()
    G.add_edges_from([("a2", "ua"), ("x3", "u3"), ("ua", "p1"), ("p1", "p2"), ("p2", "p3"), ("p3", "u3"), ("p3", "b1")])
    assert_path(G, ["s", "a1", "b1", "p3", "u3", "x3", "x4", "x5", "b2", "t"], "III.2 p3-b1")

def test_path9_to_C16():
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
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("  path9=>C16 PASS")

def test_regression():
    root = Path(__file__).resolve().parent
    r = subprocess.run([sys.executable, str(root / "verify_open201.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("  open201 regression PASS")

if __name__ == "__main__":
    print("Part I:")
    test_I1a_wa_w4()
    test_I1c_table()
    test_I3_ua_dist5_ub()
    print("Part II:")
    test_II_clean()
    test_II2_ua_ub()
    test_II3_landings()
    print("Part III:")
    test_III2_p3_x4()
    print("Meta:")
    test_path9_to_C16()
    test_regression()
    print("ALL verify_freeport PASS")
