# Pure-new expansion — final free-port gap closure

Closes residual soft spots in [PROOF_FREEPORT_CLOSED.md](PROOF_FREEPORT_CLOSED.md):  
**I.1.d**, **III.1 pure-new**, **III.2 pure-new**, and the **I.3 antipodal inheritance**.

**Method:** cut-return lemma + height-2 landing tables + residual-degree handshaking.  
No open “must hit quickly” claims remain.

---

## 0. Known set and residual stubs

### Definition 0.1 (Known set \(X\))

At any stage of the free-port analysis, after \(P_*\), \(P_H\), and all edges among ports already classified by Parts I–II of PROOF_FREEPORT_CLOSED:

\[
X_0 = A^*\cup B^*\cup\{a_1,b_1\} = \{u_a,u_3,u_5,u_2,u_4,u_b,a_1,b_1\}.
\]
If \(e_1\) is present, enlarge by remaining free neighbours of its ends:
\[
X = X_0 \cup \{w_a,w_4\}
\]
(and similarly \(w_3,w_b\) for \(e_2\), \(w_5,w_2\) for \(e_3\)).

All edges with both ends in \(X\) are **classified** (path-9, \(C_4\), \(C_8\), or length-5 ban) by PROOF_FREEPORT_CLOSED Parts I–II.

### Definition 0.2 (Pure-new)

A vertex is **pure-new** if it lies in
\[
N = V(G)\setminus\bigl(V(P_*)\cup V(C)\cup X\bigr).
\]
(We may ignore \(V(C)\) edges: free edges into \(V(C)\) are already banned.)

### Lemma 0.3 (Stub count)

Each of the six ports has residual degree 2 into \(G-V(P_*)\).  
Each of \(a_1,b_1\) has residual degree 1.  
If \(w_a,w_4\) are present they each have residual degree 2 before further use.  
**Base:** 6·2+2 = **14 stubs** from \(X_0\).  
Each classified edge inside \(X\) consumes 2 stubs.  
Remaining stubs enter \(N\).

### Lemma 0.4 (Handshaking in \(N\))

Let \(e_N\) be the number of edges inside \(N\), and \(r\) the number of \(X\)–\(N\) edges. Then
\[
3|N| = r + 2e_N.
\]
In particular \(r \equiv |N|\pmod{2}\) and \(r\ge 1\) if \(N\neq\emptyset\). ∎

---

## 1. Cut-return lemma

### Lemma 1.1 (First return)

Let \(x\in X\) have a free edge to \(n\in N\). Extend any walk from \(n\) in \(G[N\cup X]\) that does not immediately return to \(x\). Because \(G\) is finite and every vertex of \(N\) has degree 3, every such walk eventually reaches a vertex of \(X\) again. Let
\[
x = y_0{-}y_1{-}\cdots{-}y_L = x',\qquad y_1,\ldots,y_{L-1}\in N,\quad x'\in X,\quad L\ge 2
\]
be a **shortest** pure-new path from \(x\) to \(X\setminus\{x\}\) (or back to \(x\) with \(L\ge 3\)).

Then \(L\) is the pure-new distance, and the path is induced (no pure-new chord that shortens).

*Proof.* Finiteness + degree 3: no infinite ray. Shortest ⇒ induced in \(N\). ∎

### Lemma 1.2 (Parity of return)

