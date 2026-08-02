#!/usr/bin/env python3
"""Seeds for PROOF_PURENEW_CLOSED.md"""
import networkx as nx
from pathlib import Path
import subprocess
import sys

def assert_path(G, nodes, name, length=9):
    for i in range(len(nodes) - 1):
        assert G.has_edge(nodes[i], nodes[i + 1]), f"{name}: missing {nodes[i]}-{nodes[i+1]}"
    assert len(nodes) - 1 == length, f"{name}: len {len(nodes)-1} != {length}"
    print(f"  {name} PASS (len {length})")

def base():
    G = nx.Graph()
    G.add_edges_from(
        [("s", "a2"), ("a2", "x2"), ("x2", "x3"), ("x3", "x4"), ("x4", "x5"), ("x5", "b2"), ("b2", "t")]
    )
    G.add_edges_from([("s", "a1"), ("a1", "b1"), ("b1", "t")])
    return G

def test_L2_C8_ban_ua_u5():
    G = base()
    G.add_edges_from([("a2", "ua"), ("x5", "u5"), ("ua", "n"), ("n", "u5")])
    # C8: ua-a2-x2-x3-x4-x5-u5-n-ua
    cyc = ["ua", "a2", "x2", "x3", "x4", "x5", "u5", "n", "ua"]
    for i in range(len(cyc) - 1):
        assert G.has_edge(cyc[i], cyc[i + 1])
    assert len(cyc) - 1 == 8
    print("  §2.1 ua-n-u5 C8 ban PASS")

def test_L2_ua_u3_path9():
    G = base()
    G.add_edges_from([("a2", "ua"), ("x3", "u3"), ("ua", "n"), ("n", "u3")])
    assert_path(G, ["s", "a2", "ua", "n", "u3", "x3", "x4", "x5", "b2", "t"], "§2.2 ua-n-u3")

def test_L2_u3_u5_path9():
    G = base()
    G.add_edges_from([("x3", "u3"), ("x5", "u5"), ("u3", "n"), ("n", "u5")])
    assert_path(G, ["s", "a2", "x2", "x3", "u3", "n", "u5", "x5", "b2", "t"], "§2.3 u3-n-u5")

def test_L2_u3_b1():
    G = base()
    G.add_edges_from([("x3", "u3"), ("u3", "n"), ("n", "b1")])
    assert_path(G, ["s", "a1", "b1", "n", "u3", "x3", "x4", "x5", "b2", "t"], "§2.3 u3-n-b1")

def test_L2_ua_n_b1_via_u3():
    G = base()
    G.add_edges_from([("a2", "ua"), ("ua", "n"), ("n", "b1"), ("x3", "u3"), ("u3", "n")])
    assert_path(G, ["s", "a2", "ua", "n", "u3", "x3", "x4", "x5", "b2", "t"], "§2.3 ua-n-b1 upgrade")

def test_L2_u5_b1():
    G = base()
    G.add_edges_from([("x5", "u5"), ("u5", "n"), ("n", "b1")])
    assert_path(G, ["s", "a2", "x2", "x3", "x4", "x5", "u5", "n", "b1", "t"], "§2.3 u5-n-b1")

def test_L2_u2_a1():
    G = base()
    G.add_edges_from([("x2", "u2"), ("u2", "n"), ("n", "a1")])
    assert_path(G, ["s", "a1", "n", "u2", "x2", "x3", "x4", "x5", "b2", "t"], "§2.3 u2-n-a1")

def test_L2_u4_a1():
    G = base()
    G.add_edges_from([("x4", "u4"), ("u4", "n"), ("n", "a1")])
    assert_path(G, ["s", "a2", "x2", "x3", "x4", "u4", "n", "a1", "b1", "t"], "§2.3 u4-n-a1")

def test_L2_w4_ua():
    G = base()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("u4", "w4"), ("ua", "n"), ("n", "w4")])
    assert_path(G, ["s", "a2", "ua", "n", "w4", "u4", "x4", "x5", "b2", "t"], "§2.3 w4-n-ua")

