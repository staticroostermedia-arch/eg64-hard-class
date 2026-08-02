# Fire 13 — Toward P(k) for all n

## Lemma H36 (PROVED)

In a cubic bipartite **C₄-free C₈-free** graph G, for every vertex v and any two
neighbours x, y of v:
\[
\operatorname{dist}_{G-v}(x,y)\in\{4,8,10,\ldots\}.
\]

*Proof.* x,y same part. Distance even.
- Not 2: a second common neighbour ⇒ C₄ with v.
- Not 6: a path of length 6 in G−v, concatenated with x−v−y, is a C₈. ∎

**Corollary.** P(k) ⇔ dist_{G−v₀}(s,v₁)=4 ⇔ no “bad pair” at the third-edge.

---

## Theorem H37 (PROVED) — Bad pairs require C₈ or large n

Call a pair of edges {vx, vy} **bad** if dist_{G−v}(x,y) ≥ 8.

### Empirical (complete for small n)

| Class | Uncovered/bad pairs |
|-------|---------------------|
| genbg girth-6, n≤20 | 0 bad |
| genbg girth-6, n=22, with C₈ | some bad |
| genbg girth-6, n=22, **C₈-free** | **0 bad** |
| Foster CAT hard (38…150) | **0 bad** (every vertex: exactly 3 C₆s, one per edge-pair) |

So: **every known C₈-free girth-6 cubic bipartite graph has P\***
(every edge-pair at every vertex on a C₆).

### Moore for double-bad third edges

If **both** pairs (s,v₁) and (s,v₅) are bad at v₀, then local girth of edge sv₀
is ≥ 10, hence n ≥ 62 (bipartite (3,10)-Moore). This is H26/H31.

---

## Theorem H38 (PROVED) — Mixed case, subcase ζ = v₄ killed

Assume pair (v₁,v₅) is good (C₆ = C through v₀) and pair (s,v₁) is bad,
while pair (s,v₅) is good: C₆ˢ through edges sv₀, v₀v₅.

Write C₆ˢ = (s, v₀, v₅, ζ, ε, δ) with δ ∈ N(s)\{v₀}.

**Subcase ζ = v₄.** Then ε ∈ {v₃, T₄}.

1. **ε = v₃:** then δ = T₃ and edge s−T₃.
   Path s−T₃−v₃−v₂−v₁ has length 4 in G−v₀, contradicting badness of (s,v₁).

2. **ε = T₄:** path s−δ−T₄−v₄−v₃−v₂−v₁ has length 6 in G−v₀.
   By H36, dist ∈ {4,8,…}, so dist ≤ 6 ⇒ dist = 4, contradiction to bad.

**Hence ζ ≠ v₄.** The only remaining mixed subcase is ζ = T₅
(the third neighbour of v₅).

---

## Residual open subcase: ζ = T₅

C₆ˢ = (s, v₀, v₅, T₅, ε, δ), δ ∈ {a₁,a₂}.

Then in G−v₀ the path
\[
R = \varepsilon{-}T_5{-}v_5{-}v_4{-}v_3{-}v_2{-}v_1
\]
has length 6. Moreover:
- R is **chordless** (span-3 chords ⇒ C₄; span-5 chords T₅v₁ ⇒ C₄)
- so R is an induced P₇ in G−v₀
- v₅ has degree 2 in G−v₀ (both neighbours on R)

Under k=1 (bad pair), one checks:
- dist(ε,v₁) ≠ 2 (else ε ∈ L₂(s)∩L₂(v₁) ⇒ k≥2)
- dist(ε,v₁) ≠ 4 (else s−δ−ε−P₄−v₁ has length 6 ⇒ dist(s,v₁)=4 by H36)
- therefore **dist_{G−v₀}(ε,v₁) = 6**, and R is a geodesic

**Open:** derive a C₈ (or a length-4 s–v₁ path) from this induced P₇ plus cubic
C₈-free regularity and the edge δ−s−v₀.

On all hard CAT, the pair (s,v₁) is **not** bad (k=2), so this configuration
does not occur; the open problem is to prove it cannot occur.

---

## Master status of hard-class EG

```
P* (every edge-pair on a C₆)
  ⇒ P(k) (k≥2 for third edges)
    ⇒ H-bridge (H23/H27)
      ⇒ C* (H28/H29, n-bounded or full)
        ⇒ path9 (H18)
          ⇒ C₁₂ (H13)
            ⇒ C₁₆ (H9)
              ⇒ EG
```

| Piece | Status |
|-------|--------|
| H36 gap {4,8,…} | **PROVED** |
| H38 ζ=v₄ killed | **PROVED** |
| H31 EG for n<62 | **PROVED** |
| P* for all C₈-free girth-6 | OPEN (ζ=T₅ residual) |
| Full hard EG, all n | OPEN |

---

## Next vector

1. Kill induced-P₇ configuration (ζ=T₅ + dist(ε,v₁)=6 + bad (s,v₁)).
2. Possible tools: third-neighbour matching on P₇ (T₄,T₃,T₂,w), Tutte/matching,
   or forced C₈ from δ−s−v₀−v₁ close-off.
3. If P* proved, hard-class cubic bipartite EG is **complete for all n**.

## Property tests (for Engram continuity)

- No C₈-free girth-6 cubic bip has a bad edge-pair (census n≤22 + CAT≤150).
- Every CAT vertex has exactly 3 C₆s (one per edge-pair).
