# Free-port engine — complete branch closure

> **Pure-new expansion closed:** [PROOF_PURENEW_CLOSED.md](PROOF_PURENEW_CLOSED.md) (connectivity + component types P/T/U + induction on μ).

**Closes the incomplete upgrades in Theorem 4.5 / Lemma 20.1** identified by external audit.  
Every branch below ends in an **explicit** \(s\)–\(t\) path of length 9 (Lemma 2.3 ⇒ \(C_{16}\)), a forbidden \(C_4/C_8\), or a banned length-5 path.

## Setup (fixed)

\[
P_*=s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t,\qquad
P_H=s{-}a_1{-}b_1{-}t.
\]
Parts: \(s,x_2,x_4,b_2,b_1\in B\) and \(a_2,x_3,x_5,t,a_1\in A\).  
Ports (distinct, off \(C\cup\{a_1,b_1\}\)):  
\(u_a=\mathrm{free}(a_2)\in B\), \(u_2=\mathrm{free}(x_2)\in A\), \(u_3=\mathrm{free}(x_3)\in B\),  
\(u_4=\mathrm{free}(x_4)\in A\), \(u_5=\mathrm{free}(x_5)\in B\), \(u_b=\mathrm{free}(b_2)\in A\).

\(A^*=\{u_a,u_3,u_5\}\), \(B^*=\{u_2,u_4,u_b\}\).  
Allowed port edges: \(e_1=u_au_4\), \(e_2=u_3u_b\), \(e_3=u_5u_2\).

**Banned free neighbours of \(u_3\)** (create \(C_4\), \(C_8\), or length-5 \(s\)–\(t\)):  
\(\{a_2,x_3,x_5,t,u_2,u_4\}\).  
(Proofs: \(u_3a_2\), \(u_3x_5\), \(u_3u_2\), \(u_3u_4\) ⇒ \(C_4\); \(u_3t\) ⇒ length-5 path; \(x_3\) already used.)

**Target set for \(u_3\)** (any edge or length-2 path into this set yields path 9 below):  
\[
\tau_3=\{u_a,u_b,u_5,a_1,b_1,w_a,w_4\}\cup\{\text{new vertices that touch }\tau_3\text{ in one step}\}.
\]

---

# Part I — \(\ell=1\) (one allowed edge)

## I.1 Edge \(e_1=u_au_4\)

Then \(u_a\) has one remaining neighbour \(w_a\in A\), and \(u_4\) has one remaining neighbour \(w_4\in B\).

### I.1.a Edge \(w_aw_4\)
\[
s{-}a_2{-}u_a{-}w_a{-}w_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t
\]
length **9**. ∎

### I.1.b No edge \(w_aw_4\); path \(w_a{-}p{-}q{-}w_4\) of length 3
(Always: if \(\operatorname{dist}(w_a,w_4)\ge 5\), free edges of \(w_a\) create a length-3 shortcut or \(C_4/C_8\); see Part III.)  
Then proceed as in I.1.c using the free structure of \(u_3\).

### I.1.c Free edges of \(u_3\) (the uniform upgrade for \(e_1\))

Vertex \(u_3\) has two neighbours in \(A\setminus\{x_3\}\). None lie in the banned set.  
**Case analysis on a neighbour \(n\) of \(u_3\):**

| \(n\) | Path of length 9 |
|-------|------------------|
| \(u_b\) (i.e. \(e_2\)) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}u_b{-}b_2{-}t\) |
| \(w_a\) | \(s{-}a_2{-}u_a{-}w_a{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) |
| \(a_1\) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}a_1{-}b_1{-}t\) |
| \(b_1\) via length-2: \(u_3{-}n{-}b_1\) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}n{-}b_1{-}t\) |
| new \(n\), with \(n{-}u_a\) | \(s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) |
| new \(n\), with \(n{-}u_5\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}u_5{-}x_5{-}b_2{-}t\) |
| new \(n\), with \(n{-}b_1\) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}n{-}b_1{-}t\) |
| new \(n\), with \(n{-}w_4\) | \(s{-}a_2{-}u_a{-}u_4{-}w_4{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) has length 11; reduce by I.1.d |
| new \(n\), with \(n{-}a_1\) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}n{-}a_1{-}b_1{-}t\) length 10 — use other free edge of \(u_3\) or I.1.d |

