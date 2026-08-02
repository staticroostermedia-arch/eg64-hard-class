# Fire 22 — L2→L3 handshake; dual-|L3*|=3 dies by C₈

## Headline

Under Arm A **dual ending** (r₁ meets both e′ and g) with minimal L₃*
(\(|L_3^*|=3\)), the C₈-free cubic bipartite geometry is **impossible**:
every admissible L₅ completion produces an explicit C₈.

---

## Theorem H178 (PROVED) — L₃ only meets L₂∪L₄

Layer adjacency from \(e\): vertices in L₃ have neighbors only at distances 2–4.  
Part B ⇒ L₂∪L₄. No L₃−e (would collapse distance). No L₃−L₆. ∎

---

## Theorem H154–H156 (PROVED) — critical stub census

L₂_crit = {e′, g, g′} with g,g′ = N(f)\{e} sends **6** edges into  
L₃\* := L₃ \ {v₁, b₂}.

- v₁ leaf on t; b₂ refuses {e′,g,g′} (H140).  
- C₄-free + left degrees 2,2,2 ⇒ **|L₃\*| ≥ 3**. ∎

---

## Theorem H167 (PROVED) — dual forbids u_g−e′

Dual: N(r₁)={e′,g,q}. If also u_g−e′: C₄ r₁−e′−u_g−g−r₁. ∎

---

## Theorem H183–H189 (PROVED) — dual |L₃\*|=3 skeleton

L₃\* = {r₁, u_g, z} with:

| Vertex | Neighborhood |
|--------|----------------|
| r₁ | {e′, g, q} |
| u_g | {g, g′, y} with y∈L₄\{q} |
| z | {e′, g′, w} with w∈L₄\{q,y} |
| g′ | {f, u_g, z} |

Also: no y−z (C₄ via g′), no z−q (C₄ via r₁−e′), no u_g−q (C₄ via r₁−g).  
**⇒ |L₄| ≥ 3** with distinct q, y, w.  

L₃\* is **L₂∪L₄–saturated** (all 9 stubs used). ∎

---

## Theorem H195–H196 (PROVED) — q’s third is a new L₅ vertex

N(q) cannot contain both c₁,c₂ (the two L₅ neighbors of a\*):  
else C₄ a\*−c₁−q−c₂−a\*.  

L₃\* full and barred from q ⇒ q’s third neighbor **c₃ ∈ L₅ \ {c₁,c₂}**.  
N(q) = {r₁, c₁, c₃} (c₁ = geodesic side). ∎

---

## Theorem H202 (PROVED) — dual |L₃\*|=3 ⇒ C₈

y and w each need **two** L₅ neighbors. Casework on c₁’s free stub and the
L₅ matching yields C₈ in every branch that stays C₄-free:

### Main C₈ (c₁−y, c₃−w, c₂−w)
\[
y{-}c_1{-}q{-}c_3{-}w{-}z{-}g'{-}u_g{-}y
\]
All eight edges forced by the skeleton + this matching.

### Via a\* (c₁−y, c₂−w, new c₄)
\[
y{-}c_1{-}a^*{-}c_2{-}w{-}z{-}g'{-}u_g{-}y
\]

### c₁ free to L₆, y−c₂
\[
y{-}c_2{-}a^*{-}c_1{-}q{-}r_1{-}g{-}u_g{-}y
\]

### c₁ free to L₆, y and w both meet {c₂,c₃}
\[
y{-}c_2{-}w{-}z{-}e'{-}r_1{-}q{-}c_3{-}y
\]

### y meets both c₁ and c₂
C₄ a\*−c₁−y−c₂−a\* — immediate kill.

Symmetric cases with c₁−w instead of c₁−y are identical under (y↔w, u_g↔z, g↔e′).

**⇒ dual ending + |L₃\*|=3 is empty in the hard class.** ∎

---

## Status map after Fire 22

| Branch | Status |
|--------|--------|
| dual + \|L₃\*\|=3 | **DEAD (H202 C₈ family)** |
| dual + \|L₃\*|≥4 | OPEN — extra L₃\* verts dilute the skeleton |
| pure f (no r₁−e′) | OPEN — α=1 counting; similar L₄ demand |
| pure T2 (no r₁−g) | OPEN — r₁ third in L₄ (H133); g,g′ need foreign L₃\* |
| p₅=b | DEAD (H70) |

### Next vector
1. Force |L₃\*|=3 under dual (C₄-free maximality / no private L₃\* verts), **or** kill dual k≥4 by the same C₈ patterns.  
2. Pure f: r₁ absorbs only g; mirror handshake.  
3. Pure T2: no g on r₁; g,g′ form a separate L₃\* component → C₈ with E–Bset spine.

## Property tests
- Dual skeleton neighborhoods as in H183  
- No residual dual model with |L₃\*|=3 (search: C₈ y-c1-q-c3-w-z-g'-ug-y)  
- H178: every L₃ nbr in L₂∪L₄  
