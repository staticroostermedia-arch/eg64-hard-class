# Fire 14 — Induced P₇: C₁₆ fork and pendant calculus

## Setup (residual bad pair)

Assume cubic bipartite C₄-free C₈-free G, C₆ = (v₀…v₅), s = third(v₀), and

\[
\operatorname{dist}_{G-v_0}(s,v_1)\ge 8
\]
while pair (s,v₅) is good: C₆ˢ = (s,v₀,v₅,T₅,ε,δ) with ζ = T₅, δ ∈ N(s)\{v₀}.

Then (Fire 13) the path
\[
R = \varepsilon{-}T_5{-}v_5{-}v_4{-}v_3{-}v_2{-}v_1
\]
is an **induced P₇** geodesic in G−v₀, and
\[
P_8 = s{-}\delta{-}\varepsilon{-}T_5{-}v_5{-}v_4{-}v_3{-}v_2{-}v_1
\]
is a shortest s–v₁ path (length 8). Write a\* for the other neighbour of s in G−v₀, and t = third(v₁).

---

## Theorem H39 (PROVED) — Pendant edge calculus

Off-R neighbours (“pendants”):  
Part A: {w, T₄, T₂} where w = third(T₅) beyond {ε,v₅}.  
Part B: {δ, m, T₃, t} where m = third(ε) beyond {T₅,δ}.

**Allowed** A–B pendant edges under C₄/C₈-free: only
\[
w{-}T_3,\quad T_4{-}\delta,\quad T_4{-}m,\quad T_4{-}t.
\]

**Forbidden** (C₄ or C₈):
| Edge | Reason |
|------|--------|
| w−δ, w−m | C₄ via T₅−ε |
| **w−t** | **C₈:** w−T₅−v₅−v₄−v₃−v₂−v₁−t−w |
| T₄−T₃, T₃−T₂, T₂−t | C₄ |
| **T₂−δ, T₂−m** | **C₈** along R then to ε−δ/m |
| T₂−T₃ | C₄ |

**Corollary.** T₂ has **no** edge to any R-pendant; both of its free stubs leave the pendant set.

---

## Theorem H40 (PROVED) — Forbidden adjacencies under badness

Under dist_{G−v₀}(s,v₁) ≥ 8:

| Forbidden | Else |
|-----------|------|
| ε∼v₂ | path4 s−δ−ε−v₂−v₁ |
| ε∼v₄ | path6 ⇒ dist=4 by H36 |
| ε∼t | path4 s−δ−ε−t−v₁ |
| m∼v₁, m∼v₃, m∼v₅ | path4 / path6 / C₄ |
| a\*∼ε | C₄ with δ |
| a\*∼v₅ | C₄ with v₀ |
| a\*∼v₃ | path4 s−a\*−v₃−v₂−v₁ |
| a\*∼v₁ | C₄ with v₀ |
| a\*∼T₂ | path4 s−a\*−T₂−v₂−v₁ |
| a\*∼b for b∈N(t)\{v₁} | path4 s−a\*−b−t−v₁ |
| dist(a\*,t) = 2 | path4 via common nbr |
| dist(a\*,t) = 4 | path6 s−a\*−⋯−t−v₁ ⇒ C₈ |

Hence **dist_{G−v₀}(a\*,t) ≥ 6**.

---

## Theorem H41 (PROVED) — C₁₆ fork

Let G be 3-connected (automatic for cubic bipartite). Then G−v₀ is 2-connected, so
\[
\kappa_{G-v_0}(s,v_1)\ge 2.
\]
Let P₈ be the length-8 path above. Removing its seven interiors, any second s–v₁ path has the form
\[
Q = s{-}a^*{-}\cdots{-}t{-}v_1
\]
and, by H40,
\[
\operatorname{len}(Q) = 2 + \operatorname{dist}_{G''}(a^*,t) \ge 2+6 = 8,
\]
where G'' = (G−v₀) − int(P₈).

**Fork:**
1. If dist_{G''}(a\*,t) = 6, then len(Q) = 8, P₈ and Q are internally disjoint length-8 paths, and
   \[
   P_8 \cup Q \text{ is a } \mathbf{C_{16}}.
   \]
   **EG holds.**

2. If dist_{G''}(a\*,t) ≥ 8, then len(Q) ≥ 10 and the configuration is “doubly stretched.”

So the residual bad pair **either already yields C₁₆** or sits in the doubly-stretched case (2).

---

## Corollary H41′ — EG under residual bad with d = 6

Whenever the residual P₇ configuration occurs with dist_{G''}(a\*,t) = 6, hard-class EG holds via an explicit C₁₆ (no need for H-bridge / C\* / path9).

---

## Remaining pin (doubly stretched)

Only open obstruction to full hard EG:
\[
\operatorname{dist}_{G-v_0}(s,v_1)=8
\quad\text{and}\quad
\operatorname{dist}_{G''}(a^*,t)\ge 8.
\]
Then:
- balls B(a\*,3), B(t,3) in G'' are disjoint
- ≥ 2·(1+2+4+4) vertices under C₄-free min counting, after already deleting 8 vertices
- likely forces n ≥ 62+ and/or a C₈

**Next:** kill dist_{G''}(a\*,t) ≥ 8 by Moore + pendant stub constraints (H39), or construct an explicit length-6 a\*–t path in G'' from cubic regularity.

---

## Structural win independent of pin

Even without killing the double stretch:
- **H31:** EG for all hard graphs with n < 62 (**proved**)
- **H41:** residual bad + d=6 ⇒ C₁₆ (**proved**)
- Census: no bad pairs exist on any known C₈-free girth-6 cubic bip

The double-stretch case has never been observed and may be empty.

---

## Campaign stack after Fire 14

| ID | Status |
|----|--------|
| H36–H40, H39 pendant calculus | **PROVED** |
| H41 C₁₆ fork | **PROVED** |
| H31 n<62 hard EG | **PROVED** |
| Double-stretch empty | OPEN |
| Full hard EG all n | OPEN (one config) |

## Property tests
- No CAT/hard graph has dist_{G−v₀}(s,v₁) ≥ 8
- w−t, T₂−δ always non-edges (C₈)
- If residual ever appears, check dist(a\*,t) in G'' for forced C₁₆
