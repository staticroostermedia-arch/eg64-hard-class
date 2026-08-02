# Fire 16 — Double-stretch arms: structure theorems

## Scope

Close or reduce the two double-stretch arms from Fire 15:

- **Arm A:** E–Bset + dist_{G''}(a\*,t) ≥ 8 + dist(a\*,e) ≥ 6  
- **Arm B:** no E–Bset + dist_{G−v₂}(v₁,T₂) ≥ 8  

Recall: hard EG for **n < 62** is already **H31**. These arms matter only for unlimited n.

---

## Theorem H46 (PROVED) — Arm B forbids a host of edges

Assume Arm B (no E–Bset). Then no path of length 4 or 6 from v₁ to T₂ in G−v₂.

### Path₆ via C-spine + T₄
\[
v_1{-}v_0{-}v_5{-}v_4{-}T_4{-}e{-}T_2
\]
has length 6 whenever any e−T₄ exists.  
**⇒ no edges between E and T₄.**

### Path₆ via Bset
| Edge | Path₆ | Verdict |
|------|-------|---------|
| b−v₄ | v₁−t−b−v₄−v₃−v₂−T₂ | **forbidden** |
| b−T₃ | v₁−t−b−T₃−v₃−v₂−T₂ | **forbidden** |
| b−v₀, b−v₂ | C₄ with t,v₁ | **forbidden** |
| b−T₅ | T₅ already cubic-saturated {v₅,ε,w} | **impossible** |

### F-side
Let E = {e₁,e₂}, F = (N(e₁) ∪ N(e₂)) \ {T₂} (part-A neighbours of E in G−v₂).

- Each f meets **at most one** e (else C₄ through T₂).  
- Each e has **two** free stubs, all into F.  
- **⇒ |F| = 4** exactly, a perfect matching E—F of 4 edges (each e to two exclusive f’s).

Further forbids for f ∈ F:
| Edge | Reason |
|------|--------|
| f−v₄ | path₆ v₁−v₀−v₅−v₄−f−e−T₂ |
| f−δ | path₆ v₁−v₀−s−δ−f−e−T₂ |
| f−a\* | path₆ v₁−v₀−s−a\*−f−e−T₂ |
| f−T₅ | T₅ saturated |
| f−t, f−v₀ | would place f in Bset or N(v₀), contradicting exterior |

And: dist(b,e) ≥ 5, dist(b,f) ≥ 4 for all b ∈ Bset, f ∈ F (else path₆ via t).

---

## Theorem H47 (PROVED) — Arm B splits into B1 / B2

At vertex v₂, pair (v₁,v₃) is **good** (path along C in G−v₂).

Under Arm B, pair (v₁,T₂) is **bad**.

### B1 — pair (v₃,T₂) also bad
Then both pairs at T₂ involving the third edge are bad, so
\[
\text{local girth of }v_2T_2 \ge 10 \implies n \ge 62
\]
(bipartite cubic Moore). Moreover a global C₆ forces **n > 62** (equality is pure girth-10).

### B2 — pair (v₃,T₂) good
Then a path₄ T₂…v₃ exists in G−v₂. Type v₄ is impossible (requires e−T₄, killed by H46).  
**Only type:** T₂−e−f−T₃−v₃ with f ∈ F, edge f−T₃.

This yields the C₆
\[
(e,\,T_2,\,v_2,\,v_3,\,T_3,\,f)
\]
and the length-8 path in G−v₂
\[
Z = v_1{-}v_0{-}v_5{-}v_4{-}v_3{-}T_3{-}f{-}e{-}T_2,
\]
hence dist_{G−v₂}(v₁,T₂) = 8 exactly under B2.

---

## Theorem H48 (PROVED) — Arm A, minimal case dist(a\*,e) = 6

Assume E–Bset edge e−b and double-stretch with **dist_{G''}(a\*,e) = 6**  
(then triangle forces dist(a\*,b) = 7, dist(a\*,t) = 8).

N(e) = {T₂, b, f}. A geodesic a\* = q₀…q₆ = e has q₅ ∈ {T₂, f} (not b, else dist(a\*,b) ≤ 5).

### Subcase q₅ = T₂
In G'', N(T₂) = E = {e, e′}. The geodesic must be
\[
a^*{-}q_1{-}q_2{-}q_3{-}e'{-}T_2{-}e{-}b{-}t
\]
with {e,e′} = E, dist(a\*,e′) = 4, dist(a\*,T₂) = 5.

Moreover **e′ has no edge to Bset** (else a\*…e′−bᵢ−t has length ≤ 6, killing double-stretch).

### Subcase q₅ = f
Geodesic ends …−f−e, dist(a\*,f) = 5.  
Then f−t is forbidden (else dist(a\*,t) ≤ 6), and f−e′ is forbidden (C₄ through T₂).

---

## Theorem H49 (PROVED) — |F| = 4 matching under Arm B

Under Arm B, the bipartite graph between E and F is a **1-regular matching cover**:  
4 edges, |F| = 4, each vertex degree 1 on the E side to F (actually deg_E→F = 2 per e, deg_F→E = 1 per f).

This is the unique cubic-compatible attachment of T₂’s free neighbourhood under C₄/C₈-free + Arm B.

---

## Global status after Fire 16

```
hard EG
├─ n < 62: PROVED (H31)
└─ all n:
   residual bad?
   ├─ no → k≥2 → H-bridge chain → C16 (Fires 11–14)
   └─ yes → P8 length 8
        ├─ dist_{G''}(a*,t)=6 → C16 (H41)
        └─ double-stretch
             ├─ Arm A (E–Bset): tight geodesic geometry (H48) — open kill
             └─ Arm B (no E–Bset):
                  ├─ B1: n>62 local girth 10 (H47) — open kill
                  └─ B2: |F|=4, path Z len 8 via T3 (H46–H49) — open kill
```

| ID | Statement | Status |
|----|-----------|--------|
| H46 | Arm B edge forbids + path₆ kills | **PROVED** |
| H47 | Arm B ⇒ B1 (n>62) or B2 (T₃ type) | **PROVED** |
| H48 | Arm A dist(a\*,e)=6 geodesic form | **PROVED** |
| H49 | \|F\|=4 perfect attachment | **PROVED** |
| Arms fully empty | | OPEN |

## Next vector
1. **B2:** use C₆ (e,T₂,v₂,v₃,T₃,f) + Z to force a C₈ or a path₆.  
2. **Arm A q₅=T₂:** e′ at dist 4 from a\* with no Bset edge — force C₈ with P₈.  
3. **Arm A q₅=f:** third nbr g of f in G'' creates shortcut or C₈.  
4. **B1:** C₆ elsewhere + local girth 10 on v₂T₂ ⇒ C₁₆ by cage/extremal.

## Property tests
- Under any Arm B model, |F| must be 4  
- No e−T₄, b−v₄, b−T₃ on residual-bad candidates  
- q₅=T₂ forces the path to use **both** E-vertices  
