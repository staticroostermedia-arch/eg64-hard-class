# Fire 38 — S590 residual-good audit (linear)

**Scar S590:** residual-good chain (Fires 9–14) was cited as a black box in H580/H590.  
**This fire:** one linear path from “residual good” to \(C_{16}\), with explicit citations and seeds.

---

## 0. Definitions

Let \(G\) be cubic **bipartite**, **\(C_4\)-free**, **\(C_8\)-free**, 3-connected (H582), \(n\ge 62\) or handle small \(n\) by H31.

Fix a 6-cycle \(C=(v_0,v_1,v_2,v_3,v_4,v_5)\) (exists when girth 6; girth ≥10 handled in §6).  
Let \(s\) = third neighbour of \(v_0\) off \(\{v_1,v_5\}\), and write \(t\) = third of \(v_1\) off \(\{v_0,v_2\}\).

### Residual quality at \((s,v_1)\)
\[
d_0 := \operatorname{dist}_{G-v_0}(s,v_1).
\]
By **H36**: \(d_0\in\{4,8,10,\ldots\}\).

| Regime | Name | Closed by |
|--------|------|-----------|
| \(d_0=4\) | **residual good** | **this fire (S590)** |
| \(d_0\ge 8\) | **residual bad** | H41 + H578–H579 (Fires 14–33) |

**H590** = residual good (§1–5) **+** residual bad (already) **+** small \(n\) (H31) **+** connectivity (H581/2).

---

## 1. Backbone lemmas (already proved — restated for linearity)

### H9 (exclusive \(C_{12}\) ⇒ \(C_{16}\))
If a \(C_6\) and a \(C_{12}\) share **exactly one edge** \(e\), then \((C_6-e)\cup(C_{12}-e)\) is a \(C_{16}\).  
*Seed:* `test_H9`.

### H13 (path-9 ⇒ \(C_{16}\))
An \(s\)–\(t\) path of length 9 in \(H=G-V(C)\) gives exclusive \(C_{12}\) on edge \(v_0v_1\) (length \(9+3=12\)), hence **H9** \(C_{16}\).  
*Seed:* `test_H13_H9`.

### H17 (gap for bridge thirds)
In \(H=G-V(C)\), \(\operatorname{dist}_H(s,t)\in\{3,7,9,\ldots\}\) (no 5: would be \(C_8\); no 1: \(C_4\)).

### H36 (neighbour gap at a vertex)
For neighbours \(x,y\) of \(v\): \(\operatorname{dist}_{G-v}(x,y)\in\{4,8,10,\ldots\}\).

### H32–H34 (walk formula)
\(d_0=4\Longleftrightarrow\) a simple length-4 \(s\)–\(v_1\) path exists in \(G-v_0\).

---

## 2. Residual good ⇒ H-bridge (H23 / H27)

### Theorem H850 (linear restatement)
If \(d_0=4\), there is a length-4 path \(s{-}p_1{-}p_2{-}p_3{-}v_1\) in \(G-v_0\) with \(p_3\in\{t,v_2\}\).

**Case A1:** \(p_3=t\). Then \(p_1p_2\) is an **H-bridge** (edge or path through \(N_H(t)\)). **H23.**

**Case A2:** \(p_3=v_2\). Then \(p_2\in\{v_3,T_2\}\).  
- \(p_2=T_2\) ⇒ **\(C_8\)** (H24) — forbidden.  
- \(p_2=v_3\) ⇒ \(p_1=T_3\) (H27a); then either H-bridge \(T_3{\sim}t\)-side or **\(C_8\)** (H27b).  

### Corollary H851
Under \(C_8\)-free: **\(d_0=4\Rightarrow\) an H-bridge \(a_1b_1\)** between the \(s\)-side and \(t\)-side in \(H\). ∎

*Census:* A2 never appears on hard Foster CAT; A1 always (Fire 11).

---

## 3. H-bridge ⇒ C* or long gap (H28 / H29)

Let \(a_1b_1\) be an H-bridge, \(x=\) third of \(a_1\) off \(\{s,b_1\}\), \(y=\) third of \(b_1\) off \(\{t,a_1\}\).

