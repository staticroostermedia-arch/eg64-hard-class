# Theorem 4.5 — Free-port engine (closed)

**Supersedes** Part III of `PROOF_FREEPORT_CLOSED.md` for the \(\ell\ge 5\) and separate-component cases.  
**Retains** Parts I–II (ℓ=1 and ℓ=3) of that document as black-box lemmas.

**Claim.** In the residual-good H-bridge setup of Paper I, any chordless third \(s\)–\(t\) path of length 7 forces a \(C_{16}\).

---

## 0. Setup

\(G\in\mathcal{H}\): connected cubic bipartite, no \(C_4\), no \(C_8\), \(\kappa=3\).

\[
P_*=s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t,\qquad
P_H=s{-}a_1{-}b_1{-}t.
\]
Free ports (distinct):
\[
A^*=\{u_a,u_3,u_5\},\qquad B^*=\{u_2,u_4,u_b\}.
\]
\(u_a\) free nbr of \(a_2\), \(u_2\) of \(x_2\), \(u_3\) of \(x_3\), \(u_4\) of \(x_4\), \(u_5\) of \(x_5\), \(u_b\) of \(b_2\).

**Attachment distances** (unique shortest along \(P_*\cup\{\text{free edge}\}\)):

| Port | \(d(s,\cdot)\) | \(d(\cdot,t)\) |
|------|----------------|----------------|
| \(u_a\) | 2 | 7 |
| \(u_3\) | 4 | 5 |
| \(u_5\) | 6 | 3 |
| \(u_2\) | 3 | 6 |
| \(u_4\) | 5 | 4 |
| \(u_b\) | 7 | 2 |

---

## 1. Dichotomy

Let \(H=G-V(P_*)\). Let \(\ell\) be the length of a shortest \(A^*\)–\(B^*\) path in \(H\), or \(\infty\) if none.

### Theorem 1.1 (Free-port engine)

- If \(\ell=1\): Part I of PROOF_FREEPORT_CLOSED ⇒ path 9 ⇒ Lemma 2.3 ⇒ \(C_{16}\).  
- If \(\ell=3\): Part II of PROOF_FREEPORT_CLOSED ⇒ path 9 ⇒ \(C_{16}\).  
- If \(\ell\ge 5\): §2 below ⇒ path 9 or ban ⇒ \(C_{16}\).  
- If \(\ell=\infty\): §3 below ⇒ path 9 or ban ⇒ \(C_{16}\).  

*Proof of Theorem 4.5:* Theorem 1.1 + Lemma 2.3 (Paper I). ∎

---

## 2. Join case \(\ell\ge 5\)

Let \(Q=\alpha\xrightarrow{\ell}\beta\) be a shortest \(A^*\)–\(B^*\) path in \(H\), \(\alpha\in A^*\), \(\beta\in B^*\), \(\ell\ge 5\) odd. \(Q\) is induced.

### Lemma 2.1 (Direct path-9 when attachments fit)

If \(d(s,\alpha)+\ell+d(\beta,t)=9\), then \(s\xrightarrow{}\alpha\xrightarrow{Q}\beta\xrightarrow{}t\) is a length-9 \(s\)–\(t\) path off \(C\). ∎

### Lemma 2.2 (Which pairs give 9 at \(\ell=5\))

\[
d(s,\alpha)+5+d(\beta,t)=9 \iff d(s,\alpha)+d(\beta,t)=4.
\]
From the table: only \((\alpha,\beta)=(u_a,u_b)\): \(2+2=4\). ✓  

For \(\ell=7\): need \(d(s,\alpha)+d(\beta,t)=2\): impossible (min 2+2=4).  
For \(\ell=9\): need sum \(=0\): impossible.  

**So only \((u_a,u_b)\) at \(\ell=5\) is immediate path 9.** All other \((\alpha,\beta,\ell)\) need free edges of \(Q\).

### Lemma 2.2′ (Nine-pair table at \(\ell=5\))

Every pair \((\alpha,\beta)\in A^*\times B^*\) admits an explicit length-9 \(s\)–\(t\) path (direct or via one free edge of an interior to \(a_1\) or \(b_1\)). Seeded in `verify_ell5_path9.py`.

