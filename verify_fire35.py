#!/usr/bin/env python3
"""Fire 35: non-bipartite EG seeds."""
import networkx as nx
import random

def find_p2(G, targets=(4, 8, 16, 32)):
    found = set()
    for c in nx.simple_cycles(G):
        L = len(c)
        if L in targets:
            found.add(L)
            if 4 in found or 8 in found:
                return found
    return found

def test_petersen_T_closed():
    G = nx.Graph()
    for i in range(5):
        G.add_edge(i, (i + 1) % 5)
        G.add_edge(i, i + 5)
        G.add_edge(i + 5, ((i + 2) % 5) + 5)
    assert nx.is_isomorphic(G, nx.petersen_graph())
    assert 8 in find_p2(G)
    print("H613d Petersen T-closed PASS")

def test_external_L4_C8():
    G = nx.Graph()
    for i in range(5):
        G.add_edge(i, (i + 1) % 5)
        G.add_edge(i, i + 5)
    # t0=5, t2=7, path length 4: 5-10-11-12-7
    G.add_edges_from([(5, 10), (10, 11), (11, 12), (12, 7)])
    assert 8 in find_p2(G)
    print("H613e external L4 C8 PASS")

def test_external_L3_C8():
    G = nx.Graph()
    for i in range(5):
        G.add_edge(i, (i + 1) % 5)
        G.add_edge(i, i + 5)
    # t0-x-y-t2: 5-10-11-7
    G.add_edges_from([(5, 10), (10, 11), (11, 7)])
    # C8 via H613f: 5-10-11-7-2-3-4-0? wait v0=0,v2=2,v3=3,v4=4
    # t0-x-y-t2-v2-v{0-2}=v3? i=0: v_{i-2}=v3, v_{i-1}=v4, v_i=0
    # cycle: 5-10-11-7-2-3-4-0-5 — need edge 2-3,3-4,4-0,0-5 and 7-2
    assert G.has_edge(7, 2) and G.has_edge(0, 5)
    c8 = any(len(c) == 8 for c in nx.simple_cycles(G))
    assert c8
    print("H613f external L3 C8 PASS")

def test_triangle_samples():
    """Config-model cubic with triangle, no C4 ⇒ has C8 for n<=16."""
    rng = random.Random(42)
    seen = 0
    for n in [10, 12, 14, 16]:
        for trial in range(400):
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
            tris = any(len(c) == 3 for c in nx.simple_cycles(G))
            c4 = any(len(c) == 4 for c in nx.simple_cycles(G))
            if tris and not c4:
                p2 = find_p2(G)
                assert 8 in p2 or 16 in p2, (n, p2)
                seen += 1
                if seen >= 5:
                    break
        if seen >= 5:
            break
    assert seen >= 1, "no triangle C4-free cubic sample (rerun)"
    print(f"H612c triangle samples PASS (seen={seen})")

def test_known_cubics():
    for name, G in [
        ("petersen", nx.petersen_graph()),
        ("frucht", nx.frucht_graph()),
        ("Y5", nx.circular_ladder_graph(5)),
        ("Y7", nx.circular_ladder_graph(7)),
    ]:
        p2 = find_p2(G)
        assert p2 & {4, 8, 16, 32}, (name, p2)
        print(f"sanity {name} p2={p2} PASS")

if __name__ == "__main__":
    test_petersen_T_closed()
    test_external_L4_C8()
    test_external_L3_C8()
    test_triangle_samples()
    test_known_cubics()
    print("ALL Fire 35 tests PASS")
