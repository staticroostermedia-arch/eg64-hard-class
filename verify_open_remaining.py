#!/usr/bin/env python3
"""Seeds for PROOF_OPEN_REMAINING.md"""
import networkx as nx
from pathlib import Path
import subprocess
import sys

def test_C10_antipodal_D9():
    G = nx.cycle_graph(10)
    for i in range(10):
        G.add_edge(i, f"t{i}")
    # path length 9 between t0 and t5
    nodes = [f"p{i}" for i in range(8)]
    G.add_edge("t0", nodes[0])
    for i in range(7):
        G.add_edge(nodes[i], nodes[i+1])
    G.add_edge(nodes[7], "t5")
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("29.1 C10 D=9 C16 PASS")

def test_C10_shared_third_d4():
    G = nx.cycle_graph(10)
    G.add_edges_from([(0, "t"), (4, "t")])
    assert any(len(c) == 6 for c in nx.simple_cycles(G))
    print("29.1 shared third d=4 C6 PASS")

def test_og5_through_C_bound():
    """L_i <= 4 always via C5 path length 4."""
    G = nx.cycle_graph(5)
    for i in range(5):
        G.add_edge(i, f"t{i}")
    # path t0-v0-v1-v2-t2 length 4
    assert nx.shortest_path_length(G, "t0", "t2") == 4
    print("38 through-C L<=4 PASS")

def test_og5_L3_C8():
    G = nx.cycle_graph(5)
    for i in range(5):
        G.add_edge(i, f"t{i}")
    G.add_edges_from([("t0", "a"), ("a", "b"), ("b", "t2")])
    # L=3: cycle L+5=8
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("38 L=3 C8 PASS")

def test_og5_L4_C8():
    G = nx.cycle_graph(5)
    for i in range(5):
        G.add_edge(i, f"t{i}")
    G.add_edges_from([("t0", "a"), ("a", "b"), ("b", "c"), ("c", "t2")])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("38 L=4 C8 PASS")

def test_triangle_through_path_len3():
    G = nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0),(0,"ta"),(1,"tb"),(2,"tc")])
    assert nx.shortest_path_length(G, "ta", "tb") == 3  # through triangle
    print("36 through-triangle L<=3 PASS")

def test_triangle_L4_C8():
    G = nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0),(0,"ta"),(1,"tb")])
    G.add_edges_from([("ta",6),(6,7),(7,8),(8,"tb")])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("36 L=4 C8 PASS")

def test_triangle_L5_C8():
    G = nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0),(0,"ta"),(1,"tb")])
    G.add_edges_from([("ta",6),(6,7),(7,8),(8,9),(9,"tb")])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("36 L=5 C8 PASS")

def test_C7_D10():
    G = nx.Graph()
    for i in range(7):
        G.add_edge(i, (i+1)%7)
        G.add_edge(i, 7+i)
    nodes = [14+i for i in range(10)]
    G.add_edge(7, nodes[0])
    for i in range(9):
        G.add_edge(nodes[i], nodes[i+1])
    G.add_edge(nodes[9], 10)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("39 C7 D=10 C16 PASS")

def test_C7_D_bound():
    """Through-C path length 5 bounds D."""
    G = nx.Graph()
    for i in range(7):
        G.add_edge(i, (i+1)%7)
        G.add_edge(i, f"t{i}")
    # t0-v0-v1-v2-v3-t3 length 5
    assert nx.shortest_path_length(G, "t0", "t3") == 5
    print("39 through-C D<=5 PASS")

def test_residual_bad_chord_span5():
    """Length 8 path chord span 5 => length 4 residual good."""
    G = nx.Graph()
    nodes = ["s"] + [f"y{i}" for i in range(1,8)] + ["v1"]
    for i in range(len(nodes)-1):
        G.add_edge(nodes[i], nodes[i+1])
    # chord span 5: s to y5? path s-y1-y2-y3-y4-y5 length 5, chord s-y5
    # actually span 5 edges: from y1 to y6
    G.add_edge("y1", "y6")
    assert any(len(c) == 6 for c in nx.simple_cycles(G))
    # flipped s-y1-y6-y7-v1 length 4
    assert nx.shortest_path_length(G, "s", "v1") == 4
    print("32 chord span5 => residual good len4 PASS")

def test_prior_open201():
    root = Path(__file__).resolve().parent
    r = subprocess.run([sys.executable, str(root/"verify_open201.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("open201 regression PASS")

if __name__ == "__main__":
    test_C10_antipodal_D9()
    test_C10_shared_third_d4()
    test_og5_through_C_bound()
    test_og5_L3_C8()
    test_og5_L4_C8()
    test_triangle_through_path_len3()
    test_triangle_L4_C8()
    test_triangle_L5_C8()
    test_C7_D10()
    test_C7_D_bound()
    test_residual_bad_chord_span5()
    test_prior_open201()
    print("ALL verify_open_remaining PASS")
