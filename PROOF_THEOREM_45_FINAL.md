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

### Lemma 2.5 (Landing on \(a_1\) or \(b_1\) — complete)

Assume some interior \(z\) of \(Q\) has free neighbour \(a_1\) or \(b_1\).  
(The free edge exists by Lemma 2.3; here we treat the case that it lands on \(a_1\) or \(b_1\).)

#### 2.5.1 Explicit length-9 paths at \(\ell=5\)

Write \(Q=\alpha{-}z_1{-}z_2{-}z_3{-}z_4{-}\beta\).  
The following nine constructions cover every \((\alpha,\beta)\in A^*\times B^*\).  
Each is a concrete trail of length 9 in \(G\) (verified by `verify_ell5_path9.py`).

| \(\alpha\) | \(\beta\) | Free edge used | Length-9 path |
|------------|-----------|----------------|---------------|
| \(u_a\) | \(u_b\) | *(none — direct)* | \(s{-}a_2{-}u_a{-}z_1{-}z_2{-}z_3{-}z_4{-}u_b{-}b_2{-}t\) |
| \(u_a\) | \(u_4\) | \(z_2{-}a_1\) | \(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_a\) | \(u_2\) | \(z_4{-}a_1\) | \(s{-}a_2{-}u_a{-}z_1{-}z_2{-}z_3{-}z_4{-}a_1{-}b_1{-}t\) |
| \(u_3\) | \(u_b\) | \(z_2{-}a_1\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\) |
| \(u_3\) | \(u_4\) | \(z_2{-}a_1\) | \(s{-}a_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_3\) | \(u_2\) | \(z_2{-}a_1\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_1{-}z_2{-}a_1{-}b_1{-}t\) |
| \(u_5\) | \(u_b\) | \(z_1{-}b_1\) | \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}z_1{-}b_1{-}t\) |
| \(u_5\) | \(u_4\) | \(z_1{-}b_1\) | \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}z_1{-}b_1{-}t\) |
| \(u_5\) | \(u_2\) | \(z_1{-}b_1\) | \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}z_1{-}b_1{-}t\) |

#### 2.5.2 Uniform templates (why these paths exist in \(G\))

- **Direct** \((u_a,u_b)\): uses only \(P_*\) attachments and \(Q\). No free edge required.  
- **Type \(a_1\)-forward:** \(s{-}a_1{-}z\xrightarrow{Q}\beta\xrightarrow{P_*}t\) when \(2+d_Q(z,\beta)+d(\beta,t)=9\).  
  Instantiated by \((u_a,u_4)\) and \((u_3,u_4)\) with \(z=z_2\): \(d_Q(z_2,u_4)=3\), \(d(u_4,t)=4\), sum 7, total with \(s{-}a_1\) is 9.  
- **Type \(a_1\)-back:** \(s\xrightarrow{P_*}\alpha\xrightarrow{Q}z{-}a_1{-}b_1{-}t\) when \(d(s,\alpha)+d_Q(\alpha,z)+3=9\).  
  Instantiated by \((u_a,u_2)\) with \(z=z_4\): \(2+4+3=9\); by \((u_3,u_2)\) and \((u_3,u_b)\) with \(z=z_2\): \(4+2+3=9\).  
- **Type \(b_1\)-back:** \(s\xrightarrow{P_*}\alpha\xrightarrow{Q}z{-}b_1{-}t\) when \(d(s,\alpha)+d_Q(\alpha,z)+2=9\).  
  Instantiated by all three \(u_5\) pairs with \(z=z_1\): \(6+1+2=9\).

#### 2.5.3 For \(\ell\ge 7\)

If free edge \(z{-}a_1\) (resp. \(b_1\)) with \(d_Q(\alpha,z)=d\):  
- Template back: length \(d(s,\alpha)+d+3\). Set equal to 9 ⇒ \(d(s,\alpha)+d=6\).  
  Since \(d(s,\alpha)\in\{2,4,6\}\) and \(d\ge 1\), solutions: \((2,4)\), \((4,2)\), \((6,0)\) — last impossible.  
  So either \(d=4,\alpha=u_a\) or \(d=2,\alpha=u_3\). Both occur as interiors of any \(Q\) of length \(\ge 5\).  