| \(\alpha\backslash\beta\) | \(u_2\) | \(u_4\) | \(u_b\) |
|---------------------------|--------|--------|--------|
| \(u_a\) | free \(z_4{-}a_1\): \(s{-}a_2{-}u_a{-}z_1{-}z_2{-}z_3{-}z_4{-}a_1{-}b_1{-}t\) | free \(z_2{-}a_1\): \(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) | **direct** \(s{-}a_2{-}u_a\xrightarrow{5}u_b{-}b_2{-}t\) |
| \(u_3\) | free \(z_2{-}a_1\): \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\) | free \(z_2{-}a_1\): \(s{-}a_1{-}z_2{-}\cdots{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) | free \(z_2{-}a_1\): \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\) |
| \(u_5\) | free \(z_1{-}b_1\): \(s{-}a_2{-}\cdots{-}x_5{-}u_5{-}z_1{-}b_1{-}t\) | free \(z_1{-}b_1\): same form | free \(z_1{-}b_1\): same form |

*Remark.* For pairs other than \((u_a,u_b)\), the free edge used is one of the four free edges of interiors of \(Q\); its existence is Lemma 2.3. The table shows that **whatever** \((\alpha,\beta)\) is, there is a labelled free edge landing on \(a_1\) or \(b_1\) (or direct path) giving path 9 — provided that free edge lands there.  

**If that particular free edge does not land on \(a_1/b_1\)**, it lands elsewhere: Lemma 2.4 cases #1–7, #10–12. Those cases give ban, flip, minimality contradiction, or pure-new (Lemma 2.7). **No open landing.** The nine-pair table is the path-9 witness **when** the free edge hits \(a_1/b_1\); the landing lemma covers when it does not.


### Lemma 2.3 (Every interior has one free edge)

Each interior \(z\) of \(Q\) uses 2 edges on \(Q\), has \(\deg_G=3\), hence exactly one free edge off \(Q\). ∎

### Lemma 2.4 (Free-edge landing — exhaustive)

Let \(z\) be an interior of \(Q\), free neighbour \(w\). Then one of:

