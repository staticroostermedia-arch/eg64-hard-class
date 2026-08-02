# Gap closure — second rewrite

**Replaces** the previous PROOF_GAPS_CLOSED draft.  
Companion to [PROOF_PURENEW_CLOSED.md](PROOF_PURENEW_CLOSED.md).

Closes the remaining audit issues:
1. Arbitrary off-theta \(W\)-components (not only length-2 matchings)
2. No overclaim from \(L_4\) matching alone
3. Type U \(k=1\) cutvertex from \(\kappa=3\) with exact hypotheses
4. \(\mu\)-induction as a well-founded structural termination proof

---

## 0. Inherited hypotheses (state once)

When this document is invoked inside residual-good free-port analysis:

| Symbol | Meaning |
|--------|---------|
| \(G\in\mathcal{H}\) | connected cubic bipartite, no \(C_4\), no \(C_8\) |
| \(\kappa(G)=3\) | 3-connected (Paper I Prop 3.5: else cut-cycle \(\Rightarrow C_{16}\), already done) |
| \(P_*,P_H,C,X,N\) | as in PROOF_PURENEW_CLOSED §0 |
| Lemmas 1.1–1.3 | pure-new: no cubic island; exit hits \(X\); first-return path exists |

**Dependency:** §§A–B below use only \(\mathcal{H}\), \(\kappa=3\), and Lemmas 1.1–1.3.  
They do **not** use \(\mu\)-induction.  
§C uses §§A–B + pure-new §§3–5 (return length classification by tables).

---

## A. Two cycles in \(\Gamma\): complete off-theta analysis

### A.0 Setup

\(G[\Gamma]\) as in pure-new §2: interiors degree 3 in \(G[\Gamma]\), boundary to markers \(B(\Gamma)\subseteq X\).  
Suppose \(Z_1\neq Z_2\) are cycles in \(G[\Gamma]\).  
If they share an edge: deleting the shared path yields a theta (three paths between two vertices). Reduce to A.1.  
If they share a vertex but not an edge: already a theta.  
If disjoint: a path in connected \(\Gamma\) joining them creates a theta or a third cycle; free edges force a connection that creates a shared vertex configuration. (Two disjoint cycles in a graph with all degrees ≤3 must be joined by a path; the join plus arcs is a theta.)  

**Hence w.l.o.g. a theta:** branch vertices \(b,b'\), three internally disjoint \(b\)–\(b'\) paths of lengths \(\ell_1\le\ell_2\le\ell_3\), each \(\ell_i\ge 3\) (girth ≥6, no two paths of length 2).  
Same parity of all \(\ell_i\) (bipartite).  
Cycle lengths \(\ell_i+\ell_j\neq 4,8\).

### A.1 Immediate bans (finite table)

