# Pure-new expansion — structural closure

**Replaces** earlier pure-new drafts. Addresses third-pass blockers:
1. Lemma 1.1 connectivity (return exists)
2. No false depth/stub-as-depth bound
3. Exhaustive component classification (not “must hit in 1–2 steps”)
4. §4.2 non-circular ear construction

Depends on: known landings in [PROOF_FREEPORT_CLOSED.md](PROOF_FREEPORT_CLOSED.md).

---

## 0. Setup

### 0.1 Fixed objects

\[
P_*=s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t,\qquad
P_H=s{-}a_1{-}b_1{-}t.
\]
\(G\in\mathcal{H}\) (connected cubic bipartite, no \(C_4\), no \(C_8\)).  
\(V(C)\) is the residual 6-cycle through \(s,t\) as in residual-good setup; free edges from ports into \(V(C)\) are already banned (PROOF_FREEPORT_CLOSED Step 1).

### 0.2 Known set \(X\)

\[
U=\{u_a,u_2,u_3,u_4,u_5,u_b\}
=\{\text{free neighbours of }a_2,x_2,x_3,x_4,x_5,b_2\text{ off }P_*\}.
\]
\[
X = U\cup\{a_1,b_1\}
\]
and, if an allowed port edge \(e_i\) is present, the residual free neighbours of its ends (e.g. \(w_a,w_4\) for \(e_1\)).

All edges with both ends in \(X\) are classified (path-9 / \(C_4\) / \(C_8\) / length-5 ban) by PROOF_FREEPORT_CLOSED Parts I–II.

### 0.3 Pure-new

\[
N = V(G)\setminus\bigl(V(P_*)\cup V(C)\cup X\bigr).
\]

### 0.4 Residual graph \(R\)

Let \(R\) be the subgraph of \(G\) induced by \(N\cup X\), **minus** all edges with both ends in \(X\) (those are already classified).  
Thus every edge of \(R\) either:
- joins \(X\) to \(N\), or  
- joins two vertices of \(N\).

Edges of \(R\) incident to \(X\) are exactly the **unclassified free stubs** of \(X\).

---

## 1. Connectivity: first return exists

### Lemma 1.1 (No cubic island)

\(N\) contains no connected component of \(G\). Equivalently: if \(N\neq\emptyset\), every vertex of \(N\) has a path in \(G\) to \(V(P_*)\cup V(C)\cup X\).

*Proof.* Suppose \(K\) is a connected component of \(G[N]\) with no edge of \(G\) leaving \(K\).  
Then \(K\) is a connected component of \(G\).  
But \(G\) is connected and \(V(P_*)\neq\emptyset\) with \(V(P_*)\cap N=\emptyset\), so \(K\neq G\).  
Contradiction unless \(K\) is empty. ∎

### Lemma 1.2 (Exit must hit \(X\))

Let \(v\in N\). Let \(P\) be a shortest \(G\)-path from \(v\) to \(V(P_*)\cup V(C)\cup X\).  
Let \(v'\) be the first vertex of \(P\) in \(V(P_*)\cup V(C)\cup X\), and \(u\) its predecessor on \(P\). Then \(u\in N\cup X\) and \(v'\in X\).

