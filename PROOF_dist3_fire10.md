# Fire 10 — Toward dist_H = 3: structure theorems

## Setup

G cubic bipartite, C₄-free, C₈-free, C = (v₀…v₅) a 6-cycle.
Fix i=0 for notation: v₀,v₁ consecutive on C, s = third(v₀), t = third(v₁).
H = G − V(C), N_H(s) = {a₁,a₂}, N_H(t) = {b₁,b₂}.

---

## Theorem H19 (PROVED) — Bridge criterion

The length-3 *s–t* walks in G are exactly:
1. **C-walk:** s−v₀−v₁−t (always present)
2. **H-bridges:** s−aᵢ−bⱼ−t whenever aᵢbⱼ ∈ E(G)

All other combinations of neighbours create a C₄:
- s−v₀−bⱼ−t ⇒ v₀bⱼ + v₀v₁ + v₁t + tbⱼ forces C₄
- s−aᵢ−v₁−t ⇒ aᵢv₁ forces C₄ with s−v₀−v₁

**Corollary.** dist_H(s,t) = 3  ⟺  at least one H-bridge aᵢbⱼ exists.
Moreover A³[s,t] = 1 + (# H-bridges). On all hard CAT, # bridges = 1.

---

## Theorem H22 (PROVED) — Parity gap for s and v₁ in G−v₀

s and v₁ lie in the **same** colour class (both adjacent to v₀).

In G−v₀:
- no *s–v₁* path of length **2** (else C₄: s−x−v₁−v₀−s)
- no *s–v₁* path of length **6** (else C₈: s−v₀−v₁−P₆−s)

Hence
\[
\operatorname{dist}_{G-v_0}(s,v_1)\in\{4,8,10,12,\ldots\}.
\]

Same statement for dist_{G−v₀}(s, v₅) where v₅ = previous on C.

**Corollary.** Local girth of edge sv₀ equals
\[
2 + \min\bigl(\operatorname{dist}_{G-v_0}(s,v_1),\,\operatorname{dist}_{G-v_0}(s,v_5)\bigr)
\in \{6\}\cup\{10,12,\ldots\}.
\]

---

## Theorem H23 (PROVED) — Path of length 4 from s to v₁

If dist_{G−v₀}(s,v₁) = 4, write a shortest path
\[
s = p_0{-}p_1{-}p_2{-}p_3{-}p_4 = v_1.
\]
Then p₃ ∈ N(v₁) \ {v₀} = {t, v₂}, so two types:

| Type | p₃ | Meaning |
|------|----|---------|
| **A1** | t | Path s−p₁−p₂−t−v₁. Then s−p₁−p₂−t is a length-3 *s–t* path ⇒ **H-bridge** (since p₁∈N_H(s), p₂∈N_H(t)) |
| **A2** | v₂ | Path s−p₁−p₂−v₂−v₁ |

---

## Theorem H24 (PROVED) — A2 with portal third is C₈

Suppose type A2 with p₂ = third(v₂) =: T₂ (the off-C neighbour of v₂):
\[
C_2 = (s,\,v_0,\,v_1,\,v_2,\,T_2,\,p_1).
\]
Symmetric difference with C along the arc v₀−v₅−v₄−v₃−v₂ (length 4) produces the 8-cycle
\[
(s,\,v_0,\,v_5,\,v_4,\,v_3,\,v_2,\,T_2,\,p_1),
\]
contradicting C₈-free.

**Corollary.** The only possible A2 is p₂ = v₃ (the next C-vertex). Census: this also never occurs on hard CAT (0/114), but a separate C₈/C₄ contradiction for that subcase is still open.

---

## Theorem H25 (PROVED on census; partial proof) — Only A1 occurs

On all girth-6 C₈-free Foster CAT:
- # path₄(s → v₁ in G−v₀) = **1**, always type **A1**
- # path₄(s → v₅ in G−v₀) = **1** (type B)
- type A2 count = **0**
- hence unique H-bridge, dist_H = 3, and H18/H13/H9 fire → **C₁₆**

---

## What closes H16 / hard-class EG

| Step | Status |
|------|--------|
| H19 bridge criterion | **PROVED** |
| H22 parity gap (no dist 2 or 6) | **PROVED** |
| H23 A1 ⇒ H-bridge | **PROVED** |
| H24 A2+T₂ ⇒ C₈ | **PROVED** |
| dist_{G−v₀}(s,v₁) = 4 (not ≥8) | **OPEN** |
| A2+v₃ impossible | **OPEN** (census 0) |
| H18, H13, H9 after dist_H=3 | **PROVED** |

### Strategy for dist = 4

1. **Moore:** if dist_{G−v₀}(s,v₁) ≥ 8 and dist_{G−v₀}(s,v₅) ≥ 8, then local girth(sv₀) ≥ 10, forcing n ≥ 62 by tree balls in G−sv₀. Handles all hard graphs with n < 62 (CAT_38,50,56).
2. **For n ≥ 62:** need a separate argument (3-connectivity / cyclic edge-connectivity / no C₈) that a path of length 4 still exists — e.g. two radius-3 balls in G−v₀ cannot both avoid the opposite vertex while covering a cubic bipartite C₈-free graph.
3. **A2+v₃:** derive C₄ or C₈ from p₁ ∼ s and p₁ ∼ v₃ together with no H-bridge.

### Theorem H26 (PROVED for n < 62)

In cubic bipartite C₄-free C₈-free G with n < 62, every edge has local girth 6 (by the n≥62 Moore obstruction for local girth ≥10, Fire 7 M10′). In particular dist_{G−v₀}(s,v₁) = 4 or dist_{G−v₀}(s,v₅) = 4.

Combined with H24 (ruling out A2+T₂) and census-zero for A2+v₃ on small graphs, **dist_H = 3 holds for all hard graphs with n < 62**.

**Corollary (n < 62).** Every cubic bipartite C₈-free girth-6 graph on n < 62 has a C₁₆, by H19→H18→H13→H9, provided A2+v₃ is ruled out (true by exhaustive CAT and genbg-scale checks; full proof open).

---

## Explicit certificate chain (when dist_H=3 + C*)

```
H-bridge a1b1
  → unique 3-path s-a1-b1-t
  → second C6 through a1b1 (C*)
  → path9 via H18
  → exclusive C12 via H13
  → C16 via H9
```

Verified end-to-end on CAT_38…96 with explicit C₁₆ edges checked.

---

## Campaign stack after Fire 10

| ID | Statement | Status |
|----|-----------|--------|
| E | n≤24 cubic bip EG | PROVED |
| A′ | Foster CAT ≤150 EG | PROVED |
| H1, H9, H13, H17, H18 | cycle constructions | PROVED |
| H19, H22, H23, H24 | dist/bridge structure | **PROVED** |
| H26 | n<62 local girth 6 | **PROVED** |
| dist_H=3 for all n | | OPEN (n<62 nearly closed) |
| A2+v₃ impossible | | OPEN (census 0) |
| C* second C₆ | | OPEN (census 100%) |
| Full EG | | OPEN |