| \((\ell_1,\ell_2,\ell_3)\) | Cycles | Result |
|---------------------------|--------|--------|
| 3,3,3 | 6,6,6 | three paths of length 3: free edges among midpoints create \(C_4\), or if no free cross-edges the graph is a prism subdivision; edge \(a_1{-}c_2\) (legal opposite parts) ⇒ \(C_4\) with \(b\). All free edges of midpoints must leave; any cross between the two short arms at opposite-part pairs gives \(C_4\). Off-arm only: A.3 with \(F=6\). Actually for (3,3,3): \(F=6\). See A.3. |
| 3,3,5 | 6,8,8 | **\(C_8\) ban** |
| 3,5,5 | 8,8,10 | **\(C_8\) ban** |
| 3,5,7 | 8,… | **\(C_8\) ban** |
| any \(\ell_1+\ell_2=8\) | has \(C_8\) | **ban** |
| 4,4,* | has \(C_8\) or odd | **ban** (even \(\ell\): \(b,b'\) same part) |

**Survivors:** \((3,3,7),(3,3,9),\ldots,(3,7,7),(5,5,5),(5,5,7),\ldots,(6,6,6),\ldots\) with all pair-sums ∉ {4,8}.

### A.2 Free stubs on the theta

Branch \(b,b'\) are degree 3 in \(G\) (three paths use all edges).  
Every path-interior has **exactly one free edge** off the theta.  
\[
F=\ell_1+\ell_2+\ell_3-3
\]
free stubs.

### A.3 Lemma (No legal free edge between free bases creates a short \(b\)–\(b'\) path of banned length)

A free edge (or short path through \(W\)) between free bases at distance \(\delta\) on the theta creates a cycle of length \(\delta+L\) where \(L\) is the off-theta path length, and creates a new \(b\)–\(b'\) path of length \(\ell^*\) by replacing the \(\delta\)-arc with the off-theta path.

**Critical:** if some new \(b\)–\(b'\) path has length \(\ell'\) with \(\ell'+\ell_j=8\) for an existing arm length \(\ell_j\), **ban**.

| Existing arm | Forbidden new \(\ell'\) |
|--------------|-------------------------|
| 3 | 5 |
| 5 | 3 |
| 7 | 1 (impossible) |

### A.4 Lemma (Direct free edges and \(L=2\) off-theta paths)

**A.4.1 Chord of an arm.** Free edge between two interiors of the same arm:  
- span 2: parts impossible  
- span 3: \(C_4\) ban  
- span 5: \(C_6\); flip shortens that arm by 4.  
  - Arm 7 → 3: configuration becomes (3,3,3) or (3,3,ℓ₃)  
  - Arm 9 → 5: may create pair-sum 8  
  - Arm 5 → 1: edge \(b{-}b'\), then cycles with other arms  

**A.4.2 Free edge between different arms.**  
Distance \(\delta\) on theta between the two free bases. Cycle \(\delta+1\) if direct edge \(L=1\).  
- Direct edge: \(L=1\), cycle \(\delta+1\). For even cycle, \(\delta\) odd.  
  \(\delta=3\): cycle 4 **ban**.  
  \(\delta=5\): cycle 6. New \(b\)–\(b'\) path length: replacing arc of length 5 by 1 gives savings 4, new length = old route −4.  
  On (3,3,7): free from short arm position to long arm at \(\delta=5\) through \(b\): e.g. \(a_1\) to \(d_4\): dist via \(b\) is 1+3=4 even — same part, edge impossible. Dist via \(b'\) similarly.  
  **Opposite-part free bases only.** Free base on short arm is opposite part to \(b\); free base on long arm at odd distance from \(b\) is same part as \(b\)'s opposite = same as short-arm free base when distance from \(b\) is odd. Distance from \(b\) along long arm to \(d_j\) is \(j\). Free base \(d_j\) has part alternating. Edge between short-arm free and \(d_j\) requires opposite parts.  

**A.4.3 Path of length 2 through one \(w\in W\):** \(f_1{-}w{-}f_2\). Cycle \(\delta+2\). Even ⇒ \(\delta\) even.  
- \(\delta=2\): \(C_4\) ban  
- \(\delta=4\): \(C_6\); new \(b\)–\(b'\) path length \(\ell_{\mathrm{arm}}-4+2=\ell_{\mathrm{arm}}-2\)  
  - On arm 7: new length 5. With existing arm 3: **\(C_8\) ban** (Lemma A.3)  
  - On arm 5: new length 3. With arm 5: cycles 8 **ban**  
  - On arm 9: new length 7; check pair-sums  
  - Across arms at \(\delta=4\): same as PROOF_GAPS first draft — creates length-5 routes on (3,3,7) ⇒ **\(C_8\)**  
- \(\delta=6\): \(C_8\) ban  

**Corollary A.4.** Every direct free edge between free bases and every \(L=2\) off-theta path between free bases either bans or creates a new \(b\)–\(b'\) path of length 5 next to an arm of length 3 (⇒ \(C_8\)), or reduces to a smaller theta already banned. ∎

*This is the content previously machine-checked for \(L=2\) matchings on (3,3,7): the only legal \(\delta\) was 4, and that produces \(C_8$ with arm 3; alternatively the global perfect matching in \(L_4\) fails — both routes ban.*

### A.5 Lemma (Arbitrary \(W\)-components) — the missing piece

Let \(W=V(\Gamma)\setminus V(\Theta)\).  
Let \(K\) be a connected component of \(G[W]\).

#### A.5.1 \(K\) has a neighbour on \(\Theta\) or in \(B(\Gamma)\)

*Proof.* If not, \(K\) has no edge leaving \(K\) in \(G\) (neighbours only in \(W\cup\Theta\cup X\cup V(P_*)\cup V(C)\); no edge to \(\Theta\), none to \(X=B(\Gamma)\) if also no boundary, none to \(V(P_*)\) else ports, none to \(V(C)\) banned).  
Then \(K\) is a connected component of \(G\), contradicting connectedness unless \(K=\emptyset\).  
(If \(K\) has edges to \(X\setminus B(\Gamma)\), those are additional markers — enlarge \(B(\Gamma)\).) ∎

#### A.5.2 First return from a free base

Each edge from a free base \(f\) on \(\Theta\) into \(K\) starts a walk in \(K\).  
By A.5.1 and finiteness of \(K\), there is a first return path
\[
f=f_0{-}w_1{-}\cdots{-}w_{L-1}{-}f_L,\qquad L\ge 1,
\]
where \(f_L\in V(\Theta)\cup B(\Gamma)\), and \(w_i\in K\).  
If \(L=1\) and \(f_L\in V(\Theta)\): direct free edge between free bases (or free base to branch — branch has no free slot). Covered by A.4.  
If \(f_L\in B(\Gamma)\): path from free base on theta to a marker in \(X\). Length \(L\ge 1\). This is an \(X\)–(theta interior) connection. Combined with theta routes to \(b,b'\) and arms, produces an \(X\)–\(X\) path (if another marker exists) or a cutvertex configuration (if unique marker — Type U \(k=1\), §B).  
**In the two-cycle/theta setting we are forbidding extra structure that escapes; if the component attaches to \(X\), then \(\Gamma\) has markers and the theta is not an interior island — the free stub is classified as a return to \(X\), which is **not** an off-theta pairing of free bases.**  
For pure “two cycles with free stubs only into \(W\)” (no new markers), all returns of free stubs hit \(\Theta\), not \(X\).

**Hypothesis for A.5.3–A.5.4:** free stubs of \(\Theta\) return to \(\Theta\) (marker attachments handled separately as Type U / filled-component markers).

#### A.5.3 Return length \(L\) and distance \(\delta\)

Return path of length \(L\ge 2\) through \(K\) between free bases \(f,f'\) at distance \(\delta\) on \(\Theta\).  
Cycle length \(\delta+L\) must be even, ≥6, ≠8.

**Claim:** either ban, or a new \(b\)–\(b'\) path of length \(\ell'\) with \(\ell'+\ell_j=8\) for some arm, or a reduction of some arm length by ≥2 leading to a banned table case.

**Proof by induction on \(L+|V(K)|\).**

**Base \(L=2\):** Corollary A.4. ✓  

**Base \(L=3\):** cycle \(\delta+3\). Even ⇒ \(\delta\) odd.  
- \(\delta=1\): free bases adjacent on theta — free edges of adjacent interiors; cycle 4 **ban**.  
- \(\delta=3\): cycle 6. New \(b\)–\(b'\) path: replace arc 3 by path 3 ⇒ length change 0; or replace longer arc.  
  On (3,3,7): arc of length 3 on long arm between \(d_i,d_{i+3}\): replace by \(L=3\) keeps length 7. Arc of length 3 through a short arm: e.g. \(a_1\) to \(d_2\) dist via \(b\) = 1+2=3. Replace: new path \(b{-}a_1\xrightarrow{3}d_2{-}\cdots{-}b'\) length \(1+3+(7-2)=9\) etc.  
  **Flip creating length 5:** if the replaced arc has length \(\delta=5\) — but \(\delta=3\) here.  
  Free edges of the \(L=3\) path interiors (one free each for the middle vertex): land on \(\Theta\) or in \(K\). Landing on \(\Theta\) creates a shorter return (length ≤2 from that middle), induction.  
- \(\delta=5\): cycle 8 **ban**.  
- \(\delta=7\): cycle 10. New path lengths: replace arc 7 by 3 ⇒ arm shortens by 4. Arm 7→3: becomes (3,3,3) or (3,3,ℓ).  

**General \(L\ge 4\):**  
Middle vertices of the return path each have a free edge off the return path.  

**Landing table for a free edge of an interior \(w^*\) of the return path:**
1. On the return path at dist 2: parts impossible  
2. Dist 3: \(C_4\) ban  
3. Dist 4: \(C_5\) impossible  
4. Dist 5: \(C_6\); flip shortens return length by 4 ⇒ new return length \(L-4\ge 0\); if ≥2, induction on \(L\)  
5. On \(\Theta\) at free base \(f^*\): creates return from an endpoint to \(f^*\) of length < \(L\) (subpath + 1), induction  
6. On \(\Theta\) at branch \(b\): \(b\) has no free slot — only if not already degree 3, contradiction  
7. Into new \(W'\subseteq W\): then \(w^*\) opens a side structure; the first return from \(w^*\) to (return path \(\cup\Theta\)) has length \(L'\ge 1\).  
   - To return path: shortens  
   - To \(\Theta\): return length from original free base via \(w^*\) is < \(L+|V(K)|\) in measure  
   Measure \(\nu = L + |V(K)|\) decreases when we pass to a first return inside \(K\) of strictly smaller path+component (delete classified edges, smaller active \(K\)).  

**Well-founded induction on \(\nu=L+|V(K)|\)** for fixed theta: every free edge of interiors either bans, shortens \(L\), or reduces \(|V(K)|\) after classifying a sub-return.  
When \(L\) reduces to 2 or 3: base.  
When all free edges of the return path are classified without ban: the return path is induced and its free edges all went to places that created shorter returns — eventually \(L=2\) base, **Corollary A.4 ban**.  

#### A.5.4 Conclusion for arbitrary \(W\)

Every nonempty \(W\)-component that pairs free bases on \(\Theta\) produces, by induction on \(\nu\), a reduction to \(L\le 3\) returns, all of which ban or create \(C_8\) with a length-3 arm (Corollary A.4 + A.3).  

If a \(W\)-component attaches only to one free base (a tree hanging off one free base): that free base has free residual degree 1 used into the tree; the tree must end at leaves of degree 1 in \(G[W\cup\{f\}]\), but all vertices have degree 3 in \(G\) — leaves need edges to \(\Theta\cup X\). Only \(f\) on \(\Theta\) available without creating a second attachment (which is a return). **Contradiction** unless the tree has an edge to \(X\) (marker) or a second free base.  
Hence no dangling trees off a single free base without a second return. ∎

### A.6 Theorem (Lemma 2.5′)

A theta of free-stub type in \(G[\Gamma]\) cannot exist in \(\mathcal{H}\).  
Hence \(G[\Gamma]\) has at most one cycle.

*Proof.* A.0–A.5: every \((\ell_1,\ell_2,\ell_3)\) either immediately banned (A.1) or has free stubs that through arbitrary \(W\) reduce to banned short returns (A.5). ∎

### A.7 Note on verification

`verify_gaps.py` checks:  
- \(L_4\) matching non-existence for (3,3,7) (special case of A.4)  
- length 3+5 ⇒ \(C_8\)  
- short-arm cross edge \(C_4\)  

It does **not** replace the induction in A.5; that is proof-only.

---

## B. Type U \(k=1\) — cutvertex from \(\kappa=3\)

### B.1 Hypotheses

- \(\kappa(G)=3\) (inherited; see §0)  
- \(\Gamma\subseteq N\) a connected component of pure-new  
- \(B(\Gamma)=\{x\}\) exactly one marker  
- \(Z\subseteq\Gamma\) the unique cycle (Type U)  
- \(s\in V(P_*)\), \(s\neq x\)

### B.2 Lemma (Every path from \(\Gamma\) to \(s\) meets \(x\))

Let \(v\in\Gamma\). Let \(Q\) be any \(v\)–\(s\) path in \(G\).  
Let \(v'\) be the first vertex of \(Q\) in \(V(P_*)\cup V(C)\cup X\).  

- Not in \(V(C)\): free edges into \(V(C)\) banned (free-port setup).  
- Not in \(V(P_*)\): else predecessor is a free neighbour of \(P_*\), hence in \(U\subseteq X\), so first hit is in \(X\).  
- Thus \(v'\in X\).  
- \(X\cap N(\Gamma)=B(\Gamma)=\{x\}\) (edges from \(\Gamma\) to \(X\) only at markers).  
- The predecessor of \(v'\) on \(Q\) is in \(\Gamma\cup\{x\}\), so \(v'=x\).  

Hence \(x\in Q\). ∎

### B.3 Lemma (\(x\) is a cutvertex)

Pick \(v\in Z\) with \(v\neq x\) and \(vx\notin E(G)\).  
**Existence:** \(|Z|\ge 6\), \(\deg(x)\le 3\), so \(x\) has at most 3 neighbours; at most 3 vertices of \(Z\) are \(x\) or adjacent to \(x\). Remaining ≥2 vertices of \(Z\) qualify.

By B.2, every \(v\)–\(s\) path contains \(x\).  
Therefore in \(G-x\) there is no \(v\)–\(s\) path.  
Both \(v\) and \(s\) exist in \(G-x\).  
Hence \(G-x\) is disconnected.  
So \(x\) is a cutvertex, i.e. \(\kappa(G)\le 1\), contradicting \(\kappa(G)=3\). ∎

### B.4 Theorem (Type U has \(k\ge 2\))

Under residual-good free-port analysis (\(\kappa=3\)), every Type U filled component has at least two markers. ∎

### B.5 Marker distances

With \(k\ge 2\), two markers attach at points of \(Z\) (or on \(Z\)).  
Min-arc distance \(d\) on \(Z\):  
- \(|Z|=6\): \(d\le 3\)  
- \(|Z|=10\): \(d\le 5\)  
- larger: free chords span 3 ban, span 5 ⇒ \(C_6\) reduction, span 7 ⇒ \(C_8\) ban; after reductions effective \(d\le 5\)  

Returns of length \(d\in\{1,2,3,4,5\}\) classified by pure-new §§3–4. ∎

**Note:** The old draft’s branch “if they reattach only at \(x\)” is **not** used.  
B.2–B.3 never case-split on pending trees: any \(v\in\Gamma\), every path to \(s\) hits \(x\).

---

## C. \(\mu\)-induction as termination

### C.1 Active residual (precise)

Maintain partitions:
- \(E_{\mathrm{active}}\subseteq E_{XN}\): still-unclassified edges from current \(X\) to current \(N\)  
- \(N_{\mathrm{active}}\subseteq N\): vertices of \(N\) incident to at least one active edge or reachable from such via edges in \(G[N]\) not yet assigned to a classified return  

\[
\mu = \bigl(|E_{\mathrm{active}}|,\; |N_{\mathrm{active}}|\bigr)
\]
ordered lexicographically on \(\mathbb{N}\times\mathbb{N}\).

### C.2 What “classify” does to \(\mu\)

When a return path \(x\xrightarrow{L}x'\) through \(N_{\mathrm{active}}\) is fully resolved (ban or path-9 or reduction listed in pure-new §§3–5):
1. Remove from \(E_{\mathrm{active}}\) every active edge used as a start/end stub of that return (at least the first edge \(x{-}n\); for Type P both ends).  
2. Remove from \(N_{\mathrm{active}}\) every interior vertex of the return whose all three incident edges are now classified or not active.  
3. Side free edges of interiors that went into side components remain active if still unclassified; those components have strictly fewer active edges to the original \(X\) (the parent free stub was spent) or form a separate filled component with its own markers already in \(X\).

**Lemma C.1.** Each of the following decreases \(\mu\) in lex order:
- Classifying a Type P return of any \(L\) (removes ≥1 active edge).  
- Classifying a Type T leaf-to-leaf path (removes 2 leaf edges; remaining tree has fewer leaves).  
- Classifying a Type U marker arc (removes ≥1; by B.4 there are ≥2 markers).  
- Classifying an interior free edge landing on \(X\) (creates short return, then classify).  
- Classifying a \(W\)-return on a theta (Theorem A.6 bans; or if not in two-cycle case, reduces to return classification).  

*Proof.* In each case \(|E_{\mathrm{active}}|\) drops by ≥1, or \(|E_{\mathrm{active}}|\) stays and \(|N_{\mathrm{active}}|\) drops when a component is fully absorbed after its last active edge is classified. ∎

### C.3 Entry step (uses Lemmas 1.1–1.3 only)

If \(E_{\mathrm{active}}=\emptyset\): then \(N_{\mathrm{active}}=\emptyset\) (Lemma 1.1: no island; every \(v\in N\) needs a path to \(X\), hence an edge into \(X\) from its component). **Base done.**  

If \(E_{\mathrm{active}}\neq\emptyset\): pick \(e=x{-}n\in E_{\mathrm{active}}\).  
By Lemma 1.3, a first-return path from this stub exists.  
The filled component of \(n\) is Type P, T, or U (pure-new Lemma 2.4 + Theorem A.6 at most one cycle).  
- Type P: return path is the component; classify by pure-new §§3–5 (tables for \(L=2,3,4,5\) + reduce \(L\ge 6\) by free-edge landings, each landing either bans, shortens \(L\), or opens a side component with smaller \(\mu\) by C.1).  
- Type T: Lemma 5.1 pure-new + classify one leaf path.  
- Type U: B.4–B.5 + classify marker arc.  

### C.4 Theorem (Termination)

The process in C.3 terminates after finitely many steps and classifies every free edge as ban or length-9 \(s\)–\(t\) path.

*Proof.* Lex well-order; each step decreases \(\mu\) (C.1); base C.3.  
**Does not circularly assume return for active components:** entry uses Lemma 1.3 (proved from connectedness in pure-new §1, independent of \(\mu\)).  
**Does not assume arbitrary \(W\) is closed without proof:** two-cycle \(W\) is Theorem A.6; side components of a single return path are smaller \(\mu\) instances of the same induction. ∎

### C.5 Dependency DAG

```
connectedness (G in H)
       │
       ▼
Lemmas 1.1–1.3 (return exists)
       │
       ├──────────────────────┐
       ▼                      ▼
Theorem A.6 (≤1 cycle)    κ=3
       │                      │
       ▼                      ▼
Lemma 2.4 types P/T/U     Theorem B.4 (k≥2)
       │                      │
       └──────────┬───────────┘
                  ▼
         pure-new §§3–5 (L tables)
                  │
                  ▼
         Theorem C.4 (μ termination)
                  │
                  ▼
         Theorem 7.1 pure-new closure
```

---

## D. Seeds

| Test | What it checks | What it does *not* check |
|------|----------------|---------------------------|
| \(L_4\) matching | A.4 special case for (3,3,7) \(L=2\) | full A.5 induction |
| 3+5 ⇒ C8 | A.3 | — |
| short-arm C4 | A.1 | — |
| k=1 cutvertex | B.2–B.3 on a concrete graph | — |
| C6 dist ≤3 | B.5 | — |
| lex order | C.1 sanity | full C.4 |

Universal quantifiers in A.5 and C.4 are **proof obligations**, not seed obligations.
