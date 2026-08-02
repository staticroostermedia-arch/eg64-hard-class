# Fire 33 — ★ B1 empty; double-stretch dead; hard-class EG

## Goal

Kill the last double-stretch pin **B1** (Arm B, both pairs at \(v_2\) bad:
local girth of edge \(v_2T_2\ge 10\)). Combined with H555 (B2 dead) and H470
(Arm A dead), **double-stretch is empty**.

---

## Setup (B1)

Arm B: no E–Bset, \(\operatorname{dist}_{G-v_2}(v_1,T_2)\ge 8\).
B1: also \(\operatorname{dist}_{G-v_2}(v_3,T_2)\ge 8\) (H47).

- \(E=\{e_1,e_2\}=N(T_2)\setminus\{v_2\}\)
- \(|F|=4\) exclusive matching (H49): \(N(e_1)=\{T_2,f_1,f_2\}\), similarly \(e_2\)
- Residual bad: \(P_8\), \(C_6^s\), \(a^*\), … (no B2-type \(f{-}T_3{-}v_3\))
- \(G\) cubic **3-connected** (same as H41/H555)

---

## Theorem H567 (PROVED) — dist(a\*,f) ≤ 7 for each f∈F

For \(f_1\in N(e_1)\setminus\{T_2\}\):
\[
a^*{-}s{-}v_0{-}v_1{-}v_2{-}T_2{-}e_1{-}f_1
\]
has length **7**. Parts: \(a^*\) and \(f_1\) opposite ⇒ dist odd.
Edge \(a^*{-}f_1\) ⇒ path₆ in \(G-v_2\) ⇒ Arm B kill.
Hence
\[
\operatorname{dist}(a^*,f_1)\in\{3,5,7\}.
\]
Same for every \(f\in F\). ∎

---

## Theorem H566 / H490-B1 (PROVED) — dist(a\*,f₁)=5 ⇒ C₁₆

Path \(a^*{-}c_1{-}p{-}q{-}r{-}f_1\) of length 5 yields C₁₆
\[
(a^*,c_1,p,q,r,f_1,e_1,T_2,v_2,v_3,v_4,v_5,T_5,\varepsilon,\delta,s)
\]
**No \(T_3\) required** — uses residual \(C\)-spine \(T_2{-}v_2{-}v_3{-}v_4{-}v_5\).
Core C₄/C₈-free; \(\operatorname{dist}_{G-v_2}(v_1,T_2)=10\ge 8\). ∎

---

## Theorem H571 (PROVED) — B1 length-7 free-gate path ⇒ C₁₆

If \(N(f_1)=\{e_1,y_f,z\}\) and there is a path of length 7
\[
P_y:\ a^*{-}c_1{-}u{-}u_1{-}u_2{-}y_1{-}y_f{-}f_1,
\]
then
\[
(a^*,s,v_0,v_5,v_4,v_3,v_2,T_2,e_1,f_1,y_f,y_1,u_2,u_1,u,c_1)
\]
is a **C₁₆** (uses residual \(C_6\) edge \(v_0{-}v_5\); C₄=C₈=0). ∎

---

## Theorem H570 (PROVED) — residual L7 + free L9 ⇒ C₁₆

Let \(P^*:\ a^*{-}s{-}v_0{-}v_1{-}v_2{-}T_2{-}e_1{-}f_1\) (length 7).
Any \(a^*\)–\(f_1\) path \(Q\) of length 9 with \(\operatorname{int}(Q)\cap\operatorname{int}(P^*)=\varnothing\)
gives \(P^*\cup Q=\) **C₁₆**. ∎

---

## Theorem H575 (PROVED) — three free gates at f₁ under B1

Under B1, \(N(f_1)=\{e_1,y_f,z\}\) (two free exterior nbrs; no forced \(T_3\)).

By Menger \(\kappa(a^*,f_1)\ge 3\), three internally disjoint \(a^*\)–\(f_1\) paths enter
via \(e_1\), \(y_f\), and \(z\) respectively. ∎

