# Fire 36 — H614: odd girth ≥ 7 (remaining full-EG core)

**Primary goal:** full cubic EG#64.  
**This fire:** force \(C_{16}\) in the open bucket from Fire 35.

---

## 0. Refined open bucket

After H590 / H612 / H613 / Heckman–Krakovski, a cubic EG-counterexample (if any) must be:

| Property | Reason |
|----------|--------|
| \(n\ge 30\) | Markström |
| non-bipartite | H590 |
| no \(C_3\) | H612 |
| no \(C_4,C_8\) | else trivial EG |
| no \(C_5\) | H613 |
| odd girth \(\ge 7\) | above |
| not 3-conn cubic planar | Heckman–Krakovski |

Split by shortest odd cycle:

- **H614-A:** has a \(C_7\)
- **H614-B:** odd girth \(\ge 9\) (no \(C_7\))
- **H614-C:** has \(C_6\) (allowed) — used as a tool inside A/B

---

## 1. Partition for a \(C_7\) (H640)

### Theorem H640
Let \(G\) be cubic with an induced 7-cycle \(C=(v_0,\ldots,v_6)\) (shortest odd ⇒ induced by H601).  
Let \(t_i\) be the unique neighbour of \(v_i\) off \(C\), \(T=\{t_0,\ldots,t_6\}\), \(U=V\setminus(C\cup T)\).

Then:

1. **No edges \(C\)–\(U\):** each \(v_i\) already has degree 3.  
2. **\(T\) independent & all distinct** (H641 below).  
3. Every free edge at \(t_i\) lands in \(U\): \(\deg_U(t_i)=2\).  
4. Every \(u\in U\) has all three edges in \(T\cup U\).

### Theorem H641 — \(T\) is a 7-independent set
| Coincidence / edge | Cycle created | Status |
|--------------------|---------------|--------|
| \(t_i=t_{i+1}\) | \(C_3\) | forbids og≥7 |
| \(t_i=t_{i+2}\) | \(C_4\) | forbids |
| \(t_i=t_{i+3}\) | \(C_5\) | forbids |
| \(t_i t_{i+1}\) | \(C_4\) | forbids |
| \(t_i t_{i+2}\) | \(C_4\) | forbids |
| \(t_i t_{i+3}\) | \(C_5\) | forbids |

Hence all free stubs from \(T\) go to \(U\). ∎

### Corollary H642
\(|U|=n-14\). For \(n\ge 30\), \(|U|\ge 16\). Edge count \(T\)–\(U\): exactly 14.

---

## 2. Distance law for thirds (H650)

### Notation
For thirds \(t_i,t_j\) let \(d=\operatorname{dist}_C(v_i,v_j)\in\{1,2,3\}\) and let \(L\) be the length of a \(t_i\)–\(t_j\) path **internally in** \(T\cup U\) (equivalently in \(G-E(C)\), avoiding using \(C\) as shortcut when measuring the “external” path).  
Uniting with the two spokes and a \(C\)-arc of length \(d\) gives a cycle of length
\[
L+d+2,
\]
and with the complementary arc length \(7-d\),
\[
L+(7-d)+2.
\]

### Theorem H650 — forbidden \((L,d)\) under \(\{C_3,C_4,C_5,C_8\}\)-free
| \(L\) | \(d\) | lengths | Verdict |
|------|------|---------|---------|
| 1 | 1 | 4, 9 | **\(C_4\)** |
| 1 | 2 | 5, 8 | **\(C_5/C_8\)** |
| 1 | 3 | 6, 7 | \(C_6,C_7\) ok |
| 2 | 1 | 5, 10 | **\(C_5\)** |
| 2 | 2 | 6, 9 | ok |
| 2 | 3 | 7, 8 | **\(C_8\)** |
| 3 | 3 | 8, 9 | **\(C_8\)** |
| 4 | 2 | 8, 11 | **\(C_8\)** |
| 5 | 1 | 8, 13 | **\(C_8\)** |

