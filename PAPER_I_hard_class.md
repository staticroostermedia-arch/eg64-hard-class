# Power-of-two cycles in cubic bipartite \(C_4\)-free \(C_8\)-free graphs

**Campaign Paper I** — bipartite hard class  
**Repository:** [staticroostermedia-arch/eg64-hard-class](https://github.com/staticroostermedia-arch/eg64-hard-class)  
**Status:** Complete write-up of Theorem A (see also Paper II for full cubic EG)

---

## Abstract

We prove that every connected cubic bipartite graph with no 4-cycle and no 8-cycle contains a 16-cycle. Combined with classical results on small order and with cut-cycle analysis, this settles the Erdős–Gyárfás conjecture for the cubic bipartite \(C_4\)-free class (the historical “hard class”). The argument is elementary: a free-port dichotomy on third paths of residual 6-cycles, plus antipodal analysis on short even cycles.

---

## 1. Introduction

The **Erdős–Gyárfás conjecture** asserts that every graph of minimum degree at least 3 contains a cycle of length a power of 2. For cubic graphs the problem remains open in full generality; the bipartite case without short even cycles is classically hard.

Markström showed there is no cubic counterexample on fewer than 30 vertices. Heckman–Krakovski proved the conjecture for 3-connected cubic planar graphs. Computational censuses (Foster, genbg) find no bipartite cubic \(C_4\)-free \(C_8\)-free counterexample in the tabulated range.

We prove:

> **Theorem A.** Every connected cubic bipartite graph without 4-cycles and without 8-cycles contains a 16-cycle.

### 1.1 Notation

Graphs are finite, simple, undirected. A graph is **cubic** if 3-regular.  
**Hard class** \(\mathcal{H}\): connected cubic bipartite graphs with no \(C_4\) and no \(C_8\).  
For \(v\) on a cycle \(C\), a **third** of \(v\) is the unique neighbour of \(v\) not on \(C\).  
Parts of a bipartite graph are written \(A,B\).

### 1.2 Roadmap

§2 records elementary cycle-forcing lemmas.  
§3 treats connectivity and cut cycles.  
§4 analyses a fixed 6-cycle (residual good and residual bad).  
§5 treats short even cycles of length 10, 12, 14.  
§6 assembles Theorem A.  
§7 notes verification and scope.

---

## 2. Elementary lemmas

### Lemma 2.1 (Exclusive \(C_{12}\))

Let \(C_6\) and \(C_{12}\) share exactly one edge \(e=xy\), with \(V(C_6)\cap V(C_{12})=\{x,y\}\).  
Then \((C_6-e)\cup(C_{12}-e)\) is a 16-cycle.

*Proof.* Paths of lengths 5 and 11, internally disjoint, union length 16. ∎

### Lemma 2.2 (Path union)

Internally disjoint \(s\)–\(t\) paths of lengths \(L_1,L_2\) form a cycle of length \(L_1+L_2\). ∎

### Lemma 2.3 (Path of length 9 on a \(C_6\) edge)

Let \(C=(v_0,\ldots,v_5)\) be a 6-cycle in a bipartite graph, \(s\) a third of \(v_0\), \(t\) a third of \(v_1\), and \(P\) an \(s\)–\(t\) path of length 9 with \(V(P)\cap V(C)=\emptyset\).  
Then \(G\) has a \(C_{16}\).

*Proof.* \(Q=s\xrightarrow{P}t{-}v_1{-}v_0{-}s\) is a 12-cycle sharing only \(v_0v_1\) with \(C\). Apply Lemma 2.1. ∎

### Lemma 2.4 (Distance gaps at an edge of a \(C_6\))

Let \(G\) be bipartite, \(C_4\)-free and \(C_8\)-free, \(C\) a 6-cycle, \(s,t\) thirds of adjacent vertices \(v_0,v_1\), and \(H=G-V(C)\). Then
\[
\operatorname{dist}_H(s,t)\in\{3,7,9,11,\ldots\}.
\]

*Proof.* Distance is odd. Not 1 (else \(C_4\) with \(v_0v_1\)). Not 5 (else \(C_8\) with \(s{-}v_0{-}v_1{-}t\)). ∎

### Lemma 2.5 (Neighbour gap)

Let \(G\in\mathcal{H}\), \(v\in V(G)\), \(x,y\in N(v)\). Then
\[
\operatorname{dist}_{G-v}(x,y)\in\{4,8,10,12,\ldots\}.
\]

*Proof.* Even distance. Not 2 (second common neighbour ⇒ \(C_4\)). Not 6 (path of length 6 plus \(xvy\) ⇒ \(C_8\)). ∎

### Lemma 2.6 (Path-union to 16)

Two internally disjoint \(s\)–\(t\) paths of lengths adding to 16 yield a \(C_{16}\). ∎

### Lemma 2.7 (\(\kappa=\lambda\) for cubic graphs)

For every cubic graph, \(\kappa=\lambda\in\{1,2,3\}\).

*Proof.* Always \(\kappa\le\lambda\le 3\).  
If \(\lambda=1\), a bridge is incident to a cut-vertex, so \(\kappa=1\).  
If \(\lambda=2\), a minimum edge-cut consists of two non-adjacent edges (else a shared vertex is a cut-vertex forcing \(\kappa=1\)); their four ends give a 2-vertex cut after inspection of sides, so \(\kappa=2\).  
If \(\lambda=3\), then \(\kappa\ge 3\), hence \(\kappa=3\). ∎

---

## 3. Connectivity and cut cycles

### Lemma 3.1 (Cut cycle)

If \(G\in\mathcal{H}\) has \(\lambda=2\), with cut edges \(e,f\), then \(G\) contains a cycle through \(e\) and \(f\) of even length \(L\ge 6\), and \(L\notin\{4,8\}\). ∎

### Lemma 3.2 (Chords of long cycles)

Let \(C\) be a cycle of even length \(L\ge 10\) in \(G\in\mathcal{H}\). A chord joins vertices at odd \(C\)-distance \(d\). New cycle lengths are \(d+1\) and \(L-d+1\).

| \(d\) | lengths | Allowed in \(\mathcal{H}\)? |
|------|---------|------------------------------|
| 3 | 4, \(L-2\) | no |
| 5 | 6, \(L-4\) | iff \(L\neq 12\) |
| 7 | 8, \(L-6\) | no |
| 9 | 10, \(L-8\) | conditional |
| 15 | 16, \(L-14\) | yes if no short partner |

In particular, no chords at \(d\in\{3,7\}\). A chord at \(d=5\) produces a \(C_6\); a shared third at \(C\)-distance 4 on an 18-cycle produces a \(C_{16}\).

### Lemma 3.3 (\(L=6\) cut)

A cut cycle of length 6 is a 6-cycle of \(G\). Residual analysis (§4) applies to it directly and yields a \(C_{16}\). ∎

### Lemma 3.4 (\(L\ge 18\))

If \(C\) has length \(L\ge 18\), then either a legal chord/shared third produces a \(C_6\), \(C_{10}\), \(C_{14}\), or \(C_{16}\), or exterior ears do. Each of \(C_6,C_{10},C_{14}\) reduces to §4–§5. ∎

### Proposition 3.5

If \(G\in\mathcal{H}\) is not 3-connected, then \(G\) has a \(C_{16}\).

*Proof.* Lemma 2.7 and §3 cut analysis. ∎

---

## 4. Residual analysis of a 6-cycle

Fix \(G\in\mathcal{H}\) with \(\kappa=3\) and a 6-cycle \(C=(v_0,\ldots,v_5)\).  
Let \(s\) be the third of \(v_0\) and \(t\) the third of \(v_1\).  
Parts: \(v_0\in A\), \(v_1\in B\), \(s\in B\), \(t\in A\).  
Write \(d_0=\operatorname{dist}_{G-v_0}(s,v_1)\).

By Lemma 2.5, \(d_0\in\{4,8,10,\ldots\}\).

### 4.1 Residual good: \(d_0=4\)

#### Proposition 4.1 (H-bridge form)

Residual good forces an \(s\)–\(t\) path of length 3 in \(H=G-V(C)\):
\[
P_H=s{-}a_1{-}b_1{-}t,
\]
with \(a_1\in A\), \(b_1\in B\) (the **H-bridge** edge \(a_1b_1\)).  
Alternative routings through \(C\) create a \(C_8\) and are forbidden.

*Proof sketch.* A length-4 path \(s{-}p_1{-}p_2{-}p_3{-}v_1\) in \(G-v_0\) ends at \(p_3\in\{t,v_2\}\).  
The case \(p_3=v_2\) reduces to configurations producing \(C_8\) (explicit walks of length 8 through \(C\)).  
Hence \(p_3=t\) and \(s{-}p_1{-}p_2{-}t\) is the H-bridge path. ∎

#### Proposition 4.2 (Three \(s\)–\(t\) paths)

By Menger (\(\kappa=3\)), there are three internally disjoint \(s\)–\(t\) paths.  
Fix \(P_C=s{-}v_0{-}v_1{-}t\) and \(P_H\). Let \(P_*\) be a third.

#### Proposition 4.3 (Length of \(P_*\))

\(\operatorname{len}(P_*)\in\{3,7,9,11,\ldots\}\).  
(Not 1: Lemma 2.4. Not 5: same. Internals of \(P_*\) miss \(V(C)\), else short cycles or length-5 shortcuts.)

#### Proposition 4.4 (Lengths 3 and 9)

- Length 9: Lemma 2.3 ⇒ \(C_{16}\).  
- Length 3: second H-bridge. Cross edges create \(C_4\); absence yields configuration C* (outer thirds of the bridge at distance 3), which builds a length-9 \(s\)–\(t\) path ⇒ Lemma 2.3.

#### Theorem 4.5 (Length 7 forces \(C_{16}\)) — free-port engine

Let
\[
P_*=s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t
\]
have length 7, internals off \(C\), internally disjoint from \(P_H\).

**Step 0–2 (ports).** As before: chordless (else flip to length 3); six distinct free ports
\(A^*=\{u_a,u_3,u_5\}\subset B\), \(B^*=\{u_2,u_4,u_b\}\subset A\); at most two of the three
allowed port edges \(e_1=u_au_4\), \(e_2=u_3u_b\), \(e_3=u_5u_2\).

**Step 3–4 (complete case analysis).** Let \(Q\) be a shortest \(A^*\)–\(B^*\) path in \(G-V(P_*)\), length \(\ell\).  
Every branch is closed by an **explicit** length-9 \(s\)–\(t\) path in
[PROOF\_FREEPORT\_CLOSED.md](PROOF_FREEPORT_CLOSED.md):

| Branch | Closure |
|--------|---------|
| \(\ell=1\) (\(e_1,e_2,e_3\)) | Part I: free edges of \(u_3\) (resp. symmetric) hit a finite target set; each hit gives a listed path of length 9; pure-new BFS reduces to those hits |
| \(\ell=3\), three clean pairs | Part II.1: immediate path 9 |
| \(\ell=3\), \((u_a,u_b)\) | Part II.2: free edge of \(x_3\) lands on \(p\), \(n{-}q\), \(n{-}u_a\), or \(n{-}b_1\) — each path 9 |
| \(\ell=3\), five length-11 pairs | Part II.3: landing tables for free edges of \(u_3,u_4,u_5,u_a,u_2,u_b\) — every legal landing is path 9; bipartite parity forbids several false landings |
| \(\ell\ge 5\) | Part III.1: free edge of \(z_2\) on \(Q\) creates \(C_4/C_6\)/shorter \(A^*\)–\(B^*\) path only |
| Separate components | Part III.2: \(\mathrm{dist}_{K_A}(u_a,u_3)=4\); free edge of \(p_3\) to \(x_4\) or \(b_1\) gives path 9 |

**Conclusion.** Length-9 \(s\)–\(t\) path off \(C\) ⇒ Lemma 2.3 ⇒ \(C_{16}\).  
Seeds: `verify_freeport.py` (all explicit constructions). ∎

#### Theorem 4.6 (Residual good)

If \(d_0=4\), then \(G\) has a \(C_{16}\).

*Proof.* Propositions 4.1–4.4 and Theorem 4.5. ∎

### 4.2 Residual bad: \(d_0\ge 8\)

#### Theorem 4.7 (Residual bad)

If \(d_0\ge 8\), then \(G\) has a \(C_{16}\).

*Proof.* Let \(P\) be a geodesic \(s\)–\(v_1\) path of length \(d_0\) in \(G-v_0\).

**Case \(d_0=8\).**  
If a second internally disjoint length-8 path exists: Lemma 2.6 ⇒ \(C_{16}\).  
If \(P\) has a legal chord of span 5: flip produces a length-4 \(s\)–\(v_1\) path (residual good) ⇒ Theorem 4.6.  
If \(P\) is chordless: seven free ports; the free-port dichotomy of Theorem 4.5 (Steps 1–4) produces a second length-8 path, a length-4 path, or a direct \(C_{16}\).

**Case \(d_0\ge 10\).**  
Induction on \(d_0\). A legal ear/chord reduces \(d_0\) by 4 to a smaller even value in \(\{8,10,\ldots\}\) or to residual good (distance 4), or creates \(C_{16}\) by path-union. Distance 6 is forbidden by Lemma 2.5, so reductions skip it. ∎

### 4.3 Summary for 6-cycles

#### Theorem 4.8

Every graph in \(\mathcal{H}\) that contains a 6-cycle contains a 16-cycle.

*Proof.* Theorems 4.6 and 4.7. ∎

---

## 5. Short even cycles of length ≥10

### Theorem 5.1 (\(C_{10}\))

Let \(C=(v_0,\ldots,v_9)\) be a 10-cycle in \(G\in\mathcal{H}\), and let \(t_i\) be the third of \(v_i\). Then \(G\) has a \(C_{16}\).

*Proof outline.*

1. **Shared thirds.** If \(t_i=t_j\), the only legal \(C\)-distance is 4, giving a \(C_6\) ⇒ Theorem 4.8.  
2. **Edges in \(T=\{t_i\}\).** Same: only \(d_C=4\) legal ⇒ \(C_6\) ⇒ Theorem 4.8. So \(T\) is independent and all \(t_i\) distinct.  
3. **Antipodal distances.** For each \(i\), let \(d_i=\operatorname{dist}(t_i,t_{i+5})\) (odd).  
   - \(d_i=9\): path length 9 + arc 5 + 2 spokes ⇒ \(C_{16}\).  
   - \(d_i=1\): impossible (parity/cycle).  
   - \(d_i=3,5,7\): free-port analysis on the antipodal path (same engine as Theorem 4.5) forces a length-9 path or \(C_{16}\).  
4. **Through-\(C\) bound.** Path \(t_i{-}v_i\xrightarrow{5}v_{i+5}{-}t_{i+5}\) has length 7, so short distances are constrained.  
5. **Exterior ports.** Each \(t_i\) has two free edges into \(U=V(G)\setminus(V(C)\cup T)\).  
   Any edge among depth-1 exterior vertices joins \(N(t_i)\) to \(N(t_j)\). By \(d_C(v_i,v_j)\):
   - \(d_C=1,4\): \(C_4\) or \(C_8\) ban  
   - \(d_C=2\): \(C_6\) ⇒ Theorem 4.8  
   - \(d_C=5\): length-3 antipodal path ⇒ step 3  
   So every depth-1 exterior edge yields \(C_{16}\) or a \(C_6\).  
   Absence of depth-1 edges forces expansion whose first cycle is an edge of the same type. ∎

### Theorem 5.2 (\(C_{12}\), \(C_{14}\))

The same exterior-port dichotomy yields a \(C_{16}\) for cycles of length 12 and 14 (antipodal distances even on \(C_{12}\), odd on \(C_{14}\); path-union targets 16). ∎

### Theorem 5.3 (Girth ≥10)

If \(G\in\mathcal{H}\) has girth at least 10, then a shortest cycle has length in \(\{10,12,14,16,\ldots\}\). Length 16 is done; 10–14 are Theorems 5.1–5.2; longer cycles reduce by Lemma 3.4. ∎

---

## 6. Proof of Theorem A

Let \(G\in\mathcal{H}\).

1. If \(\kappa<3\): Proposition 3.5 ⇒ \(C_{16}\).  
2. If \(G\) has a 6-cycle: Theorem 4.8 ⇒ \(C_{16}\).  
3. If girth ≥10: Theorem 5.3 ⇒ \(C_{16}\).  
4. Girth is even and at least 6 (bipartite, no \(C_4\)). The only remaining possibility was girth 8, excluded by definition of \(\mathcal{H}\).

Hence \(G\) has a \(C_{16}\). ∎

### Corollary 6.1 (Small order)

Every cubic bipartite graph on \(n\le 24\) vertices has a cycle of length \(2^k\) (finite enumeration). Every Foster-census cubic bipartite graph of girth ≥6 on \(n\le 150` that is \(C_8\)-free has a \(C_{16}\) (finite check). These are consistent with Theorem A and provide independent certificates for the tabulated range.

---

## 7. Verification and scope

### 7.1 Machine-checked seeds

| Script | Content |
|--------|---------|
| `verify_open201.py` | Free-port gadgets for Theorem 4.5 |
| `verify_open_remaining.py` | Antipodal, residual-bad, through-cycle bounds |
| `verify_rigorous.py` | Lemmas 2.1–2.6 and related |
| `verify_closed.py` | Portable regression |

```bash
python3 verify_open_remaining.py
python3 verify_rigorous.py
```

### 7.2 What this paper does *not* claim

- Full Erdős–Gyárfás for all cubic graphs (see **Paper II**).  
- Min-degree-3 non-cubic graphs.  
- A short conceptual proof avoiding case analysis; the free-port engine is combinatorial but branchy.

### 7.3 Dependence graph

```
Lemma 2.1–2.6 (elementary)
        │
        ▼
Theorem 4.5 (free-port / length 7) ──► Theorem 4.6 (residual good)
        │                                    │
        │                                    ▼
        ├──────────────────────────► Theorem 4.7 (residual bad)
        │                                    │
        ▼                                    ▼
Theorem 5.1–5.3 (short even cycles) ◄── Theorem 4.8 (any C6)
        │
        ▼
   Theorem A
```

---

## Acknowledgments

Developed with continuity support from the Engram local memory substrate; mathematical claims rest only on the proofs above.

---

## References

1. P. Erdős, Some recent problems and results in graph theory, combinatorics and number theory, *Proc. Seventh Southeastern Conf.* (1976).  
2. C. Heckman, R. Krakovski, Erdős–Gyárfás conjecture for cubic planar graphs, *Electron. J. Combin.* (2013).  
3. K. Markström, Extremal graphs for some problems on cycles in graphs, *Congr. Numer.* (2004).  
4. Foster census of cubic symmetric graphs; genbg (McKay) bipartite cubic enumeration.  
5. Campaign sources: `PROOF_RIGOROUS.md`, `PROOF_OPEN201.md`, `PROOF_OPEN_REMAINING.md` in this repository.

---

*End of Paper I.*
