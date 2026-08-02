#!/usr/bin/env python3
"""Fire 37: abstract C16 fork + girth≥9 antipodal seeds."""
import networkx as nx

def path_union_graph(L1, L2):
    G = nx.Graph()
    for i in range(L1):
        G.add_edge(i, i + 1)
    s, t = 0, L1
    nodes = [f"q{i}" for i in range(L2 - 1)]
    G.add_edge(s, nodes[0])
    for i in range(L2 - 2):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[-1], t)
    return G

def test_path_union():
    for L1, L2 in [(8, 8), (6, 10), (7, 9), (4, 12), (5, 11)]:
        G = path_union_graph(L1, L2)
        assert any(len(c) == L1 + L2 for c in nx.simple_cycles(G)), (L1, L2)
    print("H810-812 path union C16 PASS")

def test_smooth_L14():
    G = nx.Graph()
    G.add_edges_from([("a", "t"), ("t", "b"), ("t", "v")])
    nodes = [f"p{i}" for i in range(13)]
    G.add_edge("a", nodes[0])
    for i in range(12):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[12], "b")
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("H820 smooth L14 C16 PASS")

def test_C10_L9():
    G = nx.cycle_graph(10)
    for i in range(10):
        G.add_edge(i, 10 + i)
    nodes = [30 + i for i in range(8)]
    G.add_edge(10, nodes[0])
    for i in range(7):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[7], 15)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("H840 C10 antipodal L9 C16 PASS")

def test_C12_L8():
    G = nx.cycle_graph(12)
    for i in range(12):
        G.add_edge(i, 20 + i)
    nodes = [50 + i for i in range(7)]
    G.add_edge(20, nodes[0])
    for i in range(6):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[6], 26)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("H841 C12 antipodal L8 C16 PASS")

def test_C14_L7():
    G = nx.cycle_graph(14)
    for i in range(14):
        G.add_edge(i, 30 + i)
    nodes = [60 + i for i in range(6)]
    G.add_edge(30, nodes[0])
    for i in range(5):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[5], 37)
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("H842 C14 antipodal L7 C16 PASS")

def test_smooth_C4():
    G = nx.Graph()
    G.add_edges_from([("a", "t1"), ("t1", "b"), ("a", "t2"), ("t2", "b")])
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    print("H701 multiedge C4 PASS")

if __name__ == "__main__":
    test_path_union()
    test_smooth_L14()
    test_C10_L9()
    test_C12_L8()
    test_C14_L7()
    test_smooth_C4()
    print("ALL Fire 37 tests PASS")