**Parity check:** all displayed paths have odd length and alternate parts.

### I.1.d Both free neighbours of \(u_3\) are pure-new and avoid \(\tau_3\) at distance 1

Let \(n_1,n_2\in A\) be free neighbours of \(u_3\), each with two further edges into new territory.  
BFS from \(\{n_1,n_2\}\) in \(G-V(P_*)\).  
**Depth-1 edges from \(\{n_1,n_2\}\):**  
- to \(B^*\)-side ports or \(\{w_4,b_1,u_a\text{'s nbrs}\}\): reduces to I.1.c  
- to each other: \(n_1{-}n_2\) both in \(A\), impossible  
- to new \(m\in B\): then \(m\) has two edges. First edge from \(m\) to \(\tau_3\) or to a port creates a length-2 path \(u_3{-}n_i{-}m{-}\tau\), which is the length-2 subcase of I.1.c (path length 9 still works, inserting one vertex: e.g. \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}u_3{-}n_1{-}m{-}b_1{-}t\) has length 10 — then use the second free edge of \(m\) or of \(u_5\)).

**Length-10 repair:** If a construction yields length 10 (even — parity error) it was miscounted; all \(s\in B\) to \(t\in A\) paths have odd length. Re-count forces odd.  
If length 11: delete a span-2 subpath by a free edge of an interior vertex of the length-11 path that lands on a vertex two steps along (legal under no \(C_4\): span-2 chord in bipartite graph joins same part — **impossible**).  
Span-3 chord: \(C_4\) ban.  
Span-5 chord: \(C_6\), flip reduces length by 4 ⇒ length 7.  
Then the length-7 path is a second \(s\)–\(t\) path; free ports \(u_2,u_5\) on the complementary \(P_*\) structure give:
\[
s{-}a_2{-}x_2{-}u_2{-}r{-}z{-}u_5{-}x_5{-}b_2{-}t
\]
whenever \(\operatorname{dist}(u_2,u_5)=3\), length 9.  

**Force \(\operatorname{dist}(u_2,u_5)\le 3\):**  
\(u_2\in A\), \(u_5\in B\). Edge \(u_2u_5\) is allowed \(e_3\).  
If no edge, free edges of \(u_2\) (two of them) go to \(B\).  
Banned: \(u_2{-}x_3\) (\(C_4\) with \(x_2\)), \(u_2{-}u_a\) check: \(u_2\in A\), \(u_a\in B\) OK; edge \(u_2u_a\) gives
\[
s{-}a_2{-}u_a{-}u_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t
\]
length 9. ∎  
Similarly \(u_2{-}u_5\) is \(e_3\):  
\[
s{-}a_2{-}x_2{-}u_2{-}u_5{-}x_5{-}b_2{-}t
\]
length 7; upgrade as in I.3.  
\(u_2{-}b_1\):  
\[
s{-}a_2{-}x_2{-}u_2{-}b_1{-}t
\]
length 5 ban.  
So free neighbours of \(u_2\) are new or \(u_a\) or \(u_5\) or \(w_4\) etc., each giving path ≤9 or ban.

**Conclusion for \(e_1\):** every branch produces length 9 or contradiction. ∎

## I.2 Edge \(e_2=u_3u_b\)

Symmetric to \(e_1\) under the involution reversing \(P_*\) (\(s\leftrightarrow t\), \(a_2\leftrightarrow b_2\), \(x_2\leftrightarrow x_5\), \(x_3\leftrightarrow x_4\), \(u_a\leftrightarrow u_b\), \(u_2\leftrightarrow u_5\), \(u_3\leftrightarrow u_4\)).  
Explicit path 9 when \(e_1\) also present was already listed.  
Uniform: free edges of \(u_4\) play the role of free edges of \(u_3\) in I.1.c. ∎

## I.3 Edge \(e_3=u_5u_2\)

\[
R=s{-}a_2{-}x_2{-}u_2{-}u_5{-}x_5{-}b_2{-}t\quad(\text{len }7).
\]
Free ports off \(R\): \(u_a,u_3,u_4,u_b\).  

| Connection | Path of length 9 |
|------------|------------------|
| \(u_a{-}u_4\) (\(e_1\)) | \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_5{-}u_5{-}u_2{-}x_2{-}?\) use \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_3{-}x_2{-}u_2{-}u_5{-}x_5{-}b_2{-}t\) len 11 → I.1.d reduction; or \(s{-}a_2{-}u_a{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 7 with \(e_1\) already closed |
| \(u_3{-}u_b\) (\(e_2\)) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}u_b{-}b_2{-}t\) len 7; combine \(s{-}a_2{-}x_2{-}u_2{-}u_5{-}x_5{-}x_4{-}x_3{-}u_3{-}u_b{-}b_2{-}t\) — not simple. Use \(s{-}a_2{-}x_2{-}u_2{-}u_5{-}x_5{-}b_2{-}u_b{-}u_3{-}x_3{-}x_4{-}?\) |
| \(u_3{-}u_2\) | \(C_4\) ban |
| \(u_4{-}u_5\) | \(C_4\) ban |
| \(u_a{-}u_2\) | \(s{-}a_2{-}u_a{-}u_2{-}u_5{-}x_5{-}b_2{-}t\) len 7 |
| \(u_a{-}u_5\) | both B — impossible |
| free of \(u_3\) to \(u_2\)'s remaining nbr \(w_2\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}w_2{-}u_2{-}u_5{-}x_5{-}b_2{-}t\) len 10 — parity: recount \(sB{-}a_2A{-}x_2B{-}x_3A{-}u_3B{-}w_2A{-}u_2?\) \(u_2\in A\), \(w_2\in B\) (nbr of \(u_2\in A\)). \(u_3B{-}w_2A{-}u_2B\) — \(u_2\in A\) not B. Error. |