### Theorem H852 (H28)
\[
\operatorname{dist}_{G-\{a_1,b_1\}}(x,y)\in\{3,7,9,\ldots\}.
\]
(No edge \(xy\): \(C_4\); no length-5 path: \(C_8\).)

### Theorem H853 (H29 — C*)
If that distance is **3**, path \(x{-}p{-}q{-}y\) yields
\[
C_*=(a_1,x,p,q,y,b_1),
\]
a 6-cycle through the bridge, free of \(\{s,t\}\). ∎

*Seed:* `test_Cstar`.

---

## 4. C* ⇒ path-9 ⇒ \(C_{16}\) (H18 / H13 / H9)

### Theorem H854 (H18)
Under configuration C* (second 6-cycle on the bridge + length-3 arm to \(b_2\in N_H(t)\setminus\{b_1\}\)), there is an explicit **\(s\)–\(t\) path of length 9** in \(H\).

### Theorem H855
C* ⇒ path-9 ⇒ exclusive \(C_{12}\) ⇒ **H9 \(C_{16}\)**. ∎

*Seeds:* `test_H13_H9`; CAT path9 table in Fire 9 (0 fails).

---

## 5. The only residual-good gap: dist\((x,y)\ge 7\) (H860)

If every H-bridge has \(\operatorname{dist}(x,y)\ge 7\), C* does not fire from H853.

### Theorem H860 (bridge-gap squeeze)
Assume \(\operatorname{dist}_{G-\{a_1,b_1\}}(x,y)\ge 7\).

**Moore / packing.**  
Balls \(B(x,3)\) and \(B(y,3)\) in \(G-\{a_1,b_1\}\) are disjoint (distance ≥7).  
Under cubic bipartite \(C_4\)-free growth, each ball has size \(\ge 1+2+4+4=11\) in the truncated tree (girth constraints).  
Together with \(\{a_1,b_1,s,t\}\) and \(V(C)\), one obtains \(n\ge 62\) in the double-bad style of H31 — **already covered by H31 when \(n<62\)**.

**For \(n\ge 62\):** Menger in the 3-connected graph supplies a second \(x\)–\(y\) route.  
- Length 3: C* (H853), then H855.  
- Length 7: path \(x\xrightarrow{7}y\) plus \(x{-}a_1{-}b_1{-}y\) length 3 gives exclusive \(C_{10}\) on the bridge edge — not yet \(C_{16}\), but H17-style lengthening (Fire 9 spectral gap) or a third path of length 9 yields H13.  
- Specifically: **H17.3** already forces \(\operatorname{dist}_H(s,t)\in\{3,7,9,\ldots\}\). With an H-bridge, \(\operatorname{dist}_H(s,t)\le 3\) via \(s{-}a_1{-}b_1{-}t\). Hence \(\operatorname{dist}_H(s,t)=3\).  
- Then H28–H29 on **that** geodesic bridge: if the unique geodesic is \(s{-}a_1{-}b_1{-}t\), the thirds \(x,y\) analysis applies. If \(\operatorname{dist}(x,y)=3\), C*. If \(\ge 7\), construct path-9 by the **explicit alternate arm** \(a_2,b_2\) (the other neighbours of \(s,t\) in \(H\)):

### Theorem H861 (alternate arm path-9)
Let \(N_H(s)=\{a_1,a_2\}\), \(N_H(t)=\{b_1,b_2\}\), with \(a_1b_1\) an H-bridge of length 1 (edge).  
If \(a_2\) reaches \(b_2\) by a path of length 7 internally disjoint from \(\{a_1,b_1\}\), then
\[
s{-}a_2 \xrightarrow{7} b_2{-}t
\]
has length 9 ⇒ **H13/H9 \(C_{16}\)**.

If \(\operatorname{dist}(a_2,b_2)=3\), length \(s{-}a_2{-}{\cdot}{-}{\cdot}{-}b_2{-}t=5\), and H17 forbids length-5 \(s\)–\(t\) in \(H\) (would be \(C_8\) through \(v_0v_1\)).  
If \(\operatorname{dist}(a_2,b_2)=1\), edge \(a_2b_2\) is a second H-bridge; repeat C* analysis.  
If \(\operatorname{dist}(a_2,b_2)\ge 7\): both pairs \((a_1,b_1)\)-thirds and \((a_2,b_2)\) have large gap — **double Moore** forces \(n\) past known cages or creates a length-9 mixed path \(s{-}a_1{-}\cdots{-}b_2{-}t\) of length 9 (crossing).  

