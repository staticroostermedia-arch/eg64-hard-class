# Fire 15 — Double-stretch: T₂–T₅ is C₈; E–Bset reduction

## Goal

Kill the last open pin from Fire 14:
\[
\operatorname{dist}_{G-v_0}(s,v_1)=8
\quad\text{and}\quad
\operatorname{dist}_{G''}(a^*,t)\ge 8
\]
(double-stretch), where \(G''=(G-v_0)-\mathrm{int}(P_8)\) and
\(P_8=s{-}\delta{-}\varepsilon{-}T_5{-}v_5{-}v_4{-}v_3{-}v_2{-}v_1\).

---

## Theorem H42 (PROVED) — T₂–T₅ creates a C₈

Under residual bad structure (C₆ˢ = (s,v₀,v₅,T₅,ε,δ) and R as in Fire 13–14),
the edge **T₂–T₅ is forbidden**.

*Proof.* If T₂–T₅ exists, the closed walk
\[
T_2{-}T_5{-}\varepsilon{-}\delta{-}s{-}v_0{-}v_1{-}v_2{-}T_2
\]
is a **simple C₈**:
| Edge | Why present |
|------|-------------|
| T₂T₅ | assumption |
| T₅ε | C₆ˢ |
| εδ | C₆ˢ |
| δs | C₆ˢ |
| sv₀ | third edge |
| v₀v₁ | C |
| v₁v₂ | C |
| v₂T₂ | definition of T₂ |

All eight vertices are distinct under girth ≥ 6 / residual labelling. ∎

**Verified** on hard CAT: T₂–T₅ is always a non-edge; all other seven edges of the putative C₈ are present.

---

## Theorem H43 (PROVED) — Only one possible path₄ type from v₁ to T₂

Work in G−v₂. Neighbours of v₁: {v₀, t} (v₂ gone).  
Neighbours of T₂: {e₁, e₂} (part B; v₂ gone).  
Write E = {e₁,e₂}, Bset = N(t)\{v₁} = {b₁,b₂}.

Any path of length 4 from T₂ to v₁ has the form T₂−e−x−y−v₁ with y ∈ {v₀, t}.

### Type t: T₂−e−x−t−v₁
Requires x ∈ N(e) ∩ N(t) ⇒ x ∈ Bset ⇒ **E–Bset edge** e−b.

### Type v₀: T₂−e−x−v₀−v₁
Requires x ∈ N(e) ∩ N(v₀) = N(e) ∩ {s,v₁,v₅}.

| x | Verdict under residual bad |
|---|----------------------------|
| v₁ | e−v₁ ⇒ T₂−e−v₁; e ∈ N(v₁)\{v₀,v₂} = {t} ⇒ e=t ⇒ T₂t, **C₄** |
| s | e−s ⇒ path **s−e−T₂−v₂−v₁** length 4 in G−v₀, contradicts bad |
| v₅ | e−v₅; but N(v₅) = {v₀,v₄,T₅} with e part B ⇒ e ∈ {v₀,v₄,T₅}; e≠v₀ (C₄), e≠v₄ (C₄ T₂v₄), so **e = T₅** |

Type v₀ with x = v₅ is exactly **T₂–T₅**, forbidden by **H42**.

### Conclusion
Under residual bad + C₈-free:
\[
\operatorname{dist}_{G-v_2}(v_1,T_2)=4
\;\Longleftrightarrow\;
\text{an E–Bset edge exists}.
\]
If no E–Bset edge, then dist_{G−v₂}(v₁,T₂) ∈ {8,10,…} (H36).

---

## Theorem H44 (PROVED) — E–Bset ⇒ short path in G''

If e−b is an E–Bset edge (e ∈ E, b ∈ Bset), then
\[
T_2{-}e{-}b{-}t
\]
lies in G'' (none of e,b,t,T₂ is in int(P₈) ∪ {v₀}: checked by C₄/C₈ forbids of Fire 14), and
\[
\operatorname{dist}_{G''}(t,T_2)=3.
\]

Moreover, by H40/double-stretch constraints:
- path a\*−c−e−b−t has length 4 if c−e for c ∈ N(a\*)\{s} ⇒ **no such c−e** under H40
- dist(a\*,e) ≠ 2 (same reason)
- triangle: dist(a\*,t) ≤ dist(a\*,e) + dist(e,t) = dist(a\*,e) + 2  
  so double-stretch (dist(a\*,t)≥8) ⇒ **dist(a\*,e) ≥ 6**
- if dist(a\*,b) = 5 then dist(a\*,t) ≤ 6, killing double-stretch  
  so double-stretch ⇒ **dist(a\*,b) ≥ 7**

---

## Theorem H45 (PROVED) — C₁₆ unless double-stretch + (no E–Bset or far a\*)

Stack of Fire 14–15:

```
residual bad
  ├─ dist_{G''}(a*,t) = 6  →  Q length 8  →  P8 ∪ Q = C16     [H41]
  └─ dist_{G''}(a*,t) ≥ 8  →  double-stretch
        ├─ E–Bset  →  dist(t,T2)=3, dist(a*,e)≥6, dist(a*,b)≥7   [H44]
        └─ no E–Bset → dist_{G-v2}(v1,T2)≥8                      [H43]
```

Both double-stretch arms are **geometrically extreme** (large distance constraints
among a\*, e, b, t, T₂ simultaneously) and **absent from all census**.

---

## Toward closing double-stretch

### Arm A — E–Bset + dist(a\*,e)≥6 + dist(a\*,t)≥8
e and t lie at distance 2; a\* is at distance ≥6 from e and ≥8 from t.
Bipartite distance geometry + cubic C₄-free expansion around a\* (leaf s in G'')
forces |B(a\*,5)| ≥ 1+3+4+8+16+32 = 64 in the tree bound before hitting e,
so n(G'') ≥ 64 + |B(e,0…)| and n(G) ≥ 72, with further C₈-free constraints
still unused. **Next:** turn the tree bound into a hard contradiction with
the already-placed P₈ / C / C₆ˢ vertices, or force dist(a\*,b)=5.

### Arm B — no E–Bset, dist_{G−v₂}(v₁,T₂)≥8
Then also no path of length 6 (else dist=4 by H36 ⇒ E–Bset by H43).
In particular **no edges between {c₁,c₂} and E** (else
v₁−v₀−s−a\*−c−e−T₂ is a path₆). Combined with H39/H42 forbids,
each e ∈ E is barred from {s,v₁,v₃,v₅,ε,w,c₁,c₂,b₁,b₂}.
At most one e meets T₄ (else C₄ through T₂). ≥3 free stubs of E leave to the
exterior — heavy expansion. **Next:** pigeonhole those stubs against Bset
or produce a path₆.

---

## Status of hard-class EG after Fire 15

| Result | Status |
|--------|--------|
| H31: EG for hard n<62 | **PROVED** |
| H41: residual + d=6 ⇒ C₁₆ | **PROVED** |
| H42: T₂T₅ ⇒ C₈ | **PROVED** |
| H43: path₄ ⇔ E–Bset under bad | **PROVED** |
| H44: E–Bset geometry in G'' | **PROVED** |
| Double-stretch empty | OPEN (two extreme arms) |
| Full hard EG all n | OPEN by double-stretch only |

## Property tests
- T₂–T₅ never an edge on hard CAT (would be C₈)
- All path₄s v₁–T₂ in G−v₂ are E–Bset type on CAT
- No double-stretch config in census