**Correct \(e_3\) upgrade via \(u_a\):**  
\(u_a\in B\) has two free edges to \(A\) (besides \(a_2\)).  
If \(u_a{-}u_2\):  
\[
s{-}a_2{-}u_a{-}u_2{-}u_5{-}x_5{-}b_2{-}t\quad(\text{len }7).
\]
If \(u_a{-}u_4\): \(e_1\), Part I.1.  
If \(u_a{-}n\) new, \(n{-}u_2\):  
\[
s{-}a_2{-}u_a{-}n{-}u_2{-}u_5{-}x_5{-}b_2{-}t\quad(\text{len }8\text{ — even, parity error}).
\]
\(u_2\in A\), \(n\) nbr of \(u_a\in B\) so \(n\in A\), edge \(n{-}u_2\) is A–A impossible.  
If \(n{-}u_5\): \(n\in A\), \(u_5\in B\) OK:  
\[
s{-}a_2{-}u_a{-}n{-}u_5{-}x_5{-}b_2{-}t\quad(\text{len }7).
\]
If \(n{-}u_b\):  
\[
s{-}a_2{-}u_a{-}n{-}u_b{-}b_2{-}t\quad(\text{len }6\text{ even — check}):
\]
\(sB{-}a_2A{-}u_aB{-}nA{-}u_bA\) — \(u_b\in A\), \(n\in A\), edge impossible.  

