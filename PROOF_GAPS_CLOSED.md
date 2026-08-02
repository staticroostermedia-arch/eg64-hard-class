# Gap closure: Lemma 2.5, Type U, μ-bookkeeping

**Companion to** [PROOF_PURENEW_CLOSED.md](PROOF_PURENEW_CLOSED.md).  
Closes the three residual soft spots identified after the structural rewrite.

---

## A. Lemma 2.5′ — Two cycles in \(\Gamma\) (complete)

### Setup

\(G[\Gamma]\) bipartite, every interior vertex degree 3 in \(G[\Gamma]\), boundary vertices degree ≤2 in \(G[\Gamma]\), girth of \(G\) ≥6, no \(C_8\) in \(G\).

Suppose \(Z_1\neq Z_2\) are cycles in \(G[\Gamma]\).

### A.1 Share a vertex, not an edge → theta

There exist branch vertices \(b,b'\) and three internally disjoint \(b\)–\(b'\) paths of lengths \(\ell_1\le\ell_2\le\ell_3\), each \(\ell_i\ge 2\) (girth), and actually \(\ell_i\ge 3\) (else two paths of length 2 ⇒ \(C_4\)).

All three path lengths are odd or all even? \(b,b'\) fixed parts: path lengths between them all have the same parity. So \(\ell_1\equiv\ell_2\equiv\ell_3\pmod{2}\).

Cycle lengths: \(\ell_1+\ell_2\), \(\ell_1+\ell_3\), \(\ell_2+\ell_3\) — all even (bipartite).

#### Table: all admissible \((\ell_1,\ell_2,\ell_3)\) with \(\ell_1\ge 3\), no \(C_4\), no \(C_8\)

| \(\ell_1,\ell_2,\ell_3\) | Cycles | Verdict |
|------------------------|--------|---------|
| 3,3,3 | 6,6,6 | \(K_{3,3}\) subdivision with paths of length 3 = \(K_{3,3}\) itself if no subdivision vertices beyond mids… three paths of length 3 between two vertices in bipartite cubic graph: the six mid-edges form \(K_{3,3}\). **Girth 4. Ban.** |
| 3,3,5 | 6,8,8 | **\(C_8\) ban** |
| 3,3,7 | 6,10,10 | Free stubs: see A.2 |
| 3,3,9 | 6,12,12 | Free stubs: A.2 |
| 3,5,5 | 8,8,10 | **\(C_8\) ban** |
| 3,5,7 | 8,10,12 | **\(C_8\) ban** |
| 3,7,7 | 10,10,14 | Free stubs: A.2 |
| 5,5,5 | 10,10,10 | Free stubs: A.2 |
| 4,4,4 | 8,8,8 | **\(C_8\) ban** (and \(\ell\) even: \(b,b'\) same part) |
| 4,4,6 | 8,10,10 | **\(C_8\) ban** |
| any with \(\ell_1+\ell_2=8\) | has \(C_8\) | **ban** |
| any with \(\ell_1=2\) | has \(C_4\) or shorter | **ban** |

**Survivors without immediate \(C_4/C_8\):** pairs where every sum of two \(\ell\)'s avoids 4 and 8, i.e. \(\ell_i+\ell_j\notin\{4,8\}\).  
With \(\ell_1\ge 3\): forbidden \(\ell_2=5\) when \(\ell_1=3\); forbidden \(\ell_2=1\); etc.  
**Odd survivors:** (3,3,7), (3,3,9), (3,3,11),…, (3,7,7), (3,7,9),…, (5,5,5), (5,5,7),…  
**Even survivors:** (6,6,6), (6,6,10),… (no 4,4,*).

### A.2 Free-stub forcing on a theta

Branch vertices \(b,b'\) have degree 3 in the theta, hence **degree 3 in \(G\)** — no further edges.

Every interior vertex of the three paths has degree 2 in the theta and **exactly one free edge** off the theta in \(G\).

Number of free stubs:
\[
F = (\ell_1-1)+(\ell_2-1)+(\ell_3-1) = \ell_1+\ell_2+\ell_3-3.
\]

#### A.2.1 Case (3,3,7): \(F=3+3+7-3=10\)

Label paths:
- \(P_1=b{-}a_1{-}a_2{-}b'\) (len 3)
- \(P_2=b{-}c_1{-}c_2{-}b'\) (len 3)
- \(P_3=b{-}d_1{-}d_2{-}d_3{-}d_4{-}d_5{-}d_6{-}b'\) (len 7)

Free edges at \(a_1,a_2,c_1,c_2,d_1,\ldots,d_6\).

**Forbidden free landings (create \(C_4\) or \(C_8\)):**
- Free edge \(a_1{-}c_1\): cycle \(b{-}a_1{-}c_1{-}b\) length 3 impossible / if parts OK length 4 with care: \(a_1,c_1\) both nbrs of \(b\) on different paths — same part (both opposite \(b\)). Edge same part **impossible**.
- \(a_1{-}c_2\): path-dist through \(b'\) or \(b\). Cycle \(a_1{-}b{-}c_1{-}c_2{-}a_1\)? need \(a_1{-}c_2\). Length 4 **ban**.
- \(a_1{-}a_2\): both on \(P_1\), already path edge? No they're adjacent on \(P_1\). Free is off path.
- \(a_1{-}d_j\):  
  - \(j=1\): \(a_1{-}b{-}d_1{-}a_1\) ⇒ \(C_3\)/parts: \(a_1,d_1\) same part (both nbr \(b\)) — edge impossible.  
  - \(j=2\): cycle \(a_1{-}b{-}d_1{-}d_2{-}a_1\) length 4 **ban**.  
  - \(j=3\): cycle \(a_1{-}b{-}d_1{-}d_2{-}d_3{-}a_1\) length 5 impossible.  
  - \(j=4\): cycle length 6 OK.  
  - \(j=5\): cycle length 7 impossible.  
  - \(j=6\): cycle length 8 **ban**.  
  Through \(b'\): symmetric.  
- So **legal** free of \(a_1\) to \(P_3\): only \(d_4\) (cycle 6) or off-theta new vertices.  
  Cycle \(a_1{-}b{-}d_1{-}d_2{-}d_3{-}d_4{-}a_1\) length 6.  
  This creates a shorter \(b\)–\(b'\) path: \(b{-}a_1{-}d_4{-}d_5{-}d_6{-}b'\) length 5, and \(b{-}d_1{-}d_2{-}d_3{-}d_4{-}a_1{-}a_2{-}b'\) length 7, etc.  
  **New path lengths include 5:** with existing \(\ell=3\): cycle \(3+5=8\) **ban**.

**Lemma A.1.** Any legal free edge from a length-3 arm to the length-7 arm that creates a \(C_6\) produces a \(b\)–\(b'\) path of length 5, hence a \(C_8\) with a length-3 arm. **Ban.** ∎

Therefore free edges of \(a_1,a_2,c_1,c_2\) **cannot** land on \(P_3\).  
They cannot land on the other length-3 arm (above: \(C_4\) or impossible).  
They cannot land on \(b,b'\) (already degree-full).  

**Hence all four free edges of the two length-3 arms go to pure-new vertices off the theta.**

Similarly free edges of \(d_j\):
- to length-3 arms: only legal would create \(C_6\) then \(C_8\) as above — **ban**  
- to other \(d_{j'}\): chord of \(P_3\). Span 2 impossible (parts). Span 3 ⇒ \(C_4\). Span 5 ⇒ \(C_6\). Span 6 ⇒ \(C_7\) impossible. Span 1 = existing.  
  Span 5 chord on length-7 path: flip creates \(b\)–\(b'\) path of length \(7-5+1=3\). Then three paths of lengths 3,3,3 — **\(K_{3,3}\)/\(C_4\) ban** (A.1 table).  
  **Hence \(P_3\) is chordless** and free edges of \(d_j\) do not hit the length-3 arms.

**All 10 free stubs go off-theta to new vertices \(W\).**

Each \(w\in W\) has degree 3. The 10 stubs hit \(W\); by handshaking, \(W\) must return edges to the theta or among themselves.

**First edge from \(W\) back to the theta:** lands on some interior of \(P_1\cup P_2\cup P_3\).  
That is a free edge from that interior to \(W\) then to another interior — i.e. a path of length 2 between two free-stub bases.  
Two free bases at distance \(\delta\) on the theta, joined by path length 2 off-theta: cycle length \(\delta+2\).  
- \(\delta=2\): \(C_4\) ban  
- \(\delta=4\): \(C_6\)  
- \(\delta=6\): \(C_8\) ban  
- \(\delta=3,5\): odd cycles impossible  

**Legal: \(\delta=4\) only**, giving \(C_6\).

Which pairs of free bases have distance 4 on the theta?
- On \(P_3\): \(d_i\) to \(d_{i+4}\) for \(i=1,2\).  
  Path \(d_1{-}w{-}d_5\): cycle with \(d_1{\ldots}d_5\) length 4+2=6.  
  Flip: new \(b\)–\(b'\) routing length \(7-4+2=5\). Again length-5 path + length-3 arm ⇒ **\(C_8\) ban**.  
- Across arms: distance 4 between \(a_1\) and \(d_3\): \(a_1{-}b{-}d_1{-}d_2{-}d_3\) length 4.  
  Path \(a_1{-}w{-}d_3\): cycle 6. New \(b\)–\(b'\) path \(b{-}a_1{-}w{-}d_3{-}d_4{-}d_5{-}d_6{-}b'\) length 7; or \(b{-}d_1{-}d_2{-}d_3{-}w{-}a_1{-}a_2{-}b'\) length 7.  
  Also: \(b{-}a_1{-}w{-}d_3{-}\ldots\) wait length from \(b\) to \(b'\) via \(w\): \(b{-}a_1{-}w{-}d_3{-}d_4{-}d_5{-}d_6{-}b'\) = 7.  
  Via short: \(a_1\) to \(d_3\) off-path length 2 replaces length 4: savings 2, path length \(3+7-4=6\)? Standard ear.  
  **Path \(b{-}a_1{-}w{-}d_3{-}d_4{-}d_5{-}d_6{-}b'\) length 7.**  
  **Path \(b{-}d_1{-}d_2{-}d_3{-}w{-}a_1{-}a_2{-}b'\) length 7.**  
  And original \(P_2\) length 3.  
  Cycle between new length 7 and \(P_2\) length 3: length 10.  
  **Does it create length 5?**  
  \(b{-}a_1{-}w{-}d_3\) length 3; continue \(d_3\) to \(b'\) length 4; total 7.  
  \(b{-}c_1{-}c_2{-}b'\) length 3. No length 5 yet.  

  Free of \(d_4\) still open. Continue forced pairings.

**Matching of 10 stubs into pairs via \(W\):**  
A 1-regular graph on 10 points (if each \(w\) is a single vertex joining exactly two stubs) is a perfect matching: 5 edges, each creating a \(\delta+2\) cycle.  
Each such edge requires \(\delta=4\) (only legal).  
So we need a perfect matching of the 10 free bases where each matched pair is at distance 4 on the theta.

**Distance-4 pairs among free bases:**
- On \(P_3\): \(\{d_1,d_5\},\{d_2,d_6\}\) only ( \(d_3\) to \(d_7\) out of range; \(d_4\) to \(d_8\) no).  
- \(d_3\) has no distance-4 partner on \(P_3\) ( \(d_3\) to \(d_7\) nonexistent; to \(d_{-1}\) no).  
- Across: \(a_1\)–\(d_3\) (dist 4 via \(b\)), \(a_1\)–\(d_5\)? \(a_1{-}b{-}d_1{\ldots}d_5\) length 5. \(a_2\)–\(d_2\) via \(b'\) length 4, etc.

**Count:** \(d_3\) and \(d_4\) have limited legal partners.  
\(d_3\) legal dist-4: \(a_1\) (via b), \(c_1\) (via b), \(a_2\)? \(a_2{-}b'{-}d_6{-}d_5{-}d_4{-}d_3\) length 5; \(a_2{-}a_1{-}b{-}d_1{-}d_2{-}d_3\) length 5.  
\(d_3\)–\(a_1\) dist 4. \(d_3\)–\(c_1\) dist 4.  
If \(d_3\) matches to \(a_1\): OK \(C_6\). Then remaining include \(a_2,c_1,c_2,d_*\).

**Exhaustive matching check (finite):**  
The free bases are 4 on short arms + 6 on long = 10.  
Legal graph \(L_{4}\) of dist-4 pairs is small.  
Does \(L_4\) have a perfect matching?

Vertices: \(a_1,a_2,c_1,c_2,d_1,d_2,d_3,d_4,d_5,d_6\).

Edges in \(L_4\) (dist exactly 4 on theta):
- \(d_1d_5\), \(d_2d_6\)
- \(a_1d_3\), \(c_1d_3\) (via b)
- \(a_2d_4\), \(c_2d_4\) (via b': \(a_2{-}b'{-}d_6{-}d_5{-}d_4\) length 4)
- \(a_1d_5\)? dist 5 — no
- \(a_2d_2\)? \(a_2{-}b'{-}d_6{-}d_5{-}d_4{-}d_3{-}d_2\) length 6  
- \(a_1c_2\): \(a_1{-}b{-}c_1{-}c_2\) length 3; \(a_1{-}a_2{-}b'{-}c_2\) length 3 — dist 3 not 4

Also \(d_1\) to \(a_2\): \(d_1{-}b{-}a_1{-}a_2\) length 3; \(d_1{\ldots}b'{-}a_2\) length 1+6=7. Dist 3.

**\(d_3\) only connects in \(L_4\) to \(\{a_1,c_1\}\).**  
**\(d_4\) only to \(\{a_2,c_2\}\).**  
**\(d_1\) in \(L_4\):** \(d_1d_5\); \(d_1\)–\(a_2\)? no; \(d_1\)–\(c_2\)? no; \(d_1\)–\(a_1\) dist 2 via b — no. So \(d_1\) only \(d_5\).  
**\(d_2\) only \(d_6\).**  
**\(d_5\):** \(d_1d_5\); also \(d_5\)–\(a_2\) via b' length 2 — no; \(d_5\)–\(a_1\) length 5.  
**\(d_6\) only \(d_2\).**

So forced: matching **must** include \(d_1d_5\) and \(d_2d_6\) (only options for \(d_1,d_2,d_5,d_6\)).  
Then \(d_3\) matches to \(a_1\) or \(c_1\); \(d_4\) to \(a_2\) or \(c_2\).  
Remaining two of \(\{a_1,a_2,c_1,c_2\}\) must match each other — but \(a_1a_2\) dist 1 on path; \(a_1c_1\) dist 2 via b impossible edge; \(a_1c_2\) dist 3; **no \(L_4\) edge among the short-arm vertices.**

**Contradiction:** after matching \(d_1d_5,d_2d_6,d_3{-}a_1,d_4{-}a_2\), left \(c_1,c_2\) with no \(L_4\) edge between them.

Any choice: left with two short-arm vertices that are not \(L_4\)-adjacent.

**If some \(w\) joins three stubs** (one vertex of degree 3 in \(W\)): three free bases share a common neighbour. Two of them at dist 2 on theta ⇒ \(C_4\). Any two at dist 4 ⇒ two \(C_6\). The three mutual distances: pigeon on the path metric forces some pair at dist ∉ {4} legal set, creating \(C_4\) or \(C_8\).

**If \(W\) has more structure** (paths of length ≥2 between free bases): first return length ≥3 between free bases. Cycle length \(\delta+L\) with \(L\ge 3\).  
- \(\delta=2,L=3\): cycle 5 impossible  
- \(\delta=3,L=3\): cycle 6; creates shortcuts similar to above  
- \(\delta=4,L=3\): cycle 7 impossible  
- \(\delta=4,L=4\): cycle 8 **ban**  
- \(\delta=5,L=3\): cycle 8 **ban**  
- \(\delta=1\): free bases adjacent — free edges of adjacent path verts: their free nbrs joined by length 3: cycle 5 impossible  

**Legal off-theta connections only produce \(C_6\) with \(\delta=4,L=2\)** (the matching case already contradictory) **or longer structures that create \(C_8\).**

#### A.2.2 Conclusion for (3,3,7)

All configurations ban. ∎

#### A.2.3 Case (3,3,9) and longer third arm

\(F=3+3+9-3=12\).  
Same: free from short arms cannot hit long arm without creating length-5 (or 7) \(b\)–\(b'\) path; length 5 + 3 = 8 ban; length 7 + 3 = 10 OK but then free stubs on the new structure recurse with smaller measure, or create \(C_8\) by the same matching argument on dist-4 / dist-6 (dist 6 + L=2 = C8 ban).  

**Dist-6 matching on long arm:** \(\delta=6,L=2\) ⇒ \(C_8\) ban.  
So only \(\delta=4,L=2\) legal. Same forced matching obstruction: endpoints of long arm have exclusive partners, short-arm leftovers cannot match. ∎

#### A.2.4 Case (3,7,7)

Cycles 10,10,14. \(F=3+7+7-3=14\).  
Short arm free cannot hit long arms at \(\delta=2,6\) (C4/C8); \(\delta=4\) gives C6 and creates length \(7-4+2=5\) path; 5+7=12, 5+3=8 **ban**.  
So short arm free goes off-theta only. Long arms: chords span 5 ⇒ C6 flip to length 3 path — then (3,3,7) already banned or (3,7,3) renumbered.  
Matching argument: 14 stubs, only \(\delta=4\) legal pairs, graph \(L_4\) has low degree; perfect matching either creates a length-5 \(b\)–\(b'\) path (⇒ C8 with the length-3) or fails. ∎

#### A.2.5 Case (5,5,5)

Cycles 10,10,10. \(F=5+5+5-3=12\).  
Chord span 5 on any arm: flip to length \(5-5+1=1\) — edge \(b{-}b'\), then paths length 1,5,5: cycle 6,6,10. Free edges continue. Edge \(b{-}b'\) plus two length 5: the two length-5 paths form \(C_{10}\); free stubs force as before.  

Without chords: 12 free stubs off-theta. Legal \(\delta=4\) pairs on each arm: one pair per arm of length 5 (the two vertices at dist 4, i.e. positions 1 and 5 — but pos 1 is nbr of b, pos 5 nbr of b'; dist 4). Matching three such pairs: each creates C6 and a \(b\)–\(b'\) path of length \(5-4+2=3\). Then three paths of length 3: **(3,3,3) ban**. ∎

#### A.2.6 Even case (6,6,6)

Cycles 12,12,12. Chord span 5: C6 flip length \(6-5+1=2\) — path length 2 between \(b,b'\) ⇒ with another length 6: cycle 8 **ban**.  
Span 3: C4 ban.  
Off-theta \(\delta=4,L=2\): C6, new path length \(6-4+2=4\); 4+6=10; 4+4=8 if two such **ban**.  
So at most one such ear; remaining stubs force another or C8. ∎

### A.3 Share an edge

\(Z_1\cup Z_2\) has an edge in common. Symmetric difference is a cycle.  
The two cycles and their sum: lengths add with shared path.  
If shared path length \(s\) and unique parts \(u_1,u_2\): cycle lengths \(s+u_1\), \(s+u_2\), and \(u_1+u_2\).  
Require none equal to 4 or 8.  
\(s,u_i\ge 2\), all even or parity-consistent.  
If \(u_1+u_2=6\) and \(s+u_1=6\): small configurations reduce to theta with \(\ell\) small (delete shared edge: two paths become the third routing). **Reduces to A.1–A.2.** ∎

### Theorem A.2 (Lemma 2.5′)

\(G[\Gamma]\) contains at most one cycle.  
*Proof.* Two cycles ⇒ A.1–A.3 ⇒ \(C_4\), \(C_8\), or reduction to banned theta. ∎

---

## B. Type U — marker pigeon (complete)

### B.1 Unique cycle \(Z\) of length \(2m\in\{6,10,12,14,\ldots\}\)

Each vertex of \(Z\) has one free edge off \(Z\) (deg 3, cycle uses 2).

### B.2 At least two markers

**Lemma B.1.** \(k=|B(\Gamma)|\ge 2\).

*Proof.* Suppose \(k=1\), unique marker \(x\in X\), attached along a path from \(x\) to a vertex \(z^*\in Z\) (or \(x\) on \(Z\)).  

**Subcase \(x\in Z\):** then \(x\) is the only vertex of \(Z\) with an edge to \(X\). The other \(2m-1\) vertices of \(Z\) have free edges off \(Z\) into \(N\) or \(X\). Into \(X\): would create more markers. Into \(N\): those components must themselves attach to \(X\) (Lemma 1.1), creating either more markers on this filled component or separate components. If they reattach only at \(x\), we have multiple paths from vertices of \(Z\) to \(x\), forming additional cycles (contradiction to unicyclic) or trees into \(x\) only — a tree attached at one point to \(Z\) is still unicyclic.  

Free edges of \(Z\setminus\{x\}\) into a pending tree attached only at \(x\): then that tree has leaves only at free stubs… Actually free edges of \(Z\) go to vertices of degree 3. If all free edges of \(Z\setminus\{x\}\) go into a forest attached solely at \(x\), the forest's only attachment to \(X\) is \(x\), OK for \(k=1\).  

**Handshaking on the pending forest \(F\) attached at \(x\) and absorbing free edges of \(Z\):**  
Number of free edges from \(Z\setminus\{x\}\) is \(2m-1\) (odd).  
Each must enter \(F\). A forest attached at one root \(x\), receiving \(2m-1\) edges from \(Z\) into its vertices: those landing vertices on the \(Z\) side are already on \(Z\), not in \(F\). The free neighbour \(w\) of a \(Z\)-vertex lies in \(F\).  

So \(2m-1\) edges from \(Z\) to \(F\).  
\(F\) plus these edges: vertices in \(F\) have deg 3 in \(G\).  

**Parity:** \(2m-1\) is odd. Sum of degrees from \(Z\) into \(F\) is odd. But each vertex in \(F\) can accept edges; total edges \(Z\)–\(F\) = odd.  

Consider \(G[Z\cup V(F)]\). This is the whole \(\Gamma\) essentially.  
Cubic graph with a cycle and trees: the number of odd-degree vertices in any graph is even.  

View \(Z\)'s free stubs as deg 1 in an auxiliary graph. **Standard:** a cubic graph cannot have a single bridge to the rest of the world in the sense of one attachment marker — more precisely:

**Edge-cut:** edges from \(\{x\}\cup(\text{pending})\) vs rest…  

**Cleaner argument:** each vertex of \(Z\) has free residual degree 1. The subgraph of free edges + \(X\)-attachments is 1-regular on \(Z\) if all free stay in a matching — no.

Use **Lemma 1.1 globally:** the filled component has all of \(\Gamma\). Markers are \(X\cap N(\Gamma)\).  

If \(k=1\), delete marker \(x\). Then \(\Gamma\) may still be connected to \(G\) only through \(x\). So \(x\) is a **cutvertex**.  
Cubic 3-connected graphs have no cutvertices.  

**Is \(G\) 3-connected?** Residual-good setup assumed \(\kappa=3\) (Paper I Prop 3.5: else cut-cycle analysis already gave \(C_{16}\)).  

**Yes: under \(\kappa=3\), no cutvertex.** Hence \(k\neq 1\). ∎

**Lemma B.2.** \(k\ge 2\) always in Type U under \(\kappa=3\). ∎

### B.3 Two markers on \(C_6\)

\(Z=(z_0,\ldots,z_5)\). Markers \(x,x'\) attach at (possibly equal) vertices of \(Z\), or are on \(Z\).

**Distance \(d\) along \(Z\) between attachment points** \(z,z'\) (min arc): \(d\in\{0,1,2,3\}\).

| \(d\) | \(X\)–\(X\) path length through \(Z\) | Outcome |
|-------|----------------------------------------|---------|
| 0 | same attachment vertex: two pending paths to same \(z\) form a cycle with \(Z\) or a theta — reduces to A or gives two markers with a short path through pending trees | induction / path ≤3 |
| 1 | length 1 along \(Z\) + pending lengths | if both markers on \(Z\): edge or length 1; if pending: length ≥1. Edge in \(X\): classified. Path len 2–3: §§3–4 of pure-new |
| 2 | length 2 | same-part return §3 |
| 3 | length 3 | opposite-part return §4 |

**Pigeon:** two distinct attachment points on a 6-cycle have min-arc distance ≤3. Always. ∎

### B.4 Two markers on \(C_{10}\)

Min-arc \(d\le 5\).  
- \(d\le 3\): §§3–4  
- \(d=4\): length 4 same-part §3.2  
- \(d=5\): length 5 opposite §4.2  

Free edges of \(Z\) may shorten arcs (span 5 chord ⇒ C6, reduce). ∎

### B.5 Longer \(Z\)

Min-arc between two markers ≤ \(m\). Free edges / chords: span 3 ban, span 5 ⇒ C6 (shorter), span 7 ⇒ C8 ban.  
After maximal C6 flips, effective marker distance ≤5. §§3–4. ∎

---

## C. μ-bookkeeping (explicit)

### Definition C.1

At every stage of the pure-new analysis, maintain:
- \(X\): current known set (grows only when we **name** a vertex, e.g. interior of a constructed path we keep)
- \(E_{XN}\): set of edges with one end in \(X\) and one end in \(N=V(G)\setminus(V(P_*)\cup V(C)\cup X)\)
- \(\mu = |E_{XN}| + |N|\)  (nonnegative integer)

### Definition C.2 (Classifying an edge)

An edge \(e\in E_{XN}\) is **classified** when we have assigned it to a filled-component outcome that is either:
1. a ban (\(C_4/C_8\)/length-5), or  
2. an explicit length-9 \(s\)–\(t\) path, or  
3. a reduction that produces a finite list of **new** edges in a strictly smaller instance.

### Lemma C.3 (μ decreases on each inductive step)

**Step type 1 — extract Type P return of length \(L\), classify by §§3–4.**  
The two endpoint edges of the return path lie in \(E_{XN}\) and become classified.  
Interior vertices of the return were in \(N\); after classification they may be absorbed into “used” structure (removed from active \(N\) for residual stubs).  
Charge: \(|E_{XN}|\) drops by ≥2, or if interiors stay in \(N\) for side free edges, those side free edges form a new instance with fewer free stubs from original \(X\) (the two stubs at ends are spent).  
**Define active stub count \(\sigma = |E_{XN}|\).** Prefer induction on \(\sigma\) primarily, \(|N|\) secondarily.  

**Refined measure:**
\[
\mu = \bigl(|E_{XN}|,\; |N|\bigr)
\]
lexicographic order.

**Step type 1:** classify return path: the two \(X\)–\(N\) end edges are removed from \(E_{XN}\) (classified). \(\sigma\) drops by 2. ✓  

**Step type 2 — free edge of interior lands on \(X\):**  
Creates a shorter return; classify it (type 1); \(\sigma\) drops. ✓  

**Step type 3 — free edge of interior to new \(w\in N\):**  
Edge interior–\(w\) is **not** in \(E_{XN}\) (both in \(N\)).  
\(w\) has two other edges. Until they hit \(X\), we explore \(G[N]\).  
When first hit \(X\), we get a return path from some \(x\) through \(w\), and classify **at least one** new \(E_{XN}\) edge (the hit). But we also may add structure.  

**Problem:** exploring new vertices increases \(|N|\) counted? No: \(|N|\) is fixed for \(G\). \(\mu\) is computed on the **active residual** — the still-unclassified part.

**Operational definition of active residual:**
- Start with all of \(N\) and all of \(E_{XN}\) unclassified.  
- When a return path is classified, **delete** its \(X\)–\(N\) end edges from the active edge set, and **delete** from active \(N\) all vertices whose three edges are fully classified.  
- \(\mu = (|E_{\mathrm{active}}|, |N_{\mathrm{active}}|)\) lex.

**Step type 3 detailed:**  
Free edge from interior \(z\in N_{\mathrm{active}}\) to \(w\).  
If \(w\notin N_{\mathrm{active}}\), already processed.  
If \(w\) new in active: follow Lemma 1.3 from any \(X\)-stub that reaches this component; the filled component of \(w\) has ≥1 edge in \(E_{\mathrm{active}}\). Extract return (Prop 2.7). Classify return: removes ≥1 (actually ≥2 for Type P) from \(E_{\mathrm{active}}\).  

**Type T step:** extract one leaf-to-leaf path; classify; removes 2 active edges; remaining tree has fewer leaves (one leaf spent); recurse with smaller \(\sigma\). ✓  

**Type U step:** extract marker arc; classify; removes 2; remaining free edges of cycle go to components with fewer markers or smaller active set. ✓  

### Lemma C.4 (Base case)

If \(|E_{\mathrm{active}}|=0\), then no unclassified free edges from \(X\) to \(N\).  
By Lemma 1.1, \(N_{\mathrm{active}}\) must be empty (else a vertex in \(N\) has a path to \(X\) using some edge to \(X\)).  
Done. ∎

### Theorem C.5 (Induction works)

Every sequence of steps terminates: lex measure \(\mu\) is a well-order on \(\mathbb{N}\times\mathbb{N}\), each step decreases \(\mu\), base case empty.  
On termination, every free edge was classified as ban or path-9. ∎

---

## D. Seeds for gap closure

See `verify_gaps.py`: theta free-stub contradictions (matching non-existence), Type U \(k\ge 2\) under cutvertex, explicit path-9 from B.3.