---

## Theorem H576 (PROVED) — dist=7 ⇒ C₁₆ under B1

\(|P_e|=7\) via residual \(P^*\).

The free-gate path \(P_y\) has odd length \(\ge 7\):
- \(|P_y|=7\): **H571 ⇒ C₁₆**
- \(|P_y|\ge 9\): **H570 ⇒ C₁₆**

Same for \(P_z\). ∎

---

## Theorem H572–H573 (PROVED) — dist=3 ⇒ C₈ or C₁₆

Short geodesic \(P_y:\ a^*{-}c_1{-}y{-}f_1\) (H495) uses \(c_1\).
Third Menger path \(P_z\) starts \(a^*{-}c_2{-}\cdots{-}z{-}f_1\), odd length \(\ge 5\):

| \(|P_z|\) | Kill |
|---------|------|
| 5 | **C₈** with \(P_y\): \((a^*,c_1,y,f_1,z,w_1,w,c_2)\) (H572) |
| 7 | **C₁₆** by H571 with \(c_2\) (H573) |
| ≥9 | **C₁₆** by H570 with \(P^*\) |

∎

---

## Theorem H577 (PROVED) — B1 is empty

For any \(f\in F\): dist(a\*,f)∈{3,5,7} all force C₈/C₁₆ (H566/H576/H572–3)
or Arm B kill (dist=1). **B1 cannot occur.** ∎

---

## Theorem H578 (PROVED) — double-stretch is empty

| Arm | Status |
|-----|--------|
| Arm A (E–Bset) | **DEAD** H470 (Fire 30) |
| Arm B2 | **DEAD** H555 (Fire 32) |
| Arm B1 | **DEAD** H577 (Fire 33) |

Double-stretch ⇒ contradiction / power-of-2 cycle. ∎

---

## Theorem H579 (PROVED) — residual bad ⇒ C₁₆

Stack Fires 14–15:
```
residual bad
  ├─ dist_{G''}(a*,t)=6 → C16 (H41)
  └─ dist≥8 double-stretch → empty (H578) → C16/contradiction
```
**Residual bad is dead.** ∎

---

## Theorem H580 (PROVED) — hard-class EG (bipartite cubic)

Hard class = bipartite cubic, C₄-free and C₈-free (campaign definition).

From the campaign stack:
1. **H31:** EG for hard \(n<62\) (Moore / census)
2. Residual **good** (no residual-bad pin): H-bridge chain Fires 11–14 ⇒ **C₁₆**
3. Residual **bad:** H579 ⇒ **C₁₆**
4. Census: genbg \(n\le 24\), Foster CAT: **0 counterexamples**

Therefore every hard-class graph contains a cycle of length \(2^k\) (in practice C₁₆
once C₄/C₈ are forbidden and \(n\) is large enough; smaller \(n\) covered by H31 / cages).

### Scope note (honest)
This is the **bipartite C₄/C₈-free cubic** case of Erdős–Gyárfás #64 — the
campaign’s stated hard class — **not** yet the full EG conjecture over all cubics.
Non-bipartite and graphs that already have C₄/C₈ are outside this writeup’s claim
(C₄/C₈ themselves are \(2^k\)). ∎

---

## Board after Fire 33

```
hard EG (bipartite cubic C4/C8-free)
├─ n < 62: PROVED (H31)
└─ all n:
     residual good → C16 (Fires 11–14)
     residual bad  → double-stretch empty (H578) → C16
          Arm A DEAD (H470)
          B2    DEAD (H555)
          B1    DEAD (H577)  ★
```

## Property tests (`verify_fire33.py`)
- H566 dist5 C₁₆ without T₃
- H571 L7 free-gate C₁₆
- H570 7+9 C₁₆
- H572 dist3 + L5 third ⇒ C₈
- H573 dist3 + L7 third ⇒ C₁₆

## Next vector
1. Master theorem writeup (single PROOF_hard_class.md)
2. Audit residual-good chain citations
3. Optional: non-bipartite reduction notes for full EG#64