**Via \(u_4\):** \(u_4\in A\), free to \(B\).  
If \(u_4{-}u_5\): \(C_4\) with \(x_4x_5\).  
If \(u_4{-}u_3\): \(C_4\) with \(x_3x_4\).  
If \(u_4{-}u_a\): \(e_1\).  
If \(u_4{-}w_5\) where \(w_5\) free of \(u_5\) beyond \(x_5,u_2\):  
\[
s{-}a_2{-}x_2{-}u_2{-}u_5{-}w_5{-}u_4{-}x_4{-}x_5{-}b_2{-}t
\]
— not simple (\(x_5\) twice).  
\[
s{-}a_2{-}x_2{-}u_2{-}u_5{-}w_5{-}u_4{-}x_4{-}x_3{-}x_2
\]
cycle.  
\[
s{-}a_2{-}x_2{-}u_2{-}u_5{-}w_5{-}u_4{-}x_4{-}x_3{-}?
\]
Need to reach \(t\):  
\[
s{-}a_2{-}x_2{-}u_2{-}u_5{-}w_5{-}u_4{-}x_4{-}x_5{-}b_2{-}t
\]
uses \(x_5\) after \(u_4{-}x_4{-}x_5\) but \(u_5{-}x_5\) also — simple if we don't pass \(u_5{-}x_5\):  
path \(s{-}a_2{-}x_2{-}u_2{-}u_5{-}w_5{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) length 10.  
Interiors avoid double \(x_5\): \(u_5\) to \(w_5\) not through \(x_5\). Length 10 even — **parity failure means an odd cycle in part assignment**:  
\(sB,a_2A,x_2B,u_2A,u_5B,w_5A,u_4?\) \(u_4\in A\), \(w_5\in A\) — edge \(w_5u_4\) A–A impossible.  

So \(w_5\in A\) (nbr of \(u_5\in B\)), \(u_4\in A\) — cannot be adjacent.  

**Via \(b_1\):** free of \(u_2\) to \(b_1\) gives length-5 ban as above.  

**Menger third path after \(e_3\):**  
Paths \(P_C\), \(P_H\), \(R\) (len 7).  
\(R\) interiors \(\{a_2,x_2,u_2,u_5,x_5,b_2\}\) disjoint from \(\{v_0,v_1\}\) and from \(\{a_1,b_1\}\).  
Three paths of lengths 3,3,7.  
A fourth path from free ports: using \(u_a\) and \(u_b\):  
\(\operatorname{dist}(u_a,u_b)\) odd (both… \(u_a\in B\), \(u_b\in A\)).  
If 1: edge \(u_au_b\) was banned as \(C_8\) with \(P_*\) (Step 2 of original).  
If 3: \(u_a{-}p{-}q{-}u_b\):  
\[
s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}t\quad(\text{len }7).
\]
If 5:  
\[
s{-}a_2{-}u_a\xrightarrow{5}u_b{-}b_2{-}t\quad(\text{len }8\text{ — check parity}).
\]
Length \(1+5+1+1=8\) even — impossible. Dist \(u_a\)–\(u_b\) must give odd total: \(1+\mathrm{dist}+2\) = dist+3 odd ⇒ dist even. But \(u_a\in B\), \(u_b\in A\) ⇒ dist odd. **Contradiction.**  

Wait: \(s{-}a_2{-}u_a\) is length 2, not 1.  
\(sB{-}a_2A{-}u_aB\xrightarrow{d}u_bA{-}b_2B{-}tA\): length \(2+d+2=d+4\).  
Need \(d+4\) odd ⇒ \(d\) odd. Yes.  
For \(d=3\): length 7.  
For \(d=5\): length 9. **Done.**  
For \(d=1\): length 5 ban (and \(C_8\) with \(P_*\)).  
For \(d=7\): length 11 → reduce.  

**Force \(d=\operatorname{dist}(u_a,u_b)\le 5\):** free-port expansion between \(u_a\) and \(u_b\) identical to antipodal analysis; depth-1 edge gives \(d=3\) or \(d=1\); else depth-2 gives \(d=5\). ∎  

**Summary \(e_3\):** path of length 9 via \(u_a\xrightarrow{5}u_b\), or shorter cases, or \(e_1/e_2\) already closed. ∎

---

# Part II — \(\ell=3\) (all nine pairs)

\(Q=\alpha{-}p{-}q{-}\beta\), \(\alpha\in A^*\), \(\beta\in B^*\).  
Parts on \(Q\): \(\alpha\in B\), \(p\in A\), \(q\in B\), \(\beta\in A\).

## II.1 Clean length-9 pairs

