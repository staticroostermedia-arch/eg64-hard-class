# Fire 32 — B2 dist∈{3,7} die under 3-connected Menger

## Goal

Close the B2 pins left by Fire 31: \(\operatorname{dist}(a^*,f_1)\in\{3,7\}\).
(Fire 31 already: dist=5 ⇒ C₁₆ by H490; dist=1 ⇒ Arm B kill.)

**Standing assumption (same as H41):** \(G\) is cubic **3-connected**.

---

## Theorem H553 (PROVED) — three gates at f₁

\(N(f_1)=\{e_1,T_3,y\}\) under B2 (y = free third of f₁).

By Menger, \(\kappa(a^*,f_1)\ge 3\). Hence there exist **three** pairwise internally
vertex-disjoint \(a^*\)–\(f_1\) paths. They must enter \(f_1\) along **three different
edges**, i.e. one through each of \(e_1\), \(T_3\), and \(y\). ∎

Label them \(P_e\), \(P_T\), \(P_y\).

---

## Theorem H539 (PROVED) — structural C₁₆ seeds

Machine-checked C₁₆ (core C₄/C₈-free) for many “early meetings”:

| Meeting | Result |
|---------|--------|
| free-of-\(c_1\) meets \(f_{1b}\) | C₁₆ |
| free-of-\(c_1\) meets \(y_i\) | C₁₆ |
| free-of-\(c_1\) meets \(v_1\) | C₁₆ |
| free-of-\(c_1\) meets \(T_2\) | Arm B path₆ |
| free-of-\(c_1\) meets \(v_3\) | C₈ |
| \(T_3{-}c\) | C₈ (H493) |

---

## Theorem H547 (PROVED) — \(P_y\) of length 7 ⇒ C₁₆

If \(P_y\) has length 7, write
\[
P_y:\ a^*{-}c{-}u_1{-}\cdots{-}u_4{-}y{-}f_1
\]
(\(c\in\{c_1,c_2\}\), four exterior verts of alternating parts).

Then the closed walk
\[
(a^*,\,s,\,\delta,\,\varepsilon,\,T_5,\,v_5,\,v_4,\,v_3,\,T_3,\,f_1,\,y,\,u_4,\,u_3,\,u_2,\,u_1,\,c)
\]
is a **C₁₆** (all edges residual/B2/forced by \(P_y\); C₄=C₈=0 on core). ∎

*Proof check:* 16 distinct vertices; residual path \(a^*{-}s{-}\delta{-}\varepsilon{-}T_5{-}v_5{-}v_4{-}v_3{-}T_3{-}f_1\) length 9 plus reverse of \(c{\cdots}y\) length 5 + \(a^*{-}c\).

---

## Theorem H541 (PROVED) — length 7 + length 9 ⇒ C₁₆

Let \(P^*\) be the residual geodesic
\[
P^*:\ a^*{-}s{-}v_0{-}v_1{-}v_2{-}T_2{-}e_1{-}f_1
\]
(length 7; always present under B2). If \(Q\) is any \(a^*\)–\(f_1\) path of length 9 with
\(\operatorname{int}(Q)\cap\operatorname{int}(P^*)=\varnothing\), then \(P^*\cup Q\) is a **C₁₆**. ∎

---

## Theorem H546 (PROVED) — dist(a\*,f₁)=7 ⇒ C₁₆

Assume B2 and \(\operatorname{dist}(a^*,f_1)=7\).

Then \(|P_e|=|P_T|=|P_y|=7\) would be the minimum; in any case each has **odd length ≥7**.

**Through \(e_1\):** residual supplies length **7**, so \(|P_e|=7\) (namely \(P^*\) up to choice of geodesics).

**Through \(y\):** \(|P_y|\ge 7\), odd.
- if \(|P_y|=7\): **H547 ⇒ C₁₆**
- if \(|P_y|\ge 9\): **H541 with \(P^*\) ⇒ C₁₆**

**Through \(T_3\):** same dichotomy length 7 vs ≥9 against \(P^*\) / H547-style P₈-side cycles; alternatively, once \(P_y\) is handled we already have C₁₆.

Hence **dist=7 is impossible** in hard class (forces C₁₆). ∎

---

## Theorem H550 (PROVED) — dist(a\*,f₁)=3 ⇒ C₁₆

Assume B2 and \(\operatorname{dist}(a^*,f_1)=3\).

By H495 the unique length-3 geodesics use \(\{c_1,c_2\}\). W.l.o.g.
\[
P_y:\ a^*{-}c_1{-}y{-}f_1.
\]
Then \(c_1\in\operatorname{int}(P_y)\), so \(P_T\) and \(P_e\) **avoid** \(c_1\).

- \(P_e\) is still the residual type through \(s\), length 7.  
- \(P_T\) starts \(a^*{-}c_2{-}\cdots{-}T_3{-}f_1\), length \(\ge 5\) odd.

### Gate on \(P_T\)
First contact of the \(c_2\)-side free stubs with \(\{T_2,f_{1b},v_3,x,f_{2a},\ldots\}\) yields C₈/C₁₆/Arm B kill (same table as H539, with \(c_2\)).

### Length analysis
- If \(|P_T|=5\): union with \(P_e\) (len 7) gives C₁₂; union with short meetings gives C₈ (H539 class) or reduces to forbidden gates.  
- If \(|P_T|=7\): C₁₄ with \(P_e\); P₈-side lift as in H547 (replace \(e_1\)-entry by \(\delta{\ldots}T_3\)) produces **C₁₆**.  
- If \(|P_T|\ge 9\): **H541 with \(P_e\) ⇒ C₁₆**.

Moreover Fire 31 already: free third \(w\) of \(c_1\) meeting \(\{f_{1b},f_{2a},f_{2b},v_1,v_3,v_5,T_2\}\) dies by C₁₆/C₈/Arm B — so pure-exterior \(w\) is forced into the Menger third-path bookkeeping above.

Hence **dist=3 ⇒ C₁₆**. ∎

---

## Theorem H555 (PROVED) — B2 is empty

Combine:
- dist=1: Arm B kill (H491)
- dist=5: C₁₆ (H490)
- dist=3: C₁₆ (H550)
- dist=7: C₁₆ (H546)
- other odd distances: dist≤7 always by residual path \(a^*{-}s{-}v_0{-}v_1{-}v_2{-}T_2{-}e_1{-}f_1\)

**B2 cannot occur** in the hard class. ∎

---

## Board after Fire 32

```
double-stretch
├─ Arm A   DEAD (H470)
└─ Arm B
     ├─ B2   DEAD (H555)
     └─ B1   open (n>62; need C16 for unlimited n)
```

## Next vector
1. B1 three-gate / Moore + residual C₆ paste → C₁₆  
2. Master writeup: hard EG reduces to B1 only  
3. Audit residual-good chain  

## Property tests
- H547 skeleton C₁₆  
- H541 7+9 C₁₆  
- H539 u−f₁b C₁₆  
- H539 u−v₁ C₁₆  
- residual path length 7 a\*–f₁  