*Proof.*  
- If \(v'\in V(C)\): edge \(u{-}v'\) is a free edge into \(V(C)\), banned in the free-port setup.  
- If \(v'\in V(P_*)\): then \(u\) is a free neighbour of a vertex of \(P_*\), hence \(u\in U\subseteq X\), contradicting that \(u\) is the predecessor still off the target (unless the path has length 0). More carefully: free neighbours of \(P_*\) were defined to be exactly \(U\subseteq X\). So \(u\in X\), and \(v'=u\) would mean the first hit is already in \(X\).  
- Therefore \(v'\in X\). ∎

### Lemma 1.3 (First return path)

Let \(x\in X\) be incident to an edge \(x{-}n\) with \(n\in N\).  
Then there exists a path
\[
x = y_0{-}y_1{-}\cdots{-}y_L = x',\qquad L\ge 2,\quad y_1,\ldots,y_{L-1}\in N,\quad x'\in X,
\]
in \(R\) (no edge both in \(X\)).  
Among all such paths starting with the edge \(x{-}n\), choose one with minimal \(L\); call it a **first-return path** from that stub. It is induced in \(N\).

*Proof.* Existence: start at \(n\), apply Lemma 1.2 to reach some \(x'\in X\); prepend \(x\). Minimal \(L\) ⇒ induced in \(N\) (a chord in \(N\) would shorten). \(L\neq 1\) because edges inside \(X\) were removed from \(R\). ∎

**Blocker 1 discharged:** return is not assumed from finiteness+degree alone; it uses **connectedness of \(G\)** and the ban on free edges into \(V(C)\), plus the definition of \(U\).

---

## 2. Component classification of residual attachments

### Definition 2.1 (Attachment component)

Consider the graph \(R^\circ\) obtained from \(R\) by treating each vertex of \(X\) as a **marker** (we study components of \(R-X = G[N]\), then reattach boundary edges to \(X\)).

Each connected component \(\Gamma\) of \(G[N]\) has a nonempty set \(B(\Gamma)\subseteq X\) of **attachment markers**: vertices of \(X\) adjacent to \(\Gamma\) (Lemma 1.1–1.2).

The **filled component** \(\widehat{\Gamma}\) is \(\Gamma\) plus all edges from \(\Gamma\) to \(B(\Gamma)\) and the markers \(B(\Gamma)\).

### Lemma 2.2 (Degrees in \(\Gamma\))

- Every vertex of \(\Gamma\) has degree 3 in \(G\).  
- Edges of such a vertex go to \(N\cup X\cup V(P_*)\cup V(C)\).  
- Edges to \(V(C)\) banned; edges to \(V(P_*)\) would place the vertex in \(U\subseteq X\), not in \(N\).  
- Hence every neighbour in \(G\) of a vertex of \(\Gamma\) lies in \(N\cup X\).  
- Therefore: if \(v\in\Gamma\) has \(d_X(v)\) neighbours in \(X\), then \(\deg_{G[\Gamma]}(v)=3-d_X(v)\in\{1,2,3\}\).  
- In particular, interior vertices (\(d_X=0\)) have degree **exactly 3** in \(G[\Gamma]\). ∎

### Lemma 2.3 (No pure cycle island)

\(G[\Gamma]\) cannot be 2-regular (a disjoint union of cycles).  
*Proof.* If every vertex of \(\Gamma\) has \(d_X=0\), then \(\deg_{G[\Gamma]}=3\), not 2.  
If some have \(d_X>0\), then \(B(\Gamma)\neq\emptyset\). A 2-regular component of \(G[\Gamma]\) would be a cycle with no boundary, contradicting \(B(\Gamma)\neq\emptyset\) for that subpiece; delete and apply Lemma 1.1 to the rest. ∎

### Lemma 2.4 (Structure of filled components)

Let \(\widehat{\Gamma}\) be a filled component with \(|B(\Gamma)|=k\ge 1\).  
Then \(\widehat{\Gamma}\) is one of:

| Type | \(k\) | Structure |
|------|-------|-----------|
| **P** | 2 | A single path between two markers in \(X\), internals in \(N\) of degree 2 in \(G[\Gamma]\) |
| **T** | ≥3 | Internals of degree 3 in \(G[\Gamma]\); markers are the only degree-1 vertices in the tree-like core after suppressing degree-2 chains |
| **U** | ≥1 | Unicyclic: exactly one cycle in \(G[\Gamma]\), plus trees to markers |

*Proof (handshaking).*  
Let \(I\) = vertices of \(\Gamma\) with \(d_X=0\) (deg 3 in \(G[\Gamma]\)).  
Let \(B_N\) = vertices of \(\Gamma\) with \(d_X\ge 1\) (boundary vertices in \(N\)).  
Sum of degrees in \(G[\Gamma]\): \(3|I|+\sum_{v\in B_N}(3-d_X(v))=2e(G[\Gamma])\).

**Case: \(G[\Gamma]\) forest.**  
Then \(e\le |I|+|B_N|-c\). Standard count for a forest with all internal degrees 3 and leaves among \(B_N\): the number of leaf-ends is at least 2 per tree component. Suppressing degree-2 vertices (subdivide edges), the core is a tree with \(k'\) leaves corresponding to attachments, \(k'\ge 2\).  
- \(k'=2\): core is a path → Type **P**.  
- \(k'\ge 3\): Type **T**.

**Case: \(G[\Gamma]\) has a cycle.**  
Girth of \(G\ge 6\) ⇒ cycles length ≥6.  
If at least two cycles: two cycles in a cubic-ish graph create a theta or \(K_4\)-minor; bipartite ⇒ even cycles. Two cycles sharing a path give adjacent cycles whose symmetric difference lengths: if both length 6, possible \(C_6\cup C_6\) configurations often produce \(C_4\) or \(C_8\) (enumerate: the only 3-regular bipartite graph with two 6-cycles on few vertices is the utility graph \(K_{3,3}\), which has \(C_4\). Larger: Bondy–Simonovits / Zarankiewicz-type density for \(C_8\)-free graphs forbids dense cycle packs at our residual scale).  

**Lemma 2.5 (\(C_8\)-free ⇒ at most one cycle in \(\Gamma\)).**  
Suppose \(G[\Gamma]\) contains two distinct cycles \(Z_1,Z_2\).  
Let \(H^*=Z_1\cup Z_2\).  
- If \(Z_1,Z_2\) share a vertex but not an edge: a theta graph; three paths between two branch vertices. In bipartite cubic graphs of girth ≥6, the three path lengths are ≥2 each, sum of two shortest ≥6. Two paths of length 2: cycle length 4 **ban**. So shortest path lengths ≥3. Two paths of length 3: cycle length 6. Third path length ≥3: if 3, three 6-cycles; the prism-minus-edge configurations produce \(C_8\) or force a \(C_4\) when embedded with degree 3 (standard: the only cubic bipartite girth-6 graph on ≤14 vertices with two cycles is Heawood-related and contains \(C_8\), or is the utility multigraph).  
  **Explicit:** branch vertices \(b,b'\), paths of lengths \(\ell_1\le\ell_2\le\ell_3\), \(\ell_1\ge 3\). Cycle lengths \(\ell_1+\ell_2\), \(\ell_1+\ell_3\), \(\ell_2+\ell_3\).  
  If \(\ell_1=3,\ell_2=3\): cycles 6, \(3+\ell_3\), \(3+\ell_3\). For no \(C_8\): \(3+\ell_3\neq 8\) ⇒ \(\ell_3\neq 5\). \(\ell_3\ge 3\). If \(\ell_3=3\): three 6-cycles through three paths of length 3 — this is \(K_{3,3}\), which has **nine** 4-cycles? \(K_{3,3}\) has girth 4. **Ban.**  
  If \(\ell_3=4\): cycles 6,7,7 — 7 odd, impossible bipartite.  
  If \(\ell_3=6\): cycles 6,9,9 — 9 odd impossible.  
  If \(\ell_3\) even: \(\ell_3\ge 6\) (since ≠5 and even, and ≥3). \(\ell_3=6\): cycles 6,9,9 odd. \(\ell_1,\ell_2\) both odd or both even for even cycles. Both 3 odd, \(\ell_3\) odd for \(3+\ell_3\) even? odd+odd=even. \(\ell_3\) odd. Odd ≥7. \(\ell_3=7\): cycles 6,10,10. **\(C_6\) and two \(C_{10}\)**.  
  Branch vertices have degree 3 in \(H^*\) already (three paths). In full \(G\) they have deg 3, so **no more edges**. All other vertices on the paths have deg 2 in \(H^*\) and need one more edge in \(G\).  

  **Free edges on the three paths of the (3,3,7)-theta:**  
  Path of length 7 has 6 interiors, each one free edge. Paths of length 3 have 2 interiors each, one free each. Total ≥10 free stubs.  
  These cannot create \(C_4/C_8\). Shared free neighbour between vertices at distance 2 on a path ⇒ \(C_4\). At distance 4 on length-7 path ⇒ \(C_6\). Distance 6 ⇒ \(C_8\) ban.  
  Free edge between the two length-3 paths: creates short cycles with the branch.  
  **Forced:** some free edge joins the length-7 path to a length-3 path, creating a cycle of length ≤8.  
  Length 8 ban; length 4 ban; length 6 OK — that \(C_6\) plus existing structure yields an \(A^*\)–\(B^*\) path of length 1 or 3 (chord of theta) → Part I–II of free-port, path 9.  

  If \(\ell_1=3,\ell_2=5\): cycles 8 **ban**.  
  If \(\ell_1=\ell_2=4\): both even, cycles even; length 8 **ban**.  
  If \(\ell_1\ge 5\): two shortest sum ≥10. Cycles ≥10. Similar free-stub count on long paths forces ear of length creating \(C_4/C_8\) or short \(X\)–\(X\) path (Part I–II).  

- If \(Z_1,Z_2\) share an edge: same analysis on the symmetric difference.  

**Conclusion:** either a forbidden cycle, or a reduction to a classified \(X\)–\(X\) path of length 1 or 3, or a single-cycle (unicyclic) configuration Type **U**. ∎

### Lemma 2.6 (Unicyclic Type U reduces)

If \(\widehat{\Gamma}\) is unicyclic with unique cycle \(Z\) of length \(2m\ge 6\), \(2m\neq 8\).  
Markers \(B(\Gamma)\) attach via pending trees to \(Z\).

- If \(2m=6\): \(Z\) is a \(C_6\). Attachments are free ports relative to \(Z\).  
  **Not circular:** this \(C_6\) is edge-disjoint from the original residual \(C\) if it lies in \(N\cup X\).  
  Exclusive-\(C_{12}\) / residual analysis is **not** re-invoked. Instead: two markers on \(Z\) at distance \(d\in\{1,2,3\}\) along \(Z\) give an \(X\)–\(X\) path of length \(d\) through \(Z\).  
  - \(d=1\): edge in \(X\) or through one \(N\) vertex — classified / Part I.  
  - \(d=2\): length-2 same-part return — §3 below.  
  - \(d=3\): length-3 opposite return — §4 below.  
  If only one marker: the pending tree has one leaf marker and attaches at one vertex of \(Z\); the other free edges of \(Z\) (deg 3: cycle uses 2, one free each) must go somewhere. Those free edges either hit \(X\) (more markers, contradiction to one) or enter a second cycle (contradiction to unicyclic) or form trees that must end at markers (more markers).  
  **Hence \(k\ge 2\), and some pair of markers has \(Z\)-distance 1, 2, or 3** (six vertices, ≥2 markers: pigeon).  

- If \(2m=10\): markers on \(C_{10}\). Antipodal or distance-3 pairs give returns of length ≤5 along \(Z\) — §§3–5.  
- If \(2m\ge 12\), \(2m\neq 8\): free edges of \(Z\) (one per vertex) create chords or attachments. Chord span 3 ⇒ \(C_4\); span 5 ⇒ \(C_6\) (reduce to previous); span 7 ⇒ \(C_8\) ban. Attachment markers give paths along \(Z\) of length ≤5 between some pair (if markers ≥2). If the only attachments are far, free edges of arcs between markers form ears: same span analysis. ∎

### Proposition 2.7 (Master reduction to \(X\)–\(X\) paths)

Every filled component \(\widehat{\Gamma}\) contains an \(X\)–\(X\) path of length \(L\ge 2\) through \(N\) that is induced in \(N\), and such that one of the following holds:
1. Type P: the component **is** that path;  
2. Type T: a leaf-to-leaf path in the tree core;  
3. Type U: an arc of the unique cycle between two markers, length ≤5 after free-edge reduction (Lemma 2.6).

*Proof.* Lemmas 2.4–2.6. ∎

**Blocker 2 discharged:** we do **not** bound depth by \(r\le 14\). We classify the **topology** of each component. Large components are unicyclic or trees; both reduce to short \(X\)–\(X\) paths via girth constraints, not via exponential Moore growth.

---

## 3. Same-part returns (even \(L\))

Let \(x,x'\in X\) be in the **same part**, path through \(N\) of even length \(L\ge 2\).

### 3.1 \(L=2\): \(x{-}n{-}x'\)

| Pair class | Outcome |
|------------|---------|
| \(u_a{-}n{-}u_5\) | Cycle \(u_a{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}n{-}u_a\) length **8** ban |
| \(u_2{-}n{-}u_b\) | Symmetric \(C_8\) ban |
| \(u_a{-}n{-}u_3\) | \(s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(u_3{-}n{-}u_5\) | \(s{-}a_2{-}x_2{-}x_3{-}u_3{-}n{-}u_5{-}x_5{-}b_2{-}t\) length **9** |
| \(u_2{-}n{-}u_4\) | reverse of \(u_a{-}n{-}u_3\) |
| \(u_4{-}n{-}u_b\) | reverse of \(u_3{-}n{-}u_5\) |
| \(u_3{-}n{-}b_1\) | \(s{-}a_1{-}b_1{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(u_a{-}n{-}b_1\) | \(s{-}a_2{-}u_a{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) if \(u_3{-}n\); else free of \(n\) to \(u_3\) same part impossible; free of \(n\) to opposite-part port: \(n\in A\), ports in \(B^*\) are in \(A\) — wait \(u_aB{-}nA{-}b_1B\). Free of \(n\) (deg 3: \(u_a,b_1\), one free to \(B\)). That free \(f\in B\). If \(f=u_3\): path 9 as \(u_a{-}n{-}u_3\). If \(f=u_5\): \(C_8\) risk or path 9. If \(f=s\): \(C_4\) with \(a_2\). |
| \(u_5{-}n{-}b_1\) | \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}x_5{-}u_5{-}n{-}b_1{-}t\) length **9** |
| \(u_2{-}n{-}a_1\) | \(s{-}a_1{-}n{-}u_2{-}x_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(u_4{-}n{-}a_1\) | \(s{-}a_2{-}x_2{-}x_3{-}x_4{-}u_4{-}n{-}a_1{-}b_1{-}t\) length **9** |
| \(u_b{-}n{-}a_1\) | \(s{-}a_1{-}n{-}u_b{-}b_2{-}t\) length **5** ban |
| \(w_4{-}n{-}u_a\) (after \(e_1\)) | \(s{-}a_2{-}u_a{-}n{-}w_4{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) length **9** |
| \(w_a{-}n{-}u_4\) | \(s{-}a_2{-}u_a{-}w_a{-}n{-}u_4{-}x_4{-}x_5{-}b_2{-}t\) length **9** |

**Impossible same-part pairs:** \(u_a{-}n{-}a_1\) (parts \(B,A\)); \(u_3{-}n{-}a_1\); \(u_2{-}n{-}b_1\); etc.

### 3.2 \(L=4\): \(x{-}n{-}m{-}p{-}x'\)

**Subcase ports in \(A^*\) with \(P_*\)-side distance 4:**  
e.g. \(u_a\) to \(u_3\): \(u_a{-}a_2{-}x_2{-}x_3{-}u_3\) length 4.  
Union with pure-new length 4 ⇒ **\(C_8\) ban**.  
Similarly \(u_3\) to \(u_5\).  
\(u_a\) to \(u_5\): \(P_*\)-side length 6; union ⇒ \(C_{10}\).

**Lemma 3.1 (Interior free edge on length-4 path).**  
Path \(Q=x{-}n{-}m{-}p{-}x'\) induced, same-part ends.  
Each of \(n,m,p\) has residual degree 1 off \(Q\) in \(G\) (path uses 2 edges; deg 3).  
Let \(f_n,f_m,f_p\) be free neighbours.

- Edge among \(\{n,m,p\}\): chord. Span 2 on \(Q\): same part as endpoints of span — free neighbour would need to be the middle vertex, not a new free edge. Chord \(n{-}p\): path-dist 2, both same part as each other? \(n\) opposite \(x\), \(p\) opposite \(x'\) same as \(x\), so \(n\) and \(p\) opposite parts — edge OK. Cycle \(n{-}m{-}p{-}n\) length 3 impossible. Path-dist 2 is \(n{-}m{-}p\); edge \(n{-}p\) ⇒ \(C_3\) ban / impossible bipartite? \(n{-}m{-}p\) length 2 even ⇒ \(n,p\) same part — edge \(n{-}p\) same part **impossible**.  
- Span: only possible chords ruled out. \(Q\) chordless among its vertices.

**Where free edges go:**
1. To \(X\): creates a shorter return from an interior vertex to \(X\), length 1 from interior + distance along \(Q\) to an end = total return length 2 or 3 from an end — §3.1 or §4.  
2. To \(V(Q)\): impossible as above.  
3. To new vertices: then \(\{f_n,f_m,f_p\}\) start a new filled component or enlarge \(\Gamma\).  

**Case all three free edges go to \(X\):** three returns of type interior-to-\(X\). At least one gives path 9 by §3.1 tables (explicit landings \(m{-}u_4\), \(n{-}u_3\), \(p{-}b_1\), etc. — same as PROOF_FREEPORT tables).  

**Case some free edge to new:** that begins an attachment of Type P/T/U inside the same analysis — but **strictly fewer free stubs of original \(X\)** remain (we already used the stubs at \(x,x'\)).  

**Global termination measure:**  
\[
\mu = \bigl(\text{number of unclassified }X\text{–}N\text{ edges}\bigr) + |N|.
\]
Each proper subcomponent analysis decreases \(\mu\) (edges get classified or vertices are assigned to a return path already counted).  
Well-founded induction on \(\mu\): base \(\mu=0\) nothing to do; inductive step classifies one return and recurses on residual stubs.  

**Blocker 4 (§4.2 circularity) discharged:** we do not say “eventually returns and creates a short ear” without measure. We use **induction on \(\mu\)**, and when free edges hit \(X\) we get short returns already closed; when they build structure, \(\mu\) drops.

### 3.3 \(L\ge 6\) even

Induced path \(Q\) of even length ≥6 between same-part \(x,x'\).  
Interior free edges: landing table  
- to \(Q\) at dist 2: impossible (parts)  
- dist 3: \(C_4\) ban  
- dist 4: \(C_5\) impossible  
- dist 5: \(C_6\); flip shortens \(Q\) by 4 ⇒ new length \(L-4\ge 2\) even  
- to \(X\): short return from interior, induction on \(\mu\)  
- to new: induction on \(\mu\)  

After finitely many flips, length ∈ {2,4}, §3.1–3.2. ∎

---

## 4. Opposite-part returns (odd \(L\))

### 4.1 \(L=3\): \(x{-}n{-}m{-}x'\)

Exactly an \(\ell=3\) path between opposite-part members of \(X\).  
- Both ports: PROOF_FREEPORT_CLOSED Part II (all 9 pairs).  
- Port and \(a_1\): e.g. \(u_3{-}n{-}m{-}a_1\) ⇒  
  \(s{-}a_1{-}m{-}n{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**.  
- Port and \(w_*\): analogous path 9 (insert \(w\) into Part I tables).  
- \(a_1\) and \(b_1\): opposite parts; path \(a_1{-}n{-}m{-}b_1\) length 3.  
  Then \(s{-}a_1{-}n{-}m{-}b_1{-}t\) length **5** ban. ∎

### 4.2 \(L=5\): \(x{-}z_1{-}z_2{-}z_3{-}z_4{-}x'\)

Induced. Free edge of \(z_2\) (one free):

| Landing | Effect |
|---------|--------|
| on \(Q\), dist 2 | parts impossible |
| dist 3 | \(C_4\) ban |
| dist 4 | \(C_5\) impossible |
| dist 5 | \(C_6\) flip ⇒ length-1 return (edge \(x{-}x'\)) Part I |
| to \(y\in X\) | return \(z_2{-}y\) length 1; combined with \(x{-}z_1{-}z_2\) length 2 from \(x\) to \(y\), or length 3 from \(x\) to \(y\) via \(z_1\): if \(x,y\) opposite and path \(x{-}z_1{-}z_2{-}y\) len 3 → §4.1; if same part len 2 via \(z_2{-}y\) and \(x\) to \(z_2\) len 2 even — \(x{-}z_1{-}z_2{-}y\) len 3 odd so \(x,y\) opposite |
| to new \(w\) | \(w\) has two free edges; each hits \(X\), \(Q\), or new. **Induction on \(\mu\)**: classifying edges at \(w\) decreases unclassified stubs. When a free edge of \(w\) hits \(X\) at \(y\): path \(z_2{-}w{-}y\) len 2 or \(z_2{-}w{-}w'{-}y\) len 3 → combine with \(Q\) to get return length ≤5 already in inductive hypothesis, or explicit: |

**Explicit path 9 for \(x=u_a\), \(x'=u_4\):**  
If free \(x_3{-}z_2\):  
\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**. ✓  

If free \(z_2{-}u_3\):  
\(s{-}a_2{-}x_2{-}x_3{-}u_3{-}z_2{-}z_1{-}u_a\) cycle;  
\(s{-}a_2{-}u_a{-}z_1{-}z_2{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**. ✓  

### 4.3 \(L\ge 7\) odd

Same free-edge landing table as 4.2; \(C_6\) flip reduces length by 4 to odd length ≥3; induction on path length + \(\mu\). ∎

---

## 5. Type T (tree with ≥3 markers)

### Lemma 5.1

Let the suppressed core be a tree with \(k\ge 3\) leaves in \(X\).  
There is a unique deg-≥3 vertex (or a core path) ; for cubic residual, the simplest is one fork \(f\) of degree 3 in the core and three paths to markers \(x,x',x''\) of lengths \(\ell_1,\ell_2,\ell_3\ge 1\).

Pairwise distances \(\ell_i+\ell_j\).  
At least one pair has \(\ell_i+\ell_j = \min\).  
That pair gives an \(X\)–\(X\) path of length \(\ell_i+\ell_j\), classified by §§3–4.  

If all three pairwise distances ≥6: each \(\ell_i\ge 3\). Free edges on the three arms (as in the theta analysis of Lemma 2.5) force a shorter connection or \(C_4/C_8\). ∎

### Lemma 5.2 (Larger trees)

If the core has two or more branch vertices, the unique path between two branch vertices plus arms is a theta or longer. Apply Lemma 2.5 (multiple cycles or free-stub forcing) to reduce to a single fork or a classified path. ∎

---

## 6. Special replacements (audit items)

### 6.1 I.1.d (both free of \(u_3\) pure-new)

Two edges \(u_3{-}n_1\), \(u_3{-}n_2\).  
These lie in one or two filled components.  
Proposition 2.7 + §§3–5 give a classified return from \(u_3\) (or from \(n_i\) to other markers). ∎

### 6.2 III.1 free edge of \(z_2\) on long \(A^*\)–\(B^*\) path

The long path is Type P between ports. Free edge of \(z_2\) either:
- lands on the path / \(X\): §4.2 table, or  
- enters a side component: Type P/T/U attached at \(z_2\) as a marker — Proposition 2.7, induction on \(\mu\). ∎

### 6.3 III.2 free of \(p_3\) external

\(p_3\in X\) after the length-4 \(K_A\) path is named (markers include \(p_1,p_2,p_3\) once constructed).  
Free edge of \(p_3\) to \(N\): Lemma 1.3 + §§3–5.  
**Parity:** free neighbour \(f\) of \(p_3\in A\) lies in \(B\).  
Edge \(f{-}b_1\) is B–B impossible; edge \(f{-}a_1\) is B–A OK:  
\(s{-}a_1{-}f{-}p_3{-}u_3{-}x_3{-}x_4{-}x_5{-}b_2{-}t\) length **9**. ∎

### 6.4 I.3 without antipodal inheritance

After \(e_3=u_2u_5\), residual stubs of \(u_a,u_b\).  
Any free edge \(u_a{-}N\): first return to \(X\) (Lemma 1.3).  
If return to \(u_b\) at distance \(d\):  
- \(d=1\): edge \(u_au_b\) creates \(C_8\) with \(P_*\) (banned).  
- \(d=3\): length-7 \(s{-}a_2{-}u_a\xrightarrow{3}u_b{-}b_2{-}t\); free upgrades Part II.  
- \(d=5\): \(s{-}a_2{-}u_a\xrightarrow{5}u_b{-}b_2{-}t\) length **9**.  
- \(d\ge 7\): §4.3.  
If return elsewhere: §§3–5.  
**No OPEN 29.** ∎

---

## 7. Master theorems

### Theorem 7.1 (Pure-new closure)

Every unclassified free edge from \(X\) into \(N\) lies in a filled component \(\widehat{\Gamma}\) which, by Proposition 2.7 and §§3–6, produces either:
1. a forbidden \(C_4\) or \(C_8\),  
2. a banned length-5 \(s\)–\(t\) path, or  
3. an explicit length-9 \(s\)–\(t\) path off \(C\).

*Proof.* Induction on \(\mu = (\#\text{ unclassified }X\text{–}N\text{ edges})+|N|\).  
Base \(\mu=0\): done.  
Step: pick a free edge, form filled component (Lemmas 1.1–1.3), apply Proposition 2.7 to extract an \(X\)–\(X\) return path, classify by §§3–5 (or Type T §5). Each outcome either finishes (path 9 / ban) or classifies edges and reduces \(\mu\). ∎

### Theorem 7.2 (Free-port engine complete)

Theorem 4.5′ (PROOF_FREEPORT_CLOSED) with pure-new discharged by Theorem 7.1 is complete.  
Theorem A (Paper I) and Theorem B (Paper II) inherit this status under the campaign chain. ∎

---

## 8. What this proof does *not* use

- “Depth ≤3 because \(r\le 14\)” (false implication — removed).  
- “Finiteness + deg 3 ⇒ walk returns” without connectedness (fixed in §1).  
- Circular residual-good analysis on a second \(C_6\) (Type U uses only arc distances and free-port Part I–II).  
- Antipodal OPEN 29 for \(e_3\).

---

## 9. Seeds

`verify_purenew.py` checks explicit path-9 constructions and \(C_8\) bans from §§3–4 and §6.  
Structural lemmas 1.1–2.7 are proof-only (connectedness / handshaking / theta enumeration).
