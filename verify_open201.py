#!/usr/bin/env python3
"""Seeds for PROOF_OPEN201.md constructions."""
import networkx as nx

def test_chord_flip_len7_to_len3():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edge("a2", "b2")  # legal chord span 5
    assert any(len(c) == 6 for c in nx.simple_cycles(G))
    assert nx.shortest_path_length(G, "s", "t") == 3
    print("Step0 chord flip PASS")

def test_shared_port_a2_x5_len5():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edges_from([("a2","w"),("x5","w")])
    assert nx.shortest_path_length(G, "s", "t") == 5
    print("Step1.3 shared a2,x5 => len5 PASS")

def test_x3_b1_len5():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edges_from([("s","a1"),("a1","b1"),("b1","t"),("x3","b1")])
    paths = list(nx.all_simple_paths(G, "s", "t", cutoff=5))
    assert any(len(p)-1 == 5 for p in paths), paths
    print("Step1.2 x3-b1 path len5 exists PASS")

def test_ell3_ua_u4_path9():
    G = nx.Graph()
    # P*
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    # ports
    G.add_edges_from([("a2","ua"),("x4","u4")])
    # length-3 A*-B* path ua-p-q-u4
    G.add_edges_from([("ua","p"),("p","q"),("q","u4")])
    assert nx.shortest_path_length(G, "s", "t") <= 9
    p9 = ["s","a2","ua","p","q","u4","x4","x5","b2","t"]
    for i in range(len(p9)-1):
        assert G.has_edge(p9[i], p9[i+1]), (p9[i], p9[i+1])
    assert len(p9)-1 == 9
    print("Step3.2 (ua,u4) path9 PASS")

def test_ell3_u3_ub_path9():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edges_from([("x3","u3"),("b2","ub"),("u3","p"),("p","q"),("q","ub")])
    p9 = ["s","a2","x2","x3","u3","p","q","ub","b2","t"]
    for i in range(len(p9)-1):
        assert G.has_edge(p9[i], p9[i+1])
    assert len(p9)-1 == 9
    print("Step3.2 (u3,ub) path9 PASS")

def test_ell3_u5_u2_path9():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edges_from([("x5","u5"),("x2","u2"),("u5","p"),("p","q"),("q","u2")])
    p9 = ["s","a2","x2","u2","q","p","u5","x5","b2","t"]
    for i in range(len(p9)-1):
        assert G.has_edge(p9[i], p9[i+1])
    assert len(p9)-1 == 9
    print("Step3.2 (u5,u2) path9 PASS")

def test_path9_gives_C16():
    G = nx.Graph()
    for i in range(6):
        G.add_edge(f"v{i}", f"v{(i+1)%6}")
    G.add_edge("v0", "s")
    G.add_edge("v1", "t")
    nodes = [f"h{i}" for i in range(8)]
    G.add_edge("s", nodes[0])
    for i in range(7):
        G.add_edge(nodes[i], nodes[i+1])
    G.add_edge(nodes[7], "t")
    assert any(len(c) == 16 for c in nx.simple_cycles(G))
    print("Thm3 path9=>C16 PASS")

def test_three_allowed_edges_C8():
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    # ports and three allowed edges
    G.add_edges_from([("a2","ua"),("x4","u4"),("ua","u4")])  # e1
    G.add_edges_from([("x3","u3"),("b2","ub"),("u3","ub")])  # e2
    G.add_edges_from([("x5","u5"),("x2","u2"),("u5","u2")])  # e3
    # cycle a2-ua-u4-x4-x5-u5-u2-x2-a2
    cyc = ["a2","ua","u4","x4","x5","u5","u2","x2"]
    for i in range(len(cyc)):
        assert G.has_edge(cyc[i], cyc[(i+1)%len(cyc)])
    assert any(len(c) == 8 for c in nx.simple_cycles(G))
    print("Step2.1 three edges C8 PASS")

def test_KA_dist4_path11():
    """dist(ua,u3)=4 gives path of length 11 s-t."""
    G = nx.Graph()
    edges = [("s","a2"),("a2","x2"),("x2","x3"),("x3","x4"),("x4","x5"),("x5","b2"),("b2","t")]
    G.add_edges_from(edges)
    G.add_edges_from([("a2","ua"),("x3","u3")])
    G.add_edges_from([("ua","p1"),("p1","p2"),("p2","p3"),("p3","u3")])
    p11 = ["s","a2","ua","p1","p2","p3","u3","x3","x4","x5","b2","t"]
    for i in range(len(p11)-1):
        assert G.has_edge(p11[i], p11[i+1])
    assert len(p11)-1 == 11
    # upgrade via p3-x4
    G.add_edge("p3", "x4")
    p9 = ["s","a2","ua","p1","p2","p3","x4","x5","b2","t"]
    for i in range(len(p9)-1):
        assert G.has_edge(p9[i], p9[i+1])
    assert len(p9)-1 == 9
    print("Step4.2 KA dist4 => path9 PASS")

if __name__ == "__main__":
    test_chord_flip_len7_to_len3()
    test_shared_port_a2_x5_len5()
    test_x3_b1_len5()
    test_ell3_ua_u4_path9()
    test_ell3_u3_ub_path9()
    test_ell3_u5_u2_path9()
    test_path9_gives_C16()
    test_three_allowed_edges_C8()
    test_KA_dist4_path11()
    print("ALL verify_open201 PASS")