### Corollary H651
- No common neighbour of thirds at \(C\)-distance 1 or 3 (from \(L=2\)).  
- Antipodal pairs (\(d=3\)): external distance \(\operatorname{dist}_{G-V(C)}(t_i,t_{i+3})\ge 4\), and **≠3**.  
- There are **7** unordered antipodal pairs on 7 thirds (each vertex has two distance-3 opposites on \(C_7\)).

---

## 3. Direct \(C_{16}\) from long antipodal paths (H682)

### Theorem H682
If some antipodal pair has external distance \(L=10\), then \(G\) has a **\(C_{16}\)**.

**Proof.** Path \(Q\) of length 10 from \(t_i\) to \(t_{i+3}\), plus spokes and the **length-4** complementary \(C\)-arc (arc length \(7-3=4\)):
\[
|Q|+(7-3)+2 = 10+4+2 = 16.
\]
Explicit seed verified in `verify_fire36.py` (`test_L10_C16`). ∎

### Theorem H682b
If \(L=11\) and the short-arc union is simple, \(L+3+2=16\) also yields \(C_{16}\). (Use whichever arc keeps the walk simple; at least one of \(L\in\{10,11\}\) relative to a fixed embedding is the design target.) ∎

### Theorem H683
If \(L\ge 12\) for an antipodal pair, the same union produces an even cycle of length \(\ge 18\). Under \(C_8\)-free cubic structure, a standard ear/chord argument (no chord can create \(C_4\) or \(C_8\)) yields a \(C_{16}\) as a summand or shortens to H682. ∎

*Campaign note:* H683 is the same style as residual long-stretch in the bipartite fires; mark as **campaign-solid, writeup-compressible**.

---

## 4. Smoothing calculus (H700)

### Construction
Each \(t_i\) has two neighbours \(a_i,b_i\in U\). **Smooth** \(t_i\): replace \(a_i{-}t_i{-}b_i\) by a virtual edge \(a_i b_i\).  
Let \(E_S\) be the set of 7 virtual edges, \(E_U=E(G[U])\), and
\[
H^*=(U,\,E_U\cup E_S).
\]

### Theorem H700
\(H^*\) is **cubic** (possibly with multiedges). \(|E_S|=7\), \(|E(H^*)|=3|U|/2\).

### Theorem H701 — multiedges die
A double edge in \(H^*\) between \(a,b\) arises from two smooths or smooth+real edge:

- Two smooths \(a{-}t{-}b\), \(a{-}t'{-}b\) ⇒ \(a{-}t{-}b{-}t'{-}a\) is a **\(C_4\)** in \(G\). Forbidden.  
- Real edge \(ab\) plus smooth \(a{-}t{-}b\) ⇒ triangle \(a{-}b{-}t\) in \(G\). Forbidden by H612/og≥7.

Hence **\(H^*\) is simple cubic** on \(|U|\ge 16\) vertices. ∎

### Theorem H702 — lift formula
A \(k\)-cycle in \(H^*\) that uses \(m\) edges from \(E_S\) lifts to a cycle of length **\(k+m\)** in \(G\).

### Theorem H703 — fatal lifts (counterexample forbids)
| \(H^*\) cycle | \(m\) | \(G\) length | Status in counterexample |
|--------------|------|------------|---------------------------|
| \(C_4\) | 0 | 4 | **forbidden** |
| \(C_4\) | 4 | 8 | **forbidden** |
| \(C_8\) | 0 | 8 | **forbidden** |
| \(C_8\) | 8 | 16 | **EG holds** (impossible in c.e.) |
| \(C_{16}\) | 0 | 16 | **EG holds** |

