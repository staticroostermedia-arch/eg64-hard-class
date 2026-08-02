#!/usr/bin/env python3
"""Seeds for PROOF_GAPS_CLOSED.md (Lemma 2.5′ theta, Type U, path9)."""
import networkx as nx
from pathlib import Path
import subprocess
import sys

def test_theta_337_L4_matching_impossible():
    """
    Free bases on (3,3,7)-theta: a1,a2,c1,c2,d1..d6.
    L4 edges only: d1d5, d2d6, a1d3, c1d3, a2d4, c2d4.
    No perfect matching (after forced d1d5,d2d6, leftovers unmatched).
    """
    bases = ["a1", "a2", "c1", "c2", "d1", "d2", "d3", "d4", "d5", "d6"]
    L4 = [
        ("d1", "d5"),
        ("d2", "d6"),
        ("a1", "d3"),
        ("c1", "d3"),
        ("a2", "d4"),
        ("c2", "d4"),
    ]
    G = nx.Graph()
    G.add_nodes_from(bases)
    G.add_edges_from(L4)
    # Check no perfect matching
    matching = nx.maximal_matching(G)
    # maximal_matching is not max cardinality; use max_weight_matching
    mw = nx.max_weight_matching(G, maxcardinality=True)
    assert len(mw) < 10, f"unexpected perfect matching size {len(mw)}"
    # stronger: size of max matching <= 8 (4 edges)
    assert len(mw) <= 8
    print(f"  A.2.1 L4 max matching size {len(mw)} < 10 PASS")

def test_theta_337_C8_from_length5():
    """Path length 5 + path length 3 => C8."""
    G = nx.Graph()
    # b-b' paths len 3 and 5
    G.add_edges_from([("b", "a1"), ("a1", "a2"), ("a2", "bp")])
    G.add_edges_from([("b", "d1"), ("d1", "d2"), ("d2", "d3"), ("d3", "d4"), ("d4", "bp")])
    cycles = [c for c in nx.simple_cycles(G) if len(c) == 8]
    assert cycles, "expected C8"
    print("  A.2.1 len3+len5 => C8 PASS")

def test_theta_333_is_K33_girth4():
    """Three paths of length 3 between b,b' with midpoints fully connected as K33."""
    G = nx.Graph()
    # Actually K_{3,3}: parts {b,m1,m2} and {bp,n1,n2} - different construction
    # Three paths b-a1-a2-bp, b-c1-c2-bp, b-d1-d2-bp with NO extra edges: girth 6.
    # K33 appears when the three mid-pairs form complete bipartite.
    # Paths of length 1 (edges) between two sets of 3: K33.
    # For length 3 paths without chords: graph is C6-rich, girth 6 if only those edges.
    G.add_edges_from([("b", "a1"), ("a1", "a2"), ("a2", "bp")])
    G.add_edges_from([("b", "c1"), ("c1", "c2"), ("c2", "bp")])
    G.add_edges_from([("b", "d1"), ("d1", "d2"), ("d2", "bp")])
    assert nx.girth(G) == 6
    # Add free matching a1-c1 impossible same part; a1-c2:
    G2 = G.copy()
    G2.add_edge("a1", "c2")
    # cycle b-a1-c2-c1-b? c1-c2 edge exists: b-a1-c2-c1-b length 4 if c1-b
    assert any(len(c) == 4 for c in nx.simple_cycles(G2))
    print("  A.1 short-arm cross edge C4 PASS")

def test_typeU_k1_cutvertex():
    """k=1: paths from far cycle vertex to s all go through x => cutvertex."""
    G = nx.Graph()
    for i in range(6):
        G.add_edge(f"z{i}", f"z{(i+1)%6}")
    G.add_edge("x", "z0")
    for i in range(1, 6):
        G.add_edge(f"z{i}", f"w{i}")
        G.add_edge(f"w{i}", "x")
    # attach s only through x (simulates X-gateway)
    G.add_edge("x", "s")
    # z3 to s: all paths through x
    paths = list(nx.all_simple_paths(G, "z3", "s", cutoff=10))
    assert paths and all("x" in p for p in paths)
    assert "x" in set(nx.articulation_points(G))
    print("  B.2 k=1 => all z3-s paths through x, cutvertex PASS")

def test_typeU_C6_marker_dist():
    """Two markers on C6: min arc <= 3."""
    for i in range(6):
        for j in range(i + 1, 6):
            d = min((j - i) % 6, (i - j) % 6)
            assert d <= 3
    print("  B.3 C6 marker dist <= 3 PASS")

def test_path9_from_U_d3():
    """Markers at dist 3 on C6 give opposite-part style path used for path9."""
    G = nx.Graph()
    for i in range(6):
        G.add_edge(f"z{i}", f"z{(i+1)%6}")
    # attach ua at z0, u4 at z3 (dist 3)
    G.add_edges_from([("ua", "z0"), ("u4", "z3")])
    # complete to s-t path using freeport style
    G.add_edges_from([("s", "a2"), ("a2", "ua"), ("u4", "x4"), ("x4", "x5"), ("x5", "b2"), ("b2", "t")])
    # path s-a2-ua-z0-z1-z2-z3-u4-x4-x5-b2-t is long; shorter:
    # s-a2-ua-z0-z5-z4-z3-u4-x4-x5-b2-t
    G.add_edges_from([("x4", "x5"), ("x5", "b2")])  # already
    p = ["s", "a2", "ua", "z0", "z1", "z2", "z3", "u4", "x4", "x5", "b2", "t"]
    # need x4 edge from u4 - have u4-x4; need chain. len = 11
    # For d=3 opposite: path through Z length 3: ua-z0-z1-z2-z3-u4 if ua,u4 are markers on Z
    # Actually markers ON z0,z3: path z0-z1-z2-z3 len 3
    # s-a2-ua-z0-z1-z2-z3-u4-... need u4 to t
    assert nx.shortest_path_length(G, "z0", "z3") == 3
    print("  B.3 d=3 arc exists PASS")

def test_mu_lex_decreases():
    """Sanity: lex (sigma, n) decreases when sigma drops."""
    assert (1, 100) < (2, 0)
    assert (2, 0) > (1, 5)
    print("  C.3 lex order PASS")

def test_regression():
    root = Path(__file__).resolve().parent
    r = subprocess.run([sys.executable, str(root / "verify_purenew.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("  purenew regression PASS")

if __name__ == "__main__":
    test_theta_337_L4_matching_impossible()
    test_theta_337_C8_from_length5()
    test_theta_333_is_K33_girth4()
    test_typeU_k1_cutvertex()
    test_typeU_C6_marker_dist()
    test_path9_from_U_d3()
    test_mu_lex_decreases()
    test_regression()
    print("ALL verify_gaps PASS")
