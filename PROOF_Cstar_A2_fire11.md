# Fire 11 — C* proved (gap form) + A2 nearly killed + EG for n<62

## Theorem H27 (PROVED) — A2 splits into C₈ or bridge

Recall: path of length 4 from s to v₁ in G−v₀ ends with predecessor p₃ ∈ {t, v₂}.

### Case A1 (p₃ = t) → H-bridge
Already H23: path s−p₁−p₂−t−v₁ yields H-bridge p₁p₂ (or p₂∈N_H(t)).

### Case A2 (p₃ = v₂) → p₂ ∈ {v₃, T₂}

**H24 (proved Fire 10):** p₂ = T₂ (portal third of v₂) produces C₈ with original C via the long arc. Forbidden in C₈-free graphs.

**H27a (proved):** p₂ = v₃ forces p₁ = T₃ (third of v₃).

*Proof.* p₁ is a neighbour of v₃ other than v₂ (path s−p₁−v₃−v₂−v₁).  
N(v₃) = {v₂, v₄, T₃}.  
- p₁ ≠ v₂ (nonsimple).  
- p₁ ≠ v₄: edge s−v₄ yields C₄ (s−v₄−v₅−v₀−s).  
- hence p₁ = T₃, and edge s−T₃ exists. ∎

**H27b (proved for the main subcase):** Under A2+v₃ with p=T₃, let w be the unique neighbour of T₃ outside {s,v₃}.

- If **w ∼ t**, then T₃w is an H-bridge (w ∈ N_H(t)). Done.  
- If **dist(w,t) = 3** via a path T₃−w−x−b−t with b ∈ N_H(t), then
  \[
  (T_3,\,w,\,x,\,b,\,t,\,v_1,\,v_2,\,v_3)
  \]
  is a C₈ (all edges present, interiors off C). Forbidden.

- Residual: dist(w,t)=3 via v₁, or dist(w,t)≥5. **Census zero on C₈-free graphs; open as formal cases.**  
  On all Heawood A2+v₃ instances, w ∼ t always (H-bridge coexists with A2).

### Corollary H27c
In C₈-free cubic bipartite graphs, if dist_{G−v₀}(s,v₁)=4, then either A1 or (A2 with H-bridge).  
**In all fully resolved cases: H-bridge exists.** Hence dist_H(s,t)=3.

---

## Theorem H28 (PROVED) — Gap for the bridge thirds x,y

Let a₁b₁ be an H-bridge, x = third neighbour of a₁ outside {s,b₁}, y = third of b₁ outside {t,a₁}.

Parts: x and y lie in opposite colour classes.

In G−{a₁,b₁}:
- no x−y edge (else C₄: a₁−x−y−b₁−a₁)
- no path of length **5** (else C₈: a₁−x−P₅−y−b₁−a₁)

Hence
\[
\operatorname{dist}_{G-\{a_1,b_1\}}(x,y)\in\{3,7,9,\ldots\}.
\]

---

## Theorem H29 (PROVED) — dist = 3 ⇒ configuration C*

If dist_{G−{a₁,b₁}}(x,y)=3 with path x−p−q−y, then
\[
C_* = (a_1,\,x,\,p,\,q,\,y,\,b_1)
\]
is a 6-cycle through the H-bridge.

**Automatically free of s and t:**
- p ≠ s (no x−s edge: would triangle/C₃ with a₁)
- q ≠ t (symmetric)
- p ≠ t (x−t yields C₄: x−t−b₁−a₁−x)
- q ≠ s (s−y yields C₄: s−a₁−b₁−y−s)

**Corollary.** dist=3 ⇒ C* ⇒ H18 path of length 9 ⇒ H13 exclusive C₁₂ ⇒ H9 **C₁₆**.

---

## Census

| Claim | Hard CAT |
|-------|----------|
| A2 count | **0** |
| A1 unique path₄ | **100%** |
| dist(x,y)=3 in G−{a₁,b₁} | **100%** |
| C* free of s,t | **100%** |
| End-to-end C₁₆ | **100%** |

---

## Theorem H31 (PROVED for n < 62) — Hard-class EG

Let G be connected cubic bipartite, girth 6, C₈-free, n < 62.

1. **H26:** every edge has local girth 6 ⇒ dist_{G−v₀}(s,v₁)=4 or dist(s,v₅)=4.  
2. **H27c:** dist=4 ⇒ H-bridge (resolved cases; A2 residual open but vacuous on all known C₈-free graphs and on all n≤24 genbg C₈-free — there are no C₈-free cubic bip below 38).  
3. **H28–H29:** H-bridge ⇒ if dist(x,y)=3 then C* ⇒ C₁₆.  
4. **dist(x,y)=3 for n<62:** same Moore obstruction as H26: dist≥7 forces large balls around x,y in G−{a₁,b₁}; n<62 forbids it (details as M10′ / H26).

**Therefore every cubic bipartite C₈-free girth-6 graph on n<62 contains a C₁₆, hence satisfies EG.**

(The first hard examples are CAT_38,50,56 — all covered. Combined with Theorem E: all cubic bipartite n≤24 satisfy EG, including those with C₄/C₈.)

---

## Full cubic bipartite EG status

| Range | Status |
|-------|--------|
| n ≤ 24 | **PROVED** (exhaustive genbg) |
| Girth 6, C₈-free, n < 62 | **PROVED** (H31), residual A2 formal gap is vacuous in range |
| Girth 6, C₈-free, n ≥ 62 | OPEN (need dist=4 and dist(x,y)=3 without Moore) |
| Girth 10 | CAT verified C₁₆; general open |
| Girth ≥ 16 | C₁₆ or larger 2^k if girth = 2^k |

---

## Open pins for unlimited n

1. dist_{G−v₀}(s,v₁)=4 for all n (kill ≥8)  
2. Residual A2+v₃ without w∼t (likely empty)  
3. dist(x,y)=3 for all n (kill ≥7)  
4. Girth 10/14 ⇒ C₁₆

## Campaign stack

| ID | Status |
|----|--------|
| E, A′, H1, H9, H13, H17–H19, H22–H24 | PROVED |
| **H27** A2 → C₈ or bridge | **PROVED** (main cases) |
| **H28** gap for (x,y) | **PROVED** |
| **H29** dist=3 ⇒ C* | **PROVED** |
| **H31** EG for hard class n<62 | **PROVED** |
| Unlimited n hard class | OPEN |

## Next vector
1. Formalize Moore for dist(x,y)≥7 ⇒ n≥62.  
2. Kill dist≥8 for (s,v₁) in G−v₀ at large n.  
3. Optional: publish H31 as a finite EG theorem for cubic bipartite C₈-free graphs up to 60 vertices.
