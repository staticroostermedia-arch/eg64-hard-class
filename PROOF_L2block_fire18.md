# Fire 18 — L2-block: c and s stay outside B(e,3)

## Goal

Under residual bad + E–Bset, force the geometry of Arm A double-stretch into an
impossible expansion, and lock residual-only forbids usable by Arm B.

---

## Theorem H55 (PROVED) — L2-block for {c₁,c₂}

Work in \(G''=(G-v_0)-\mathrm{int}(P_8)\). Let \(e\) be the E–Bset vertex with
\(N(e)=\{T_2,b,f\}\). Layers from \(e\):

| Layer | Part | Contents (forced) |
|-------|------|-------------------|
| L0 | B | \(e\) |
| L1 | A | \(T_2,b,f\) |
| L2 | B | at least \(e',t\) and \(N(f)\setminus\{e\}\); plus β if β∈G'' |

For \(c\in\{c_1,c_2\}=N(a^*)\setminus\{s\}\):

- **c−e:** dist(a\*,e)=2 ⇒ dist(a\*,t)≤4, contradicts H40.  
- **c−q for q∈L2:** path \(a^*{-}c{-}q{-}P_2{-}e\) has length 4 ⇒ dist(a\*,e)≤4 ⇒ **C₁₆ by H52**.

**⇒ no edge from {c₁,c₂} into L0∪L2 without already giving C₁₆.**

---

## Theorem H56 (PROVED) — residual edge forbids

| Edge | Kill | Needs E–Bset? |
|------|------|----------------|
| **s−T₃** | path₄ \(s{-}T_3{-}v_3{-}v_2{-}v_1\) | **no** |
| **b−m** | path₆ \(s{-}\delta{-}\varepsilon{-}m{-}b{-}t{-}v_1\) | yes |
| **c−v₄** | path₆ \(s{-}a^*{-}c{-}v_4{-}v_3{-}v_2{-}v_1\) | no |
| **c−e′** | path₄ \(a^*{-}c{-}e'{-}T_2{-}e\) ⇒ H52 | yes |
| **c−δ** | C₄ \(a^*{-}c{-}\delta{-}s{-}a^*\) | no |
| **c−v₀** | C₄ \(a^*{-}c{-}v_0{-}s{-}a^*\) | no |

**Corollary.** Under residual bad alone, **s−T₃ is impossible**.

---

## Theorem H57 (PROVED) — β = N(b)\{t,e} options

Under residual + E–Bset, β ∉ {δ, e′, m, T₅, v₀, v₂, t, e}.  
Remaining: **β ∈ {v₄, T₃, exterior part-B}**.

- If β=v₄: in G'', b loses v₄ so deg_{G''}(b)=2 (only t,e).  
- If β=T₃: no s−T₃ (H56); no c−T₃ under no-C₁₆ (else a\*−c−T₃−b−e length 4).  
- If β exterior: β∈L2, so c−β forbidden by H55 under no-C₁₆.

---

## Theorem H58 (PROVED) — L1 is stub-saturated in G''

In G'' under E–Bset:

| Vertex | N_{G''} | Full? |
|--------|---------|-------|
| T₂ | {e, e′} (v₂ gone) | **yes** (deg 2) |
| b | {t, e, β} or {t,e} if β=v₄ | **yes** |
| f | {e, g₁, g₂} | **yes** |

**⇒ L1 absorbs zero free stubs from L2.**  
All free L2 stubs (from e′, g₁, g₂, and β if present: **6–8 stubs**) enter L3∪L5∪… .

---

## Theorem H59 (PROVED) — {c₁,c₂,s} lie outside B(e,3)

Under residual + E–Bset + no C₁₆ yet:

- dist(e,c) ≠ 1 (c−e H40)  
- dist(e,c) ≠ 3 (else a\*−c + path₃ to e ⇒ dist(a\*,e)≤4 ⇒ H52)  
- **⇒ dist(e,c) ≥ 5** for c∈{c₁,c₂}

- dist(e,s) ≠ 1 (s−e residual path₄)  
- dist(e,s) ≠ 3 (else path₃ + s−a\* ⇒ dist(a\*,e)≤4 ⇒ H52)  
- **⇒ dist(e,s) ≥ 5**

So the entire a\*-star {s,c₁,c₂} sits **outside B(e,3)**.

**Corollary for Arm A double-stretch.**  
dist(a\*,e)≥6 with geodesics of the form a\*−c−P₅−e (c at distance 5 from e).  
The 4 stubs of {c₁,c₂} land in L4(e)∪L6(e)∪… only.

---

## Theorem H60 (structure) — L2 free-stub dump

Forced L2 part-B set under E–Bset in G'':
\[
\{e',\,t\}\ \cup\ N(f)\setminus\{e\}\ \cup\ (\{\beta\}\text{ if }\beta\in G'')
\]
Size 4 (if β=v₄) or 5 (if β exterior/T₃).

Free stubs from L2 into L3+: **6 (β=v₄) or 8 (β exterior)**, since L1 is full (H58).

c₁,c₂ ∉ L3 (H59), so these stubs feed a pure L3 population **disjoint from the a\*-star**.

---

## Arm B note

H56 (s−T₃ path₄) is residual-only — applies inside Arm B / B2 as well, cutting T₃ from s.

QB⊥QF (H53) + |F|=4 (H49) + s−T₃ forbid still pin B2.

---

## Status after Fire 18

| Claim | Status |
|-------|--------|
| L2-block for c (H55) | **PROVED** |
| s−T₃ path₄ (H56) | **PROVED** (residual-only) |
| c outside B(e,3) (H59) | **PROVED** |
| L1 saturated, L2 dumps to L3+ (H58/H60) | **PROVED** |
| Arm A: dist(a\*,e)≤4 always | OPEN — hinge is force one L2 contact or L4 shortcut |
| Arm B empty | OPEN — B2 + QB⊥QF |

### Next hinge (Arm A)
The 4 stubs of {c₁,c₂} into L4(e) and the 6–8 stubs of L2 into L3 must meet in L3–L4.  
C₄-free bipartite adjacency between L3 and L4 is a biregular graph whose edge count  
forces either a length-4 a\*–e path (C₁₆) or a C₈ with the E–Bset spine.

### Next hinge (Arm B)
B2: T₃∈QF with s−T₃ forbidden; feed Z through the only remaining T₃-stub and overflow QB⊥QF.

## Property tests
- s−T₃ never an edge under residual labelling on hard CAT  
- no c−e, c−e′, c−t under residual+E–Bset candidates  
- deg_{G''}(T₂)=2 always when P₈ removes v₂  