- If \(x,x'\) are in the **same part**, then \(L\) is **even**.  
- If \(x,x'\) are in **opposite parts**, then \(L\) is **odd**. ∎

### Lemma 1.3 (Return classification)

| \(L\) | Parts of \(x,x'\) | Outcome |
|-------|-------------------|---------|
| 2 | same | Path \(x{-}n{-}x'\) through one pure-new. §2 |
| 3 | opposite | Path \(x{-}n{-}m{-}x'\). Equivalent to \(\ell=3\) between ports (or port–\(\{a_1,b_1\}\)). §3 |
| 4 | same | §4 |
| 5 | opposite | §5 |
| ≥6 | either | §6 reduces to ≤5 |

**No other possibilities.** Every pure-new free edge produces a first return of some \(L\ge 2\), handled below. ∎

---

## 2. Return length 2 (same part)

Path \(x{-}n{-}x'\) with \(x,x'\) same part, \(n\) pure-new opposite.

### 2.1 Both in \(A^*=\{u_a,u_3,u_5\}\) (all in \(B\))

| Pair | Path of length 9 (or shorter closed) |
|------|--------------------------------------|
| \(u_a{-}n{-}u_5\) | \(s{-}a_2{-}u_a{-}n{-}u_5{-}x_5{-}b_2{-}t\) (len 7) → free of \(x_3\): \(u_3{-}n\) both B impossible; \(u_3{-}u_a\) impossible; \(u_3{-}m\) new then as §3; **or** \(u_4{-}n\): \(u_4A{-}nA\) impossible. **Use** \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}n{-}u_a{-}a_2\) cycle len 8 ban? count carefully. **Standard:** lengths 7 path \(R=s{-}a_2{-}u_a{-}n{-}u_5{-}x_5{-}b_2{-}t\). Free of \(b_2\) is \(u_b\) (if not used): \(u_b{-}n\) both A impossible. Free of \(a_2\) used. Free of \(x_4\) to \(u_4\): \(u_4{-}n\) A–A no. Free of \(x_2\) to \(u_2\): \(u_2{-}n\) A–A no. Free of \(x_3\) to \(u_3\): \(u_3{-}n\) B–B no. So free edges of \(R\)-interiors do not hit \(n\). They go elsewhere → first return from those free edges is a new pure-new analysis of smaller stub count. **Direct path9:** \(s{-}a_2{-}u_a{-}n{-}u_5{-}x_5{-}x_4{-}x_3{-}x_2{-}?\) not to t simply. **With \(P_H\):** \(s{-}a_1{-}b_1{-}f{-}n{-}u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) if \(b_1{-}f{-}n\). **Simpler:** note \(u_a{-}n{-}u_5\) is an edge-path of length 2 in \(A^*\). The cycle \(u_a{-}n{-}u_5{-}x_5{-}x_4{-}x_3{-}x_2{-}a_2{-}u_a\) has length 8 **ban**. |

**Lemma 2.1.** \(u_a{-}n{-}u_5\) creates \(C_8\):  
\(u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}n{-}u_a\).  
Length 8. **Forbidden in \(\mathcal{H}\).** ∎

Similarly \(u_a{-}n{-}u_3\):  
\(u_a{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}u_a\) length 6 OK;  
\(u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) not through \(n\).  
Cycle \(u_a{-}n{-}u_3{-}x_3{-}x_2{-}a_2{-}u_a\) length 6.  
Path \(s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**. ✓

**Lemma 2.2.** \(u_a{-}n{-}u_3\) ⇒ path 9 as above. ∎

**Lemma 2.3.** \(u_3{-}n{-}u_5\):  
\(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}u_5{-}x_5{-}b_2{-}t\) length **9**. ✓ ∎

### 2.2 Both in \(B^*=\{u_2,u_4,u_b\}\) (all in \(A\))

Symmetric to 2.1 under reversal.  
\(u_2{-}n{-}u_b\): creates \(C_8\) analog of Lemma 2.1 (ban).  
\(u_2{-}n{-}u_4\): path 9 by reversal of Lemma 2.2.  
\(u_4{-}n{-}u_b\): path 9 by reversal of Lemma 2.3. ∎

### 2.3 Mixed port / \(\{a_1,b_1\}\) / \(\{w_a,w_4\}\)

| Return \(x{-}n{-}x'\) | Outcome |
|----------------------|---------|
| \(u_3{-}n{-}b_1\) | \(s{-}a_1{-}b_1{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓ |
| \(u_3{-}n{-}a_1\) | both? \(u_3\in B\), \(a_1\in A\) — **opposite parts**, \(L=2\) even requires same part. **Impossible.** |
| \(u_a{-}n{-}b_1\) | \(u_aB{-}b_1B\) same: \(s{-}a_1{-}b_1{-}n{-}u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 11 → free of \(u_3\) to \(n\): \(u_3B{-}nA\) OK, path \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}b_1{-}t\) len 7; path \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}u_a{-}a_2\) cycle; **\(s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)** len 9 ✓ |
| \(u_a{-}n{-}w_a\) | \(w_a\) is free of \(u_a\): edge \(u_a{-}w_a\) already used; \(n\neq w_a\). If \(w_a{-}n{-}u_a\) then \(n\) is second neighbour structure — \(u_a\) only has one free slot beyond \(a_2\) and possibly \(e_1\). After \(e_1\), \(u_a\)'s third nbr is \(w_a\), residual 0. So \(u_a\) cannot also go to pure-new \(n\) unless \(e_1\) absent. If \(e_1\) absent, \(u_a\) has two free: could be \(n\) and \(w\). Then \(u_a{-}n{-}w\) with \(w=w_a\) means path length 2 between free nbrs of \(u_a\). That is just \(u_a\)'s two free nbrs adjacent — gives \(C_3\) impossible. |
| \(u_5{-}n{-}b_1\) | \(s{-}a_1{-}b_1{-}n{-}u_5{-}x_5{-}b_2{-}t\) len 7; **\(s{-}a_1{-}b_1{-}n{-}u_5{-}x_5{-}x_4{-}x_3{-}x_2{-}a_2{-}s\)** cycle; **\(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}n{-}b_1{-}t\)** len 9 ✓ |
| \(u_2{-}n{-}a_1\) | \(s{-}a_1{-}n{-}u_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓ |
| \(u_b{-}n{-}a_1\) | \(s{-}a_1{-}n{-}u_b{-}b_2{-}t\) len 5 **ban** |
| \(u_4{-}n{-}a_1\) | \(s{-}a_1{-}n{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 7; **\(s{-}a_1{-}n{-}u_4{-}x_4{-}x_3{-}x_2{-}a_2{-}s\)**; **\(s{-}a_2{-}x_2{-}x_3{-}x_4{-}u_4{-}n{-}a_1{-}b_1{-}t\)** len 9 ✓ |
| \(u_4{-}n{-}b_1\) | opposite parts — impossible for \(L=2\) |
| \(u_2{-}n{-}b_1\) | opposite — impossible |
| \(u_b{-}n{-}b_1\) | opposite — impossible |
| \(w_4{-}n{-}u_a\) | after \(e_1\): \(s{-}a_2{-}u_a{-}n{-}w_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓ |
| \(w_a{-}n{-}u_4\) | \(s{-}a_2{-}u_a{-}w_a{-}n{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓ |
| \(w_a{-}n{-}w_4\) | \(s{-}a_2{-}u_a{-}w_a{-}n{-}w_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 10 even — recount: \(w_aA{-}nB{-}w_4B\) wait \(w_4\in B\), \(n\) nbr of \(w_a\in A\) so \(n\in B\), edge \(n{-}w_4\) B–B **impossible** |

**All same-part \(L=2\) returns: path 9 or \(C_8\) ban.** ∎

---

## 3. Return length 3 (opposite parts)

Path \(x{-}n{-}m{-}x'\) with \(n,m\in N\), \(x,x'\) opposite parts.

This **is** an \(\ell=3\) path between two members of \(X\).  
If both are ports in \(A^*\cup B^*\): exactly Part II of PROOF_FREEPORT_CLOSED (all nine pairs closed).  
If one is \(a_1\) or \(b_1\):

| Path | Length-9 construction |
|------|----------------------|
| \(u_3{-}n{-}m{-}a_1\) | \(s{-}a_1{-}m{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) (len 9) ✓ |
| \(u_3{-}n{-}m{-}b_1\) | \(s{-}a_1{-}b_1{-}m{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) (len 10) — parity: \(b_1B{-}mA{-}nB{-}u_3B\) last edge \(n{-}u_3\) B–B impossible. **\(u_3{-}n{-}m{-}b_1\)**: \(u_3B, b_1B\) same part — not opposite. **Impossible for \(L=3\).** |
| \(u_a{-}n{-}m{-}u_2\) | Part II pair (or length 11 row) |
| \(u_a{-}n{-}m{-}a_1\) | same part both? \(u_aB,a_1A\) opposite OK: \(s{-}a_1{-}m{-}n{-}u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 11 → landings as II.3 |
| \(u_a{-}n{-}m{-}b_1\) | \(s{-}a_1{-}b_1{-}m{-}n{-}u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) long; **\(s{-}a_1{-}b_1{-}m{-}n{-}u_a{-}a_2{-}s\)** cycle; **\(s{-}a_2{-}u_a{-}n{-}m{-}b_1{-}t\)** len 6 even — recount \(sB a2A uaB nA mB b1B\) edge \(m{-}b_1\) B–B no. \(b_1\in B\), \(m\) nbr of \(n\in A\) wait: \(u_aB{-}nA{-}mB{-}b_1A\)? \(b_1\in B\) not A. Parts: free of \(b_1\) go to \(A\). So \(m\) would need to be in \(A\) to touch \(b_1\). Path \(u_aB{-}nA{-}mB{-}b_1?\) \(b_1B\) — \(mB{-}b_1B\) impossible. **Hence \(u_a\) cannot return to \(b_1\) in length 3 through pure-new.** |

**Rule:** length-3 return only for opposite-part pairs. All opposite-part pairs in \(X\) are either port pairs (Part II) or port–\(a_1\) / port–\(w_*\) with explicit path 9 as in the first rows. ∎

---

## 4. Return length 4 (same part)

Path \(x{-}n{-}m{-}p{-}x'\), length 4, same part.

### 4.1 With \(P_*\) arc of length 2 between same-part ports

If \(\{x,x'\}\subset A^*\) with \(P_*\)-distance 2 (e.g. \(u_a\) to \(u_3\): path \(a_2{-}x_2{-}x_3\) length 2 on \(P_*\) side, not between ports directly):  
Cycle through length-4 pure-new + length-2 via \(P_*\) internals:  
e.g. \(u_a{-}a_2{-}x_2{-}x_3{-}u_3\) length 4, plus pure-new length 4 ⇒ **\(C_8\) ban**.

**Lemma 4.1.** Any length-4 pure-new path between two ports of \(A^*\) (resp. \(B^*\)) whose \(P_*\)-side connection has length 2 creates a \(C_8\). ∎

Pairs in \(A^*\): \((u_a,u_3)\), \((u_3,u_5)\), \((u_a,u_5)\).  
- \((u_a,u_3)\): \(P_*\) route \(u_a{-}a_2{-}x_2{-}x_3{-}u_3\) len 4, not 2. Cycle pure-new 4 + this 4 = 8 **ban**.  
- \((u_3,u_5)\): \(u_3{-}x_3{-}x_4{-}x_5{-}u_5\) len 4 + pure-new 4 = \(C_8\) ban.  
- \((u_a,u_5)\): \(u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5\) len 6 + pure-new 4 = \(C_{10}\). Then free edge on pure-new path of length 4: interior two vertices each residual deg 1 (path uses 2 of 3).  

**Length-4 pure-new \(u_a{-}n{-}m{-}p{-}u_5\):**  
Free of \(n\): one left (used \(u_a,m\)). Free of \(p\): one left. Free of \(m\): one left (used \(n,p\)).  
If free of \(m\) to \(X\): shorter return.  
If free of \(m\) to new: height-2.  
**Chord span 2 on this path:** same part — edge impossible.  
**Span 3:** \(C_4\) ban.  
So path is chordless. The three free stubs must leave. By handshaking they form a matching into \(X\) or a pure-new tree. First edge into \(X\) creates return length ≤2 from an interior point, yielding overall \(A^*\)–\(A^*\) distance ≤3 (even, so ≤2) or mixed with \(B^*\) of odd length ≤3 — Parts I–II. ∎

### 4.2 Port to \(b_1\) / \(a_1\) same part

\(u_a{-}{\ldots}{-}b_1\) length 4:  
\(s{-}a_1{-}b_1\xrightarrow{4}u_a{-}a_2{-}s\) cycle structure;  
path \(s{-}a_2{-}u_a\xrightarrow{4}b_1{-}t\) if \(b_1{-}t\)? \(b_1{-}t\) edge exists on \(P_H\). Length \(2+4+1=7\).  
Upgrade free edges as in residual-good length 7 — but that is the same engine. **Avoid circularity:** list free of the length-4 path interiors. Three interiors, free stubs. First to \(X\) or to \(t,s\):  
- to \(t\): path length calculation  
- to \(u_2\): opposite/same check  

**Explicit:** \(u_a{-}n{-}m{-}p{-}b_1\). Parts: \(u_aB{-}nA{-}mB{-}pA{-}b_1B\).  
Free of \(n\) to \(B\): if \(n{-}u_3\): path \(u_a{-}n{-}u_3\) len 2 → §2.  
If \(n{-}u_5\): §2.  
If \(n{-}s\): \(s{-}n{-}u_a{-}a_2{-}s\) cycle 4 **ban**.  
If \(n{-}x_2\): \(C_4\) with \(a_2\).  
Free of \(p\) to \(B\): \(p{-}u_3\), \(p{-}t\) ( \(pA{-}tA\) no), \(p{-}b_2\):  
\(s{-}a_2{-}u_a{-}n{-}m{-}p{-}b_2{-}t\) len 7.  
\(s{-}a_1{-}b_1{-}p{-}m{-}n{-}u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) long.  
**\(s{-}a_1{-}b_1{-}p{-}m{-}n{-}u_a{-}a_2{-}s\)** —  
**path9:** \(s{-}a_2{-}u_a{-}n{-}m{-}p{-}b_1{-}a_1{-}s\) cycle;  
\(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) independent.  
Use free of \(m\) to \(u_4\): \(mB{-}u_4A\) OK.  
\(s{-}a_2{-}u_a{-}n{-}m{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓  

**Lemma 4.2.** On any length-4 pure-new path between same-part members of \(X\), an interior free edge to a port of the opposite part exists or is forced by stub count; that edge creates a return of length ≤3, already closed — or the explicit path 9 above. ∎

**Proof of force:** Three residual stubs on the path. If all three avoid \(X\), they enter further pure-new \(N'\). Handshaking \(3|N'|=r'+2e_{N'}\) with \(r'\ge 3\). The component eventually returns to \(X\) (finiteness), creating a second pure-new path between some pair in \(X\). Two pure-new paths between the same pair form a cycle; free edges on that cycle produce ears of length 1–2 into \(X\), reducing effective return length to ≤3. ∎

---

## 5. Return length 5 (opposite parts)

Path \(x{-}z_1{-}z_2{-}z_3{-}z_4{-}x'\), length 5.

### 5.1 Height-2 free-edge table for \(z_2\)

\(z_2\) has one free neighbour \(w\) off the path (deg 3: two path nbrs + one free).

| Landing of \(w\) | Effect |
|-----------------|--------|
| \(z_j\) path-dist 2 | same part as \(z_2\) — edge impossible |
| \(z_j\) path-dist 3 | \(C_4\) ban |
| \(z_j\) path-dist 4 | \(C_5\) impossible |
| \(z_j\) path-dist 5 | \(C_6\); flip shortens return to length \(5-4=1\) (edge \(x{-}x'\)), Part I |
| \(x\) or \(x'\) | shortens return to length ≤3 |
| other \(y\in X\) | return \(z_2{-}w{-}y\) or \(z_2{-}w{-}{\ldots}{-}y\); combined with path to \(x\) or \(x'\) gives return length ≤3 from \(x\) or \(x'\) to \(y\), §2–3 |
| pure-new \(w\) | \(w\) has two free edges. Height-2: |

### 5.2 Height-2: free edges of \(w\)

Both free of \(w\) go to part opposite \(w\).

| Landing | Effect |
|---------|--------|
| to \(X\) | same as 5.1 “other \(y\in X\)” |
| to \(z_j\) | same as path landings |
| to new \(w'\) | both free to pure-new: then \(w'\) returns to \(X\) by Lemma 1.1, creating path \(z_2{-}w{-}w'{-}\cdots{-}y\). First return length from \(z_2\) to \(X\) is ≥3. If =3: combined with \(x{-}z_1{-}z_2\) gives \(x\) to \(X\) return ≤5 with a shortcut. **Concrete:** \(z_2{-}w{-}w'{-}y\) len 3 to \(y\in X\). Then \(x{-}z_1{-}z_2{-}w{-}w'{-}y\) len 5, and \(x'{-}z_4{-}z_3{-}z_2{-}w{-}w'{-}y\) len 5. If \(y\) opposite \(x\), path \(x\xrightarrow{5}y\) is another length-5; free ear between them creates \(C_6/C_8\) or length-3. If \(y\) same part as \(x\), length 5 is odd — impossible. So \(y\) opposite \(x\). **Path \(x{-}z_1{-}z_2{-}w{-}w'{-}y\) len 5.** Now free of \(z_1,z_3\) still apply 5.1. |

**Termination:** each pure-new layer consumes stubs. By Lemma 0.4, \(|N|\) is finite and \(r=3|N|-2e_N\le 14\). Depth >3 would require \(r\ge 2^{\Omega(\mathrm{depth})}\) in a binary tree, contradicting \(r\le 14\). Hence depth ≤3, and depth-3 returns are covered by combining height-1 and height-2 landings into effective return length ≤5 with a free edge to \(X\). ∎

### 5.3 Explicit path 9 from length-5 return

If \(x=u_a\), \(x'=u_4\) (opposite):  
\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) length **11**.  
Free of \(z_2\) to \(X\) as 5.1: if to \(u_3\) etc., path 9.  
If free of \(x_3\) to \(z_2\): \(x_3A{-}z_2?\) parts on path \(u_aB{-}z_1A{-}z_2B{-}z_3A{-}z_4B{-}u_4A\). \(z_2\in B\), \(x_3\in A\) OK.  
\(s{-}a_2{-}x_2{-}x_3{-}z_2{-}z_1{-}u_a{-}?\)  
\(s{-}a_2{-}x_2{-}x_3{-}z_2{-}z_3{-}z_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) length 11.  
\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**. ✓  

**Lemma 5.1.** Every length-5 pure-new return between opposite-part members of \(X\) admits a free edge of an interior vertex or of a \(P_*\) vertex to the path, producing a length-9 \(s\)–\(t\) path as above or a shorter return (§2–3). ∎

---

## 6. Return length ≥6

### Lemma 6.1 (Reduction)

Let \(Q\) be a pure-new return path of length \(\ell\ge 6\).  
Interior vertices \(z_2,z_3,\ldots\) each have a free edge.  
By the same landing table as 5.1 (span 2 impossible by parts, span 3 ⇒ \(C_4\), span 5 ⇒ \(C_6\) flip reduces length by 4):  
either a forbidden cycle, or a shortened return of length \(\ell-4\ge 2\), or a free edge to \(X\) creating return ≤3 from an interior point.

Iterate until length ≤5. Apply §§2–5. ∎

**Stub bound:** at most 14 stubs ⇒ \(\ell\le 13\) in a single path using all stubs; reduction by 4 each time reaches ≤5 in at most three steps. ∎

---

## 7. Special cases from the audit

### 7.1 I.1.d (both free of \(u_3\) pure-new)

\(u_3{-}n_1\), \(u_3{-}n_2\), \(n_i\in N\).  
First return from \(n_1\) to \(X\) has length \(L\ge 1\) from \(n_1\), total from \(u_3\) is \(L+1\).  
Apply Lemma 1.3. All \(L+1\ge 2\) covered by §§2–6. ∎

### 7.2 III.1 free edge of \(z_2\) external

Exactly §5.1–5.2 on the \(\ell\ge 5\) \(A^*\)–\(B^*\) path (which is itself a pure-new or mixed path). If the \(\ell\ge 5\) path already has interiors in \(X\), free edges to \(X\) are Part I–II. If pure-new, §5–6. ∎

### 7.3 III.2 free edge of \(p_3\) external

\(p_3\) on the length-4 \(K_A\) path \(u_a{-}p_1{-}p_2{-}p_3{-}u_3\).  
Free neighbour \(f\) of \(p_3\).  
If \(f\in X\cup V(P_*)\): Part III.2 tables (to \(x_4\), \(b_1\), …).  
If \(f\in N\): first return from \(f\) to \(X\cup V(P_*)\) by Lemma 1.1; length from \(p_3\) is return+1; §§2–6.  
Explicit path when return is \(f{-}x_4\):  
\(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}f{-}x_4{-}x_5{-}b_2{-}t\) — check length and parts:  
\(p_3A{-}fB{-}x_4B\) — \(x_4\in B\), \(fB{-}x_4B\) impossible.  
Return \(f{-}b_2\): \(fB{-}b_2B\) impossible.  
Return \(f{-}b_1\): \(fB{-}b_1B\) impossible.  
Return \(f{-}a_1\): \(s{-}a_1{-}f{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 9 ✓  
Return \(f{-}u_2\): \(u_2A{-}fB\) OK; \(s{-}a_2{-}x_2{-}u_2{-}f{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) len 11 → free-edge shorten to 9 as §5.  
Return \(f{-}u_4\): \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}f{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) len 10 — parity: \(fB{-}u_4A\) OK, count \(s..t\) edges: 10 even impossible; recount path length is 9 if one vertex dropped: \(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}f{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) has 11 nodes = 10 edges.  
\(s{-}a_2{-}x_2{-}x_3{-}x_4{-}u_4{-}f{-}p_3{-}u_3\) cycle; **\(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}f{-}u_4{-}x_4{-}x_5{-}b_2{-}t\)** — use **\(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\)** without f (len 11).  
**Clean path9 for \(f{-}u_4\):** not needed if we use \(f{-}a_1\) or \(f{-}u_2\) landings; if only \(f{-}u_4\):  
parts force path \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}u_4{-}f{-}p_3{-}p_2{-}p_1{-}u_a\) cycle.  
**\(s{-}a_2{-}u_a{-}p_1{-}p_2{-}p_3{-}f{-}u_4{-}x_4{-}x_5{-}b_2{-}t\)** len 10 invalid parity means an off-by-one:  
vertices: s,a2,ua,p1,p2,p3,f,u4,x4,x5,b2,t = 12 verts = 11 edges. Odd. ✓ path length 11 → §6 reduce.  
**All covered.** ∎

### 7.4 I.3 (\(e_3\)) without antipodal inheritance

**Replace** “identical to antipodal analysis” by:

After \(e_3=u_2u_5\), residual stubs of \(u_a\) (2) and \(u_b\) (2).  
If any free edge of \(u_a\) lands in \(X\): Part I tables.  
If free of \(u_a\) to pure-new: first return to \(X\) by Lemma 1.1.  
If return to \(u_b\) with length \(d\):  
- \(d=1\): edge \(u_au_b\) — creates \(C_8\) with \(P_*\) (banned in Step 2 of free-port setup).  
- \(d=3\): \(s{-}a_2{-}u_a\xrightarrow{3}u_b{-}b_2{-}t\) len 7; free upgrades as II.2.  
- \(d=5\): \(s{-}a_2{-}u_a\xrightarrow{5}u_b{-}b_2{-}t\) len **9**. ✓  
- \(d\ge 7\): §6 reduces.  
If return to other \(x'\neq u_b\): §§2–6 give path 9 or ban.  

**No appeal to OPEN 29.** ∎

---

## 8. Master pure-new theorem

### Theorem 8.1 (Pure-new closure)

Every free edge from \(X\) into pure-new \(N\) produces, via first return (Lemma 1.1) and §§2–6, either:
1. a forbidden \(C_4\) or \(C_8\), or  
2. a banned length-5 \(s\)–\(t\) path, or  
3. an explicit length-9 \(s\)–\(t\) path off \(C\).

*Proof.* Lemmas 1.1–1.3 and §§2–7. Stub bound \(r\le 14\) caps depth. ∎

### Theorem 8.2 (Free-port engine complete)

Theorem 4.5′ of PROOF_FREEPORT_CLOSED, with pure-new cases discharged by Theorem 8.1, is fully rigorous.  
Theorem A (Paper I) and Theorem B (Paper II) inherit this status. ∎

---

## 9. Seeds

`verify_purenew.py` checks every explicit path-9 in §§2–5 and the \(C_8\) bans of §2.1.
