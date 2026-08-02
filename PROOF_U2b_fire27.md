# Fire 27 — U2b forbids; pure-f C₈ laws

## Theorems (machine-checked cores)

### H371 — s and s₂ cannot both meet c₂
C₄ \(s{-}c_2{-}s_2{-}p_b{-}s\). ∎

### H375 — y and s cannot share an L₅ neighbour
C₈ \(s{-}c{-}y{-}u_g{-}g{-}f{-}g'{-}p_b{-}s\).  
Same for \((y,s_2)\), \((y',s)\), \((y',s_2)\). ∎

### H384 — U2b forbids s−c₁ (and s₂−c₁)
C₈ \(s{-}c_1{-}q{-}r_1{-}e'{-}p_a{-}g'{-}p_b{-}s\).  
Also C₈ via f: \(s{-}c_1{-}q{-}r_1{-}g{-}f{-}g'{-}p_b{-}s\). ∎

### H387 — U2b + c₁−w + c₂−s ⇒ C₈
C₈ \(w{-}c_1{-}a^*{-}c_2{-}s{-}p_b{-}g'{-}p_a{-}w\). ∎

### H391 — y cannot meet both c₁ and c\*
C₄ \(y{-}c_1{-}q{-}c^*{-}y\). ∎

### H399 — pure f forbids s−c₁
C₈ \(s{-}c_1{-}q{-}r_1{-}g{-}f{-}g'{-}p_b{-}s\). ∎

---

## U2b main surviving pattern (H390)

\[
N(c_1)=\{a^*,q,y\},\qquad N(c_2)=\{a^*,s,\tau\}
\]
with \(\tau\notin\{y,y',w,q,s_2\}\) (H289, H371), and \(c_1\not\ni w\) when \(c_2{-}s\) (H387).

### Still forced

| Constraint | Source |
|------------|--------|
| L₅ sets of \(\{y,y'\}\) disjoint | H293 |
| L₅ of w disjoint from y,y' | H297 |
| L₅ of s disjoint from y,y' | H375 |
| s,s₂ disjoint L₅ | H293 |
| y,y',w ↛ c₂ | H289 |
| s,s₂ ↛ c₁ | H384 |
| c₁ free ∈ {y,y′,L₆,…} not {s,s₂,w} under c₂−s | H384/H387 |

### Open

- Complete exclusive L₅ fill for \(\{y',w,s_2\}\) + L₆ without C₈  
- Symmetric \(c_2{-}s_2\) instead of \(c_2{-}s\)  
- \(c_1{-}y'\) instead of \(c_1{-}y\)  
- \(c_1\) → L₆ (neither y nor y′)

---

## Pure f updates

- H368: e′ meets ≤1 of star(g′)  
- H399: s−c₁ forbidden (f-path C₈)  
- z₁=p_a merge C₄/C₈-free at skeleton  
- z₁=u_g forces only one free on u_g (U1-style pure f)

---

## Dual k=4 board after Fire 27

```
U0,U1,U2a     DEAD
U2b           only — H390 pattern heavily constrained
```

## Next vector
1. Kill H390: c₁−y + c₂−s exclusive L₅ remainder.  
2. Kill c₁→L₆ branch.  
3. Pure f z₁=p_a full.  
4. Pure T2.

## Property tests
- U2b core + s−c₁ ⇒ C₈ (two distinct cycles)  
- U2b core + c₁−w + c₂−s ⇒ C₈  
- U2b core + y−s share L₅ ⇒ C₈  
- pure f core + s−c₁ ⇒ C₈  
