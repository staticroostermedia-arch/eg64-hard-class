# Fire 31 — Arm B structure lock; B2 C₁₆ criterion; H390-style map

## Scope

Arm A is empty (H470). Remaining double-stretch branch: **Arm B** (no E–Bset),
split by H47 into **B1** (local girth ≥10 on v₂T₂) and **B2** (path₄ T₂–e–f–T₃–v₃).

---

## Setup (Arm B)

- Residual bad (Fire 14): P₈, C₆ˢ, a\*, T₂−v₂, …
- No E–Bset ⇒ dist_{G−v₂}(v₁,T₂) ≥ 8 (H43)
- E = {e₁,e₂} = N(T₂)\{v₂}; |F| = 4 exclusive (H46/H49)

### B2 attachments
\[
T_2{-}e_1{-}f_1{-}T_3{-}v_3,\quad
C_6=(e_1,T_2,v_2,v_3,T_3,f_1),\quad
Z=v_1{-}v_0{-}v_5{-}v_4{-}v_3{-}T_3{-}f_1{-}e_1{-}T_2
\]
(length 8). e₁ also meets f₁b; e₂ meets f₂a,f₂b.

---

## Theorem H475 (PROVED) — F ↛ Bset

Any f∈F meeting b∈Bset yields
\(v_1{-}t{-}b{-}f{-}e{-}T_2\) length **5**, contradicting Arm B. ∎

## Theorem H479–H482 (PROVED) — T₃ free stub

Cubic: \(N(T_3)=\{v_3,f_1,x\}\) (exactly one free).

| x | Kill |
|---|------|
| e₁ | C₄ with f₁ |
| e₂ | path₇ v₁…T₃−e₂−T₂ |
| b∈Bset | path₆ via t |
| c∈{c₁,c₂} | **C₈** (H493) |
| ε | C₈ |
| w=third(T₅) | C₈ |
| f₁b | C₄ e₁−f₁−T₃−f₁b |

**Survivors:** exterior, or f₂a / f₂b (same part links).

## Theorem H493 (PROVED) — T₃−c ⇒ C₈

\[
(v_0,v_1,v_2,v_3,T_3,c,a^*,s)
\quad\text{and}\quad
(v_0,v_5,v_4,v_3,T_3,c,a^*,s)
\]
both C₈. ∎

---

## Theorem H491 (PROVED) — dist(a\*,f₁) ∈ {3,5,7}

Path \(a^*{-}s{-}v_0{-}v_1{-}v_2{-}T_2{-}e_1{-}f_1\) has length **7**
⇒ dist ≤ 7.

Parts: a\* even, f₁ odd ⇒ dist odd.

- dist = 1 (edge a\*−f₁): path₆ v₁…a\*−f₁−e₁−T₂ ⇒ **Arm B kill**
- ⇒ **dist ∈ {3,5,7}**

## Theorem H490 (PROVED) — dist(a\*,f₁)=5 ⇒ C₁₆

Length-5 path \(a^*{-}p_1{-}p_2{-}p_3{-}p_4{-}f_1\) yields C₁₆
\[
(a^*,p_1,p_2,p_3,p_4,f_1,e_1,T_2,v_2,v_3,v_4,v_5,T_5,\varepsilon,\delta,s)
\]
All residual/B2 edges forced; core C₄/C₈-free. **EG holds.** ∎

## Theorem H495 (PROVED) — dist=3 only through {c₁,c₂}

N(a\*)={s,c₁,c₂} saturated. Length-3 path a\*−x−y−f₁ ⇒ x∈{s,c₁,c₂}.

- x=s ⇒ path₆ v₁−v₀−s−y−f₁−e₁−T₂ (y≠v₀) ⇒ **Arm B kill**
- ⇒ x∈{c₁,c₂}: \(a^*{-}c_1{-}y{-}f_1\) (wlog)

### y-forbids under dist=3 (machine)

| y meets | Result |
|---------||--------|
| s, δ, T₅, v₀,v₄,v₅, e₂, b, t, a\* | short dist or kill |
| ε, w | **C₈** (+ often C₁₆) |
| f₁b | C₄ |
| f₂a | C₈ |
| c₂ | C₄ a\*−c₁−y−c₂ |
| pure exterior | open (C₁₄ only so far) |

**H490 already kills dist=5.** Open B2 pin: **dist∈{3,7}** with y / T₃ free exterior.

---

## Near-miss C₁₄ (not EG)

dist=3: \((a^*,c_1,y,f_1,e_1,T_2,v_2,v_3,v_4,v_5,T_5,\varepsilon,\delta,s)\) is C₁₄.
Useful scaffold, not a power-of-2 win.

---

## B1 status

| Fact | Status |
|------|--------|
| Local girth ≥10 on v₂T₂ | H47 |
| Moore cubic bipartite g=10 | n≥62 |
| Global residual C₆ | **n>62** strict |
| H31 | only n<62 |
| Minimal F-paths for dist=8 | exist via Bset chain length 5; no forced C₁₆ yet |

B1 remains open for unlimited n; finite range already covered if n≤62.

---

## Board after Fire 31

```
double-stretch
├─ Arm A  DEAD (H470)
└─ Arm B
     ├─ B2: dist(a*,f1)=5 → C16 (H490)
     │      dist=3,7 exterior pin OPEN
     │      T3/f1 forbids locked (H475–H493)
     └─ B1: n>62; C16 open
```

## Next vector
1. Kill dist=7 (force path length 5 a\*–f₁ via c₁ stubs / C₄-free expansion)  
2. Kill dist=3 exterior y (third of y + third of c₁)  
3. B1: paste residual C₆ with long F-chains → C₁₆  
4. Master writeup: hard EG ⇔ Arm B pin only  

## Property tests (`verify_fire31.py`)
- T₃−c₁ ⇒ C₈  
- dist(a\*,f₁)=5 skeleton ⇒ C₁₆, no C₄/C₈  
- f₁−b₁ ⇒ dist_{G−v₂}(v₁,T₂)<8  
- a\*−f₁ ⇒ dist<8  
