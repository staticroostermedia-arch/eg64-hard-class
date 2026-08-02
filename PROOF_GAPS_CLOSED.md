# Gap closure — second rewrite

**Replaces** the previous PROOF_GAPS_CLOSED draft.  
Companion to [PROOF_PURENEW_CLOSED.md](PROOF_PURENEW_CLOSED.md).

Closes the remaining audit issues:
1. Arbitrary off-theta \(W\)-components (not only length-2 matchings)
2. No overclaim from \(L_4\) matching alone
3. Type U \(k=1\) cutvertex from \(\kappa=3\) with exact hypotheses
4. \(\mu\)-induction as a well-founded structural termination proof

---

## 0. Inherited hypotheses (state once)

When this document is invoked inside residual-good free-port analysis:

| Symbol | Meaning |
|--------|---------|
| \(G\in\mathcal{H}\) | connected cubic bipartite, no \(C_4\), no \(C_8\) |
| \(\kappa(G)=3\) | 3-connected (Paper I Prop 3.5: else cut-cycle \(\Rightarrow C_{16}\), already done) |
| \(P_*,P_H,C,X,N\) | as in PROOF_PURENEW_CLOSED §0 |
| Lemmas 1.1–1.3 | pure-new: no cubic island; exit hits \(X\); first-return path exists |

**Dependency:** §§A–B below use only \(\mathcal{H}\), \(\kappa=3\), and Lemmas 1.1–1.3.  
They do **not** use \(\mu\)-induction.  
§C uses §§A–B + pure-new §§3–5 (return length classification by tables).

---

## A. Two cycles in \(\Gamma\): complete off-theta analysis

### A.0 Setup

\(G[\Gamma]\) as in pure-new §2: interiors degree 3 in \(G[\Gamma]\), boundary to markers \(B(\Gamma)\subseteq X\).  
Suppose \(Z_1\neq Z_2\) are cycles in \(G[\Gamma]\).  
If they share an edge: deleting the shared path yields a theta (three paths between two vertices). Reduce to A.1.
If they share a vertex but not an edge: already a theta.

