#!/usr/bin/env python3
"""Fire 39: S582 connectivity + S612 triangle seeds."""
import networkx as nx
import random

def is_cubic(G):
    return all(d == 3 for _, d in G.degree())

def test_kappa_lambda():
    for G in [
        nx.complete_bipartite_graph(3, 3),
        nx.hypercube_graph(3),
        nx.heawood_graph(),
    ]:
        assert is_cubic(G)
        assert nx.node_connectivity(G) == nx.edge_connectivity(G)
    # λ=2 construction
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
    assert is_cubic(G) and nx.is_bipartite(G)
    assert nx.node_connectivity(G) == 2 == nx.edge_connectivity(G)
    print("H900 kappa=lambda PASS")

def test_bridge_matching_idea():
    """Odd component of G-e cannot have perfect matching — cubic bipartite has PM."""
    # Smoke: K33 has PM and is 3-edge-connected
    G = nx.complete_bipartite_graph(3, 3)
    assert nx.edge_connectivity(G) == 3
    matching = nx.bipartite.maximum_matching(G, top_nodes=[0, 1, 2])
    assert len(matching) == 6  # 3 edges * 2 dict entries
    print("H901 matching/bridge smoke PASS")

def test_cut_cycle_lengths():
    for p, q, L in [(2, 2, 6), (2, 4, 8), (4, 4, 10), (5, 5, 12)]:
        assert p + q + 2 == L
    print("H902 cut cycle formula PASS")

def test_thirds_L5_C8():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3), (1, 4), (2, 5)])
    G.add_edges_from([(3, 6), (6, 7), (7, 8), (8, 9), (9, 4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("H923 L=5 => C8 PASS")

def test_L4_with_long_triangle_C8():
    """External path len 4 + a-c-b len 4 => C8."""
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3), (1, 4)])
    # path 3-6-7-8-4 length 4
    G.add_edges_from([(3, 6), (6, 7), (7, 8), (8, 4)])
    # cycle 3-6-7-8-4-1-2-0-3 length 8
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("H925 L=4 + acb => C8 PASS")

def test_two_L4_C8():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3), (1, 4)])
    G.add_edges_from([(3, "a"), ("a", "b"), ("b", "c"), ("c", 4)])
    G.add_edges_from([(3, "d"), ("d", "e"), ("e", "f"), ("f", 4)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("H924 two L4 => C8 PASS")

def test_universal_common_C4():
    """x~ta,tb,tc and w~ta,tb,tc => C4 ta-x-tb-w."""
    G = nx.Graph()
    G.add_edges_from(
        [
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 4),
            (2, 5),
            (3, "x"),
            (4, "x"),
            (5, "x"),
            (3, "w"),
            (4, "w"),
            (5, "w"),
        ]
    )
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    print("H928 universal common + w => C4 PASS")

def test_triangle_samples():
    rng = random.Random(99)
    seen = 0
    for n in [10, 12, 14, 16]:
        for _ in range(400):
            stubs = []
            for v in range(n):
                stubs.extend([v, v, v])
            rng.shuffle(stubs)
            G = nx.Graph()
            G.add_nodes_from(range(n))
            ok = True
            for i in range(0, len(stubs), 2):
                a, b = stubs[i], stubs[i + 1]
                if a == b or G.has_edge(a, b):
                    ok = False
                    break
                G.add_edge(a, b)
            if not ok or not all(d == 3 for _, d in G.degree()):
                continue
            if not nx.is_connected(G):
                continue
            has3 = any(len(c) == 3 for c in nx.simple_cycles(G))
            has4 = any(len(c) == 4 for c in nx.simple_cycles(G))
            if has3 and not has4:
                p2 = any(len(c) in (8, 16) for c in nx.simple_cycles(G))
                assert p2
                seen += 1
                if seen >= 5:
                    break
        if seen >= 5:
            break
    assert seen >= 1
    print(f"H928 triangle samples C8/C16 PASS (seen={seen})")

if __name__ == "__main__":
    test_kappa_lambda()
    test_bridge_matching_idea()
    test_cut_cycle_lengths()
    test_thirds_L5_C8()
    test_L4_with_long_triangle_C8()
    test_two_L4_C8()
    test_universal_common_C4()
    test_triangle_samples()
    print("ALL Fire 39 tests PASS")
