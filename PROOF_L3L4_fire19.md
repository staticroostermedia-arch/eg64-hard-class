# Fire 19 — L3–L4 geodesics; kill b−e endings (H70)

## Setup

Arm A double-stretch under residual + E–Bset:
\(\operatorname{dist}_{G''}(a^*,e)=6\), \(\operatorname{dist}_{G''}(a^*,t)=8\).

Layers from \(e\) in \(G''\); \(N(e)=\{T_2,b,f\}\).

---

## Theorem H65 (PROVED) — every length-6 geodesic hits L4 at step 2

Let \(a^*=p_0{-}p_1{-}\cdots{-}p_6=e\) be a geodesic.
Then \(p_1\in\{c_1,c_2\}\) and \(p_2\in L_4(e)\).

*Proof.* \(p_1\) is part A ⇒ \(p_1\in\{c_1,c_2\}\) (s is a leaf; path through s cannot continue).  
Remaining distance \(e\) is 4, so \(\operatorname{dist}(e,p_2)\le 4\).  
By H55/H59 and triangle, \(\operatorname{dist}(e,p_2)\ge 4\). Even ⇒ \(=4\), so \(p_2\in L_4\). ∎

---

## Theorem H63 (PROVED) — v₁ is a leaf in G''

\(N_G(v_1)=\{v_0,v_2,t\}\); both \(v_0\) and \(v_2\) are deleted in \(G''\).  
**⇒** \(N_{G''}(v_1)=\{t\}\), deg 1.

Also \(t\in L_2(e)\) and already uses edges to \(L_3\ni\{v_1,b_2\}\).

---

## Theorem H70 (PROVED) — no length-6 a\*–e geodesic ends with b−e

Suppose \(p_5=b\), so the geodesic ends \(\cdots{-}r_2{-}b{-}e\).

Prefix to \(b\) has length 5: \(a^*{-}\cdots{-}b\).  
Replace last hop \(b{-}e\) by \(b{-}t\):
\[
a^*{-}\cdots{-}b{-}t
\]
has length **6**. Hence \(\operatorname{dist}_{G''}(a^*,t)\le 6\).

But then H40/H41: not 2 or 4, so \(=6\) ⇒ **C₁₆**, contradicting double-stretch (needs dist(a\*,t)≥8) and in any case yielding EG.

**⇒ Arm A double-stretch forbids \(p_5=b\).** ∎

(This also kills both subcases \(r_2=t\) and \(r_2=\beta\) from the L1-exit analysis.)

---

## Theorem H71 (PROVED) — no g−b for g∈N(f)\{e}

If \(g{-}b\) with \(g{-}f\) and \(f{-}e\), \(e{-}b\): **C₄** \(g{-}f{-}e{-}b{-}g\). ∎

---

## Theorem H82 (PROVED) — under DS, g avoids {b₂,v₁,T₂}

| Edge | Kill under DS / residual |
|------|---------------------------|
| g−b₂ | a\*…g−b₂−t length ≤6 ⇒ dist(a\*,t)≤6 |
| g−v₁ | same with v₁−t |
| g−T₂ | C₄ g−T₂−e−f−g |

---

## Remaining Arm A cases after H70

By Fire 16, \(p_5\in\{T_2,f\}\) (not \(b\); now H70 re-proves not \(b\) via dist to t).

| Ending | Status |
|--------|--------|
| **p₅=b** | **DEAD** (H70) |
| **p₅=f** | open — path a\*−c−q−r₁−g−f−e; dist(a\*,t)≤8 tight |
| **p₅=T₂** | open — path a\*−c−q−r₁−e′−T₂−e; uses both E-verts |

### Next vector
1. Kill p₅=f: force g−b₂ / length-6 to t, or C₈ with E–Bset spine.  
2. Kill p₅=T₂: e′ at dist 4 from a\* (H78) + no Bset on e′ ⇒ C₈ or dist(a\*,t)≤6.  
3. Arm B: s−T₃ (H56) + QB⊥QF.

---

## Property tests
- No residual+E–Bset model with a length-6 a\*–e path through b  
- v₁ deg 1 in G'' after P₈ removal  
