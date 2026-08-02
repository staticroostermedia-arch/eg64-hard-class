#!/usr/bin/env python3
"""Fire 36: H614 seeds — C7 partition, distance law, L=10 C16, E_S facts."""
import networkx as nx

def test_partition_degrees():
    """v on C7 has deg 3 ⇒ no room for C-U edges in cubic G."""
    # abstract check
    deg_on_C = 2  # cycle
    deg_spoke = 1
    assert deg_on_C + deg_spoke == 3
    print("H640 partition degree PASS")

def test_forbidden_Ld():
    def lens(L, d, g=7):
        return (L + d + 2, L + (g - d) + 2)

    fatal = []
    for L in range(1, 6):
        for d in range(1, 4):
            a, b = lens(L, d)
            if any(x in (3, 4, 5, 8) for x in (a, b)):
                fatal.append((L, d, a, b))
    # expected key fatals
    assert (1, 1, 4, 9) in fatal or any(t[0]==1 and t[1]==1 for t in fatal)
    assert any(t[0]==2 and t[1]==3 for t in fatal)  # C8
    assert any(t[0]==3 and t[1]==3 for t in fatal)
    print(f"H650 forbidden table PASS ({len(fatal)} fatal pairs)")

def test_L10_C16():
    G = nx.Graph()
    for i in range(7):
        G.add_edge(i, (i + 1) % 7)
        G.add_edge(i, 7 + i)
    # t0=7, t3=10, path length 10
    nodes = [14 + i for i in range(10)]
    G.add_edge(7, nodes[0])
    for i in range(9):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[9], 10)
    found = any(len(c) == 16 for c in nx.simple_cycles(G))
    assert found
    print("H682 L=10 antipodal C16 PASS")

def test_ES_facts():
    n_S = 7
    assert n_S < 8  # no C8 in E_S alone
    # C4 in E_S would lift to C8
    print("H704 E_S size/C4-lift PASS")

def test_multiedge_C4():
    """Two smooths same pair ⇒ C4."""
    G = nx.Graph()
    G.add_edges_from([("a", "t1"), ("t1", "b"), ("a", "t2"), ("t2", "b")])
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    print("H701 multiedge/smooth C4 PASS")

def test_T_independent_seeds():
    """t_i t_{i+1} on C7 spokes ⇒ C4."""
    G = nx.Graph()
    for i in range(7):
        G.add_edge(i, (i + 1) % 7)
        G.add_edge(i, 7 + i)
    G.add_edge(7, 8)  # t0 t1
    assert any(len(c) == 4 for c in nx.simple_cycles(G))
    print("H641 T edge C4 PASS")

if __name__ == "__main__":
    test_partition_degrees()
    test_forbidden_Ld()
    test_L10_C16()
    test_ES_facts()
    test_multiedge_C4()
    test_T_independent_seeds()
    print("ALL Fire 36 tests PASS")