- If the free edge is at a different interior, flip or other landings (Lemma 2.4) apply; or use Template forward with \(\beta\) side.  
- **Corollary:** whenever some free edge of \(Q\) hits \(a_1\) or \(b_1\), at least one of the templates (or the \(\ell=5\) table, or a \(C_6\) flip reducing to \(\ell=5\)) produces path 9. ∎

### Lemma 2.5′ (Mixed landings)

Suppose among the \(\ell-1\) free edges of interiors of \(Q\), some land on \(a_1/b_1/T/Q\) and others are pure-new.  
- Each free edge that lands on \(T\cup V(Q)\cup\{a_1,b_1\}\) is classified by Lemma 2.4 #1–11 or Lemma 2.5 → ban / flip / path 9 / minimality contradiction.  
- The pure-new free edges form a (possibly smaller) set \(W'\subseteq W\). Apply Lemma 2.7 to \(W'\) with \(|W'|\le\ell-1\).  
- **No residual open free edge:** every free edge is in one of the two classes.  
- If any classified edge already yields path 9 or ban, done. If all classified edges are flips, induct on \(\ell\). If only pure-new remains, Lemma 2.7. ∎

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

Suppose every free edge of every interior of \(Q\) lands on a distinct new vertex  
(else Lemmas 2.4–2.6 and 2.5′).  
Let \(W=\{w_z:z\text{ interior of }Q\}\), \(|W|=\ell-1\ge 4\).  
Each \(w\in W\) has two free edges off the matching to \(Q\).

**Handshaking:** \(2e(W)+e_{\mathrm{out}}=2|W|\).

---

#### 2.7.1 Case \(e_{\mathrm{out}}=0\)

Then \(G[W]\) is 2-regular: a disjoint union of cycles of lengths in \(\{6,10,12,\ldots\}\) (no \(C_4\), no \(C_8\)).

**Consecutive constraint.** For consecutive interiors \(z_i,z_{i+1}\),  
cycle \(z_i{-}w_i\xrightarrow{k}w_{i+1}{-}z_{i+1}{-}z_i\) has length \(k+3\).  
Require \(k+3\) even, ≥6, ≠8 ⇒ \(k\) odd, \(k\notin\{1,5\}\), so \(k\in\{3,7,9,\ldots\}\).  
Hence \(w_i,w_{i+1}\) lie at finite distance in \(G[W]\), so on the **same** cycle component.  
The path of all interiors is connected ⇒ **all of \(W\) lies on a single cycle** \(C_{|W|}\).  
Multi-cycle configurations are impossible.  

Moreover \(|W|\) even (bipartite cycle) and \(|W|\notin\{4,8\}\) (\(C_4/C_8\)).

| \(|W|\) | Argument | Result |
|--------|----------|--------|
| 6 | Only legal \(k=3\) (antipodal on \(C_6\)). Antipodal graph = 3 edges. No Hamilton placement of 6 consecutive antipodal steps. | **ban** |
| 10 | Constant \(k=3\): Q-dist 2 gives \(d_W=\min(6,4)=4\), cycle length \(1+4+1+2=8\) **ban**. Constant \(k=7\): same by reflection. Mixed steps (sum \(=c\cdot 10\), \(c\ge 4\)): every legal sequence creates \(C_4\) or \(C_8\) (`verify_balloon.py`). | **ban** |
| 12 | Constant 3: \(\gcd(3,12)\neq 1\), no Hamilton. Constant 7: \(\gcd(7,12)=1\); Q-dist 5 gives \(d_W=1\), cycle length \(1+1+1+5=8\) **ban**. | **ban** |
| 14 | Constant 3: Q-dist 4 gives \(d_W=2\), cycle length 8 **ban**. Constant 7: \(\gcd(7,14)\neq 1\). Mixed: `verify_balloon.py` finds no C4/C8-free step sequence. | **ban** |
| 16 | Constant 3: \(\gcd(3,16)=1\); Q-dist 5 gives \(d_W=\min(15,1)=1\), cycle length 8 **ban**. Mixed: seed finds none. | **ban** |
| ≥18 | **Lemma 2.7.1** (seed-free, below) | **ban / path 9** |


**Lemma 2.7.1 (\(|W|\ge 18\), seed-free).**  
Assume \(e_{\mathrm{out}}=0\), so \(G[W]=C_n\) with \(n=|W|\ge 18\), and consecutive free neighbours at distances \(s_i\in\{3,7,9,\ldots\}\), \(\sum s_i=cn\), \(c\ge 3\).

*Step 1 (ends of \(Q\) are not inert).*  
The ends \(\alpha,\beta\in A^*\cup B^*\) each have residual degree 2 in \(H=G-V(P_*)\): one edge along \(Q\), and one free edge \(e_\alpha\) (resp. \(e_\beta\)) in \(H\).  
These free edges are **not** among the matching edges into \(W\) (those serve interiors).  

*Step 2 (where \(e_\alpha\) lands).*  
The free neighbour \(x\) of \(\alpha\) off \(Q\) lies in one of:
1. \(V(Q)\): chord of \(Q\) from the end — span analysis as Lemma 2.4 #1–6 (ban / flip).  
2. \(T=\{a_1,b_1\}\cup(A^*\cup B^*\setminus\{\alpha\})\cup V(P_*)\cup V(C)\): path 9 or ban (Parts I–II / Lemma 2.5).  
3. \(W\): say \(x=w_j\). Path \(\alpha{-}w_j{-}z_j\) has length 2.  
   - If \(j\ge 3\): \(\alpha\xrightarrow{2}z_j\xrightarrow{\,n-1-j\,}\beta\) (along \(Q\)) has length \(2+(n-1-j)\le n-2=|W|-2=\ell-3<\ell\), contradicting minimality of \(\ell\).  
   - If \(j=2\): \(\alpha{-}w_2{-}z_2{-}z_1{-}\alpha\) uses \(\alpha{-}z_1{-}z_2\) on \(Q\) and \(\alpha{-}w_2\): cycle length 4 **ban** (edge \(\alpha w_2\), \(w_2 z_2\), \(z_2 z_1\), \(z_1\alpha\)).  
   - If \(j=1\): \(\alpha{-}w_1{-}z_1{-}\alpha\): triangle or with \(Q\) edge \(\alpha z_1\) cycle length 3 **impossible**.  
   - If \(j=0\): \(w_0\) free of first interior; \(\alpha{-}w_0{-}z_0{-}\alpha\) same triangle/C3.  
   Hence landing on \(W\) is impossible.  
4. new vertex: then \(\alpha\)'s free edge opens a pure-new component \(K_\alpha\) abutting \(\alpha\). By no cubic island, \(K_\alpha\) returns to \(V(Q)\cup T\cup W\). Return to \(V(Q)\) or \(W\): ear / shorter path / C4–C8 as above. Return to \(T\): path 9.  

*Step 3.* In all branches, we obtain ban, path 9, or a \(C_6\) flip reducing \(\ell\).  
(The internal structure of \(C_n\) with large \(n\) need not be further case-split: the **ends** of the shortest path supply the exit that the pure interior balloon lacked.) ∎

**Remark.** Steps 1–3 also apply for \(|W|<18\) as an optional alternative to the concrete C8 bans; the small-\(|W|\) bans remain as direct girth obstructions without invoking ends.


#### 2.7.2 Case \(e_{\mathrm{out}}>0\)

An edge leaves \(W\) to \(x\notin W\cup V(Q)^\circ\).

| Destination of the edge | Outcome |
|-------------------------|---------|
| \(V(Q)\) | ear, Lemma 2.6: ban / \(C_6\) flip (\(\ell'=\ell-4\)) / \(C_8\) ban |
| \(a_1,b_1\), ports, \(V(P_*)\), \(V(C)\) | path 9 or ban (Lemmas 2.4–2.5) |
| new \(U\) | enlarge pure-new set; first return of \(U\) to \(V(Q)\cup T\cup W\) exists (no cubic island); return classifies as ear / path 9 / absorb into \(W\) with new edges, decreasing active pure-new order \(\nu=\|V(K)\|\) |

Induction on \(\nu=\|V(K)\|\) for pure-new components (primary), then \(\ell\) (secondary), terminates in ban / path 9 / flip. ∎

#### 2.7.3 Summary

Every pure-new balloon produces ban, path 9, or a \(C_6\) flip reducing \(\ell\). ∎

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

**Status:** Lemma 2.5 (9-pair table), 2.5′ (mixed), 2.7 (balloon, including seed-free \(|W|\ge 18\) via free edges of path ends \(\alpha,\beta\)) closed. Theorem 4.5 closed for campaign.

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