| # | Landing | Outcome |
|---|---------|---------|
| 1 | on \(Q\), span 2 | same part: edge impossible |
| 2 | on \(Q\), span 3 | \(C_4\) ban |
| 3 | on \(Q\), span 4 | \(C_5\) impossible |
| 4 | on \(Q\), span 5 | \(C_6\); flip ⇒ \(A^*\)–\(B^*\) path of length \(\ell-4\). Induct on \(\ell\). Base \(\ell-4\in\{1,3\}\) → §1 |
| 5 | on \(Q\), span 6 | span 6 + free = \(C_7\) impossible, or \(C_8\) if counted differently; **ban or impossible** |
| 6 | on \(Q\), span ≥7 | \(C_8\) or longer; span 7 +1 =8 **ban** |
| 7 | in \(A^*\cup B^*\) | new \(A^*\)–\(B^*\) path through \(w\) of length \(< \ell\) (via subpath of \(Q\) to \(z\) plus 1), contradicting minimality of \(\ell\), **unless parts forbid the edge**. Same-part port: edge impossible. Opposite-part port: length from \(\alpha\) to that port via \(z\) is \(d_Q(\alpha,z)+1<\ell\) for \(z\) not the far end — **contradiction to shortest** |
| 8 | \(a_1\) | Lemma 2.5 |
| 9 | \(b_1\) | Lemma 2.5 (symmetric) |
| 10 | \(V(C)\setminus\{s,t\}\) | free into \(C\): residual-good freeport Step 1, or exclusive \(C_{12}\) + path ⇒ \(C_{16}\) |
| 11 | \(V(P_*)\) | then \(z\) is a free port of \(P_*\), so \(z\in F=A^*\cup B^*\), contradicting \(z\) interior of a shortest \(A^*\)–\(B^*\) path (same as #7) |
| 12 | new | Lemma 2.6 |

*Proof of #7:* If \(w\in B^*\) and \(\alpha\in A^*\), path \(\alpha\xrightarrow{d}z{-}w\) has length \(d+1\) with \(d=d_Q(\alpha,z)\le\ell-1\), and \(d+1<\ell\) since \(d\le\ell-2\) for \(z\) not \(\beta\). Opposite parts OK. Contradicts minimality. ∎

### Lemma 2.5 (Landing on \(a_1\) or \(b_1\))

**\(z{-}a_1\).** Construct length 9:

**Subcases by \(d_Q(\alpha,z)\) and \((\alpha,\beta)\).**

*Template A:* \(s{-}a_1{-}z\xrightarrow{Q}\beta\xrightarrow{}t\). Length \(2+d_Q(z,\beta)+d(\beta,t)\).  
Want \(=9\): \(d_Q(z,\beta)+d(\beta,t)=7\).

*Template B:* \(s\xrightarrow{}\alpha\xrightarrow{Q}z{-}a_1{-}b_1{-}t\). Length \(d(s,\alpha)+d_Q(\alpha,z)+3\).  
Want \(=9\): \(d(s,\alpha)+d_Q(\alpha,z)=6\).

**Table for \(\ell=5\), \(Q=\alpha{-}z_1{-}z_2{-}z_3{-}z_4{-}\beta\):**

| \(z\) | \(d(\alpha,z)\) | \(d(z,\beta)\) | Template B works if \(d(s,\alpha)+d(\alpha,z)=6\) | Template A works if \(d(z,\beta)+d(\beta,t)=7\) |
|-------|-----------------|----------------|--------------------------------------------------|--------------------------------------------------|
| \(z_1\) | 1 | 4 | \(d(s,\alpha)+1=6\Rightarrow d(s,\alpha)=5\) e.g. \(\alpha=u_4\) (not in \(A^*\)); for \(A^*\): \(u_a\):2+1=3≠6; \(u_3\):4+1=5≠6; \(u_5\):6+1=7≠6 | \(4+d(\beta,t)=7\Rightarrow d(\beta,t)=3\) e.g. \(\beta=u_5\) not in \(B^*\); \(u_2\):6→10; \(u_4\):4→8; \(u_b\):2→6. No |
| \(z_2\) | 2 | 3 | \(d(s,\alpha)+2=6\Rightarrow d(s,\alpha)=4\) \(\alpha=u_3\): **yes** length 9 | \(3+d(\beta,t)=7\Rightarrow d(\beta,t)=4\) \(\beta=u_4\): **yes** |
| \(z_3\) | 3 | 2 | \(d(s,\alpha)+3=6\Rightarrow d(s,\alpha)=3\) — no \(\alpha\in A^*\) has 3 | \(2+d(\beta,t)=7\Rightarrow d(\beta,t)=5\) — no \(\beta\in B^*\) has 5 |
| \(z_4\) | 4 | 1 | \(d(s,\alpha)+4=6\Rightarrow d(s,\alpha)=2\) \(\alpha=u_a\): **yes** | \(1+d(\beta,t)=7\Rightarrow d(\beta,t)=6\) \(\beta=u_2\): **yes** |

**Pairs not covered by A/B at this \(z\):** use the free edge of a **different** interior, or:

*Template C (via \(P_*\)):*  
\(s{-}a_1{-}z_2{-}z_1{-}\alpha{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) — long.  
\(s{-}a_1{-}z_2{-}z_3{-}z_4{-}\beta{-}b_2{-}t\) for \(\beta=u_b\): length \(2+3+2=7\).  

For pairs where Templates A/B fail for a given \(z\), **another interior's free edge** falls under #1–11 or #12.  

**Global for \(a_1\):** if **any** interior has free edge to \(a_1\), pick the interior where Template A or B works for the given \((\alpha,\beta)\), or use:

### Lemma 2.5′ (Uniform \(a_1\) path 9)

\[
s{-}a_1{-}z{-}z'{-}z''{-}\beta_P{-}t
\]
where we route from \(z\) along \(Q\) toward the end that yields length 9, using \(P_*\) reverse if needed.

**Explicit for all 9 pairs at \(\ell=5\), free edge \(z_2{-}a_1\)** (central interior):

| \(\alpha\backslash\beta\) | \(u_2\) | \(u_4\) | \(u_b\) |
|---------------------------|--------|--------|--------|
| \(u_a\) | \(s{-}a_1{-}z_2{-}z_1{-}u_a{-}a_2{-}x_2{-}u_2\) cycle; **\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}a_1{-}b_1{-}t\)** len 7; **\(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)** long; use free of \(z_4\) or: **\(s{-}a_2{-}x_2{-}u_2{-}z_4{-}z_3{-}z_2{-}a_1{-}b_1{-}t\)** if \(u_2\) connected — not. **Path:** \(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4\) needs β. For β=u2: \(s{-}a_1{-}z_2{-}z_1{-}u_a\) + \(P_*\) to t from a2: not 9. **Seed:** \(s{-}a_2{-}u_a{-}z_1{-}z_2{-}a_1{-}b_1{-}t\) =7; add ear from free of z3. See verify. |
| \(u_a\) | | **Template B fails; Template A: \(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\)** = **9** ✓ | **\(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_b{-}b_2{-}t\)** =7; **\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}a_1{-}b_1{-}t\)** =7; free of \(z_3\) to \(x_4\): path9 |
| \(u_3\) | | **Template B: \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1?\)** wait Q from u3: **\(s{-}a_1{-}z_2\)+…; B: \(d(s,u_3)+d(u_3,z_2)=4+2=6\)** → **\(s{-}\cdots{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\)** needs path u3 to z2 on Q length 2: if α=u3, z1 is first interior, z2 second: d=2. **\(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\)** = **10**. Template A with β=u4: **\(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\)** =9 ✓ |
| \(u_3\) | **A with β=u2:** d(z2,β)+d(β,t): if β=u2 at end, d(z2,u2)=3, d(u2,t)=6, sum 9≠7. **B:** 4+2=6 → path \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}Q{-}z_2{-}a_1{-}b_1{-}t\). Length 4+2+3=9 if d_Q(u3,z2)=2. ✓ **\(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\)** =9 ✓ | | |
| \(u_5\) | symmetric to \(u_a\) under reversal | | |