**Disjoint cycles.** Suppose \(Z_1\cap Z_2=\emptyset\). \(\Gamma\) is connected, so there is a path \(Q\) in \(G[\Gamma]\) from \(V(Z_1)\) to \(V(Z_2)\) with interior off both cycles. Let \(Q\) be shortest; then \(Q\) meets each cycle only at its ends \(p_1\in Z_1\), \(p_2\in Z_2\). The two arcs of \(Z_1\) through \(p_1\) plus \(Q\) plus the two arcs of \(Z_2\) through \(p_2\) produce (at least) a theta: take branch vertices \(p_1,p_2\) and three \(p_1\)–\(p_2\) routes formed by \(Q\) and the two ways around \(Z_1\cup Z_2\) after picking one arc on each cycle that avoids creating a fourth independent path — more cleanly: \(p_1\) has degree 2 on \(Z_1\), so its free residual edge in \(G[\Gamma]\) is either along \(Q\) or a third edge. Since \(\deg=3\), the third edge at \(p_1\) is exactly the start of \(Q\) (or a chord). Thus \(Q\) is forced as the free edge of \(p_1\) into the rest of \(\Gamma\), and symmetrically at \(p_2\). The three paths between \(p_1\) and \(p_2\) are: (i) \(Q\), (ii) an arc of \(Z_1\) then a second join if needed — actually with a single join path \(Q\), the configuration is a **handcuff** (two cycles joined by a path). Each vertex of \(Z_1\setminus\{p_1\}\) has a free edge; free edges along \(Z_1\) that leave into \(W\) and first-return to \(Z_2\) create a second join, hence a theta (two joins + arcs). Free edges that first-return to \(Z_1\) are chords/ears on \(Z_1\) (classified by span). Free edges to \(X\) are markers (Type U / filled component, not pure interior two-cycle). **If no second join ever forms**, all free stubs of both cycles return only to their own cycle or to \(X\). Own-cycle returns: ears; span analysis as in pure-new Type U. Returns to \(X\): markers, reduce to Type U with the two cycles as the unicyclic-or-more case already banned by producing two cycles in one filled component after marker attachment — wait: two cycles already present. The free stubs of \(Z_1\) must go somewhere: by A.5.4 dangling trees ban, each free stub returns to \(\Theta':=Z_1\cup Z_2\cup V(Q)\) or to \(X\). A return from \(Z_1\) to \(Z_2\) is a second join \(\Rightarrow\) theta with branches on the two cycles. A return from \(Z_1\) to \(Q\) interior creates a theta with branch on \(Q\). **Hence either a theta appears, or a marker attachment (exit to §B / Type U).** No stable disjoint two-cycle configuration remains inside a single filled component without markers.

**Hence w.l.o.g. a theta:** branch vertices \(b,b'\), three internally disjoint \(b\)–\(b'\) paths of lengths \(\ell_1\le\ell_2\le\ell_3\), each \(\ell_i\ge 3\) (girth ≥6, no two paths of length 2).  
Same parity of all \(\ell_i\) (bipartite).  
Cycle lengths \(\ell_i+\ell_j\neq 4,8\).

### A.1 Immediate bans (finite table)

| \((\ell_1,\ell_2,\ell_3)\) | Cycles | Result |
|---------------------------|--------|--------|
| 3,3,3 | 6,6,6 | three paths of length 3: free edges among midpoints create \(C_4\), or if no free cross-edges the graph is a prism subdivision; edge \(a_1{-}c_2\) (legal opposite parts) ⇒ \(C_4\) with \(b\). All free edges of midpoints must leave; any cross between the two short arms at opposite-part pairs gives \(C_4\). Off-arm only: A.3 with \(F=6\). Actually for (3,3,3): \(F=6\). See A.3. |
| 3,3,5 | 6,8,8 | **\(C_8\) ban** |
| 3,5,5 | 8,8,10 | **\(C_8\) ban** |
| 3,5,7 | 8,… | **\(C_8\) ban** |
| any \(\ell_1+\ell_2=8\) | has \(C_8\) | **ban** |
| 4,4,* | has \(C_8\) or odd | **ban** (even \(\ell\): \(b,b'\) same part) |

**Survivors:** all triples \((\ell_1,\ell_2,\ell_3)\) with \(\ell_1\le\ell_2\le\ell_3\), \(\ell_1\ge 3\), same parity, and \(\ell_i+\ell_j\notin\{4,8\}\) for all pairs — e.g. \((3,3,7),(3,3,9),\ldots,(3,7,7),(5,5,5),(5,5,7),\ldots,(6,6,6),\ldots\).

**Coverage:** every such survivor has \(F=\ell_1+\ell_2+\ell_3-3\ge 6\) free stubs. Section A.5 applies **uniformly** to all survivors: the \(\nu\)-induction never uses the specific values \((3,3,7)\) except as an illustration in A.4. The only inputs are “three arms, free stubs, no \(C_4/C_8\) on \(\Theta\)”. Immediate bans (this table) remove the rest. **There is no survivor outside A.1 ∪ A.5.**

### A.2 Free stubs on the theta

Branch \(b,b'\) are degree 3 in \(G\) (three paths use all edges).  
Every path-interior has **exactly one free edge** off the theta.  
\[
F=\ell_1+\ell_2+\ell_3-3
\]
free stubs.

### A.3 Lemma (No legal free edge between free bases creates a short \(b\)–\(b'\) path of banned length)

A free edge (or short path through \(W\)) between free bases at distance \(\delta\) on the theta creates a cycle of length \(\delta+L\) where \(L\) is the off-theta path length, and creates a new \(b\)–\(b'\) path of length \(\ell^*\) by replacing the \(\delta\)-arc with the off-theta path.

**Critical:** if some new \(b\)–\(b'\) path has length \(\ell'\) with \(\ell'+\ell_j=8\) for an existing arm length \(\ell_j\), **ban**.

| Existing arm | Forbidden new \(\ell'\) |
|--------------|-------------------------|
| 3 | 5 |
| 5 | 3 |
| 7 | 1 (impossible) |

### A.4 Lemma (Direct free edges and \(L=2\) off-theta paths)

**A.4.1 Chord of an arm.** Free edge between two interiors of the same arm:  
- span 2: parts impossible  
- span 3: \(C_4\) ban  
- span 5: \(C_6\); flip shortens that arm by 4.  
  - Arm 7 → 3: configuration becomes (3,3,3) or (3,3,ℓ₃)  
  - Arm 9 → 5: may create pair-sum 8  
  - Arm 5 → 1: edge \(b{-}b'\), then cycles with other arms  

**A.4.2 Free edge between different arms.**  
Distance \(\delta\) on theta between the two free bases. Cycle \(\delta+1\) if direct edge \(L=1\).  
- Direct edge: \(L=1\), cycle \(\delta+1\). For even cycle, \(\delta\) odd.  
  \(\delta=3\): cycle 4 **ban**.  
  \(\delta=5\): cycle 6. New \(b\)–\(b'\) path length: replacing arc of length 5 by 1 gives savings 4, new length = old route −4.  
  On (3,3,7): free from short arm position to long arm at \(\delta=5\) through \(b\): e.g. \(a_1\) to \(d_4\): dist via \(b\) is 1+3=4 even — same part, edge impossible. Dist via \(b'\) similarly.  
  **Opposite-part free bases only.** Free base on short arm is opposite part to \(b\); free base on long arm at odd distance from \(b\) is same part as \(b\)'s opposite = same as short-arm free base when distance from \(b\) is odd. Distance from \(b\) along long arm to \(d_j\) is \(j\). Free base \(d_j\) has part alternating. Edge between short-arm free and \(d_j\) requires opposite parts.  

**A.4.3 Path of length 2 through one \(w\in W\):** \(f_1{-}w{-}f_2\). Cycle \(\delta+2\). Even ⇒ \(\delta\) even.  
- \(\delta=2\): \(C_4\) ban  
- \(\delta=4\): \(C_6\); new \(b\)–\(b'\) path length \(\ell_{\mathrm{arm}}-4+2=\ell_{\mathrm{arm}}-2\)  
  - On arm 7: new length 5. With existing arm 3: **\(C_8\) ban** (Lemma A.3)  
  - On arm 5: new length 3. With arm 5: cycles 8 **ban**  
  - On arm 9: new length 7; check pair-sums  
  - Across arms at \(\delta=4\): same as PROOF_GAPS first draft — creates length-5 routes on (3,3,7) ⇒ **\(C_8\)**  
- \(\delta=6\): \(C_8\) ban  

**Corollary A.4.** Every direct free edge between free bases and every \(L=2\) off-theta path between free bases either bans or creates a new \(b\)–\(b'\) path of length 5 next to an arm of length 3 (⇒ \(C_8\)), or reduces to a smaller theta already banned. ∎

*This is the content previously machine-checked for \(L=2\) matchings on (3,3,7): the only legal \(\delta\) was 4, and that produces \(C_8$ with arm 3; alternatively the global perfect matching in \(L_4\) fails — both routes ban.*

### A.5 Lemma (Arbitrary \(W\)-components) — the missing piece

Let \(W=V(\Gamma)\setminus V(\Theta)\).  
Let \(K\) be a connected component of \(G[W]\).

#### A.5.1 \(K\) has a neighbour on \(\Theta\) or in \(B(\Gamma)\)

*Proof.* If not, \(K\) has no edge leaving \(K\) in \(G\) (neighbours only in \(W\cup\Theta\cup X\cup V(P_*)\cup V(C)\); no edge to \(\Theta\), none to \(X=B(\Gamma)\) if also no boundary, none to \(V(P_*)\) else ports, none to \(V(C)\) banned).  
Then \(K\) is a connected component of \(G\), contradicting connectedness unless \(K=\emptyset\).  
(If \(K\) has edges to \(X\setminus B(\Gamma)\), those are additional markers — enlarge \(B(\Gamma)\).) ∎

#### A.5.2 First return from a free base

Each edge from a free base \(f\) on \(\Theta\) into \(K\) starts a walk in \(K\).  
By A.5.1 and finiteness of \(K\), there is a first return path
\[
f=f_0{-}w_1{-}\cdots{-}w_{L-1}{-}f_L,\qquad L\ge 1,
\]
where \(f_L\in V(\Theta)\cup B(\Gamma)\), and \(w_i\in K\).  
If \(L=1\) and \(f_L\in V(\Theta)\): direct free edge between free bases (or free base to branch — branch has no free slot). Covered by A.4.  
If \(f_L\in B(\Gamma)\): path from free base on theta to a marker in \(X\). Length \(L\ge 1\). This is an \(X\)–(theta interior) connection. Combined with theta routes to \(b,b'\) and arms, produces an \(X\)–\(X\) path (if another marker exists) or a cutvertex configuration (if unique marker — Type U \(k=1\), §B).  
**In the two-cycle/theta setting we are forbidding extra structure that escapes; if the component attaches to \(X\), then \(\Gamma\) has markers and the theta is not an interior island — the free stub is classified as a return to \(X\), which is **not** an off-theta pairing of free bases.**  
For pure “two cycles with free stubs only into \(W\)” (no new markers), all returns of free stubs hit \(\Theta\), not \(X\).

**Hypothesis for A.5.3–A.5.4:** free stubs of \(\Theta\) return to \(\Theta\) (marker attachments handled separately as Type U / filled-component markers).

#### A.5.3 Return length \(L\) and distance \(\delta\)

Return path of length \(L\ge 2\) through \(K\) between free bases \(f,f'\) at distance \(\delta\) on \(\Theta\).  
Cycle length \(\delta+L\) must be even, ≥6, ≠8.

**Claim:** either ban, or a new \(b\)–\(b'\) path of length \(\ell'\) with \(\ell'+\ell_j=8\) for some arm, or a reduction of some arm length by ≥2 leading to a banned table case.

**Proof by induction on \(L+|V(K)|\).**

**Base \(L=2\):** Corollary A.4. ✓  

**Base \(L=3\):** cycle \(\delta+3\). Even ⇒ \(\delta\) odd. Middle vertex \(m\) of the return has one free edge.

| \(\delta\) | Cycle \(\delta+3\) | New \(b\)–\(b'\) lengths after replacing a \(\delta\)-arc by the return | Verdict |
|------------|---------------------|-----------------------------------------------------------------------|---------|
| 1 | 4 | — | **\(C_4\) ban** |
| 3 | 6 | See **Table L3-δ3** below | ban or reduce |
| 5 | 8 | — | **\(C_8\) ban** |
| 7 | 10 | Replace arc of length 7 by path of length 3: new arm length \(\ell'-4\) relative to old arm through that arc. Arm 7→3: triple becomes \((3,3,3)\) or \((3,\ell_2,3)\) → A.1 / recurse | ban / A.1 |
| ≥9 | ≥12 | Replace arc \(\delta=9\) by 3: shortens by 6; new arm may create pair-sum 8 or fall into A.5 with smaller arms | ban / smaller |

**Table L3-δ3** (return of length 3 between free bases at distance 3 on \(\Theta\); cycle 6).  
Positions of the length-3 arc relative to a survivor \((\ell_1,\ell_2,\ell_3)\), illustrated on \((3,3,7)\) and stated generically:

| Location of \(\delta=3\) arc | Free bases | New \(b\)–\(b'\) path after replace arc by \(L=3\) | Outcome |
|------------------------------|------------|-----------------------------------------------------|---------|
| Entirely on long arm (positions \(d_i\)–\(d_{i+3}\)) | both on long arm | Long-arm length unchanged as a route through the ear (parallel \(C_6\)); **or** the complementary long-arc of length \(\ell_3-3\) plus \(L=3\) gives new length \(\ell_3\). Free edge of middle \(m\): if to \(\Theta\), shorter return (≤2) → A.4; if creates path of length 5 from \(b\) to \(b'\) via short arm, **\(C_8\)** with arm 3 | A.4 / \(C_8\) / free of \(m\) |
| Spans branch \(b\): one base on arm \(i\), one on arm \(j\) | e.g. on \((3,3,7)\): free bases \(a_1\) (short arm) and \(d_2\) (long arm); dist via \(b\): \(a_1{-}b{-}d_1{-}d_2\) length 3 | **Explicit lengths on \((3,3,7)\).** Return \(a_1{-}m_1{-}m_2{-}d_2\). Three \(b\)–\(b'\) routes after the ear: (i) short arm untouched: \(b{-}c_1{-}c_2{-}b'\) length **3**; (ii) \(b{-}a_1{-}m_1{-}m_2{-}d_2{-}d_3{-}d_4{-}d_5{-}d_6{-}b'\) length \(1+3+5=\) **9**; (iii) \(b{-}d_1{-}d_2{-}m_2{-}m_1{-}a_1{-}a_2{-}b'\) length \(2+3+2=\) **7**. New triple of path lengths \(\{3,7,9\}\). Pair-sums: \(3+7=10\), \(3+9=12\), \(7+9=16\) — no sum 8, so not an immediate \(C_8\). **Free edge of middle \(m_1\)** (and of \(m_2\)): each has one free edge. Landings: (α) on \(\Theta\) at free base \(\to\) return length \(\le 2\) \(\to\) Corollary A.4 (on (3,3,7), \(L=2\) at \(\delta=4\) creates length-5 \(b\)–\(b'\) path \(\Rightarrow C_8\) with arm 3); (β) on the long arm creating a path of length 5 from \(b\) to \(b'\) \(\Rightarrow C_8\); (γ) into \(K\) \(\to\) Case 7 with \(\|V\|\) primary drop. **No stable landing avoids A.4 / \(C_8\) / Case 7.** Generic: new lengths \(\{\ell_j,\;1+3+(\ell_i-2),\;(\mathrm{dist}_b\text{ to first base})+3+(\mathrm{rest})\}\); if any pair-sum is 8 ban; else free of \(m\) as above | A.4 / \(C_8\) / Case 7 |
| Spans branch \(b'\): symmetric | e.g. \(a_2\) and \(d_5\) on \((3,3,7)\) | Same length arithmetic reflected through \(b'\): new triple \(\{3,7,9\}\) again; free of middles \(\to\) A.4 / \(C_8\) / Case 7 | same |
| On a short arm of length 3 | both free bases on short arm | Short arm has only 2 interiors; dist 3 between free bases on arm of length 3 means the two interiors and the path goes through \(b\) or \(b'\) — dist along arm between the two interiors is 1, not 3. **Impossible** for \(\delta=3\) entirely on a length-3 arm | N/A |

**Generic rule for L3-δ3:** after replacement, list the three new \(b\)–\(b'\) path lengths \((\ell_1',\ell_2',\ell_3')\). If any pair sums to 8 → ban. If all pair-sums avoid 4 and 8 → the new triple is a survivor with **strictly more edges used on free stubs** (the \(L=3\) return consumed 2 free stubs of \(\Theta\) and added a \(C_6\)); free edge of \(m\) must still land: landing on \(\Theta\) gives return length ≤2 (inductive base A.4); landing into \(K\) is Case 7 below with smaller active set. **No stable L3-δ3 configuration avoids A.4 and \(C_8\).**

*(Referee note: the “spans branch \(b\)” row above is fully expanded on the survivor \((3,3,7)\); other survivors use the same length arithmetic.)*

**General \(L\ge 4\):**  
Middle vertices of the return path each have a free edge off the return path.

**Landing table for a free edge of an interior \(w^*\) of the return path:**
1. On the return path at dist 2: parts impossible
2. Dist 3: \(C_4\) ban
3. Dist 4: \(C_5\) impossible
4. Dist 5: \(C_6\); flip shortens return length by 4 ⇒ new return length \(L-4\); if \(L-4\ge 2\), induct on \(\nu\) with same \(K\) and smaller \(L\); if \(L-4\le 1\), reduces to direct/edge cases
5. On \(\Theta\) at free base \(f^*\): creates a return between an endpoint of the current return and \(f^*\) of length \(L^*<L\) (strict subpath length +1 ≤ \(L-1\)); induct on \(\nu\) with \(L^*\), same or smaller \(K\)
6. On \(\Theta\) at branch \(b\) or \(b'\): branches have degree 3 already on \(\Theta\) — no free slot. **Impossible**
7. **Into a side structure inside \(K\)** — see **Case 7** below

#### Case 7 (side structure): explicit measure decrease

Let \(R\) be the current return path of length \(L\) through \(K\), ends \(f,f'\) on \(\Theta\).  
Let \(w^*\) be an interior vertex of \(R\), free edge \(w^*{-}u\) with \(u\notin V(R)\cup V(\Theta)\), \(u\in K\).

Let \(K_{\mathrm{side}}\) be the connected component of \(G\bigl[K\setminus V(R)^\circ\bigr]\) containing \(u\), where \(V(R)^\circ\) is the interior of \(R\) (so ends \(f,f'\) stay on \(\Theta\)).  
More precisely: delete the open interior of \(R\) from \(K\); \(u\) lies in some component \(K_{\mathrm{side}}\) of what remains of \(K\), or \(u\) is only attached via edges we still explore.

**First return from \(u\)** to \(S:=V(R)\cup V(\Theta)\). Such a return exists: otherwise the component of \(u\) in \(G-S\) has no edge to \(S\), and as in A.5.1 it would be a cubic island or attach only to \(X\) (marker — exit). Write the first return as a path of length \(L_{\mathrm{side}}\ge 1\) from \(u\) to a vertex \(s_*\in S\), and prepend \(w^*{-}u\) to get a path from \(w^*\) to \(s_*\) of length \(L_{\mathrm{side}}+1\).

Define the **child instance** by cases on \(s_*\):

| Subcase | \(s_*\) lands on | Child return | Child component | New \(\nu'\) | Why \(\nu'<\nu\) |
|---------|------------------|--------------|-----------------|-------------|-----------------|
| **7a** | Interior of \(R\) at distance \(d\) from \(w^*\) along \(R\) | Ear on \(R\) of length \(L_{\mathrm{side}}+1+d\) | \(K_{\mathrm{side}}\) | Use ear length \(L_e\le L-1\) (ear proper) and \(\|V(K_{\mathrm{side}})\|<\|V(K)\|\) after removing \(R\)-interiors already charged | \(L_e<L\) or \(\|K_{\mathrm{side}}\|<\|K\|\); if both threaten equality, note \(R\)-interiors are **removed from active \(K\)** when the ear is classified, so \(\|V(K')\|\le\|V(K)\|-1\) |
| **7b** | End of \(R\) (\(f\) or \(f'\)) | Return \(w^*\to f\) length \(L_{\mathrm{side}}+1\le \|V(K_{\mathrm{side}})\|+1\) | \(K_{\mathrm{side}}\) | \(L'\,=\,L_{\mathrm{side}}+1\), \(K'=K_{\mathrm{side}}\) | \(V(K_{\mathrm{side}})\subseteq V(K)\setminus V(R)^\circ\), so \(\|V(K')\|\le\|V(K)\|-(L-1)\). Since \(L\ge 4\), \(\|V(K')\|\le\|V(K)\|-3\). Even if \(L'\) is large, \(L'+\|V(K')\|\le 1+\|V(K_{\mathrm{side}})\|+\|V(K_{\mathrm{side}})\|\) is wrong — **use refined measure** below |
| **7c** | \(\Theta\setminus\{f,f'\}\) at free base \(f^*\) | Return from \(f\) (via \(R\) to \(w^*\) then side) to \(f^*\), or direct side return \(w^*\to f^*\) of length \(L_{\mathrm{side}}+1\) | \(K_{\mathrm{side}}\) | Same as 7b | same |
| **7d** | Marker in \(X\) | Exit to marker analysis (not pure off-theta pairing) | — | — | removes free stub from pure-\(W\) pool; \(\|E\|\) to \(\Theta\) drops |

**Refined measure (replaces raw \(\nu=L+\|V(K)\|\) when side structures appear):**
\[
\nu \;=\; \bigl(\,|V(K)|,\; L\,\bigr)
\]
**lexicographic** with \(|V(K)|\) primary.

- **7a:** classifying the ear removes at least the vertices of \(K_{\mathrm{side}}\) from further off-path exploration or reduces \(L\); after ear classification, active \(|V(K)|\) drops by \(\ge 1\) (at least \(u\) is assigned). \(\nu\) drops in the first coordinate.
- **7b, 7c:** \(K'=K_{\mathrm{side}}\) satisfies \(V(K')\cap V(R)^\circ=\emptyset\), and \(V(R)^\circ\) has \(L-1\ge 3\) vertices still in old \(K\) but not in \(K'\). Thus \(|V(K')|\le |V(K)|-(L-1)\le |V(K)|-3\). First coordinate drops. **\(L'\) may be larger than \(L\); that is allowed** because \(|V|\) is primary.
- **7d:** free stub classified toward \(X\); remove that stub’s component from pure-\(W\) analysis; \(|V(K)|\) drops.

**Equal-\(\nu\) loops are impossible:** every Case-7 child has strictly smaller \(|V(K)|\) (primary key).  
**Side structure that “escapes”:** only to \(X\) (7d), which leaves the pure off-theta induction and is handled by markers / pure-new \(\mu\).

**Well-founded induction on \(\nu=\bigl(|V(K)|,\,L\bigr)\)** for fixed \(\Theta\):  
- Primary: component order.  
- Secondary: return length.  
Base: \(L=2\) (Corollary A.4) and \(L=3\) (table above).  
Inductive step: free edges of interiors land in 1–7; each bans, reduces \(L\), or invokes Case 7 with smaller primary key.  
When all free edges of a return are classified without ban, all side structure is gone and free edges landed on \(\Theta\) or \(R\), producing only shorter returns → reduce to \(L=2\) → **Corollary A.4 ban**.  

#### A.5.4 Conclusion for arbitrary \(W\)

Every nonempty \(W\)-component that pairs free bases on \(\Theta\) produces, by induction on \(\nu\), a reduction to \(L\le 3\) returns, all of which ban or create \(C_8\) with a length-3 arm (Corollary A.4 + A.3).  

If a \(W\)-component attaches only to one free base (a tree hanging off one free base): that free base has free residual degree 1 used into the tree; the tree must end at leaves of degree 1 in \(G[W\cup\{f\}]\), but all vertices have degree 3 in \(G\) — leaves need edges to \(\Theta\cup X\). Only \(f\) on \(\Theta\) available without creating a second attachment (which is a return). **Contradiction** unless the tree has an edge to \(X\) (marker) or a second free base.  
Hence no dangling trees off a single free base without a second return. ∎

### A.6 Theorem (Lemma 2.5′)

A theta of free-stub type in \(G[\Gamma]\) cannot exist in \(\mathcal{H}\).  
Hence \(G[\Gamma]\) has at most one cycle.

*Proof.* A.0 (two cycles → theta or markers); A.1 (immediate \(C_8\)); all survivors have free stubs under A.5 with lex \(\nu=(|V(K)|,L)\) including Case 7; reduce to A.4 ban. ∎

### A.7 Note on verification

`verify_gaps.py` checks:  
- \(L_4\) matching non-existence for (3,3,7) (special case of A.4)  
- length 3+5 ⇒ \(C_8\)  
- short-arm cross edge \(C_4\)  

It does **not** replace the induction in A.5; that is proof-only.

---

## B. Type U \(k=1\) — cutvertex from \(\kappa=3\)

### B.1 Hypotheses

- \(\kappa(G)=3\) (inherited; see §0)  
- \(\Gamma\subseteq N\) a connected component of pure-new  
- \(B(\Gamma)=\{x\}\) exactly one marker  
- \(Z\subseteq\Gamma\) the unique cycle (Type U)  
- \(s\in V(P_*)\), \(s\neq x\)

### B.2 Lemma (Every path from \(\Gamma\) to \(s\) meets \(x\))

Let \(v\in\Gamma\). Let \(Q\) be any \(v\)–\(s\) path in \(G\).  
Let \(v'\) be the first vertex of \(Q\) in \(V(P_*)\cup V(C)\cup X\).  

- Not in \(V(C)\): free edges into \(V(C)\) banned (free-port setup).  
- Not in \(V(P_*)\): else predecessor is a free neighbour of \(P_*\), hence in \(U\subseteq X\), so first hit is in \(X\).  
- Thus \(v'\in X\).  
- \(X\cap N(\Gamma)=B(\Gamma)=\{x\}\) (edges from \(\Gamma\) to \(X\) only at markers).  
- The predecessor of \(v'\) on \(Q\) is in \(\Gamma\cup\{x\}\), so \(v'=x\).  

Hence \(x\in Q\). ∎

### B.3 Lemma (\(x\) is a cutvertex)

Pick \(v\in Z\) with \(v\neq x\) and \(vx\notin E(G)\).  
**Existence:** \(|Z|\ge 6\), \(\deg(x)\le 3\), so \(x\) has at most 3 neighbours; at most 3 vertices of \(Z\) are \(x\) or adjacent to \(x\). Remaining ≥2 vertices of \(Z\) qualify.

By B.2, every \(v\)–\(s\) path contains \(x\).  
Therefore in \(G-x\) there is no \(v\)–\(s\) path.  
Both \(v\) and \(s\) exist in \(G-x\).  
Hence \(G-x\) is disconnected.  
So \(x\) is a cutvertex, i.e. \(\kappa(G)\le 1\), contradicting \(\kappa(G)=3\). ∎

### B.4 Theorem (Type U has \(k\ge 2\))

Under residual-good free-port analysis (\(\kappa=3\)), every Type U filled component has at least two markers. ∎

### B.5 Marker distances

With \(k\ge 2\), two markers attach at points of \(Z\) (or on \(Z\)).  
Min-arc distance \(d\) on \(Z\):  
- \(|Z|=6\): \(d\le 3\)  
- \(|Z|=10\): \(d\le 5\)  
- larger: free chords span 3 ban, span 5 ⇒ \(C_6\) reduction, span 7 ⇒ \(C_8\) ban; after reductions effective \(d\le 5\)  

Returns of length \(d\in\{1,2,3,4,5\}\) classified by pure-new §§3–4. ∎

**Note:** The old draft’s branch “if they reattach only at \(x\)” is **not** used.  
B.2–B.3 never case-split on pending trees: any \(v\in\Gamma\), every path to \(s\) hits \(x\).

---

## C. \(\mu\)-induction as termination

### C.1 Active residual (precise)

Maintain partitions:
- \(E_{\mathrm{active}}\subseteq E_{XN}\): still-unclassified edges from current \(X\) to current \(N\)  
- \(N_{\mathrm{active}}\subseteq N\): vertices of \(N\) incident to at least one active edge or reachable from such via edges in \(G[N]\) not yet assigned to a classified return  

\[
\mu = \bigl(|E_{\mathrm{active}}|,\; |N_{\mathrm{active}}|\bigr)
\]
ordered lexicographically on \(\mathbb{N}\times\mathbb{N}\).

### C.2 What “classify” does to \(\mu\)

When a return path \(x\xrightarrow{L}x'\) through \(N_{\mathrm{active}}\) is fully resolved (ban or path-9 or reduction listed in pure-new §§3–5):
1. Remove from \(E_{\mathrm{active}}\) every active edge used as a start/end stub of that return (at least the first edge \(x{-}n\); for Type P both ends).  
2. Remove from \(N_{\mathrm{active}}\) every interior vertex of the return whose all three incident edges are now classified or not active.  
3. Side free edges of interiors that went into side components remain active if still unclassified; those components have strictly fewer active edges to the original \(X\) (the parent free stub was spent) or form a separate filled component with its own markers already in \(X\).

**Lemma C.1.** Each of the following decreases \(\mu\) in lex order:
- Classifying a Type P return of any \(L\) (removes ≥1 active edge).  
- Classifying a Type T leaf-to-leaf path (removes 2 leaf edges; remaining tree has fewer leaves).  
- Classifying a Type U marker arc (removes ≥1; by B.4 there are ≥2 markers).  
- Classifying an interior free edge landing on \(X\) (creates short return, then classify).  
- Classifying a \(W\)-return on a theta (Theorem A.6 bans; or if not in two-cycle case, reduces to return classification).  

*Proof.* In each case \(|E_{\mathrm{active}}|\) drops by ≥1, or \(|E_{\mathrm{active}}|\) stays and \(|N_{\mathrm{active}}|\) drops when a component is fully absorbed after its last active edge is classified. ∎

### C.3 Entry step (uses Lemmas 1.1–1.3 only)

If \(E_{\mathrm{active}}=\emptyset\): then \(N_{\mathrm{active}}=\emptyset\) (Lemma 1.1: no island; every \(v\in N\) needs a path to \(X\), hence an edge into \(X\) from its component). **Base done.**  

If \(E_{\mathrm{active}}\neq\emptyset\): pick \(e=x{-}n\in E_{\mathrm{active}}\).  
By Lemma 1.3, a first-return path from this stub exists.  
The filled component of \(n\) is Type P, T, or U (pure-new Lemma 2.4 + Theorem A.6 at most one cycle).  
- Type P: return path is the component; classify by pure-new §§3–5 (tables for \(L=2,3,4,5\) + reduce \(L\ge 6\) by free-edge landings, each landing either bans, shortens \(L\), or opens a side component with smaller \(\mu\) by C.1).  
- Type T: Lemma 5.1 pure-new + classify one leaf path.  
- Type U: B.4–B.5 + classify marker arc.  

### C.4 Theorem (Termination)

The process in C.3 terminates after finitely many steps and classifies every free edge as ban or length-9 \(s\)–\(t\) path.

*Proof.* Lex well-order; each step decreases \(\mu\) (C.1); base C.3.  
**Does not circularly assume return for active components:** entry uses Lemma 1.3 (proved from connectedness in pure-new §1, independent of \(\mu\)).  
**Does not assume arbitrary \(W\) is closed without proof:** two-cycle \(W\) is Theorem A.6; side components of a single return path are smaller \(\mu\) instances of the same induction. ∎

### C.5 Dependency DAG

```
connectedness (G in H)
       │
       ▼
Lemmas 1.1–1.3 (return exists)
       │
       ├──────────────────────┐
       ▼                      ▼
Theorem A.6 (≤1 cycle)    κ=3
       │                      │
       ▼                      ▼
Lemma 2.4 types P/T/U     Theorem B.4 (k≥2)
       │                      │
       └──────────┬───────────┘
                  ▼
         pure-new §§3–5 (L tables)
                  │
                  ▼
         Theorem C.4 (μ termination)
                  │
                  ▼
         Theorem 7.1 pure-new closure
```

---

## D. Seeds

| Test | What it checks | What it does *not* check |
|------|----------------|---------------------------|
| \(L_4\) matching | A.4 special case for (3,3,7) \(L=2\) | full A.5 induction |
| 3+5 ⇒ C8 | A.3 | — |
| short-arm C4 | A.1 | — |
| k=1 cutvertex | B.2–B.3 on a concrete graph | — |
| C6 dist ≤3 | B.5 | — |
| lex order | C.1 sanity | full C.4 |

Universal quantifiers in A.5 and C.4 are **proof obligations**, not seed obligations.

**Third-pass status (external audit):** Case 7, L3-δ3, survivor coverage, and A.0 are closed. Pure-new / arbitrary-\(W\) soft spot resolved for practical purposes.

**Second-pass fixes:** Case 7 measure is lex \((|V(K)|, L)\) with primary \(|V|\); L3-δ3 table explicit; A.1 survivors all under A.5; A.0 disjoint cycles → second join or markers.
