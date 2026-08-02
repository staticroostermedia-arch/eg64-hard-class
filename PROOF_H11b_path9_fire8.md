# Fire 8 — H11b via path-of-length-9 between thirds

## Theorem H13 (PROVED)

Let G be cubic bipartite, C a 6-cycle, tᵢ the third-neighbour of vᵢ off C, and H = G − V(C).

**If** there is a path of length **9** in H from tᵢ to tᵢ₊₁, **then**:
1. The walk
   \[
   v_i \to t_i \xrightarrow{\text{path length 9}} t_{i+1} \to v_{i+1} \to v_i
   \]
   is a **12-cycle** Q.
2. V(Q) ∩ V(C) = {vᵢ, vᵢ₊₁} (path interiors lie in H).
3. E(Q) ∩ E(C) = {vᵢvᵢ₊₁} (exclusive edge share).
4. By **Theorem H9**, (C − e) ∪ (Q − e) is a **16-cycle**.

**Proof.** (1) Length = 1+9+1+1 = 12; interiors of the H-path are disjoint from C, and tᵢ ∉ C, so all 12 vertices are distinct.  
(2)–(3) immediate from the construction.  
(4) H9. ∎

**Corollary.** To prove EG for cubic bipartite girth-6 C₈-free graphs, it **suffices** to prove:

> **Open H16.** For every 6-cycle and every i, consecutive thirds tᵢ, tᵢ₊₁ are joined by a path of length 9 in H = G−V(C).

---

## Port geometry (VERIFIED — candidate for proof)

On all girth-6 C₈-free Foster CAT graphs, for every C₆ and every consecutive thirds s,t in H:

| Object | Value (100%) |
|--------|----------------|
| deg_H(s) = deg_H(t) | 2 |
| \|E(N(s), N(t))\| | **1** (unique link a₁b₁) |
| 3-path | s−a₁−b₁−t unique |
| dist(a₁,a₂) | 2 (via s) |
| dist(b₁,b₂) | 2 (via t) |
| dist(a₁,b₂) in H | 3 (via b₁−t−b₂, uses t) |
| dist(a₁,b₂) in H−{s,t} | **5** |
| path a₁→b₂ length 7 in H−{s,t} | **exists** |
| path s→t length 9 | **exists** (= s−a₁−P₇−b₂−t) |
| H13 fires (exclusive C₁₂ + H9 → C₁₆) | **100%** of pairs |

Counts: CAT_38: 114/114; CAT_50: 150/150; CAT_56: 168/168.

### Explicit C₁₆ construction (algorithmic)

```
Input: cubic bipartite G, 6-cycle C = (v0..v5)
For i in 0..5:
  s = third(vi), t = third(v_{i+1})
  H = G - V(C)
  Find path P of length 9 from s to t in H   // Open H16 guarantees
  Q = (vi, s, ...P..., t, v_{i+1})           // 12-cycle exclusive on edge vi v_{i+1}
  C16 = H9(C, Q)                              // Theorem H9
  return C16
```

---

## Why length 9 is the sweet spot

| Path s–t length d | Cycle via H1 (d+3) | Exclusive C₁₂ route? |
|-------------------|--------------------|----------------------|
| 3 | C₆ | base 3-path |
| 5 | C₈ | **forbidden** in hard class |
| 7 | C₁₀ | via a₁−P₅−b₂ |
| **9** | **C₁₂** | **via a₁−P₇−b₂ → H13** |
| 11 | C₁₄ | |
| 13 | C₁₆ | direct H1 (needs C₁₂-ear; circular for existence) |

H13 uses d=9 to get C₁₂ **without** presupposing a C₁₂-ear, then H9 upgrades to C₁₆.

---

## Sub-lemmas toward H16

### Lemma P3 (open — verified)
dist_H(s,t) = 3 and the shortest path is unique: s−a₁−b₁−t.

*Approach:* C₄-free ⇒ no edge s−t and no 2-path of wrong shape; C₈-free ⇒ no path of length 5; connectivity + cubic ⇒ length 3 exists for n in the hard range (cf. Moore / Fire 7).

### Lemma P-ports (open — verified)
N(s)={a₁,a₂}, N(t)={b₁,b₂} with unique bridge a₁b₁; dist_{H−{s,t}}(a₁,b₂)=5.

### Lemma P7 (open — verified)
There is a path of length 7 from a₁ to b₂ in H−{s,t}.

*Approach:* Shortest path length 5; need one non-shortest path of length 7.  
(C₆-ear on a length-5 path gives length 9, not 7 — so length 7 uses a different route.)

### Lemma P9 from P7 (PROVED)
s−a₁−(path₇ to b₂)−b₂−t is a simple s–t path of length 9 in H, provided the path₇ avoids s,t (true in H−{s,t}).

---

## Relationship to earlier pins

| Old pin | Status after Fire 8 |
|---------|---------------------|
| H11b (exclusive C₁₂ on C₆-edge) | **Reduced to H16** (path length 9) via H13 |
| Middle edge on C₁₂ (for d=13 ear) | Alternative route; not needed if H16 holds |
| Claim A (every edge on C₆) | Still stronger than needed |
| H9 | PROVED (unchanged) |
| H1 | PROVED (unchanged) |

---

## Theorem package (proved this campaign)

1. **E** — cubic bipartite n≤24: EG exhaustive  
2. **A′** — Foster CAT ≤150: EG  
3. **H1** — third-path length d ⇒ cycle d+3  
4. **H9** — C₆ + exclusive C₁₂ ⇒ C₁₆  
5. **H13** — third-path length 9 ⇒ exclusive C₁₂ ⇒ C₁₆  
6. **L1–L2** — local girth calculus  
7. **M10** — girth ≥10 ⇒ n≥62  

## Single open gate for girth-6 C₈-free EG

**H16:** path of length 9 between consecutive thirds in H = G−V(C).

Verified on all available hard examples; port geometry completely uniform.

## Next vector
1. Prove Lemma P3 (dist=3 unique).  
2. Prove dist_{H−{s,t}}(a₁,b₂)=5.  
3. Prove existence of a₁–b₂ path of length 7 (or any construction of s–t path length 9).  
4. Extend genbg EG check to n=26.
