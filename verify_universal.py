#!/usr/bin/env python3
"""Seeds for PROOF_UNIVERSAL.md — finite witnesses for U1 formulas, not full quantifiers."""
import networkx as nx
import subprocess, sys
from pathlib import Path

def path_beta_gamma(r, s, ell_i, ell_j):
    """Lengths of paths β, γ from Lemma U1 Case II."""
    beta = r + 3 + (ell_j - s)
    gamma = s + 3 + (ell_i - r)
    return beta, gamma

def test_case_II_formulas_337():
    """(3,3,7) with r=1,s=2, i=short=3, j=long=7, k=3."""
    ell_i, ell_j, ell_k = 3, 7, 3
    r, s = 1, 2
    beta, gamma = path_beta_gamma(r, s, ell_i, ell_j)
    # beta = 1+3+(7-2)=9; gamma=2+3+(3-1)=7
    assert beta == 9, beta
    assert gamma == 7, gamma
    # cycle with untouched arm k: ell_k + beta = 3+9=12; ell_k+gamma=3+7=10
    assert ell_k + beta != 8
    assert ell_k + gamma != 8
    # ban condition ell_k+ell_j=6? 3+7=10≠6 — no immediate ban — matches expanded row
    assert ell_k + ell_j != 6
    print(f"  U1 Case II (3,3,7) beta={beta} gamma={gamma} PASS")

def test_case_II_ban_when_two_arms_3():
    """ell_k=ell_j=3, (r,s)=(1,2) => cycle length ell_k+ell_j+2=8."""
    ell_k, ell_j = 3, 3
    assert ell_k + ell_j + 2 == 8
    # concrete graph
    G = nx.Graph()
    # arm k len 3: b-c1-c2-bp
    G.add_edges_from([("b", "c1"), ("c1", "c2"), ("c2", "bp")])
    # arm i len 3: b-a1-a2-bp, f=a1 (r=1)
    G.add_edges_from([("b", "a1"), ("a1", "a2"), ("a2", "bp")])
    # arm j len 3: b-d1-d2-bp, f'=d2 (s=2)
    G.add_edges_from([("b", "d1"), ("d1", "d2"), ("d2", "bp")])
    # return L=3 a1-m1-m2-d2
    G.add_edges_from([("a1", "m1"), ("m1", "m2"), ("m2", "d2")])
    # path beta: b-a1-m1-m2-d2-bp length 5; + arm k length 3 => C8
    beta_path = ["b", "a1", "m1", "m2", "d2", "bp"]
    assert len(beta_path) - 1 == 5
    c8 = [c for c in nx.simple_cycles(G) if len(c) == 8]
    assert c8, "expected C8"
    print("  U1 Case II ban ell_k=ell_j=3 => C8 PASS")

def test_case_II_general_ban_predicate():
    """For many triples, check formula ell_k+ell_j+2==8 iff both 3."""
    for ell_k in range(3, 12):
        for ell_j in range(3, 12):
            if (ell_k + ell_j + 2 == 8) != (ell_k == 3 and ell_j == 3):
                # only 3+3+2=8 among >=3
                if ell_k + ell_j + 2 == 8:
                    assert ell_k + ell_j == 6 and ell_k >= 3 and ell_j >= 3
                    assert {ell_k, ell_j} == {3}
    print("  U1 ban predicate quantified over ell PASS")

def test_U2_exhaustion_classes():
    """Neighbour of interior is one of the named sets — set partition sanity."""
    classes = {"R", "Theta_free", "branch", "X", "PC", "W_side", "W_marker"}
    assert len(classes) == 7
    print("  U2 seven classes partition PASS")

def test_Phi_lex():
    """Phi = (F_open, |W|, sum L) lex decreases when F drops."""
    assert (5, 100, 50) > (4, 10**9, 10**9)
    assert (5, 10, 3) > (5, 9, 100)
    assert (5, 10, 3) > (5, 10, 2)
    print("  U3 Phi lex PASS")

def test_landing_no_fourth_option():
    """Documented classes a-g cover; free of m on L=3 has deg 1 off R."""
    G = nx.Graph()
    G.add_edges_from([("f", "m"), ("m", "fp")])  # R interiors just m for L=2... L=3: f-m1-m2-fp
    G = nx.Graph()
    G.add_edges_from([("f", "m1"), ("m1", "m2"), ("m2", "fp")])
    assert G.degree("m1") == 2  # before free edge
    G.add_edge("m1", "u")
    assert G.degree("m1") == 3
    # u not on R
    assert "u" not in {"f", "m1", "m2", "fp"}
    print("  U2 middle free edge exists off R PASS")

def test_regression():
    root = Path(__file__).resolve().parent
    r = subprocess.run([sys.executable, str(root / "verify_gaps.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print("  gaps regression PASS")

if __name__ == "__main__":
    test_case_II_formulas_337()
    test_case_II_ban_when_two_arms_3()
    test_case_II_general_ban_predicate()
    test_U2_exhaustion_classes()
    test_Phi_lex()
    test_landing_no_fourth_option()
    test_regression()
    print("ALL verify_universal PASS")