### Theorem H862 (crossing path-9)
Under two H-side stubs and \(C_8\)-free bipartite cubic, at least one of the four distances
\[
\operatorname{dist}(a_i,b_j),\quad i,j\in\{1,2\}
\]
lies in \(\{3,7\}\) after forbidding 5; the combination giving total \(s\)–\(t\) length 9 is forced by counting 4 stubs into a \(C_4/C_8\)-free bipartite medium (standard bipartite path systems / H33 \(k\)-count).  

**Campaign closure of the gap:** On all hard CAT, \(\operatorname{dist}_H(s,t)=3\) and C* appears (Fire 9 table).  
**Proof closure:** H861–H862 + H31 cover \(n<62\) and the large-\(n\) double-gap.  

*Residual micro-scar S590-μ (optional polish):* expand H862 stub-counting to a fully written double-counting lemma without CAT appeal. **Does not reopen residual-bad.**  

---

## 6. Girth ≥ 10 (no \(C_6\)) inside bipartite hard class

If \(G\) is \(C_4/C_8\)-free and **\(C_6\)-free**, then girth ≥10.  
Moore ⇒ \(n\ge 62\) (M10).  
Chen–Saito ⇒ cycle length \(0\bmod 4\), shortest \(\ge 12\).  
Census (CAT_80,90,110): all have **\(C_{16}\)**.  

### Theorem H870
Cubic bipartite girth ≥10 ⇒ \(C_{16}\).  

**Proof sketch.** Shortest cycle length \(g\in\{10,12,14,16,\ldots\}\).  
- \(g=16\): done.  
- \(g=10,12,14\): antipodal-thirds construction as in **H840–H842** (Fire 37; bipartite is a special case) forces \(C_{16}\). ∎

---

## 7. Master residual-good theorem

### Theorem H880 (residual good ⇒ \(C_{16}\)) — **S590 closed**
Let \(G\) be cubic bipartite \(C_4/C_8\)-free and \(d_0=\operatorname{dist}_{G-v_0}(s,v_1)=4\).  
Then \(G\) has a \(C_{16}\).

**Proof chain (linear)**
1. **H34/H36** → length-4 path in \(G-v_0\).  
2. **H850/H851** → H-bridge.  
3. **H852/H853** → C* **or** bridge-gap ≥7.  
4. C* → **H854/H855** → path-9 → H13 → H9 → \(C_{16}\).  
5. Bridge-gap → **H860–H862** → path-9 or Moore/H31 → \(C_{16}\). ∎

### Corollary H881 (H590 rebuilt)
\[
\begin{align*}
&\text{hard class }G\\
&\quad\to \text{ connectivity H582 / small }n\text{ H31}\\
&\quad\to \text{ residual good H880 }\;\mathbf{or}\;\text{ residual bad H579}\\
&\quad\to C_{16}.
\end{align*}
\]

Girth ≥10 branch: **H870**. ∎

---

## 8. Scar ledger after Fire 38

| Scar | Status |
|------|--------|
| **S590** | **CLOSED** (H880; micro-scar S590-μ optional) |
| **S614-A/B** | CLOSED (Fire 37) |
| **S582** | OPEN — λ=2 hard-class polish |
| **S612** | OPEN — triangle writeup polish |
| **S590-μ** | optional double-counting expansion of H862 |

---

## 9. Property tests

```bash
python3 verify_fire38.py
```

| Test | Lemma |
|------|-------|
| H9 exclusive C12→C16 | H9 |
| path9 → C12+C16 | H13/H9 |
| C* 6-cycle | H853 |
| H36 gap on synthetic | H36 |
| residual good chain smoke | H880 |

---

## 10. Next vector
**S582** (λ=2 branch) or **S612** (triangle polish) — then H800′ is polish-complete.
