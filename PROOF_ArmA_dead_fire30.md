# Fire 30 — BREAKTHROUGH: Arm A double-stretch forces C₁₆

## What was stopping us

Fires 24–29 analyzed the **dual L₃\* skeleton in isolation** from the residual
P₈. Local C₄/C₈ casework on H390 plateaued because that core is short-cycle-free.

The dual/geodesic does not live in a vacuum: under residual bad it is attached to
**a\*** which is attached to **s**, which sits on **P₈ / C₆ˢ**. Coupling those
forced edges produces a **C₁₆ immediately**.

---

## Theorem H470 (PROVED) — Arm A is empty

**Assume:** residual bad (Fire 14) + E–Bset + double-stretch with
\(\operatorname{dist}_{G''}(a^*,e)=6\) (H48).

Then there is a length-6 geodesic from \(a^*\) to \(e\) in \(G''\), ending at
\(q_5\in\{f,T_2\}\) (not \(b\), H70).

### Case A — f-ending: \(a^*{-}c{-}q{-}u{-}g{-}f{-}e\)

**C₁₆:**
\[
(v_0,v_1,v_2,T_2,e,f,g,u,q,c,a^*,s,\delta,\varepsilon,T_5,v_5)
\]

| Edge | Source |
|------|--------|
| \(v_0{-}v_1{-}v_2\) | residual C₆ |
| \(v_2{-}T_2\) | cubic at \(v_2\) |
| \(T_2{-}e{-}f\) | E–Bset |
| \(f{-}g{-}u{-}q{-}c{-}a^*\) | geodesic |
| \(a^*{-}s{-}\delta{-}\varepsilon{-}T_5{-}v_5\) | residual \(s\)-star + P₈/C₆ˢ |
| \(v_5{-}v_0\) | residual C₆ |

### Case B — T₂-ending: \(a^*{-}c{-}q{-}u{-}e'{-}T_2{-}e\)

**C₁₆:**
\[
(v_0,v_1,t,b,e,T_2,e',u,q,c,a^*,s,\delta,\varepsilon,T_5,v_5)
\]

| Edge | Source |
|------|--------|
| \(v_0{-}v_1{-}t{-}b{-}e\) | residual + E–Bset |
| \(e{-}T_2{-}e'{-}u{-}q{-}c{-}a^*\) | geodesic |
| \(a^*{-}s{-}\cdots{-}v_5{-}v_0\) | residual |

### Both cases

- All 16 vertices distinct under residual labeling  
- Graph remains C₄-free and C₈-free on the forced core  
- **C₁₆ is a power-of-2 cycle ⇒ hard-class EG holds**  
- **Double-stretch Arm A cannot occur**

∎

---

## Corollaries

| ID | Statement |
|----|-----------|
| **H471** | Dual ending (r₁−g) under Arm A ⇒ C₁₆ (subcase of A) |
| **H472** | Pure f / pure T2 geodesics under Arm A ⇒ C₁₆ (same) |
| **H473** | **H390 is dead** — not by L₅ casework, by H470 |
| **H474** | Entire Arm A branch of the double-stretch tree is **empty** |

---

## Why H141 near-miss is not a contradiction

Path \(S = s{-}a^*{-}c{-}q{-}r_1{-}e'{-}T_2{-}v_2{-}v_1\) shares \(v_2\) with \(P_8\)
⇒ C₁₄ only (H141). The **H470 cycles use a different return** through
\((v_5{-}v_0)\) or \((t{-}b{-}e)\), never needing a second internally disjoint
length-8 \(s\)–\(v_1\) path. Different C₁₆, still EG.

---

## Updated decision tree

```
hard cubic bipartite C4/C8-free
├─ n < 62 → EG (H31)
└─ all n
   residual bad?
   ├─ no  → H-bridge / walk chain → C16 (Fires 11–14)
   └─ yes → P8 length 8
        ├─ dist_{G''}(a*,t)=6 → C16 (H41)
        └─ double-stretch
             ├─ Arm A (E–Bset) → C16 (H470)  ★ DEAD
             └─ Arm B (no E–Bset)
                  ├─ B1: local girth ≥10 → n>62 open pressure
                  └─ B2: |F|=4, T3 type — open
```

---

## What was wrong with Fires 24–29

Not the local lemmas (those still hold). The **strategy**: trying to kill dual
by L₃–L₆ adjacency alone, without pasting onto residual C₆/P₈. The global
lemma is a **cycle through both halves**, length 16, all edges already forced
by definitions of residual bad + E–Bset + dist(a\*,e)=6.

---

## Property tests (`verify_fire30.py`)

- f-ending geodesic + residual + E–Bset ⇒ ∃ C₁₆, no C₄/C₈  
- T₂-ending geodesic + residual + E–Bset ⇒ ∃ C₁₆, no C₄/C₈  
- residual + E–Bset alone ⇒ no C₁₆ (geodesic necessary)

## Next vector
1. Arm B2 (path Z + C₆ through T₃)  
2. Arm B1 (girth-10 + global C₆ ⇒ C₁₆ / n bound)  
3. Audit residual-**good** chain for publishable completeness  
4. Master writeup: hard-class EG reduces to Arm B only  

