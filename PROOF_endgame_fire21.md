# Fire 21 — Layer adjacency, C₁₆ framework, pure-T2 structure

## Goal

Shrink Arm A double-stretch to exterior-only free stubs with explicit
bookkeeping; lock the C₁₆ criterion and residual forbids on e′-third.

---

## Theorem H125 (PROVED) — u_g ∈ L₃(e)

On an f-ending geodesic, \(g\in L_2(e)\) and \(u_g\in N(g)\setminus\{f,r_1\}\) (part A).

BFS layers from \(e\): adjacent vertices differ by at most 1 in distance.  
So \(\operatorname{dist}(e,u_g)\in\{1,2,3\}\). Part A ⇒ odd ⇒ \(\in\{1,3\}\).

- dist 1 ⇒ \(u_g\in L_1=\{T_2,b,f\}\), all forbidden (C₄ / already used as \(f\)).  
- **⇒ dist = 3: \(u_g\in L_3(e)\).** ∎

---

## Theorem H120 (PROVED) — no r₁−β under residual+E–Bset

If \(r_1{-}\beta\) with \(\beta=N(b)\setminus\{t,e\}\):
\[
a^*{-}c{-}q{-}r_1{-}\beta{-}b{-}e
\]
is a length-6 geodesic ending \(b{-}e\) ⇒ **H70 ⇒ C₁₆**. ∎

---

## Theorem H141 (PROVED framework) — C₁₆ criterion under residual bad

Under residual bad, \(\operatorname{dist}_{G-v_0}(s,v_1)\ge 8\), and \(P_8\) is a length-8 path.

**C₁₆** arises iff there exists another \(s\)–\(v_1\) path of length 8 in \(G-v_0\) whose
interior is **disjoint** from \(\operatorname{int}(P_8)\).

*Near-miss (T2-ending):*
\[
S:\ s{-}a^*{-}c{-}q{-}r_1{-}e'{-}T_2{-}v_2{-}v_1
\]
has length 8 but \(\operatorname{int}(S)\cap\operatorname{int}(P_8)=\{v_2\}\) ⇒ only C₁₄.  
No diversion around \(v_2\) (T₂ and e′ saturated; forbids block e′−{v₀,t,v₂}). ∎

---

## Theorem H133 (PROVED) — pure T2-ending forces r₁’s third stub into L₄

Pure T2-ending geodesic: \(a^*{-}c{-}q{-}r_1{-}e'{-}T_2{-}e\) (no r₁−g).

\(N(r_1)=\{e',q,x\}\). Layer law: \(x\in L_2\cup L_4\).

| x | Status |
|---|--------|
| t / via N(t) | residual / H40 |
| β | H120 / H70 |
| v₂ | C₄ with e′−T₂ |
| g∈N(f) | **not pure** — dual ending |
| e | H52 |
| **L₄ exterior** | only pure-T2 option |

**⇒** pure T2 ⇒ \(x\in L_4\setminus\{q\}\). ∎

---

## Theorem H140 (PROVED) — b₂ free stubs avoid E–Bset / f-neighbourhood

Under DS: no b₂−e (C₄), no b₂−e′ (dist(a\*,t)≤6 via e′ when dist(a\*,e′)=4; else dual cuts),  
no b₂−g for g∈N(f)\{e} (H82), no b₂−q (H40).

**⇒** b₂ does **not** absorb L₂ stubs from {e′, g₁, g₂}.  
Those **6 stubs** land in \(L_3\setminus\{v_1,b_2\}\). ∎

---

## Theorem H149 (PROVED) — third of e′ avoids s

Under u_g−e′: \(N(e')=\{T_2,u_g,z\}\).  
If \(z=s\): path \(s{-}e'{-}T_2{-}v_2{-}v_1\) has length **4** (or with T₂−v₂−v₁ length 3 from e′),  
and \(s{-}z{-}e'{-}T_2{-}v_2{-}v_1\) length **5** if z is between — directly:
\[
s{-}e'{-}T_2{-}v_2{-}v_1 \quad\text{length 4 if }s{-}e',\ \text{or}\quad s{-}z{-}e'{-}T_2{-}v_2{-}v_1\text{ length 5}.
\]
Either **contradicts residual bad** (dist(s,v₁)≥8).  
Also \(z\neq a^*\) (else dist(a\*,e′)≤2 ⇒ path₄ to e ⇒ H52). ∎

---

## Theorem H151 (structure) — u_g−β forces β exterior and ≠v₄,T₃

H105/H109 already bar u_g−{v₄,T₃}.  
So u_g−β ⇒ β pure exterior L₂, with r₁−β forbidden (H120).

---

## Arm A map after Fire 21

```
Arm A DS dist(a*,e)=6
├─ p5=b     DEAD (H70)
├─ p5=f
│   └─ u_g ∈ L3 (H125)
│       free stubs ⊆ {e′, m, β_ext, L2_ext, L4_ext}
│       barred: v0,v2,v4,T3,δ,e,t,q (H105–109)
│       r1−β dead (H120)
└─ p5=T2
    ├─ dual (r1−g): both endings, C6 e′-T2-e-f-g-r1
    └─ pure: r1 third ∈ L4 only (H133); g1,g2 need foreign L3 (H140)
```

### Next vector (Fire 22)
1. **L₂→L₃ handshake:** 6 stubs into L₃\{v₁,b₂}, each L₃-vert ≤2 L₂-edges,  
   r₁ absorbs 1 (e′ or g); force u_g and u_{g′} to create L₄ bridge ⇒ path₄ a\*–e.  
2. **u_g−e′:** z-third exterior + layer ⇒ path₆ to t or C₈.  
3. **Arm B** in parallel if Arm A stays open one more fire.

## Property tests
- No residual model with r₁−β  
- No residual model with s−e′ or s−z−e′ short path to v₁  
- Layer check: any f-geodesic has u_g at hop-distance 3 from e  