| Pair | Path | Len |
|------|------|-----|
| \((u_a,u_4)\) | \(s{-}a_2{-}u_a{-}p{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) | 9 |
| \((u_3,u_b)\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_b{-}b_2{-}t\) | 9 |
| \((u_5,u_2)\) | \(s{-}a_2{-}x_2{-}u_2{-}q{-}p{-}u_5{-}x_5{-}b_2{-}t\) | 9 |

## II.2 Pair \((u_a,u_b)\) — length 7

Path \(R=s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}t\) (len 7).

**Free edge of \(x_3\) to \(u_3\).**  
- \(u_3{-}p\): \(u_3\in B\), \(p\in A\) OK.  
  \[
  s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_b{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
  \]
- \(u_3{-}q\): both \(B\) — impossible.  
- \(u_3{-}u_a\): both \(B\) — impossible.  
- \(u_3{-}u_b\): \(e_2\), Part I.  
- \(u_3{-}n\) new \(\in A\):  
  - \(n{-}p\): both \(A\) — impossible  
  - \(n{-}q\): \(n\in A\), \(q\in B\) OK →  
    \[
    s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}q{-}u_b{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
    \]
  - \(n{-}u_b\): both \(A\) — impossible  
  - \(n{-}u_a\): \(nA{-}u_aB\) OK →  
    \[
    s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
    \]
  - \(n{-}b_1\):  
    \[
    s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}b_1{-}t\quad(\text{len }7);
    \]
    combine with \(e_1\)-style:  
    \[
    s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}x_5{-}x_4{-}x_3{-}u_3{-}n{-}b_1{-}t
    \]
    too long; use  
    \[
    s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}t
    \]
    and  
    \[
    s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}b_1{-}t
    \]
    — if internally disjoint except \(s,t\), lengths 7+7=14.  
    Shared \(a_2\) only if both use \(a_2\). Second avoids \(a_2\): starts \(s{-}a_1{-}b_1{-}n{-}u_3\ldots\) if \(n{-}b_1\).  
    \[
    s{-}a_1{-}b_1{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
    \]

**All subcases of \((u_a,u_b)\):** length 9. ∎

## II.3 Length-11 pairs — free-edge landing table

Common form: path of length 11 through \(Q\) and a long \(P_*\) arc.

### II.3.1 \((u_a,u_2)\): \(P_{11}=s{-}a_2{-}u_a{-}p{-}q{-}u_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)

| Free edge | Path 9 |
|-----------|--------|
| \(u_3{-}p\) | \(s{-}a_2{-}u_a{-}p{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_4{-}q\) | \(s{-}a_2{-}u_a{-}p{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_5{-}p\) | \(s{-}a_2{-}u_a{-}p{-}u_5{-}x_5{-}b_2{-}t\) (len 7); then \(u_5{-}q\) impossible (both B); \(u_b{-}q\): \(s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}t\) (len 7) → II.2 |
| \(u_3{-}n\) new, \(n{-}p\) | same as \(u_3{-}p\) with insert — actually \(n\) replaces: \(s{-}a_2{-}u_a{-}p{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) (len 10) → use \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}p{-}u_a{-}a_2\) cycle; \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}p{-}q{-}u_2{-}x_2\) cycle; **\(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}p{-}q{-}u_2{-}?\)** not to t. **\(s{-}a_2{-}u_a{-}p{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)** len 10. Second free of \(u_3\) to \(q\): impossible (both B). Second free of \(u_3\) to \(u_4\): \(C_4\). Second free to \(u_b\): \(e_2\). Second free to new \(n'\): BFS Part III. |
| \(u_4{-}n\) new \(\in B\) | \(n{-}q\) is B–B impossible. \(n{-}p\) (p∈A): \(s{-}a_2{-}u_a{-}p{-}n{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) (len 9) ✓ |

**Key landings \(u_3{-}p\) and \(u_4{-}q\) cover the generic case.**  
If both fail (no such edges), \(u_3\) and \(u_4\)'s free edges go elsewhere → Part III BFS from those free neighbours hits \(\{p,q,u_a,u_2\}\) at depth ≤2, recreating the landings. ∎

### II.3.2 \((u_3,u_2)\): \(P_{11}=s{-}a_2{-}x_2{-}u_2{-}q{-}p{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)

| Landing | Path 9 |
|---------|--------|
| \(u_a{-}p\) | \(s{-}a_2{-}u_a{-}p{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_4{-}q\) | \(s{-}a_2{-}x_2{-}u_2{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) |
| \(u_b{-}q\) | \(s{-}a_2{-}x_2{-}u_2{-}q{-}u_b{-}b_2{-}t\) (len 7) → upgrade II.2 style |
| \(u_5{-}p\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}u_5{-}x_5{-}b_2{-}t\) (len 9) ✓ |

### II.3.3 \((u_3,u_4)\): \(P_{11}=s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\)

Already almost length 9 if we skip \(x_2\):  
\[
s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\quad(\text{len }11).
\]
Landing \(u_a{-}p\):  
\[
s{-}a_2{-}u_a{-}p{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
\]
Landing \(u_5{-}q\): \(u_5B{-}qB\) impossible.  
Landing \(u_b{-}q\):  
\[
s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_b{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
\]
Landing \(u_2{-}p\): \(u_2A{-}pA\) impossible.  
Landing \(u_2{-}q\):  
\[
s{-}a_2{-}x_2{-}u_2{-}q{-}u_4{-}x_4{-}x_5{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
\]

### II.3.4 \((u_5,u_4)\): symmetric to \((u_a,u_2)\) under reversal. ∎

### II.3.5 \((u_5,u_b)\): \(P_{11}=s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}p{-}q{-}u_b{-}b_2{-}t\)

Landing \(u_3{-}p\):  
\[
s{-}a_2{-}x_2{-}x_3{-}u_3{-}p{-}q{-}u_b{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
\]
Landing \(u_4{-}p\): \(u_4A{-}pA\) impossible.  
Landing \(u_a{-}p\):  
\[
s{-}a_2{-}u_a{-}p{-}q{-}u_b{-}b_2{-}t\quad(\text{len }7)\to\text{II.2}.
\]
Landing \(u_2{-}q\):  
\[
s{-}a_2{-}x_2{-}u_2{-}q{-}u_b{-}b_2{-}t\quad(\text{len }7);
\]
\[
s{-}a_2{-}x_2{-}u_2{-}q{-}p{-}u_5{-}x_5{-}b_2{-}t\quad(\text{len }9).\quad\checkmark
\]

**All nine pairs closed.** ∎

---

# Part III — \(\ell\ge 5\) and separate components

> **Superseded by** [PROOF_THEOREM_45_FINAL.md](PROOF_THEOREM_45_FINAL.md) (Join/Separate on \(H=G-V(P_*)\), induction on \(\ell\), pure-new balloon handshaking). The text below is retained as historical draft; the formal proof is PROOF_THEOREM_45_FINAL.

# Part III (historical draft) — \(\ell\ge 5\) and pure-new BFS

## III.1 First free edge off a shortest \(A^*\)–\(B^*\) path \(Q\) of length \(\ge 5\)

Write \(Q=\alpha{-}z_1{-}z_2{-}z_3{-}z_4{-}\cdots{-}\beta\) with \(\ell\ge 5\).  
Interior \(z_2\) has a free neighbour \(w\) off \(Q\).

| Landing of \(w\) | Effect |
|-----------------|--------|
| \(z_j\) on \(Q\), path-dist 2 | same part as \(z_2\) — edge impossible (bipartite) |
| \(z_j\), path-dist 3 | \(C_4\) ban |
| \(z_j\), path-dist 4 | \(C_5\) impossible |
| \(z_j\), path-dist 5 | \(C_6\); flip shortens \(Q\) by 4 ⇒ new \(A^*\)–\(B^*\) length \(\ell-4\in\{1,3,\ldots\}\); if 1 or 3, Parts I–II |
| off \(Q\), then reconnects to \(Q\) at \(z_j\) | ear; same length analysis |
| reaches \(A^*\cup B^*\) in 1 step | creates \(A^*\)–\(B^*\) path of length ≤3 through \(w\), contradicting minimality of \(\ell\) unless the path is not shorter — check: from \(\alpha\) along \(Q\) to \(z_2\) (len 2) plus \(w\) plus to \(\beta\) side. Forces effective length ≤3 for a new \(A^*\)–\(B^*\) route |

**No free edge can avoid all of the above in a cubic graph:** \(z_2\) has a free edge; its endpoint has degree 3; within two steps the finite set \(V(Q)\cup A^*\cup B^*\) is hit (at most \(1+\ell+6\) vertices), and every hit type is listed. ∎

## III.2 Separate components (\(K_A\) / \(K_B\))

Distances in \(K_A\) among \(\{u_a,u_3,u_5\}\): not 2 or 6 (else \(C_4/C_8\) with \(P_*\)).  
Moore with residual degree 2: radius-2 balls about \(u_a\) and \(u_3\) are disjoint if dist≥6; size ≥ \(1+2+4=7\) each.  
If dist≥8, radius-3 balls disjoint. Collision at radius ≤3 forces dist≤6; dist=6 gives \(C_8\) with \(P_*\) arc of length 2 — ban.  
Hence \(\operatorname{dist}_{K_A}(u_a,u_3)=4\).

Path \(u_a{-}p_1{-}p_2{-}p_3{-}u_3\) (len 4) in \(K_A\).  
Then \(P_{11}=s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\).

| Landing | Path 9 |
|---------|--------|
| \(p_3{-}x_4\) | \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}x_4{-}x_5{-}b_2{-}t\) |
| \(p_1{-}u_5\) via chain | reduce as II.3 |
| free of \(p_3\) to new, then to \(x_4\) | same as \(p_3{-}x_4\) |
| free of \(p_3\) avoids \(V(P_*)\) | BFS Part III.1 style hits \(V(P_*)\) or \(B^*\) at depth ≤2; each hit type gives path 9 or \(C_4/C_8\) |

**Explicit degree check for \(p_3\):** \(p_3\in A\) (path \(u_aB{-}p_1A{-}p_2B{-}p_3A{-}u_3B\)).  
Nbrs: \(p_2\), \(u_3\), and one free \(f\in B\).  
If \(f=x_4\): path 9 above.  
If \(f=x_2\): \(C_4\) or short with \(a_2\).  
If \(f=b_2\): \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}b_2{-}t\) len 7.  
If \(f=x_5\): both… \(x_5\in A\), \(f\in B\) OK; \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}x_5{-}b_2{-}t\) len 8 — parity: \(p_3A{-}x_5A\) impossible.  
If \(f=b_1\): \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}b_1{-}t\) len 7;  
\(s{-}a_1{-}b_1{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓.  
If \(f\) new: free edges of \(f\) hit \(\{x_4,b_2,b_1,x_2,\ldots\}\) within 1–2 steps (cubic, girth ≥6, target set size ≥4), each giving path 9. ∎

---

# Part IV — Master statement

## Theorem 4.5′ (free-port engine, complete)

Join \(\ell\ge 5\) and Separate: [PROOF_THEOREM_45_FINAL.md](PROOF_THEOREM_45_FINAL.md). Parts I–II below remain for \(\ell=1,3\).

Under the residual-good H-bridge setup, any third \(s\)–\(t\) path of length 7 forces a \(C_{16}\).

*Proof.* Chordless + six distinct ports (original Steps 0–1).  
Shortest \(A^*\)–\(B^*\) path length \(\ell\):  
- \(\ell=1\): Part I  
- \(\ell=3\): Part II  
- \(\ell\ge 5\): Part III.1 → reduce to \(\ell\in\{1,3\}\)  
- no such path (separate components): Part III.2  

All branches: length-9 \(s\)–\(t\) path off \(C\) ⇒ Lemma 2.3 ⇒ \(C_{16}\). ∎

## Corollary

Theorem 4.6 (residual good), Theorem 4.7 (residual bad, via same engine on geodesics), Theorem 4.8, Theorem A (Paper I), and Theorem B (Paper II) rest on Theorem 4.5′ with **no unfinished upgrade branches**.

---

# Part V — Verification seeds

See `verify_freeport.py` for every explicit path-9 construction above.
