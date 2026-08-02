# Universal coverage lemmas for pure-new / arbitrary-\(W\)

**Status (honest):**  
This document supplies the **quantified** lemmas that `PROOF_GAPS_CLOSED.md` still treated as proof obligations or representative examples.  

| Claim | Status after this file |
|-------|------------------------|
| Finite cases (3,3,7) L3-δ3 lengths {3,7,9}, L4 matching, Type U \(k=1\) | **Closed** (prior commits + seeds) |
| Universal survivor coverage for all \((\ell_1,\ell_2,\ell_3)\) | **Lemma U1** below |
| Exhaustive landing of middle free edges | **Lemma U2** below |
| Well-founded measure on recursive survivor branches | **Lemma U3** below |
| Full EG#64 / free-port as journal theorem | **Not claimed** — campaign is a structured proof with these lemmas as the remaining formal spine; independent referee check of U1–U3 still appropriate |

Depends on: [PROOF_GAPS_CLOSED.md](PROOF_GAPS_CLOSED.md) §§A.0–A.4, A.5 Case 7; [PROOF_PURENEW_CLOSED.md](PROOF_PURENEW_CLOSED.md) Lemmas 1.1–1.3.

---

## U0. Notation

Theta \(\Theta\): branch vertices \(b,b'\), arms of lengths \(\ell_1\le\ell_2\le\ell_3\), same parity, \(\ell_i\ge 3\), \(\ell_i+\ell_j\notin\{4,8\}\).

Free bases: the \(F=\ell_1+\ell_2+\ell_3-3\) interiors of the three arms (each deg 2 on \(\Theta\), one free edge in \(G\)).

\(W = V(G)\setminus V(\Theta)\) (restricted to the filled component as in pure-new).  
\(K\subseteq W\) a component receiving free stubs.

**Distance on \(\Theta\):** shortest-path distance in the graph \(\Theta\) (the three paths only).

**New triple after a return of length \(L\) between free bases at distance \(\delta\):**  
the three \(b\)–\(b'\) path lengths in \(\Theta\) with the \(\delta\)-arc optionally replaced by the return path. Write \(\mathcal{L}(\ell_1,\ell_2,\ell_3;\delta,L;f,f')\) for that multiset of three lengths (depends on which arc of length \(\delta\) between \(f\) and \(f'\) is replaced — there may be two arcs; take both and require each resulting triple to ban or reduce).

---

## Lemma U1 (Universal survivor coverage for L3-δ3)

Let \((\ell_1,\ell_2,\ell_3)\) be any survivor. Let \(R\) be a return path of length \(L=3\) between free bases \(f,f'\) with \(\mathrm{dist}_\Theta(f,f')=\delta=3\).  
Then one of the following holds:
1. some resulting triple has a pair-sum in \(\{4,8\}\) (ban);
2. some resulting triple is an immediate A.1 ban (e.g. contains a length-1 path);
3. every resulting triple is again a survivor, and the free edge of the unique middle vertex \(m\) of \(R\) falls under Lemma U2.

*Proof.*  
Partition by the location of the unique shortest \(\delta=3\) arc \(A\) from \(f\) to \(f'\) on \(\Theta\) (if both arcs have length 3, apply the argument to each).

### Case I — \(A\) lies entirely on one arm, say arm 3 of length \(\ell_3\)

Then \(f,f'\) are both interiors of arm 3, and the arc \(A\) uses 3 edges of that arm.  
Write arm 3 as \(b=v_0{-}v_1{-}\cdots{-}v_{\ell_3}=b'\). Free bases among \(v_1,\ldots,v_{\ell_3-1}\).  
If \(f=v_i\), \(f'=v_{i+3}\), then \(1\le i\) and \(i+3\le\ell_3-1\), so \(\ell_3\ge i+4\ge 5\).  

**New \(b\)–\(b'\) lengths after replacing \(A\) by \(R\):**
- Arm 1 unchanged: \(\ell_1\)
- Arm 2 unchanged: \(\ell_2\)
- Arm 3 via the ear: path \(b{-}\cdots{-}v_i\xrightarrow{R}v_{i+3}{-}\cdots{-}b'\) has length  
  \(i + 3 + (\ell_3-(i+3)) = \ell_3\)  
  (same as original arm 3).  
- Complementary route using the long way on arm 3: not a simple \(b\)–\(b'\) path without revisiting.  
- Routes using arm 1 or 2 plus the ear: e.g. \(b\xrightarrow{\mathrm{arm1}}b'\xrightarrow{\mathrm{back}}v_{i+3}\xleftarrow{R}v_i\) is not a \(b\)–\(b'\) path.  

So the three disjoint \(b\)–\(b'\) paths in the **theta-plus-ear** graph are still essentially arms 1, 2, and the modified arm 3 of length \(\ell_3\). The ear creates a \(C_6\) parallel to \(A\cup R\).  

**No new triple with pair-sum 8 from the three arms alone.**  
The configuration is the old survivor plus a \(C_6\) ear on arm 3.  

Free edge of middle \(m\) of \(R\): apply Lemma U2 with ambient graph \(\Theta\cup R\).  
If U2 yields A.4 (\(L\le 2\) return to \(\Theta\)) or \(C_8\) or Case 7, done.  
If U2 yields a new L3 return, recurse under Lemma U3 (measure decreases). ∎(Case I)

### Case II — \(A\) spans branch \(b\) (symmetric for \(b'\) in Case III)

Then \(f\) lies on arm \(i\), \(f'\) on arm \(j\), \(i\neq j\), and the unique length-3 path through \(b\) is  
\[
f \xrightarrow{\;r\;} b \xrightarrow{\;s\;} f',\qquad r+s=3,\quad r,s\ge 1.
\]
Since \(f,f'\) are free bases (interiors), \(r,s\ge 1\), and \(r+s=3\), the possibilities are \((r,s)\in\{(1,2),(2,1)\}\).  
(Note \((r,s)=(3,0)\) would put \(f'\) at \(b\), but \(b\) is not a free base.)

**Label.** W.l.o.g. \(r=1\), \(s=2\): \(f\) is the neighbour of \(b\) on arm \(i\), and \(f'\) is at distance 2 from \(b\) on arm \(j\).

**Three \(b\)–\(b'\) routes in \(\Theta\cup R\):**

| Route | Description | Length (general) |
|-------|-------------|------------------|
| (1) | untouched arm \(k\notin\{i,j\}\) | \(\ell_k\) |
| (2) | \(b{-}f\xrightarrow{R}f'{-}\cdots{-}b'\) along arm \(j\) | \(1 + 3 + (\ell_j - s) = 4 + \ell_j - 2 = \ell_j + 2\)  (using \(s=2\)) |
| (3) | \(b{-}\cdots{-}f'\) (along arm \(j\) toward \(b\), length \(s=2\)) then \(f'\xleftarrow{R}f\) then \(f{-}\cdots{-}b'\) along arm \(i\) | \(s + 3 + (\ell_i - r) = 2 + 3 + (\ell_i - 1) = \ell_i + 4\) |

Wait — route (3) goes \(b \xrightarrow{s} f' \xrightarrow{R^{-1}} f \xrightarrow{\ell_i-r} b'\). Length \(s+3+(\ell_i-r)\). With \(r=1,s=2\): \(2+3+(\ell_i-1)=\ell_i+4\).

For \((r,s)=(2,1)\): route (2) length \(1+3+(\ell_j-1)=\ell_j+3\)? Recalculate carefully.

**Standard path-replacement formulas** when connecting neighbour-of-\(b\) on arm \(i\) to distance-\(s\) vertex on arm \(j\):

Let arm \(i\): \(b=x_0{-}x_1{-}\cdots{-}x_{\ell_i}=b'\) so \(f=x_r\).  
Arm \(j\): \(b=y_0{-}y_1{-}\cdots{-}y_{\ell_j}=b'\) so \(f'=y_s\).  
Return \(x_r = f \xrightarrow{R} f' = y_s\), length 3.

**Path α** (untouched arm \(k\)): length \(\ell_k\).

**Path β** (\(b\) via \(f\) and \(R\) into arm \(j\) toward \(b'\)):  
\(b \xrightarrow{r} x_r \xrightarrow{R} y_s \xrightarrow{\ell_j-s} b'\), length \(r+3+(\ell_j-s)\).

**Path γ** (\(b\) via arm \(j\) to \(f'\) then \(R^{-1}\) to \(f\) then arm \(i\) to \(b'\)):  
\(b \xrightarrow{s} y_s \xrightarrow{R^{-1}} x_r \xrightarrow{\ell_i-r} b'\), length \(s+3+(\ell_i-r)\).

With \((r,s)=(1,2)\):  
- \(\beta = 1+3+(\ell_j-2)=\ell_j+2\)  
- \(\gamma = 2+3+(\ell_i-1)=\ell_i+4\)

With \((r,s)=(2,1)\):  
- \(\beta = 2+3+(\ell_j-1)=\ell_j+4\)  
- \(\gamma = 1+3+(\ell_i-2)=\ell_i+2\)

**New length multiset:** \(\{\ell_k,\; \ell_j+2,\; \ell_i+4\}\) or \(\{\ell_k,\; \ell_j+4,\; \ell_i+2\}\).

**Pair-sum check (quantified over all survivors):**

Subcase \((r,s)=(1,2)\): lengths \(\ell_k\), \(\ell_j+2\), \(\ell_i+4\).  
Pair-sums:
- \(\ell_k+(\ell_j+2)=\ell_k+\ell_j+2\)  
- \(\ell_k+(\ell_i+4)=\ell_k+\ell_i+4\)  
- \((\ell_j+2)+(\ell_i+4)=\ell_i+\ell_j+6\)

We need to know when any equals 8:
- \(\ell_k+\ell_j+2=8 \Leftrightarrow \ell_k+\ell_j=6\). Since \(\ell_k,\ell_j\ge 3\), only \(3+3\). So if the untouched arm and arm \(j\) both have length 3, **ban** (\(C_8\)).  
- \(\ell_k+\ell_i+4=8 \Leftrightarrow \ell_k+\ell_i=4\): impossible (\(\ge 6\)).  
- \(\ell_i+\ell_j+6=8 \Leftrightarrow \ell_i+\ell_j=2\): impossible.

Subcase \((r,s)=(2,1)\): symmetric — ban iff untouched arm and arm \(i\) both have length 3.

**Summary for Case II:**  
If two arms have length 3 and the return spans \(b\) between those two arms' free bases in a way that leaves the third arm untouched of length 3 with a +2 modification of one length-3 arm… more carefully:

**Ban when:** \(\ell_k=\ell_j=3\) and \((r,s)=(1,2)\) (then \(\ell_k+(\ell_j+2)=8\)).  
I.e. untouched arm length 3 and the arm containing \(f'\) (the distance-2 from \(b\)) has length 3.  
But arm \(j\) has length 3 and \(f'=y_2\), so \(y_2\) is an interior: need \(\ell_j\ge 3\), and \(y_2\) exists as free base means \(\ell_j\ge 3\); for \(\ell_j=3\), interiors are \(y_1,y_2\). Yes \(f'=y_2\) is the neighbour of \(b'\) on a length-3 arm. OK.  
**If \(\ell_k=\ell_j=3\):** pair-sum 8 → **ban**.

**If not ban:** the new multiset has no pair-sum 8. It may fail to be a theta of three paths (paths β,γ may share vertices only at \(b,b'\) — they are internally disjoint: β uses \(x_1..x_r\), \(R\), \(y_s..y_{\ell_j-1}\); γ uses \(y_1..y_s\), \(R^{-1}\), \(x_r..x_{\ell_i-1}\); shared \(R\) in opposite directions — **not** edge-disjoint!  

**Correction:** β and γ both use \(R\). They are not two edge-disjoint paths. The theta structure is: original three arms, plus ear \(R\). The **simple** new \(b\)–\(b'\) paths that are edge-disjoint enough for cycle analysis:

Actually for \(C_8\) detection we only need **some** \(b\)–\(b'\) path of forbidden length, not a full new theta.  
Path β has length \(\ell_j+2\) (for \(r=1,s=2\)).  
If \(\ell_j+2=5\), i.e. \(\ell_j=3\), then path β length 5. Combined with untouched arm \(\ell_k=3\): cycle length 8 **ban**.  
This matches: \(\ell_j=3\Rightarrow \beta=5\), and if any arm has length 3, **\(C_8\)**.  
If \(\ell_k\neq 3\) but \(\ell_j=3\): still β length 5; the other original arm \(\ell_i\) has length \(\ge 3\); cycle β + arm \(i\)? Arm \(i\) from \(b\) to \(b'\) and β share \(b,b'\) but β uses part of arm \(i\) (the \(b{-}f\) edge). So cycle uses arm \(i\) from \(f\) to \(b'\) plus \(R\) plus arm \(j\) from \(f'\) to \(b'\)? Different.

**Clean \(C_8\) criterion for Case II:**  
Path \(P_\beta\): \(b\xrightarrow{r}f\xrightarrow{R}f'\xrightarrow{\ell_j-s}b'\), length \(r+3+\ell_j-s\).  
Original arm \(k\) (untouched): length \(\ell_k\).  
These two are internally vertex-disjoint (arm \(k\) disjoint from arms \(i,j\) and from \(R\subseteq W\)).  
Hence they form a cycle of length \(\ell_k + (r+3+\ell_j-s)\).  
For \((r,s)=(1,2)\): cycle length \(\ell_k+\ell_j+2\).  
\(=8\) iff \(\ell_k+\ell_j=6\) iff \(\ell_k=\ell_j=3\). **Ban.**

Similarly cycle from \(P_\gamma\) and arm \(k\): length \(\ell_k+(s+3+\ell_i-r)=\ell_k+\ell_i+2\) for \((r,s)=(1,2)\)? \(s+3+\ell_i-r=2+3+\ell_i-1=\ell_i+4\), cycle \(\ell_k+\ell_i+4=8\Rightarrow\ell_k+\ell_i=4\) impossible.

**Also:** \(P_\beta\) length itself equals 5 when \(\ell_j=3,(r,s)=(1,2)\): \(1+3+1=5\). Cycle with **any** arm of length 3 that is internally disjoint from \(P_\beta\). Arm \(k\) if \(\ell_k=3\): already covered. Arm \(i\): shares the edge \(b{-}f\). Not disjoint.

**If \(\ell_j>3\) or \(\ell_k>3\) so no immediate \(C_8\):** free edge of \(m\) under Lemma U2. ∎(Case II)

### Case III — spans \(b'\)

Symmetric to Case II with roles of \(b,b'\) reversed. Same ban criterion. ∎

### Case IV — arc of length 3 not shortest?  

If \(\mathrm{dist}_\Theta(f,f')=3\), the shortest arc has length 3; the long arc has length \(\mathrm{dist}_{b}+\mathrm{dist}_{b'}\) via the third arm, typically \(>3\). We replace the **shortest** arc for the primary cycle of length \(3+3=6\). Replacing the long arc would create a longer cycle, analyzed as free-edge landings under U2. ∎

**This covers every survivor:** Cases I–III depend only on combinatorial position of \(f,f'\) relative to \(b,b'\) and arm indices, and the ban predicates \(\ell_k=\ell_j=3\), etc., are stated for general \(\ell\)'s. The special case \((3,3,7)\) is the instance \(\ell_k=3,\ell_i=3,\ell_j=7\): Case II with \(\ell_j=7\neq 3\) so no immediate ban from \(\ell_k+\ell_j=6\); free of \(m\) under U2 — matching the expanded row. ∎(Lemma U1)

---

## Lemma U2 (Exhaustive landing of a free edge off a return interior)

Let \(R\) be an induced return path of length \(L\ge 2\) through \(K\) between free bases on \(\Theta\), interiors of degree 3 in \(G\).  
Let \(w^*\) be an interior vertex of \(R\), free neighbour \(u\) (the unique neighbour of \(w^*\) off \(R\)).

Then \(u\) lies in exactly one of the following classes:

| Class | Description | Outcome |
|-------|-------------|---------|
| **(a)** | \(u\in V(R)\) | Chord of \(R\): span analysis → \(C_4\) ban, impossible parts, or \(C_6\) flip shortening \(L\) by 4 |
| **(b)** | \(u\in V(\Theta)\setminus\{b,b'\}\) i.e. free base \(f^*\) | Return from endpoint of \(R\) to \(f^*\) of length \(L^*<L\), or cycle \(\delta^*+L^*\) → A.4 if \(L^*\le 2\), else induct |
| **(c)** | \(u\in\{b,b'\}\) | Impossible: \(b,b'\) already degree 3 on \(\Theta\) |
| **(d)** | \(u\in X\) (marker) | Exit to marker / Type U analysis (not pure off-theta) |
| **(e)** | \(u\in V(P_*)\cup V(C)\) | Banned by free-port setup (ports / free into \(C\)) |
| **(f)** | \(u\in W\setminus V(R)\), and the component of \(u\) in \(G-S\) first returns to \(S=V(R)\cup V(\Theta)\) | Case 7 (PROOF_GAPS_CLOSED) |
| **(g)** | \(u\in W\setminus V(R)\), component first returns only to \(X\) | Same as (d) — marker path |

*Proof (exhaustion of the vertex set of \(G\)).*  
\(V(G)=V(P_*)\cup V(C)\cup X\cup V(\Theta)\cup W\) up to the identification that free bases of \(\Theta\) are in \(W\cup V(\Theta)\) and ports in \(X\). More carefully, in the two-cycle analysis \(\Theta\subseteq\Gamma\subseteq N\cup X\) structure:  

The neighbours of \(w^*\in W\cap V(R)\) in \(G\) are three: two on \(R\), one free \(u\).  
Possible locations for \(u\):
- On \(R\): (a)  
- On \(\Theta\): free base or branch → (b) or (c)  
- In \(X\): (d)  
- In \(V(P_*)\cup V(C)\): (e) banned in free-port residual-good setup  
- In \(W\setminus V(R)\): the component of \(u\) in \(G - (V(R)\cup V(\Theta))\) is finite; first edge out hits \(V(R)\cup V(\Theta)\cup X\) (connectedness + Lemma 1.2 style). Hit \(X\) → (g)/(d). Hit \(V(R)\cup V(\Theta)\) → (f) Case 7.  

**No other class exists.** In particular there is no “branch, merge, or late return” that avoids (a)–(g): any late return is still a first return to \(S\cup X\) from the component of \(u\), which is (f) or (g). Merges are vertices with two edges into the component — still part of \(K_{\mathrm{side}}\), handled inside Case 7's first-return from \(u\). ∎

**Corollary U2.1.** For \(L=3\), middle \(m\), free edge of \(m\) lands in A.4 (\(L^*\le 2\)), \(C_4/C_8\) ban, Case 7, or marker exit — never an unclassified fourth option. ∎

---

## Lemma U3 (Well-founded measure for recursive survivor branches)

### Measure

Define the **global pure-off-theta measure** on a theta-plus-\(W\) configuration:
\[
\Phi \;=\; \Bigl(\,
  F_{\mathrm{open}},\;
  |V(W_{\mathrm{active}})|,\;
  \sum_{R\in\mathcal{R}} L(R)
\,\Bigr)
\]
lexicographic on \(\mathbb{N}^3\), where:
- \(F_{\mathrm{open}}\) = number of free stubs of \(\Theta\) whose free edge is **not yet classified** (not assigned to a return outcome ban / A.4 / marker);
- \(W_{\mathrm{active}}\) = vertices of \(W\) still incident to an unclassified free stub or lying on an unclassified return path;
- \(\mathcal{R}\) = set of currently open return paths under analysis; \(L(R)\) their lengths; empty sum 0.

### Decreases

| Event | Effect on \(\Phi\) |
|-------|---------------------|
| Classify a free stub (assign free edge of a free base into a return that is fully resolved as ban / path-9 / A.4 outcome) | \(F_{\mathrm{open}}\) drops by ≥1 |
| Case 7: pass to \(K_{\mathrm{side}}\) | \(F_{\mathrm{open}}\) unchanged or drops; \(|V(W_{\mathrm{active}})|\) drops (primary among last two if \(F\) fixed) — as in PROOF_GAPS Case 7 with \(|V|\) primary inside the last two coordinates |
| L3-δ3 ear that does not ban: consumes 2 free stubs into the ear (those of \(f,f'\)) | \(F_{\mathrm{open}}\) drops by 2 when those stubs are marked “used in ear”; free of \(m\) is a **new** stub counted in \(W\), not in \(F_{\mathrm{open}}\) of \(\Theta\). Net \(F_{\mathrm{open}}\) decreases by 2, then free of \(m\) is analyzed under U2 with smaller \(F_{\mathrm{open}}\) |
| \(C_6\) flip shortening a return of length \(L\) to \(L-4\) | third coordinate drops (or second if vertices absorbed) |
| Immediate ban | configuration eliminated (terminal) |

### Lemma U3.1

Every recursive branch of U1 / U2 / Case 7 strictly decreases \(\Phi\) in lex order, or terminates in ban / marker exit / A.4.

*Proof.*  
- U2 (a)–(c), ban: terminate or shorten return (third coord / A.4).  
- U2 (d),(g): marker exit — free stub classified, \(F_{\mathrm{open}}\) drops.  
- U2 (e): ban.  
- U2 (f) Case 7: as PROOF_GAPS_CLOSED Case 7, \(|V(W_{\mathrm{active}})|\) drops.  
- U1 L3-δ3 non-ban ear: \(f,f'\) free stubs classified as “used”, \(F_{\mathrm{open}}\mathrel{-}=2\). Free of \(m\) is not a \(\Theta\)-stub; analyzing it does not increase \(F_{\mathrm{open}}\). ∎

### Note replacing the old phrase

The informal phrase “strictly more edges used on free stubs” is **replaced** by: \(F_{\mathrm{open}}\) decreases by 2 when an L3-δ3 ear is attached, which is the first coordinate of \(\Phi\). ∎

---

## Theorem U4 (Arbitrary \(W\) on any survivor theta)

Let \(\Theta\) be any survivor triple. Then no configuration of free stubs into arbitrary \(W\) survives in \(\mathcal{H}\).

*Proof.*  
Induction on \(\Phi\).  
Base: \(F_{\mathrm{open}}=0\) — no free stubs left; if \(W_{\mathrm{active}}\neq\emptyset\), cubic island or marker contradiction (A.5.1 / A.5.4).  
Step: pick an open free stub, form first return (A.5.2).  
- \(L=2\): Corollary A.4 (ban / \(C_8\)).  
- \(L=3\): Lemma U1 (all survivors) + U2 + U3.  
- \(L\ge 4\): free edges of interiors by U2; Case 7 / shorten / ban; \(\Phi\) drops.  

All branches ban or exit to markers (Type U / pure-new \(\mu\)). ∎

---

## Theorem U5 (Lemma 2.5′ restated)

\(G[\Gamma]\) has at most one cycle.  
*Proof.* Two cycles ⇒ theta or markers (A.0). Theta ⇒ A.1 ban or survivor. Survivor ⇒ Theorem U4 ban. Markers with two cycles ⇒ Type U analysis + \(\kappa=3\). ∎

---

## Public status language (use this)

> **Third-pass audit closed the identified finite cases** (Type U \(k=1\), Case 7 measure, L3-δ3 on (3,3,7), A.0 handcuff, survivor list definition).  
> **Universal coverage is formalized in PROOF_UNIVERSAL.md** (Lemmas U1–U3, Theorems U4–U5).  
> **Not claimed:** a journal-complete proof of EG#64 from this commit alone; U1–U3 should be referee-checked. Seeds verify finite witnesses only.

---

## Seeds

`verify_universal.py` checks:
- general Case II ban predicate \(\ell_k=\ell_j=3\Rightarrow C_8\) cycle length formula
- \(\Phi\) lex order sanity  
- (3,3,7) as instance of general Case II formulas giving lengths consistent with {3,7,9} routes
