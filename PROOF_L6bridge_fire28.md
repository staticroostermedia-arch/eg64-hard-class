# Fire 28 — L₆-bridge map for H390; honest status

## Headline

H390 (the last dual k=4 pattern) is **not fully killed** this fire, but its L₅–L₆
interface is now almost completely classified. Private-L₆ completion is
C₄/C₈-free (computational) — the remaining obstruction must be **cubic cascade**,
**C₁₆ residual**, or a **layer-law** argument.

---

## H390 residual config

\[
N(c_1)=\{a^*,q,y\},\quad N(c_2)=\{a^*,s,\tau\},\quad N(y)=\{u_g,c_1,\alpha\}
\]
plus exclusive L₅ pairs for \(y',w,s_2\) and free \(\sigma\) for \(s\).

---

## Theorem H404 (PROVED) — τ ↛ σ

If \(\tau=c_2\)'s third and \(\sigma=s\)'s other L₅: C₄ \(s{-}\sigma{-}\tau{-}c_2{-}s\). ∎

---

## Theorem H413 (PROVED) — L₆-bridge map under H390

An L₆ vertex meeting L₅-ports of two of \(\{y,y',w,s,s_2\}\) yields:

| L₅ clusters bridged | C₄/C₈? |
|---------------------|--------|
| y — s (α–σ) | **C₈** via a\* |
| w — s (δ–σ) | **C₈** via g′–p_b |
| w — s₂ (δ–μ) | **C₈** via g′–p_b |
| s₂ internal (μ–ν) | **C₄** (sibling L₅ of s₂) |
| y — y′ (α–β) | free |
| y — w (α–δ) | free |
| y — s₂ (α–μ) | free |
| y′ — w, y′ — s, y′ — s₂ | free |
| s — s₂ (σ–μ) | free |

### τ (c₂'s third L₆) forbids

| Meets L₅ of | Result |
|-------------|--------|
| s (σ) | C₄ H404 |
| w (δ) | C₈ |
| y′ (β/γ) | C₈ via a\* |
| y (α) | C₆ only (OK) |
| s₂ (μ) | free at core |

### c\* (cs) L₆ forbids

| Meets L₅ of | Result |
|-------------|--------|
| y (α) | C₈ via r₁–g–u_g |
| s (σ) | C₈ via a\* |
| w (δ) | C₈ via e′–p_a |
| y′ (β) | C₈ via r₁–g–u_g |
| s₂ (μ) | free at core |

### c\* direct L₄ forbids (Fire 27)

cs−s, cs−s₂, cs−w ⇒ C₈; cs−y + c₁−y ⇒ C₄; **cs−y′ free**.

---

## Theorem H424 (computational) — private L₆ is short-cycle free

Completing every L₅-port with **private** L₆ pairs (no bridges from H413-forbidden
list) yields a bipartite graph with **C₄ = C₈ = 0**.

**Interpretation:** H390 is not killed by C₄/C₈ alone under private completion.
Pads are not cubic — cascade or C₁₆ must finish the job.

---

## C₁₆ residual status

Under H390 + spine:
- exactly **one** length-8 \(s_{\mathrm{spine}}\!\to\!v_1\) path:
  \(s_{\mathrm{spine}}{-}a^*{-}c_1{-}q{-}r_1{-}e'{-}T_2{-}v_2{-}v_1\)
- many length-10 paths via \(c_2{-}s\) and via \(y\)
- **zero** disjoint length-8 pairs ⇒ H141 C₁₆ not forced yet

---

## Pure f notes

- H399 s−c₁ still holds  
- pure f + cs−s ⇒ C₈ (same as dual)  
- z₁=p_a, z₂=u_g skeleton C₄/C₈-free (u_g has one free only)

---

## Dual k=4 board after Fire 28

```
U0,U1,U2a     DEAD
U2b / H390    alive but L6-bridge locked;
              private completion C48-free;
              needs cubic cascade or C16
```

## Next vector
1. Cubic L₆–L₇ cascade overflow under H413 free-bridge constraints.  
2. Force a second length-8 \(s_{\mathrm{spine}}\!\to\!v_1\) path (C₁₆).  
3. c₁→L₆ branch.  
4. Pure f z₁=p_a with H399 L₅ laws.

## Property tests
- H390 + τ−σ ⇒ C₄  
- H390 + τ−δ ⇒ C₈  
- H390 + α−σ L₆ bridge ⇒ C₈  
- H390 + δ−μ L₆ bridge ⇒ C₈  
- private L₆ completion ⇒ no C₄/C₈  
