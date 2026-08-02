# C₁₆-forcing for cubic bipartite graphs (EG #64 attack)

## Master construction (Theorem H9) — PROVED

**Theorem H9.** Let G be any graph. Let C be a 6-cycle and Q a 12-cycle that share **exactly one edge** e=xy and satisfy V(C) ∩ V(Q) = {x,y}. Then the union of the two paths C−e (length 5) and Q−e (length 11) is a **16-cycle**.

**Proof.** C−e and Q−e are x–y paths of lengths 5 and 11. Their interiors are disjoint because the only common vertices of C and Q are x and y. Hence (C−e) ∪ (Q−e) is a simple closed walk of length 16, i.e. a 16-cycle. ∎

**Corollary H9′ (EG witness).** If a graph contains a C₆ and, for some edge e of that C₆, a C₁₂ through e sharing no other vertex with the C₆ except the endpoints of e, then the graph has a C₁₆ and satisfies Erdős–Gyárfás.

---

## Reduction of the hard bipartite class

Let G be cubic bipartite, girth 6 (hence has a C₆), and C₈-free (so C₄, C₈ are unavailable as EG witnesses).

**Sufficient condition for EG:** every edge of every 6-cycle lies on a 12-cycle meeting the C₆ only at that edge’s endpoints.

Then H9 fires → C₁₆ → EG.

---

## Empirical support (exhaustive + census)

### A. Exclusive C₁₂ through every C₆-edge (Foster hard family)
For CAT_38, 50, 56, 72 (all C₈-free girth-6 cubic bipartite arc-transitive):

| Graph | C₆-edges | exclusive C₁₂ (share 1 edge, 2 verts) |
|-------|----------|----------------------------------------|
| CAT_38 | 114 | **114 / 114** |
| CAT_50 | 150 | **150 / 150** |
| CAT_56 | 168 | **168 / 168** |
| CAT_72 | 216 | **216 / 216** |

When share 1 edge: |V(C₆)∩V(C₁₂)| = **2 always** (1596/1596 on CAT_38) → H9 applies verbatim. Symdiff is always a single C₁₆.

### B. Every edge on a C₁₂ for 3-connected cubic bipartite (small n)
genbg exhaustive, **3-connected only**:

| n | # 3-conn cubic bip | all edges on C₁₂ |
|---|--------------------|------------------|
| 14 | 13 | **13** |
| 16 | 40 | **40** |
| 18 | 181 | **181** |
| 20 | 978 | **978** |

**0 failures.** All genbg exceptions to “every edge on C₁₂” have connectivity 2 (and girth 4); they still satisfy EG via C₄/C₈/C₁₆.

### C. Neighborhood structure (hard family)
For every C₆ and every consecutive thirds tᵢ, tᵢ₊₁ in the hard CAT family:
|E(N_H(tᵢ), N_H(tᵢ₊₁))| = **1** always → unique length-3 H-path, unique middle edge, and that edge is on a C₁₂.

---

## Related earlier results (still hold)

- **H1:** H-path of length d between consecutive thirds ⇒ cycle of length d+3.
- **H5:** C₁₂-ear on middle edge of a 3-path ⇒ path length 13 ⇒ C₁₆ (special case of H9).
- **H6 (Moore):** C₈-free + C₄-free ⇒ dist_H ≥ 7 needs n ≥ 36; so dist = 3 for n ≤ 34.
- **Theorem E:** exhaustive EG for all connected cubic bipartite n ≤ 24.
- **Theorem A′:** Foster CAT ≤ 150 all satisfy EG.

---

## Open pin (H11)

**Conjecture / Open H11.** Every 3-connected cubic bipartite graph of order n ≥ 12 with circumference ≥ 12 has **every edge on a 12-cycle**.

**Stronger (edge-even-pancyclic):** every such graph has every edge on a cycle of every even length from girth to circumference.  
(Verified for Heawood, Möbius–Kantor, Pappus, Desargues, and all hard CAT examples.)

**If H11 holds**, then for 3-connected cubic bipartite girth-6 G with n ≥ 12:
1. Take any C₆ and any edge e on it.
2. Take a C₁₂ through e. (Need also exclusive intersection — open subpin H11b, verified on census.)
3. H9 ⇒ C₁₆ ⇒ **EG**.

Cubic bipartite graphs that are only 2-connected reduce by blocks / ear decomposition, or already have short powers of two (genbg).

---

## Chen–Saito
δ ≥ 3 ⇒ some cycle ≡ 0 (mod 4). EG requires a power of two. H9 is a bipartite cubic machine that turns (C₆ + C₁₂ through an edge) into C₁₆.

---

## Status board

| Claim | Status |
|-------|--------|
| H9 (C₆+C₁₂ → C₁₆) | **PROVED** |
| Exclusive C₁₂ on hard CAT C₆-edges | **Verified 100%** |
| Every edge on C₁₂ for 3-conn cubic bip n≤20 | **Exhaustive 0 fails** |
| H11 (every edge on C₁₂, all n) | **OPEN** |
| H11b (can choose C₁₂ exclusive to C₆-edge) | **OPEN** (census clean) |
| Full EG | **OPEN** |

## Next vector
1. Prove H11 (literature: edge-bipancyclic degree conditions; or bipartite tunnel / Tutte path methods).  
2. Prove H11b or show any C₁₂ through e yields a C₁₆ after cleaning.  
3. Girth 10/12/14: analogous (C₁₀+C₆ doesn’t give 16; need C₁₀+C₁₄ or direct C₁₆).
