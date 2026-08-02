# Fire 9 — H17 proved + H16 construction + single spectral gap

## Lemma H17 (PROVED)

Let G be bipartite, C = (v₀…v₅) a 6-cycle, s the third neighbour of vᵢ,
t the third neighbour of vᵢ₊₁, and H = G − V(C).

**H17.1** s is not adjacent to t.  
*Proof.* Else s−vᵢ−vᵢ₊₁−t−s is a 4-cycle. ∎

**H17.2** There is no *s–t* path of length 5 in H.  
*Proof.* Such a path P, concatenated with s−vᵢ−vᵢ₊₁−t, yields a simple 8-cycle
(V(P) ∩ V(C) = ∅). ∎

**H17.3** Consequently, in a C₄-free C₈-free graph,
\[
\operatorname{dist}_H(s,t) \in \{3,7,9,11,\ldots\}.
\]

**H17.4** (H1 restated) Any *s–t* path of length *d* in H produces a cycle of
length *d+3* through the edge vᵢvᵢ₊₁.

---

## Theorem H18 — Constructive path of length 9 (configuration theorem)

**Setup.** Assume dist_H(s,t) = 3 with **unique** shortest path s−a₁−b₁−t.
Write N_H(s) = {a₁,a₂}, N_H(t) = {b₁,b₂}, and let x be the unique neighbour of a₁
outside {s,b₁}.

**Configuration C*** (verified on all girth-6 C₈-free Foster CAT):
1. a₁b₁ lies on a second 6-cycle free of {s,t}:
   \[
   C_2 = (a_1,\, b_1,\, y,\, p,\, q,\, x)
   \]
2. dist_{H−{s,t}}(y, b₂) = 3
3. A shortest *y–b₂* path in H−{s,t} is vertex-disjoint from {x,q,p} except at y

**Then** the walk
\[
a_1 \to x \to q \to p \to y \xrightarrow{\text{len }3} b_2
\]
is a simple *a₁–b₂* path of length 7, and
\[
s \to a_1 \to x \to q \to p \to y \xrightarrow{\text{len }3} b_2 \to t
\]
is a simple *s–t* path of length **9**.

**Proof.** Length count: 1+1+1+1+1+3+1 = 9 from s to t; simplicity from (3) and
a₁∉{x,q,p,y,b₂}, s,t removed from H−{s,t}. ∎

**Corollary H18′.** Under C*, Theorem H13 fires: exclusive C₁₂ on vᵢvᵢ₊₁, hence
**C₁₆** by H9.

### Verification of C* + end-to-end C₁₆

| Graph | path9 constructed | fail |
|-------|-------------------|------|
| CAT_38 | 114 | 0 |
| CAT_50 | 120 | 0 |
| CAT_56 | 120 | 0 |
| CAT_72 | 120 | 0 |
| CAT_96 | 120 | 0 |

Explicit CAT_38 example:
```
path9 = [35,26,17,11,6,8,16,13,14,23]
C12   = [1,35,26,17,11,6,8,16,13,14,23,33]
C16   = [1,35,26,17,11,6,8,16,13,14,23,33,31,36,2,0]  ✓ edges checked
```

---

## What remains for full H16

| Subclaim | Status |
|----------|--------|
| H17 (dist ∈ {3,7,9,…}) | **PROVED** |
| dist_H(s,t) = 3 (not ≥7) | **OPEN** (100% on CAT; no counterexample n≤24) |
| Unique shortest path | **OPEN** (100% on CAT) |
| Configuration C* | **OPEN** as proof; **verified** as census |
| H18: C* ⇒ path9 | **PROVED** |
| H13: path9 ⇒ C₁₆ | **PROVED** (Fire 8) |
| H9: exclusive C₁₂ ⇒ C₁₆ | **PROVED** |

### Why dist = 3 is plausible (not yet proof)

- The path s−vᵢ−vᵢ₊₁−t already realises dist_G(s,t) = 3
- An *H*-geodesic of length ≥7 would mean every length-3 *s–t* path in G uses V(C)
- In all enumerated cubic bipartite girth-6 graphs, an off-C length-3 path exists
- If dist_H ≥ 7, balls B_H(s,3) and B_H(t,3) are disjoint and C₈-free constraints
  force large n (Moore-type); hard C₈-free graphs start at n=38 and still have dist=3

### Proof strategy for dist = 3

1. **Matching/counting:** 4 stubs out of N(s) toward the t-side; C₈-free forbids
   long detours as the only connections.
2. **3-connectivity:** three independent *s–t* paths by Menger; one uses C, so two
   live in G−{vᵢvᵢ₊₁} — analyse whether one lies in H of length 3.
3. **Assume dist≥7, derive C₈ or C₄** from the second C₆ forced by girth 6 elsewhere.

---

## Algorithmic EG certificate (hard class)

```
for each 6-cycle C:
  for each edge e of C:
    s,t = thirds of the endpoints of e
    construct path9 via H18/C*   # or DFS length 9 in H
    if path9 found:
      build exclusive C12 (H13)
      build C16 (H9)
      return CERTIFICATE
```
This **always returns** on every hard Foster CAT graph tested.

---

## Campaign theorem stack

| ID | Statement | Status |
|----|-----------|--------|
| E | cubic bip n≤24 ⇒ EG | PROVED |
| A′ | Foster CAT ≤150 ⇒ EG | PROVED |
| H1 | third-path d ⇒ cycle d+3 | PROVED |
| H9 | C₆+excl C₁₂ ⇒ C₁₆ | PROVED |
| H13 | third-path 9 ⇒ C₁₆ | PROVED |
| H17 | dist_H ∈ {3,7,9,…} | **PROVED** |
| H18 | C* ⇒ path9 | **PROVED** |
| M10 | girth≥10 ⇒ n≥62 | PROVED |
| H16 | path9 always | OPEN (= dist=3 + C*) |
| EG | full conjecture | OPEN |

## Next vector
Prove dist_H(s,t)=3 for consecutive thirds in cubic bipartite girth-6 C₈-free graphs.
Then prove C* (second C₆ + dist(y,b₂)=3).
