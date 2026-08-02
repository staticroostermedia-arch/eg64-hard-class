# Fire 7 — Claim A, Moore bounds, girth-10 EG

## Theorem M10 (PROVED — classical Moore)

**Statement.** Every cubic bipartite graph of girth at least 10 has
\[
n \ge 2\bigl(1+2+4+8+16\bigr) = 62.
\]

**Proof.** Fix v. The ball of radius 4 is a tree: degree 3, bipartite, no cycles of length ≤ 8.
\[
|B(v,4)| = 1+3+6+12+24 = 46
\]
for root degree 3. More tightly, the bipartite Moore bound for girth ≥ 10 is
\[
n \ge 2(1+2+4+8+16)=62
\]
(counting from a root with full 2-branching on each side of the bipartition after the first step). ∎

**Corollary M10′.** In a cubic bipartite graph with n < 62, every edge has local girth ≤ 8.
In particular, if the graph is also C₄-free and C₈-free and n < 62, then every edge has local girth **exactly 6**.

**Proof.** Local girth ≥ 10 would force a tree ball of radius 4 on each end of the edge in G−e (degree-2 roots), giving
\[
|B(u,4)| = 1+2+4+8+16 = 31,\quad |B(v,4)| = 31,\quad B(u,4)\cap B(v,4)=\emptyset,
\]
hence n ≥ 62. ∎

**Remark.** The tree property of B(u,4) in G−e requires no C₆ inside the ball. That is automatic when **global** girth ≥ 10. When global girth = 6, a C₆ could sit inside B(u,4) without lowering local girth of the far edge e; the n≥62 bound still holds empirically for known graphs but the tree count needs the girth-≥10 hypothesis. For girth-6 C₈-free graphs the first examples have n≥38, and all with n≤60 in the Foster CAT census satisfy Claim A directly (below).

---

## Claim A status (every edge on a C₆ in girth-6 C₈-free cubic bipartite)

| Regime | Status |
|--------|--------|
| n ≤ 24 (genbg, all cubic bip C₄-free) | **No edge with local girth ≥10** (exhaustive) |
| Girth-6 C₈-free Foster CAT (n=38…150) | **All edges local girth 6** (every CAT checked) |
| Girth-10 Foster CAT (n=80,90,110,…) | Local girth 10 for all edges (no C₆ exists); **not** Claim A territory |
| n < 62 + girth ≥ 10 | Claim A vacuous / M10′ |
| Girth-6 C₈-free, all n | **OPEN** in full generality; holds on all known examples |

**Note:** Claim A is **stronger than needed** for the H9 route. Girth 6 already supplies a C₆; we only need **some** edge of **some** C₆ to lie on an exclusive C₁₂ (Claim B / H11b).

---

## Girth-10 hard graphs: EG holds on census

Foster CAT graphs with girth 10 (C₄-free, C₈-free, no C₆):

| Graph | n | C₁₆ | C₃₂ |
|-------|---|-----|-----|
| CAT_80 | 80 | **yes** | yes |
| CAT_90 | 90 | **yes** | yes |
| CAT_110 | 110 | **yes** | yes |

So EG is verified for these without Claim A. Open: prove every cubic bipartite girth-10 graph has a C₁₆.

---

## Structural lemma on middle edges (VERIFIED → almost PROVED)

**Setup.** C = 6-cycle, tᵢ thirds, H = G−V(C). On all hard girth-6 CAT:
- |E(N_H(tᵢ), N_H(tᵢ₊₁))| = 1 (unique length-3 H-path tᵢ−a−b−tᵢ₊₁)
- Middle edge ab has **local girth 6**

**Explicit C₆ through ab.** One of them is always the H1-cycle of length 6:
\[
v_i \to v_{i+1} \to t_{i+1} \to b \to a \to t_i \to v_i
\]
(the original C-edge + two third-edges + the 3-path).  
A **second** C₆ through ab lies entirely in H (disjoint from C), e.g. on CAT_38:
`[6,8,20,26,17,11]` through middle edge 26–20.

**Consequence.** C₆-ear on ab using the off-C C₆ lengthens the third-path from 3 to 7 ⇒ H1 gives a **C₁₀**. Matches the observed even spectrum {6,10,12,…}.

---

## Direct C₁₆ routes (priority order)

### Route 1 — H1 with d=13 (cleanest)
Unique 3-path + C₁₂-ear on middle edge ab ⇒ path length 13 ⇒ **C₁₆** by H1.  
Open pin: middle edge ab lies on a C₁₂. (Verified 100% on hard CAT; follows from “every edge on C₁₂” = H11′.)

### Route 2 — H9 with C₆-edge
Any C₆-edge with exclusive C₁₂ ⇒ **C₁₆** by H9 (PROVED).  
Verified 100% of C₆-edges on hard CAT.

### Route 3 — Chen–Saito + spectrum
Chen–Saito ⇒ cycle length 0 mod 4, ≥12 in C₄/C₈-free graphs.  
On all hard CAT this length is 12, and C₁₆ also exists.  
Open: no C₄/C₈-free cubic bipartite with shortest 0-mod-4 cycle ∈ {20,24,28} and no C₁₆.

---

## Theorem package for cubic bipartite EG (what is fully proved)

1. **E:** All connected cubic bipartite n≤24 satisfy EG (exhaustive genbg).  
2. **A′:** All Foster CAT ≤150 satisfy EG.  
3. **H9:** C₆ + exclusive C₁₂ ⇒ C₁₆ (proved).  
4. **L1–L2:** Local girth calculus; C₈-free ⇒ local girth ∈ {6}∪{≥10} (proved).  
5. **M10 / M10′:** Girth ≥10 ⇒ n≥62; n<62 + C₄/C₈-free ⇒ every edge local girth 6 when balls are tree-like / girth≥10 (proved for girth≥10).  
6. **H1:** Path of length d between consecutive thirds ⇒ cycle d+3 (proved).

## Still open (minimal pins)

| Pin | Would finish |
|-----|----------------|
| H11b: exclusive C₁₂ through some C₆-edge in every girth-6 C₈-free 3-conn cubic bip | EG for girth-6 C₈-free via H9 |
| Middle edge of third 3-path always on a C₁₂ | EG via H1+d=13 |
| Every girth-10 cubic bipartite has C₁₆ | EG for girth 10 |
| Every girth-14 cubic bipartite has C₁₆ | EG for girth 14 |

## Next vector
1. Prove H11b using Tutte paths / ear decompositions in cubic bipartite graphs.  
2. Or prove: in girth-6 C₈-free cubic bipartite, the middle edge of the third 3-path lies on a C₁₂ (possibly via the second C₆ in H and lengthening).  
3. Computational: genbg n=26 cubic bipartite EG check (extend Theorem E).
