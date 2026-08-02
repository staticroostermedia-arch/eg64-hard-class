# Fire 12 — The walk formula: dist = 4 ⟺ k ≥ 2

## Setup

G cubic bipartite **C₄-free**. Vertex v₀ with neighbours {s, v₁, v₅}
(s = third of v₀ relative to a 6-cycle through v₀, or simply any labelling of the three neighbours).
s and v₁ lie in the **same** colour class; unique common neighbour v₀ (C₄-free).

Write N(s) = {v₀, a₁, a₂}, N(v₁) = {v₀, v₂, t}.

---

## Theorem H32 (PROVED) — Exactly seven through-walks

There are **exactly 7** walks of length 4 from s to v₁ that visit v₀:

| # | Walk | Reason |
|---|------|--------|
| 2 | s−v₀−v₁−x−v₁ for x ∈ {v₂, t} | backtrack at v₁ |
| 1 | s−v₀−v₅−v₀−v₁ | backtrack at v₀ via v₅ |
| 1 | s−v₀−s−v₀−v₁ | backtrack at v₀ via s |
| 1 | s−v₀−v₁−v₀−v₁ | backtrack v₀−v₁−v₀ |
| 2 | s−aᵢ−s−v₀−v₁ for i=1,2 | out-and-back on aᵢ |

**No other through-walks exist** under C₄-free:
- s−v₀−v₅−x−v₁ with x ∈ {v₂,t} ⇒ edge v₅x ⇒ C₄
- s−aᵢ−x−v₀−v₁ with x ∈ {v₁,v₅} ⇒ C₄
- s−aᵢ−v₀−⋯ ⇒ edge aᵢv₀ ⇒ C₄

---

## Theorem H33 (PROVED) — A⁴ formula and the avoid count

For any two same-part vertices at distance 2 in cubic bipartite C₄-free G:
\[
A^4[u,w] = 6 + k, \qquad k = \bigl|L_2(u)\cap L_2(w)\bigr|
\]
where L₂ = vertices at distance exactly 2.

**Proof.** A²[u,u]=3, A²[u,w]=1, and A⁴[u,w] = ∑_z A²[u,z]A²[z,w]
= 3·1 + 1·3 + ∑_{z∉{u,w}} 1_{dist(u,z)=dist(z,w)=2} = 6+k. ∎

**Always k ≥ 1:** v₅ ∈ L₂(s) ∩ L₂(v₁) (both via v₀).

**Corollary H33′.** Number of length-4 walks s → v₁ **avoiding** v₀:
\[
A^4[s,v_1] - 7 = (6+k) - 7 = k - 1.
\]

---

## Theorem H34 (PROVED) — Avoid walks are simple paths

Any length-4 walk s → v₁ in G−v₀ is a **simple path**.

*Proof.* A non-simple walk of length 4 revisits a vertex. Possible patterns
s−a−x−a−v₁ or s−a−s−⋯ require an edge a−v₁ or similar, each of which is a C₄
with s−v₀−v₁. Forbidden. ∎

**Corollary H34′ (master equivalence).**
\[
\boxed{\operatorname{dist}_{G-v_0}(s,v_1)=4 \;\Longleftrightarrow\; k\ge 2
\;\Longleftrightarrow\; \text{a length-4 }s\text{–}v_1\text{ path in }G-v_0\text{ exists}}
\]
And by H23/H27: such a path is type A1 (H-bridge) or A2 (⇒ C₈ or H-bridge).

---

## Census of k

| Graph | k | avoid = k−1 | dist₄ |
|-------|---|-------------|-------|
| Hard CAT (38…150) | **2** | 1 | yes |
| Heawood (has C₈) | 5 | 4 | yes |
| CAT_80 (girth 10, no C₆) | 1 on dist-2 pairs | — | N/A |

On all C₈-free **girth-6** graphs tested: **k = 2** exactly (one extra common = the H-bridge midpoint b₁).

---

## Theorem H35 (PROVED) — Identity of the second common when k=2

When k=2, the unique z ∈ L₂(s)∩L₂(v₁) \ {v₅} satisfies:
- z is adjacent to some aᵢ ∈ N_H(s) and to t (or v₂)
- the path s−aᵢ−z−t−v₁ is the unique avoid walk (H-bridge case when z−t and aᵢ−z)

In particular **k ≥ 2 ⇒ H-bridge or A2**, hence (C₈-free) **⇒ H-bridge** (Fire 11).

---

## What H32–H35 buy

The entire dist_H=3 problem reduces to one numerical claim:

### Open pin P(k): **k ≥ 2** for consecutive (s, v₁) on a 6-cycle in cubic bipartite C₈-free graphs

Equivalent forms:
1. |L₂(s) ∩ L₂(v₁)| ≥ 2
2. A⁴[s,v₁] ≥ 8
3. dist_{G−v₀}(s,v₁) = 4
4. H-bridge exists
5. dist_H(s,t) = 3

**H31** already gives this for n < 62 (Moore: k=1 ⇒ local girth ≥10 ⇒ n≥62).

---

## Attack on P(k) for all n

### Strategy A — Second C₆ through v₀
v₀ lies on C = (v₀ v₁ v₂ v₃ v₄ v₅). The pair of edges (v₀v₁, v₀v₅) is used by C.
If a second C₆ through v₀ uses (v₀s, v₀v₁), that is exactly path₄ in G−v₀ ⇒ k≥2.

### Strategy B — No k=1 under C₈-free + girth 6
Assume k=1. Then no H-bridge, dist_{G−v₀}(s,v₁)≥8.
Balls B(s,3) and B(v₁,3) in G−v₀ are disjoint, tree-like, and the C₆ C must sit awkwardly relative to the cut {v₀}. Derive C₈ or C₄ from the forced expansion of a₁,a₂ toward t,v₂.

### Strategy C — Global A⁴ minimum
Prove: every dist-2 same-part pair on a girth-6 cubic bipartite C₈-free graph has A⁴ ≥ 8 (i.e. k≥2).
(False for girth ≥10: CAT_80 has A⁴=7. So girth 6 is essential.)

### Strategy D — Eigenvalue rigidity
Girth-6 cubic bipartite graphs have spectrum constrained (e.g. z in the complex plane); A⁴ entries may have a uniform lower bound for dist-2 pairs.

---

## Girth ≥ 10 side result

For girth ≥ 10: no C₆, so the third-edge construction changes.
CAT_80, 110 (girth 10) and CAT_120 (girth 8) all have **C₁₆** by direct check.
**Conjecture G10:** every cubic bipartite graph of girth 10 has a C₁₆ (EG for this class).
Moore n≥62 for girth 10; known cages and near-cages all satisfy EG by census.

---

## Campaign stack after Fire 12

| ID | Statement | Status |
|----|-----------|--------|
| H32 | Exactly 7 through-walks | **PROVED** |
| H33 | A⁴=6+k; avoid=k−1 | **PROVED** |
| H34 | avoid walks are simple; dist=4⇔k≥2 | **PROVED** |
| H35 | k=2 ⇒ H-bridge (C₈-free) | **PROVED** |
| H31 | EG hard class n<62 | **PROVED** |
| P(k) | k≥2 always on girth-6 C₈-free | **OPEN** (n≥62) |
| Full hard-class EG | P(k) + H18–H29 chain | open for n≥62 |

## Next vector
Prove P(k): k≥2 for all girth-6 cubic bipartite C₈-free graphs (eliminate size bound).
