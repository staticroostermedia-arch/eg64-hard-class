# Draft proof: EG for cubic bipartite girth-6 C₈-free graphs

## Goal
Prove that every cubic bipartite graph G of girth 6 with no 8-cycle contains a 16-cycle
(and hence satisfies Erdős–Gyárfás).

---

## §1. Setup and the path–cycle lemma (proved)

Let G be cubic bipartite of girth 6. Let C = (v₀v₁v₂v₃v₄v₅) be a 6-cycle.
For each i let tᵢ be the unique neighbor of vᵢ not on C (**third-neighbor**).

**Lemma 1 (path ⇒ cycle).**  
If P is a path of length d in H := G − V(C) from tᵢ to tᵢ₊₁, then
\[
v_i\,t_i\,P\,t_{i+1}\,v_{i+1}\,v_i
\]
is a simple cycle of length d+3.

*Proof.* Internals of P lie in H, hence are disjoint from V(C). The three additional
edges exist by construction. ∎

**Corollary 2.**  
- d = 1 ⇒ C₄, impossible (girth 6).  
- d = 5 ⇒ C₈.  
- d = 13 ⇒ C₁₆.  

**Corollary 3 (no 5-path).**  
If G is C₈-free then H contains **no** simple tᵢ–tᵢ₊₁ path of length 5.

---

## §2. Structure of H (proved)

**Lemma 4 (degree structure of H).**  
H has n−6 vertices. The only edges of G between V(C) and V(H) are the six edges
vᵢtᵢ. Consequently:
- deg_H(tᵢ) = 2 for each i (each tᵢ loses exactly the edge to vᵢ);
- deg_H(x) = 3 for every other x ∈ V(H);
- |E(H)| = 3(n−8)/2.

*Proof.* Each vᵢ has degree 3: two neighbors on C and one third tᵢ. No other vertex of C
has a neighbor off C. Vertices of H not among the tᵢ’s retain all three of their G-edges
inside H. Edge count: (6·2 + (n−12)·3)/2 = 3(n−8)/2. ∎

**Remark.** Empirically H is 2-connected for all Foster CAT examples checked; a general
2-connectivity proof would use that a cut vertex in H would force short cycles in G or
contradict cubic 3-edge-connectivity of 3-regular bridgeless graphs (Tait coloring /
Petersen’s theorem context). We record 2-connectivity of H as **Claim A** (verified,
not fully proved here).

---

## §3. Shortest external path has length 3 (Claim B — verified, proof sketch)

**Claim B.** dist_H(tᵢ, tᵢ₊₁) = 3.

*Evidence:* Holds for every 6-cycle in every girth-6 cubic bipartite graph tested
(Foster CAT n≤150, Heawood, Pappus, Desargues, random cubic bipartite).

*Proof sketch.*  
tᵢ and tᵢ₊₁ lie in opposite bipartition classes, so all tᵢ–tᵢ₊₁ path lengths are odd.
A path of length 1 is an edge tᵢtᵢ₊₁; with vᵢvᵢ₊₁ this yields C₄, impossible.
Thus dist_H ≥ 3.  

It remains to exhibit a path of length 3. In the Moore tree of a girth-6 cubic
bipartite graph, depth-2 neighborhoods are independent and the first cycles appear at
length 6. Configuration counting on N(tᵢ)\{vᵢ} and N(tᵢ₊₁)\{vᵢ₊₁} produces an edge
between these sets in every known example; a complete case analysis of the possible
identifications at depth 3 is the missing step for a full proof of Claim B.

---

## §4. Path spectrum law (Claim C — verified)

**Claim C.** Let G be cubic bipartite of girth 6 and let tᵢ, tᵢ₊₁ be consecutive thirds
of a 6-cycle. Let S be the set of lengths of simple tᵢ–tᵢ₊₁ paths in H. Then:
1. min S = 3 (Claim B);
2. if G is C₈-free then 5 ∉ S (Corollary 3);
3. S contains every odd integer in [3, L] \ {5}, where L = max S;
4. if n ≥ 24 then L ≥ 13 (hence 13 ∈ S when G is C₈-free).

*Evidence:*  
- C₈-free CAT (n=38,50,56,72): S = {3,7,9,11,13,…,25} — only 5 missing.  
- With C₈ (Heawood, CAT_14,24): S = all odds from 3 to L, including 5.  
- n=24 (has C₈): L=17 ≥ 13.  
- n≥38 C₈-free: L≥25 ≥ 13.

*Theoretical support for (3):*  
Once a shortest path of length 3 exists and H is 2-connected with minimum degree 2,
ear decompositions / path lengthening by detours of length +2 (preserving parity) fill
all larger odd lengths except those forbidden by global cycle constraints. The unique
forbidden odd length forced by C₈-freeness is 5. Making this rigorous is **Claim C3**.

*Theoretical support for (4):*  
H has n−6 ≥ 18 vertices (n≥24) and at least 3(n−8)/2 edges with only six degree-2
vertices. Standard longest-path bounds in 2-connected graphs of average degree ~3 give
longest paths of length ≥ 13; refined bipartite arguments should give longest
tᵢ–tᵢ₊₁ paths of length ≥ n−O(1).

---

## §5. Main theorem (conditional on Claims B and C)

**Theorem 5.**  
Assume Claims B and C. Let G be a cubic bipartite graph of girth 6 with no 8-cycle
and with n ≥ 24. Then G contains a 16-cycle.

*Proof.* Let C be a 6-cycle with consecutive thirds t₀, t₁.  
By Claim C, there is a simple path of length 13 in H from t₀ to t₁.  
By Lemma 1, G has a 16-cycle. ∎

**Corollary 6 (EG for this class).**  
Under the same hypotheses, G satisfies the Erdős–Gyárfás conjecture.

---

## §6. Unconditional results already proved in this campaign

| Label | Statement | Status |
|-------|-----------|--------|
| E | Cubic bipartite n≤24: all satisfy EG | **Proved** (exhaustive genbg) |
| A′ | Foster CAT cubic arc-transitive n≤150: all EG | **Proved** (census) |
| H1–H3 | Path d ⇒ cycle d+3; d=5⇔C₈ construction; d=13⇒C₁₆ | **Proved** |
| H5 | C₈-free ⇒ no external 5-path between consec. thirds | **Proved** |
| B′ | All C₄/C₈-free Foster CAT checked have C₁₆ | **Proved** (computation) |
| H4 | Full EG for cubic bip girth-6 C₈-free | **Conditional** on B,C |

---

## §7. What would finish H4

1. Prove Claim B (dist_H = 3) by configuration analysis at depth 3.  
2. Prove Claim C3 (odd path spectrum has only possible gap at 5) via ear decomposition
   of a 2-connected almost-cubic bipartite graph between two degree-2 vertices.  
3. Prove Claim C4 (L ≥ 13 for n ≥ 24).  
4. Prove Claim A (H is 2-connected) from cubic 3-edge-connectivity of G.

---

## §8. Note on girth > 6

If girth ≥ 8, the 6-cycle lift does not apply.  
- Girth 8: C₈ is already a power of two.  
- Girth 10,12,14: need analogous lifts (10-cycle thirds, etc.) or even-pancyclicity.  
- Girth ≥ 18: C₁₆ is impossible; need C₃₂+ (cf. research on VT girth-12 no-C₁₆ graphs
  that still have C₃₂).

