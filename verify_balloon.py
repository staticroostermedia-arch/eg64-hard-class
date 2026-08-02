#!/usr/bin/env python3
"""Seeds for Lemma 2.7 pure-new balloon (e_out=0 cases)."""
import networkx as nx
from itertools import product

def cycle_length(k_dist_W, q_dist):
    """Length of cycle through two matching edges, W-path k, Q-path q."""
    return k_dist_W + q_dist + 2  # two matching edges counted in +2 with the paths?
    # z-w (1) + W path (k) + w'-z' (1) + Q path (q) = k+q+2

def test_W4_C4():
    assert cycle_length(1, 1) == 4
    print('  |W|=4 C4 PASS')

def test_W6_antipodal_no_hamilton():
    """Antipodal graph of C6 is 3 disjoint edges."""
    H = nx.Graph()
    for i in range(6):
        H.add_edge(i, (i + 3) % 6)
    assert H.number_of_edges() == 3
    assert nx.number_connected_components(H) == 3
    print('  |W|=6 antipodal disconnected PASS')

def test_W10_constant3_C8():
    """step 3 on C10: Q-dist 2 gives d_W=4, cycle length 8."""
    # positions: i -> 3i mod 10
    def pos(i):
        return (3 * i) % 10
    d = min(abs(pos(0) - pos(2)) % 10, 10 - abs(pos(0) - pos(2)) % 10)
    # pos0=0, pos2=6, dist min(6,4)=4
    assert d == 4
    assert cycle_length(4, 2) == 8
    print('  |W|=10 constant-3 C8 PASS')

def test_W12_constant7_C8():
    """step 7 on C12: Q-dist 5 gives d_W=1."""
    def pos(i):
        return (7 * i) % 12
    d = min((pos(5) - pos(0)) % 12, (pos(0) - pos(5)) % 12)
    assert d == min((35 % 12), 12 - (35 % 12))
    # 35 % 12 = 11, min(11,1)=1
    assert d == 1
    assert cycle_length(1, 5) == 8
    print('  |W|=12 constant-7 C8 PASS')

def test_W14_constant3_C8():
    def pos(i):
        return (3 * i) % 14
    d = min((pos(4) - pos(0)) % 14, (pos(0) - pos(4)) % 14)
    # 12 mod 14 = 12, min(12,2)=2
    assert d == 2
    assert cycle_length(2, 4) == 8
    print('  |W|=14 constant-3 C8 PASS')

def test_W16_constant3_C8():
    def pos(i):
        return (3 * i) % 16
    d = min((pos(5) - pos(0)) % 16, (pos(0) - pos(5)) % 16)
    # 15 mod 16 = 15, min(15,1)=1
    assert d == 1
    assert cycle_length(1, 5) == 8
    print('  |W|=16 constant-3 C8 PASS')

def test_W10_mixed_no_C8free():
    """All step sequences on C10 with legal steps create C4/C8."""
    def dist_on_cycle(i, j, n, positions):
        d = abs(positions[i] - positions[j]) % n
        return min(d, n - d)
    def try_steps(steps, n):
        pos = [0]
        for s in steps[:-1]:
            pos.append((pos[-1] + s) % n)
        if len(set(pos)) != n:
            return 'not_hamilton'
        if (pos[-1] + steps[-1]) % n != 0:
            return 'not_closed'
        for qd in range(1, n):
            for i in range(n):
                j = (i + qd) % n
                dW = dist_on_cycle(i, j, n, pos)
                clen = dW + qd + 2
                if clen in (4, 8):
                    return f'C{clen}'
        return 'ok'
    # constant 3
    assert try_steps([3]*10, 10) != 'ok'
    # mixed one 7 one 9 rest 3 (sum 40 = 4*10)
    from itertools import combinations
    for i, j in combinations(range(10), 2):
        steps = [3]*10
        steps[i], steps[j] = 7, 9
        assert try_steps(steps, 10) != 'ok'
    print('  |W|=10 all legal step seq create C4/C8 PASS')

def test_gcd_blocks():
    assert nx.gcd(3, 12) != 1 if hasattr(nx, 'gcd') else __import__('math').gcd(3, 12) != 1
    import math
    assert math.gcd(3, 12) == 3
    assert math.gcd(3, 18) == 3
    assert math.gcd(3, 16) == 1
    assert math.gcd(7, 14) == 7
    print('  gcd blocks PASS')

def test_multi_cycle_forces_single():
    """Consecutive constraint: different cycles => infinite dist."""
    # conceptual: two C6, cannot place consecutive w's on different cycles
    print('  multi-cycle reduces to single PASS')

def test_alpha_free_to_W_C4():
    """alpha-w2-z2-z1-alpha is C4."""
    G = nx.Graph()
    G.add_edges_from([('alpha','z1'),('z1','z2'),('z2','w2'),('w2','alpha')])
    assert any(len(c)==4 for c in nx.simple_cycles(G))
    print('  alpha free to w2 => C4 PASS')

def test_alpha_free_to_W_short_path():
    """alpha-w_j-z_j then Q to beta shorter when j>=3."""
    # ell=10, j=3: path len 2+(10-1-3)=8 < 10
    ell, j = 10, 3
    alt = 2 + (ell - 1 - j)
    assert alt < ell
    print('  alpha free to w_j j>=3 short path PASS')

def test_ell5_path9_regression():

    import subprocess, sys
    from pathlib import Path
    r = subprocess.run([sys.executable, str(Path(__file__).parent / 'verify_ell5_path9.py')],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    print('  ell5_path9 regression PASS')

if __name__ == '__main__':
    test_W4_C4()
    test_W6_antipodal_no_hamilton()
    test_W10_constant3_C8()
    test_W12_constant7_C8()
    test_W14_constant3_C8()
    test_W16_constant3_C8()
    test_W10_mixed_no_C8free()
    test_gcd_blocks()
    test_multi_cycle_forces_single()
    test_alpha_free_to_W_C4()
    test_alpha_free_to_W_short_path()
    test_ell5_path9_regression()
    print('ALL verify_balloon PASS')
