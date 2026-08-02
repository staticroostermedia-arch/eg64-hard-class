# Fire 29 — Chord forbids; PF4 pure-f k=4; cascade cover exists

## Honest status

| Line | Status |
|------|--------|
| Dual k=4 H390 | **Still open** — free L₆ cover exists (H430); private L₆ C₄₈-free (H424) |
| Pure f **PF4** | New tight k=4 target, heavily constrained |
| Pure T2 | Open, \|L₃\*\|≥5 |

---

## Dual H390: what we proved this fire

### H430 — free-bridge L₆ cover exists
Randomized covering finds **6 L₆** meeting port demand under H413 free-cluster rules.
**⇒ cubic L₆ sharing alone does not obstruct H390.**

### H435–H439 — no short chords on the length-10 residual paths

| Edge | Reason |
|------|--------|
| s−f | C₄ s-f-g′-p_b-s |
| c₂−g′ | C₄ c₂-g′-p_b-s-c₂ |
| p_b−e | C₄ p_b-g′-f-e-p_b |
| a\*−p_b | C₄ a\*-p_b-s-c₂-a\* |
| y−f | C₄ y-u_g-g-f-y |

So the length-10 paths via \(c_2{-}s\) and via \(y\) cannot shorten by those chords.
Still only **one** forced L8: \(s_{\mathrm{spine}}{-}a^*{-}c_1{-}q{-}r_1{-}e'{-}T_2{-}v_2{-}v_1\).

### H441 — edge census (dual U2b / H390)

\[
E_{54}=12,\quad |L_5|\ge 11,\quad E_{56}=21
\]
(If every L₅ has three L₄∪L₆ nbrs.) Compatible with \(m=7\) pure L₆ if no L₇, or \(m\ge 7\) with L₇.

---

## Pure f: PF4 (main tight case)

### Definition H449 (PROVED structure)

Pure f with both e′ free stubs on \(\{p_a,u_g\}\) (legal under H368):
\[
\begin{align*}
N(e')&=\{T_2,p_a,u_g\},\\
N(r_1)&=\{g,q,x\},\\
N(u_g)&=\{g,e',y\},\\
N(p_a)&=\{g',e',w\},\\
N(p_b)&=\{g',s,s_2\},\\
L_3^*&=\{r_1,u_g,p_a,p_b\}\quad (k=4).
\end{align*}
\]
Skeleton is C₄/C₈-free.

### Forbids (machine-checked)

| ID | Forbid | Cycle |
|----|--------|-------|
| H399 | s−c₁ | C₈ via f–g–g′ |
| H452 | w−c₁ | C₈ via f–g–g′–p_a |
| H453 | x−c₁ or x−c\* | **C₄** x-c-q-r₁-x |
| H454 | y−c₂ | C₈ y-c₂-a\*-c₁-q-r₁-g-u_g-y |
| H455 | y−c₁ + w−c₂ | C₈ a\*-c₁-y-u_g-e′-p_a-w-c₂-a\* |
| H368 | e′ meets both p_a and p_b | C₄ |

### Surviving PF4 L₅ pattern (analog of H390)

Likely:
\[
N(c_1)=\{a^*,q,y\},\quad N(c_2)=\{a^*,s,\tau\},
\]
with x’s two L₅ both new (H453), and w avoiding c₁ (H452).

**H455** is new: under PF4, **c₂ cannot meet w if c₁ meets y** — a\*-bridge through e′-u_g path unique to pure f.

---

## Board after Fire 29

```
dual H390     open (cover exists; chords blocked; need new idea)
pure f PF4    open, H390-like box with H453–H455
pure f other  z2=new (larger k); z2=pb DEAD H368
pure T2       open
```

## Next vector
1. **New dual idea:** force s_spine ∈ L₅ (not L₇) ⇒ a\* degree/layer contradiction, or force second L8 via L₅-port path.  
2. PF4 exclusive L₅ map (copy Fire 27–28 toolkit).  
3. pure T2 min k=5 skeleton.

## Scar
Do **not** claim H390 dead. H430 free cover + H424 private C₄₈-free stand.

## Property tests
- H390 + s−f ⇒ C₄  
- PF4 + x−c₁ ⇒ C₄  
- PF4 + y−c₂ ⇒ C₈  
- PF4 + y−c₁ + w−c₂ ⇒ C₈  
- free L₆ cover exists under H413  