def test_L2_wa_u4():
    G = base()
    G.add_edges_from([("a2", "ua"), ("x4", "u4"), ("ua", "u4"), ("ua", "wa"), ("wa", "n"), ("n", "u4")])
    assert_path(G, ["s", "a2", "ua", "wa", "n", "u4", "x4", "x5", "b2", "t"], "§2.3 wa-n-u4")

def test_L3_u3_a1():
    G = base()
    G.add_edges_from([("x3", "u3"), ("u3", "n"), ("n", "m"), ("m", "a1")])
    assert_path(G, ["s", "a1", "m", "n", "u3", "x3", "x4", "x5", "b2", "t"], "§3 u3-n-m-a1")

def test_L4_interior_to_u4():
    G = base()
    G.add_edges_from([("a2", "ua"), ("ua", "n"), ("n", "m"), ("m", "p"), ("p", "b1"), ("m", "u4"), ("x4", "u4")])
    assert_path(G, ["s", "a2", "ua", "n", "m", "u4", "x4", "x5", "b2", "t"], "§4 ua..b1 free m-u4")

def test_L5_x3_z2_path9():
    G = base()
    G.add_edges_from([("a2", "ua"), ("x4", "u4")])
    # path ua-z1-z2-z3-z4-u4 length 5
    G.add_edges_from([("ua", "z1"), ("z1", "z2"), ("z2", "z3"), ("z3", "z4"), ("z4", "u4")])
    # free x3-z2
    G.add_edge("x3", "z2")
    assert_path(G, ["s", "a2", "ua", "z1", "z2", "x3", "x4", "x5", "b2", "t"], "§5.3 x3-z2")

def test_I3_d5():
    G = base()
    G.add_edges_from([("x2", "u2"), ("x5", "u5"), ("u2", "u5"), ("a2", "ua"), ("b2", "ub")])
    G.add_edges_from([("ua", "m1"), ("m1", "m2"), ("m2", "m3"), ("m3", "m4"), ("m4", "ub")])
    assert_path(G, ["s", "a2", "ua", "m1", "m2", "m3", "m4", "ub", "b2", "t"], "§7.4 e3 d=5")

def test_III2_p3_b1():
    G = base()
    G.add_edges_from(
        [("a2", "ua"), ("x3", "u3"), ("ua", "p1"), ("p1", "p2"), ("p2", "p3"), ("p3", "u3"), ("p3", "b1")]
    )
    assert_path(G, ["s", "a1", "b1", "p3", "u3", "x3", "x4", "x5", "b2", "t"], "§7.3 p3-b1")

def test_III2_p3_f_a1():
    G = base()
    G.add_edges_from(
        [
            ("a2", "ua"),
            ("x3", "u3"),
            ("ua", "p1"),
            ("p1", "p2"),
            ("p2", "p3"),
            ("p3", "u3"),
            ("p3", "f"),
            ("f", "a1"),
        ]
    )
    # s-a1-f-p3-u3-x3-x4-x5-b2-t length 9 (f-b1 is B-B impossible)
    assert_path(G, ["s", "a1", "f", "p3", "u3", "x3", "x4", "x5", "b2", "t"], "§7.3 p3-f-a1")

def test_regression():
    root = Path(__file__).resolve().parent
    for s in ["verify_freeport.py", "verify_open201.py"]:
        r = subprocess.run([sys.executable, str(root / s)], capture_output=True, text=True)
        assert r.returncode == 0, s + r.stdout + r.stderr
        print(f"  {s} regression PASS")

if __name__ == "__main__":
    print("§2 L=2:")
    test_L2_C8_ban_ua_u5()
    test_L2_ua_u3_path9()
    test_L2_u3_u5_path9()
    test_L2_u3_b1()
    test_L2_ua_n_b1_via_u3()
    test_L2_u5_b1()
    test_L2_u2_a1()
    test_L2_u4_a1()
    test_L2_w4_ua()
    test_L2_wa_u4()
    print("§3 L=3:")
    test_L3_u3_a1()
    print("§4 L=4:")
    test_L4_interior_to_u4()
    print("§5 L=5:")
    test_L5_x3_z2_path9()
    print("§7 special:")
    test_I3_d5()
    test_III2_p3_b1()
    test_III2_p3_f_a1()
    print("regression:")
    test_regression()
    print("ALL verify_purenew PASS")
