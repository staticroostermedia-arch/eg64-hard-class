# Fire 17 — C₈ massacre under E–Bset; Arm A threshold

## Theorem H50 (PROVED) — f cannot touch the C-spine

Assume residual bad + E–Bset edge \(e{-}b\), and \(f\) = the third neighbour of \(e\)  
(\(N(e)=\{T_2,b,f\}\)).

| Edge | Contradiction |
|------|----------------|
| **f−v₄** | **C₈:** \(f{-}v_4{-}v_3{-}v_2{-}v_1{-}t{-}b{-}e{-}f\) (all other edges forced) |
| **f−T₃** | **C₈:** \(f{-}T_3{-}v_3{-}v_2{-}v_1{-}t{-}b{-}e{-}f\) |
| **f−t** | **C₄:** \(f{-}e{-}b{-}t{-}f\) |
| **f−v₂** | **C₄:** \(f{-}e{-}T_2{-}v_2{-}f\) |
| **f−e′** | **C₄:** \(f{-}e{-}T_2{-}e'{-}f\) |
| **f−δ** | path₆ \(s{-}\delta{-}f{-}e{-}b{-}t{-}v_1\) (contradicts dist≥8) |
| **f−v₀** | path₆ \(s{-}v_0{-}f{-}e{-}b{-}t{-}v_1\) |
| **f−T₅** | T₅ cubic-saturated |
| **f−a\*** | path₄ \(a^*{-}f{-}e{-}b{-}t\) (H40) |

**Verified** on CAT: all non-f edges of the two C₈s are present; f−v₄ and f−T₃ are non-edges.

**Corollary.** Both free neighbours of \(f\) are exterior part-B vertices (or possibly \(m\)).

---

## Theorem H51 (PROVED) — b−δ forbidden under E–Bset

Path of length 6:
\[
s{-}\delta{-}b{-}e{-}T_2{-}v_2{-}v_1
\]
contradicts residual dist_{G−v₀}(s,v₁) ≥ 8.  
**⇒ no b−δ.**

Also **b−e′** is C₄: \(e{-}b{-}e'{-}T_2{-}e\) (both E meet T₂).

---

## Theorem H52 (PROVED) — Arm A threshold

Under residual bad + E–Bset:
\[
\operatorname{dist}_{G''}(a^*,e)\le 4 \;\Longrightarrow\; \operatorname{dist}_{G''}(a^*,t)=6 \;\Longrightarrow\; \mathbf{C_{16}}
\]
(by triangle \(+2\) through \(e{-}b{-}t\), H40 ruling out 2 and 4, then H41).

**Corollary.** Double-stretch Arm A requires the strict inequality
\[
\operatorname{dist}_{G''}(a^*,e)\ge 6,
\]
i.e. **all three** of \(T_2,b,f\) lie outside \(B(a^*,4)\) in \(G''\).

---

## Theorem H53 (PROVED) — Arm B: QB ⊥ QF

Under Arm B, let
- \(\mathrm{QB} = N(\mathrm{Bset})\setminus\{t\}\) (4 stubs from Bset),
- \(\mathrm{QF} = N(F)\setminus E\) (8 stubs from F beyond E).

If \(q\in \mathrm{QB}\cap\mathrm{QF}\), then some \(b{-}q{-}f\) has length 2, so dist(b,f)=2, forbidding Arm B (path₆).  
**⇒ QB ∩ QF = ∅.**

Moreover QF-vertices have **no** edges into Bset (same reason).

Under B2, \(T_3\in\mathrm{QF}\) (via f−T₃) and \(T_3\notin\mathrm{QB}\) (b−T₃ path₆).

---

## Theorem H54 (PROVED) — Arm A q₅=f forbids spine for g

In the geodesic case dist(a\*,e)=6 with q₅=f:
\(N(f)=\{q_4,e,g\}\). Then g avoids the same spine list as H50  
(plus g≠q₂ else dist(a\*,t)≤6 kills double-stretch).  
**⇒ g pure exterior part B.**

---

## Status after Fire 17

| Pin | Status |
|-----|--------|
| n<62 hard EG | **PROVED** (H31) |
| residual + d=6 ⇒ C₁₆ | **PROVED** (H41) |
| T₂T₅ ⇒ C₈ | **PROVED** (H42) |
| E–Bset + dist(a\*,e)≤4 ⇒ C₁₆ | **PROVED** (H52) |
| f-spine C₈ massacre | **PROVED** (H50–H51) |
| Arm A needs dist(a\*,e)≥6, all N(e) far | **PROVED** (H52 cor.) |
| Arm B QB⊥QF, \|F\|=4 | **PROVED** (H49,H53) |
| Arm A fully empty | OPEN (need dist(a\*,e)≤4 always, or C₈ in far case) |
| Arm B fully empty | OPEN (B1 n>62 / B2 with QB⊥QF) |

### The single hinge for Arm A
Prove under residual + E–Bset that \(a^*\) cannot stay at distance ≥6 from all of \(\{T_2,b,f\}\) simultaneously — e.g. via the third neighbour β of b and \(\{c_1,c_2\}\), or via m-bridge.

### The single hinge for Arm B  
B2: four F-verts + disjoint QB/QF stub systems force a path₆ or C₈ with C₆ˢ.  
B1: two local-girth-10 edges (s−v₀ and v₂T₂) + a global C₆ force C₁₆ or n-bound beyond Moore.

## Property tests
- f−v₄, f−T₃, f−t, b−δ never edges when E–Bset present on hard CAT  
- QB ∩ QF empty whenever no E–Bset in synthetic models  
