# Fire 24 — a*-bridge C₈ lemma; dual k=4 collapse (partial)

## Theorem H289 (PROVED) — a*-bridge C₈

**Setup (dual ending, c₁−q on the geodesic).** Let \(c_1,c_2\) be the two L₅
neighbours of \(a^*\).

**Lemma.** If \(y\in L_4\) is adjacent to \(u\in L_3^*\) and there is a length-4 path
\[
y{-}u{-}\cdots{-}r_1{-}q
\]
in the dual skeleton, then **\(y{-}c_2\) is forbidden**:
\[
y{-}c_2{-}a^*{-}c_1{-}q{-}r_1{-}\cdots{-}u{-}y \quad\text{is a C₈}.
\]

### Instances under dual k=4 tight

| L₄ nbr | Length-4 path to q | Forbidden edge |
|--------|--------------------|----------------|
| \(y\) nbr of \(u_g\) | \(y{-}u_g{-}g{-}r_1{-}q\) | \(y{-}c_2\) (**H279**) |
| \(w\) nbr of \(p_a\) | \(w{-}p_a{-}e'{-}r_1{-}q\) | \(w{-}c_2\) (**H267**) |

**Corollary H290.** Every L₄-neighbour of \(\{u_g,p_a\}\) has its L₅-neighbours in
\(\{c_1\}\cup(L_5\setminus\{c_1,c_2\})\) only — **never \(c_2\)**. ∎

---

## Theorem H261 (PROVED) — U0a + c₁−s ⇒ C₈

Under U0 (u_g both free L₂) + H247 \(N(p_b)=\{g',q,s\}\) + \(c_1{-}s\):
\[
s{-}c_1{-}q{-}r_1{-}e'{-}p_a{-}g'{-}p_b{-}s. \quad\square
\]

---

## Theorem H293 (PROVED) — sibling L₄s cannot share L₅

If \(y,y'\) are both L₄-neighbours of the same \(u\in L_3^*\), they share no L₅
neighbour (else C₄ \(y{-}c{-}y'{-}u{-}y\)). ∎

---

## Theorem H297 (PROVED) — w cannot share L₅ with y or y′

Under U2 (\(N(u_g)=\{g,y,y'\}\), \(N(p_a)=\{g',e',w\}\)):
if \(w\) and \(y\) share L₅-nbr \(c\), then
\[
y{-}c{-}w{-}p_a{-}e'{-}r_1{-}g{-}u_g{-}y \quad\text{is C₈}.
\]
Same with \(y'\). ∎

---

## Theorem H299 (PROVED) — s cannot share L₅ with y

Under H247 \(p_b{-}q{-}s\): if \(s\) and \(y\) share L₅-nbr \(c\), then
\[
s{-}c{-}y{-}u_g{-}g{-}r_1{-}q{-}p_b{-}s \quad\text{is C₈}. \quad\square
\]

---

## Dual k=4 status after Fire 24

### Forced under U0 (both free of u_g in L₂)
Budget ⇒ W-L4 and P2. With H247: U0a config.

| Subbranch | Status |
|-----------|--------|
| c₁−s | **DEAD H261** |
| c₂−w | **DEAD H267** |
| c₁−w + c₂−s | **DEAD H262** |
| c₁−w + c₂−w | **DEAD H264** |
| c₁→L₆, c₂−s only, w on tertiary L₅ | open micro |
| c₁→L₆, c₂→L₆, w/s on tertiary only | open micro |

### Under U2 (both free of u_g in L₄) + H247
| Tool | Effect |
|------|--------|
| H289 | y,y',w avoid c₂ |
| H293 | y,y' disjoint L₅ |
| H297 | w disjoint L₅ from y,y' |
| H299 | s disjoint L₅ from y |
| Net | L₅ set forced large; remaining = tertiary-only completions |

### U1 (mixed) 
Open; inherits a*-bridge on the L₄ free stub of u_g.

### z-new (k≥5 dual)
Open; same stars plus isolated z.

---

## Also proved this fire

| ID | Statement |
|----|-----------|
| H255 | E₃₂+E₃₄=12 budget for k=4 |
| H256 | U0 forces W-L4 + P2 |
| H281 | y cannot meet both c₁ and c₂ (C₄ via a*) |

---

## Next vector
1. Close U0a tertiary microbranches (c₁→L₆).  
2. Close U2 tertiary (H297 forces |L₅|≥7 — overflow vs cubic?).  
3. U1 + pure f as dual-without-r₁−e′.  
4. Pure T2 at |L₃*|≥5.

## Property tests
- No dual model with L₄-nbr of u_g or p_a adjacent to c₂  
- No dual U0a model with c₁−s or c₂−w  
- Sibling L₄s of one L₃* have disjoint L₅ neighbourhoods  