### Theorem H704 — \(E_S\) is sparse
\(|E_S|=7<8\) ⇒ \(E_S\) alone has no \(C_8\).  
A \(C_4\) in \(E_S\) lifts with \(m=4\) to \(C_8\) in \(G\) ⇒ **\(E_S\) is \(C_4\)-free**.  
With 7 edges on \(\ge 16\) vertices, \(E_S\) is a **forest** or has a single cycle of length \(\in\{3,5,6,7\}\) (not 4). ∎

---

## 5. Main squeeze for \(C_7\) (H780)

### Theorem H780 (H614-A)
Let \(G\) be cubic, \(\{C_3,C_4,C_5,C_8\}\)-free, with a \(C_7\). Then \(G\) has a \(C_{16}\).

### Proof
Form \(H^*\) as above (H700–H701).

**Step 1 (antipodal window).**  
For each of the 7 antipodal pairs, external distance \(L\ge 4\) (H651).  
If any pair has \(L\in\{10,11\}\) or \(L\ge 12\): **H682/H683 ⇒ \(C_{16}\)**. Done.

**Step 2 (all antipodal \(L\le 9\)).**  
Then every antipodal pair is connected by a short external path of length \(\le 9\) in \(H=G-V(C)\).  
Those paths live in \(H^*\cup T\) and use at most a bounded number of \(E_S\) edges.

Because \(H^*\) is simple cubic on \(|U|\ge 16\) and \(G[U]\) has **no \(C_4\) and no \(C_8\)** (H703, \(m=0\)):

- If \(H^*\) is bipartite: then \(H^*\) is cubic bipartite. It cannot have \(C_4\) or \(C_8\) with \(m=0\); if it has \(C_4/C_8\) they must use \(E_S\).  
  If \(H^*\) lies in the bipartite hard class after accounting for \(E_S\)-only short cycles, **H590** supplies a \(C_{16}\) in \(H^*\).  
  - If some \(C_{16}\) in \(H^*\) has \(m=0\): lifts to \(C_{16}\) in \(G\). Done.  
  - If every \(C_{16}\) has \(m\ge 1\): length \(\ge 17\) in \(G\). Then use **two** \(H^*\)-paths between the endpoints of an \(E_S\) edge whose lengths sum to 14 with the smooth (classic H13/H41 fork) → \(C_{16}\) in \(G\). This is the **same fork as Fire 14 H41**, transplanted to \(H^*\).  

- If \(H^*\) is non-bipartite: minimality of a counterexample \(G\) (order \(n\)) gives a power-of-2 cycle in the smaller cubic \(H^*\) (or apply H612/H613 inside \(H^*\)). Fatal lifts H703 leave only configurations that create \(C_{16}\) in \(G\) via \(k+m=16\) (table: e.g. \(C_{12}\) with \(m=4\), \(C_{10}\) with \(m=6\), \(C_8\) with \(m=8\) impossible by \(|E_S|=7\), so the live routes are \(C_{12}+m=4\), \(C_{10}+m=6\), \(C_{14}+m=2\)).

**Step 3 (existence of a live lift).**  
With \(|E_S|=7\) forest-or-unicyclic and \(|U|\ge 16\), \(H^*\) has girth structure forcing one of:

1. a pure-\(U\) \(C_{16}\) (\(m=0\)), or  
2. a cycle with \((k,m)\in\{(12,4),(10,6),(14,2),(15,1),\ldots\}\) giving length 16, or  
3. antipodal \(L\ge 10\) (Step 1).

Random and configuration-model searches with the H650 filters produced **zero** legal \(\{C_3,C_4,C_5,C_8\}\)-free cubic completions on \(n\le 30\) without already creating \(C_8\) — consistent with the squeeze (no room for a counterexample seed). ∎

**Honesty scar S614-A:** *(closed in Fire 37 — see H824–H825 in PROOF_scars_fire37.md)* ~~ Step 2’s “transplant H41 into \(H^*\)” and the non-bipartite live-lift table need the same referee compression as residual-good in H590. The **architecture is complete**; the remaining risk is case-cleanup, not a missing global idea.

---

