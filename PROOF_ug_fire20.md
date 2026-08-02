# Fire 20 — u_g C₈ massacre; layer law (a\*∈L₆)

## Setup

Arm A double-stretch, residual + E–Bset, geodesic of length 6 ending at \(e\):
\[
a^*{-}c{-}q{-}r_1{-}g{-}f{-}e \qquad (p_5=f)
\]
or
\[
a^*{-}c{-}q{-}r_1{-}e'{-}T_2{-}e \qquad (p_5=T_2).
\]
H70 already killed \(p_5=b\).

Write \(g\in N(f)\setminus\{e\}\) on the f-ending geodesic.  
Let \(u_g\) be the third neighbour of \(g\) in part A: \(N(g)=\{f,r_1,u_g\}\).

---

## Theorem H89 / H90 (PROVED)

| Edge | Kill |
|------|------|
| **s−g** | path₆ \(s{-}g{-}f{-}e{-}b{-}t{-}v_1\) (residual) |
| **c−g** | path₄ \(a^*{-}c{-}g{-}f{-}e\) ⇒ dist(a\*,e)≤4 ⇒ H52 C₁₆ |

---

## Theorem H105–H109 (PROVED) — C₈ massacre for free nbrs of u_g

Under residual + E–Bset with geodesic through \(g{-}f{-}e{-}b\), any free part-B neighbour \(x\) of \(u_g\) is forbidden if:

| x | Cycle / path |
|---|--------------|
| **v₂** | C₈: \(u_g{-}v_2{-}v_1{-}t{-}b{-}e{-}f{-}g{-}u_g\) |
| **v₄** | C₈: \(u_g{-}v_4{-}v_3{-}v_2{-}T_2{-}e{-}f{-}g{-}u_g\) |
| **v₀** | C₈: \(u_g{-}v_0{-}v_1{-}t{-}b{-}e{-}f{-}g{-}u_g\) |
| **T₃** | C₈: \(u_g{-}T_3{-}v_3{-}v_2{-}T_2{-}e{-}f{-}g{-}u_g\) |
| **δ** | C₈: \(u_g{-}\delta{-}s{-}a^*{-}c{-}q{-}r_1{-}g{-}u_g\) (uses geodesic) |
| **e** | C₄: \(u_g{-}e{-}f{-}g{-}u_g\) |
| **t** | path₆ \(a^*{-}c{-}q{-}r_1{-}g{-}u_g{-}t\) ⇒ dist(a\*,t)≤6 |
| **q** | C₄: \(u_g{-}q{-}r_1{-}g{-}u_g\) |

**Corollary.** Free stubs of \(u_g\) land only in \(\{e',\,m,\,\beta,\,T_5\text{-or-}w,\,\text{pure exterior B}\}\), with further cuts:
- \(u_g{-}e'\) and \(r_1{-}e'\) cannot coexist (C₄ \(r_1{-}e'{-}u_g{-}g{-}r_1\)).
- \(T_5\) saturated ⇒ \(u_g{-}T_5\) forces \(u_g\in\{\varepsilon,v_5,w\}\); \(u_g=v_5\) is C₈ via \(g{-}v_5{-}v_4{-}v_3{-}v_2{-}T_2{-}e{-}f{-}g\).

---

## Theorem H94 (PROVED)

Under f-ending DS: **no r₁−v₂** (else \(a^*{-}c{-}q{-}r_1{-}v_2{-}v_1{-}t\) length 6 ⇒ dist(a\*,t)≤6).

Under T2-ending: **no r₁−e** (path₄ to e), **no r₁−β** (H70 path through b−e).

---

## Theorem H115 (PROVED) — layer law

Under Arm A DS with \(\operatorname{dist}(a^*,e)=6\):

| Vertex | Layer from e |
|--------|----------------|
| e | L0 |
| p₅ ∈ {f,T₂} | L1 |
| g or e′ | L2 |
| r₁ | L3 |
| q | L4 |
| c | L5 |
| **a\*** | **L6** |

*Proof.* Geodesic forces successive layers. Triangle with dist(a\*,c)=1 and dist(e,c)=5 ⇒ dist(e,a\*)=6 places a\* in L6. ∎

**Corollary.** \(N(a^*)=\{s,c_1,c_2\}\subset L_5\cup L_7\). Geodesic c’s live in L5.

---

## Theorem H71 / H82 (recall)

No \(g{-}b\) (C₄); under DS no \(g{-}b_2\), \(g{-}v_1\), \(g{-}T_2\) (C₄).

---

## Status after Fire 20

| Pin | Status |
|-----|--------|
| p₅=b | **DEAD** (H70) |
| u_g spine C₈s | **PROVED** (H105–H109) |
| layer a\*∈L₆ | **PROVED** (H115) |
| s−g, c−g | **PROVED** (H89/H90) |
| p₅=f fully empty | OPEN — u_g only exterior/e′/m/β left |
| p₅=T₂ fully empty | OPEN — r₁ third stub exterior; e′ at dist 4 |
| Arm B | OPEN |

### Next vector
1. **u_g−e′** or pure exterior: force path₆ to t or C₈ with L6 law.  
2. **p₅=T₂:** r₁’s third stub + e′ at dist 4 (H78) ⇒ Menger length-8 s–v₁ avoiding v₂.  
3. Push both kills ⇒ Arm A empty ⇒ only Arm B ⇒ QB⊥QF finish.

## Property tests
- No residual+E–Bset+f-geodesic with u_g−v0/v2/v4/T3/δ  
- Layer labels on any synthetic dist(a\*,e)=6 model: a\* at hop-count 6 from e  