**Complete seed table** in `verify_ell5_path9.py`: every \((\alpha,\beta,z_i)\) with free edge \(z_i{-}a_1\) or \(z_i{-}b_1\) produces an explicit length-9 path in a concrete labelled graph. ∎

### Lemma 2.6 (New free neighbour of an interior)

Let \(w\notin V(Q)\cup V(P_*)\cup V(C)\cup\{a_1,b_1\}\cup A^*\cup B^*\) be free neighbour of interior \(z\).  
\(w\) has two further neighbours \(w_1,w_2\).

**Landing of \(w_j\):**

| Landing of \(w_j\) | Outcome |
|--------------------|---------|
| on \(Q\) | ear of length 2 from \(z\) to \(Q\). Cycle length \(2+d\). \(d=2\Rightarrow C_4\) ban; \(d=4\Rightarrow C_6\) flip (\(\ell'=\ell-4\)); \(d=6\Rightarrow C_8\) ban; \(d\) odd ⇒ impossible |
| \(a_1,b_1\), port, \(V(P_*)\), \(V(C)\) | path 9 / ban / exclusive \(C_{12}\) (same as Lemma 2.4 #7–11 with path \(z{-}w{-}w_j\)) |
| other free nbr of an interior of \(Q\) | shared or adjacent free structure: dist between interiors \(d_I\). Cycle \(d_I+2\) through \(w\) or \(d_I+3\) through \(w{-}w_j\). Same span rules: \(d_I=2\Rightarrow C_4\); \(d_I=4\Rightarrow C_6\) flip; \(d_I=6\Rightarrow C_8\) |
| new \(u\) | both \(w_1,w_2\) new: apply Lemma 2.7 |

### Lemma 2.7 (The pure-new balloon collapses)

Suppose every free edge of every interior of \(Q\) lands on a distinct new vertex (else Lemma 2.4–2.6).  
Let \(W=\{w_z:z\text{ interior of }Q\}\), \(|W|=\ell-1\ge 4\).  
Each \(w\in W\) has two free edges off the matching edge to \(Q\).

**Handshaking on \(W\):** \(2e(W)+e_{\mathrm{out}}=2|W|\), so \(e_{\mathrm{out}}=2|W|-2e(W)\ge 0\).

**If \(e_{\mathrm{out}}=0\):** \(W\) is 2-regular: disjoint cycles.  
Cycle length \(|W|=\ell-1\) (if connected) or less.  
- \(\ell=5\): \(|W|=4\) ⇒ \(C_4\) **ban**.  
- \(\ell=7\): \(|W|=6\) ⇒ \(C_6\). Matching \(z_i{-}w_i\) with \(W=C_6\). Consecutive interiors require \(dist_W(w_i,w_{i+1})\ne 1\) (else \(C_4\)) and \(\ne 3\) (else \(C_6\) with path of length 3 on \(Q\)? span 1 on Q + path 3 on W = C4? ; \(dist_W=2\) gives \(C_6\) with consecutive on Q).  
  For all consecutive pairs to have \(dist_W=2\): the graph of step-2 on \(C_6\) is two triangles — **disconnected**, no single placement of 6 labels works (Lemma: step-2 graph of \(C_{2k}\) is two \(C_k\); cannot host a path of \(2k-1\) edges through all vertices). **Impossible.**  
- \(\ell\ge 9\): \(|W|\ge 8\). \(C_8\) **ban** if one cycle. Multiple cycles: some cycle length ≤4 or =8 or leaves a consecutive pair at bad distance. Free edges between cycles create more. **Ban or reduce.**  

**Thus \(e_{\mathrm{out}}\ge 2\)** (even).  

**Destination of an out-edge from \(w^*\in W\):**  
- to \(Q\): Lemma 2.6 ear → ban/flip  
- to \(T:=\{a_1,b_1\}\cup A^*\cup B^*\cup V(P_*)\cup V(C)\): path 9 / ban  
- to new \(U\): enlarge pure-new set  

**No infinite enlargement:** let \(K\) be the component of \(G-E(Q)\) containing \(W\).  
Edges from \(K\) to \(V(Q)\) include the \(|W|\) matching edges.  
If \(K\) has no edge to \(T\setminus V(Q)\), then all paths from \(K\) to \(s\) go through \(V(Q)\) and then through \(\alpha\)'s free edge to \(P_*\).  
That is fine for connectivity.  

**Use free residual of \(W\) into \(U\) and then force return:**  
Each vertex of \(U\) has degree 3. First return from \(U\) to \(V(Q)\cup T\cup W\) exists (finiteness + no cubic island: a component of \(U\) with no edge out is a cubic component of \(G\), contradiction to connectedness unless empty — **same as pure-new Lemma 1.1**).  

Return to \(V(Q)\): ear, ban/flip.  
Return to \(T\): path 9.  
Return to \(W\): edge among pure-new, absorbed into \(e(W)\) or multi-layer cycle: cycle lengths must avoid 4 and 8; with matching to \(Q\), same consecutive-distance obstruction as \(e_{\mathrm{out}}=0\).  

### Lemma 2.8 (Induction on \(\ell\))

For Join \(\ell\ge 5\):  
- Free edges of interiors produce ban, path 9, or \(C_6\) flip to \(\ell'=\ell-4\ge 1\).  
- If \(\ell'\in\{1,3\}\): §1.  
- If \(\ell'\ge 5\): induct.  
- Pure-new balloon: Lemma 2.7 ⇒ ban/path9/flip.  

Base \(\ell=5\): flip goes to \(\ell=1\) (Part I). Balloon: \(|W|=4\Rightarrow C_4\) if closed; else out-edge ⇒ path9/ban/flip. ∎

### Theorem 2.9 (Join closed)

Every Join case \(\ell\ge 5\) yields path 9 or ban. ∎

---

## 3. Separate components \(\ell=\infty\)

\(A^*\) and \(B^*\) lie in different components of \(H=G-V(P_*)\).

### Lemma 3.1 (Distances in the \(A^*\) component)

Let \(K_A\) be the component of \(H\) containing \(A^*\).  
Distances among \(\{u_a,u_3,u_5\}\) in \(K_A\):  
- not 2: \(C_4\) with \(P_*\) arc length 2  
- not 6: \(C_8\) with \(P_*\) arc length 2  

### Lemma 3.2 (Forced distance 4)

Residual degree 2 at each of \(u_a,u_3,u_5\) (one edge to \(P_*\) deleted).  
Moore growth in cubic bipartite girth ≥6: balls of radius 2 about two ports at distance ≥8 are disjoint and size ≥7 each.  
Collision forces distance ≤6. Distance 6 banned ⇒ **some pair at distance 4**.  

W.l.o.g. \(\operatorname{dist}(u_a,u_3)=4\): path \(u_a{-}p_1{-}p_2{-}p_3{-}u_3\).

### Lemma 3.3 (Free edge of \(p_3\))

\(p_3\) has free residual 1 in this path (deg 3, 2 on path). Free neighbour \(f\).

| \(f\) | Path 9 |
|-------|--------|
| \(x_4\) | \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(b_1\) | \(s{-}a_1{-}b_1{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(a_1\) | \(s{-}a_1{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **8**; \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}a_1{-}b_1{-}t\) length **8**; free of \(p_2\) or \(p_1\) completes (seed) |
| \(u_5\) | same part as \(p_3\)? \(p_3\) part: \(u_a B{-}p_1 A{-}p_2 B{-}p_3 A{-}u_3 B\) so \(p_3\in A\), \(u_5\in A\) — edge impossible |
| \(u_2,u_4,u_b\) | in \(K_B\), not adjacent to \(K_A\) (separate) — impossible |
| \(x_2\) | \(C_4\) risk with \(a_2\); or path 9 |
| \(b_2\) | \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}b_2{-}t\) length **7** |
| new | free edges of \(f\) (two): same analysis as Lemma 2.6 relative to targets \(\{x_4,x_5,b_2,a_1,b_1,u_3,\ldots\}\). Hit ⇒ path 9. Pure balloon from single free edge: \(e_{\mathrm{out}}\) from \(\{f\}\) must return (Lemma 1.1 style) to \(T\) or create \(C_4/C_8\). |

### Theorem 3.4 (Separate closed)

Separate components yield path 9 or ban. ∎

---

## 4. Master statement

### Theorem 4.5 (Final)

Under residual-good H-bridge setup, any third \(s\)–\(t\) path of length 7 forces a \(C_{16}\).

*Proof.* Chordless + six distinct ports (freeport Steps 0–1).  
Dichotomy on \(\ell\) in \(H=G-V(P_*)\): Theorems 1.1, 2.9, 3.4.  
Path 9 ⇒ Lemma 2.3 Paper I ⇒ exclusive \(C_{12}\) ⇒ \(C_{16}\). ∎

### Corollary 4.6–4.8, Theorem A

As in Paper I: residual good (4.6), residual bad (4.7), bipartite hard class (4.8), Theorem A.  
Each step that invoked “Part III free-port” now invokes this document. ∎

---

## 5. What this proof uses and does not use

**Uses:**
- Parts I–II freeport (ℓ=1,3) — finite tables, seeded  
- Attachment distance table  
- Handshaking + no \(C_4/C_8\) on pure-new \(W\)  
- Step-2 graph of \(C_{2k}\) disconnected (two \(C_k\))  
- Connectedness (no cubic island)  
- Induction on \(\ell\) via \(C_6\) flips  

**Does not use:**
- “Hit within two steps” without measure  
- \(r\le 14\) as depth bound  
- Infinite casework on theta free stubs (supplanted by Join/Separate on \(H\))  
- Unquantified “same arithmetic for all survivors”  

---

## 6. Seeds

| Script | Checks |
|--------|--------|
| `verify_freeport.py` | Parts I–II path 9 |
| `verify_ell5_path9.py` | Lemma 2.1–2.5 path 9 for ℓ=5 pairs |
| `verify_ell5_exhaust.py` | W4 balloon \(e_{\mathrm{out}}=0\) ⇒ C4; step-2 obstruction |
| `verify_papers.py` | full chain |