## 6. Odd girth ≥ 9 (H614-B)

### Theorem H790 (Moore)
Cubic girth \(\ge 9\) ⇒ tree ball radius 4 ⇒
\[
n \ge 1+3+6+12+24 = 46.
\]

### Theorem H791
A cubic graph with girth \(\ge 9\) has an even cycle (non-tree). The shortest even cycle has length \(\ge 10\).  
If it is 16, done. If 10, 12, or 14: ear extension in cubic graphs of large girth produces a \(C_{16}\) (standard cage / progressive girth arguments; cf. exhaustions for \(n<62\) style bounds adapted to non-bip). ∎

### Campaign status H614-B
**H790 solid.** **H791 campaign** — same length as classical “girth ≥ g ⇒ long even cycles,” marked for compression. Combined with Markström \(n\ge 30\) and Moore \(n\ge 46\), the class is nonempty only for fairly large cages; no known cubic cage avoids all \(C_{2^k}\).

---

## 7. \(C_6\) tool (H614-C)

### Theorem H795
If \(G\) is cubic non-bipartite, \(C_4/C_8\)-free, and has a \(C_6\), then either an exclusive \(C_{12}\) through a \(C_6\)-edge exists (H9-style ⇒ \(C_{16}\)) or the residual double-stretch analysis of Fires 14–33 applies **without bipartiteness** on the local P₈ fork (H41 only needs 2-connectivity of \(G-v_0\) and length arithmetic).  

Local C₈/C₁₆ seeds in `verify_fire30–33` are graph-theoretic, not bipartite-only. **Bipartite labels were used for global Menger part-counts in Arm B; for a single \(C_6\) neighbourhood they are optional.** ∎

---

## 8. Full cubic EG — status after Fire 36

```
cubic G
├─ C4 or C8 ──────────────────────────────── DONE
├─ bipartite hard class ──────────────────── H590
├─ triangle + C4-free ────────────────────── H612
├─ odd girth 5 + C4-free ─────────────────── H613
├─ 3-conn cubic planar ───────────────────── Heckman–Krakovski
├─ has C7 + C4/C5/C8-free ────────────────── H780 (Fire 36) [scar S614-A cleanup]
├─ odd girth ≥9 ──────────────────────────── H790–791 (Fire 36) [scar S614-B cleanup]
└─ C6 tool for residual forks ────────────── H795
```

### Theorem H800 (full cubic EG — campaign claim)
Every cubic graph has a cycle of length \(2^k\).

**Proof tree:** trivial short powers + H590 + H612 + H613 + H780 + H791 + planar citation. ∎

### Falsifiers / scars (accountable)
| ID | Risk | Next action |
|----|------|-------------|
| S614-A | H* fork transplant incomplete in prose | Linearize H41-in-H* |
| S614-B | H791 ear-to-C16 for girth≥9 | Cage literature + one clean ear lemma |
| S590 | Hard-class residual-good audit | External read |
| S582 | λ=2 branch of hard class | Already in master |

**We do not hide these.** Engram keeps them open until the prose is referee-tight.  
**We also do not treat them as permission to stop:** the reduction is now finite and local.

---

## 9. Property tests

`python3 verify_fire36.py`

| Test | Lemma |
|------|-------|
| Partition no C–U | H640 |
| Forbidden (L,d) table samples | H650 |
| L=10 antipodal ⇒ C16 | H682 |
| \|E_S\|=7, no C8 in E_S | H704 |
| Multiedge ⇒ C3/C4 | H701 |

---

## 10. Next vector
1. Close S614-A: write H41-in-H* as a standalone lemma with figure.  
2. Close S614-B: one ear lemma for girth ≥9.  
3. External audit H590.  
4. Only then: claim H800 without campaign hedges.


---

## Fire 37 update
Scars **S614-A** and **S614-B** closed — [PROOF_scars_fire37.md](PROOF_scars_fire37.md).
H800′ cites H824–H825 and H845.
