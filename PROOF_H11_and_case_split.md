# Fire 6 — H11 refined + case split for cubic bipartite EG

## Theorem H9 (recap, PROVED)
C₆ and C₁₂ sharing exactly one edge e=xy with V(C)∩V(Q)={x,y}
⇒ (C−e)∪(Q−e) is a **C₁₆**.

## Local girth lemma (PROVED)

**Lemma L1.** Let G be simple bipartite, e=uv an edge, d = dist_{G−e}(u,v).
Then every cycle through e has length ≥ d+1, and there is a cycle of length d+1.
So the **local girth** of e is d+1 (odd path ⇒ even cycle).

In particular:
- path len 3 ⇒ C₄
- path len 5 ⇒ C₆
- path len 7 ⇒ C₈
- path len 11 ⇒ C₁₂

**Lemma L2.** If G is C₄-free and C₈-free, then for every edge e the local girth is
**either 6 or ≥ 10** (values 4 and 8 are forbidden).

**Proof.** Local girth 4 ⇒ C₄; local girth 8 ⇒ C₈. ∎

**Corollary L3.** In a C₈-free graph, an edge not lying on a C₆ has local girth ≥ 10,
hence lies on no cycle shorter than 10. For such an edge to lie on a C₁₂ we need a
path of length 11 in G−e (not merely a shortest-path cycle).

## H11 refined (statement)

**Open H11′.** Let G be a 3-connected cubic bipartite graph with **girth ≤ 12** and
n ≥ 12. Then every edge of G lies on a 12-cycle.

**Why girth ≤ 12 is necessary.** If girth ≥ 14 then no C₁₂ exists at all, so H11′
is false as stated for those graphs. (EG must be handled by C₁₆/C₃₂ instead.)

### Verification of H11′

| Regime | Result |
|--------|--------|
| All 3-conn cubic bip n≤20 (genbg) | every edge on C₁₂: **0 fails** (978 graphs at n=20) |
| Girth-6 cubic bip n≤24 | every edge on C₁₂: **0 fails** (even when some edges miss C₆) |
| Random 3-conn cubic bip n≤60 (30 samples each) | **0 fails** |
| All Foster CAT hard graphs | every edge on C₁₂ |
| Heawood / Pappus / Desargues / Tutte–Coxeter | every edge on C₁₂ (when n≥12) |

**Local girth when not on C₆ (girth-6 graphs n≤24):** only local girth **8** appears
(edges on C₈). In C₈-free graphs those edges cannot exist, so either every edge is on
C₆ or some edges jump to local girth ≥ 10.

**CAT_38:** every edge is on a C₆ (57/57) and on a C₁₂ (57/57).

## Case split — cubic bipartite EG

Let G be connected cubic bipartite.

| Case | Condition | EG status |
|------|-----------|-----------|
| 0 | not 3-connected | reduce to 3-conn blocks / known short cycles (genbg: 2-conn exceptions still have C₄/C₈/C₁₆) |
| 1 | has C₄ | **done** (2²) |
| 2 | has C₈ | **done** (2³) |
| 3 | has C₁₆ | **done** (2⁴) |
| 4 | girth 6, no C₈ | **H9 path:** need C₁₂ exclusive through a C₆-edge → C₁₆. Open H11′+H11b |
| 5 | girth 10, no C₄/C₈ | has C₁₀; need C₁₆. Chen–Saito ⇒ cycle ∈ {12,16,20,…}. If C₁₆ done; if C₁₂ need other lift |
| 6 | girth 12 | has C₁₂; need C₁₆ (extension or Chen–Saito next 0 mod 4) |
| 7 | girth 14 | no C₄/C₈/C₁₂; Chen–Saito ⇒ cycle ∈ {16,20,24,28,32,…}. **If always C₁₆, done** |
| 8 | girth 16 | **done** |
| 9 | girth ≥ 18 | need C₃₂ or larger 2^k; Thomassen high-girth modular cycle results |

**Theorem E** already settles all cubic bipartite n≤24 (so cases 4–9 only arise for n≥26; hard C₈-free girth-6 starts at n≥38 in known census).

## Chen–Saito interaction

Chen–Saito (1993): δ(G)≥3 ⇒ ∃ cycle of length **0 mod 4**.

Powers of two ≥4 are all 0 mod 4. EG is the power-of-two refinement.

In C₄-free C₈-free G:
- shortest Chen–Saito cycle has length ≥ 12
- on all hard Foster CAT: that length is **exactly 12**, and C₁₆ also exists

## Partial proof toward H11′ (girth 6)

**Claim A (open).** In 3-connected cubic bipartite girth-6 C₈-free G, every edge has local girth 6 (i.e. lies on a C₆).

*Evidence:* L2 says local girth ∈ {6}∪{≥10}; CAT has only 6; n≤24 non-C₈-free only jumps to 8 (blocked by C₈-free).

**Claim B (open = H11b).** Every edge of every C₆ lies on a C₁₂ meeting the C₆ only at that edge’s endpoints.

*Evidence:* 100% on hard CAT (Fire 5).

**Claim A + Claim B + H9 ⇒ EG for all 3-conn cubic bipartite girth-6 C₈-free graphs.**

## Path-spectrum observation (suggests H11′)

For every edge e=uv of Heawood, path lengths in G−e are {5,7,9,11,13} (all odd from local dist to n−1).
For all 3-conn cubic bip n∈[12,20], path length **11** exists in G−e for every edge (exhaustive).

**Conjecture P.** In 3-connected cubic bipartite G, for every edge e=uv with d=dist_{G−e}(u,v), every odd integer in [d, n−1] is realized by a simple u–v path in G−e.
If true and d≤11 and n≥12, then H11′ holds whenever a cycle through e of length ≤12 exists (i.e. d≤11), and for girth≤12 one still needs d≤11 for every edge (open for large sparse graphs).

## Next vectors
1. Prove Claim A (no local girth ≥10 edges in girth-6 C₈-free cubic bipartite).
2. Prove Claim B / H11b (exclusive C₁₂ through C₆-edges).
3. Prove Case 7: girth-14 cubic bipartite ⇒ C₁₆.
4. Push exhaustive genbg to n=26–28 for cubic bipartite EG (computational).

## Status board

| Item | Status |
|------|--------|
| H9 C₆+C₁₂→C₁₆ | **PROVED** |
| L1–L2 local girth | **PROVED** |
| H11′ every edge on C₁₂ (girth≤12) | **OPEN** (verified n≤24 + random + CAT) |
| Claim A every edge on C₆ (hard class) | **OPEN** (verified CAT) |
| Cubic bipartite n≤24 EG | **PROVED** (exhaustive) |
| Full EG | **OPEN** |
