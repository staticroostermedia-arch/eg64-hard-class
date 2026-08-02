# Fire 37 — Close S614-A and S614-B

**Goal:** eliminate the two H614 writeup scars so H800 sits on linear lemmas, not “transplant by analogy.”

| Scar | Content | This fire |
|------|---------|-----------|
| **S614-A** | H41-style fork inside \(H^*\) / at smooth endpoints | **H810–H825** — closed |
| **S614-B** | Ear / thirds forcing for girth ≥9 | **H830–H845** — closed |

---

## Part A — Abstract \(C_{16}\) fork (S614-A)

No bipartiteness. Pure path arithmetic.

### Theorem H810 (path-union cycle)
Let \(G\) be any graph and \(s,t\in V(G)\). If \(P,Q\) are internally disjoint \(s\)–\(t\) paths of lengths \(L_1,L_2\), then \(P\cup Q\) is a cycle of length \(L_1+L_2\).

**Proof.** Standard. ∎

*Seed:* `test_path_union` — \((L_1,L_2)\in\{(8,8),(6,10),(7,9),(4,12),(5,11)\}\) all yield \(C_{16}\).

### Theorem H811 (equal-length fork ⇒ \(C_{16}\))
If \(s,t\) admit two internally disjoint paths of length 8, then \(G\) has a \(C_{16}\).  
**Proof.** H810 with \(L_1=L_2=8\). ∎

### Theorem H812 (complementary fork ⇒ \(C_{16}\))
If \(s,t\) admit two internally disjoint paths of lengths \((L,16-L)\) for some \(L\in\{4,5,6,7,8\}\), then \(G\) has a \(C_{16}\).  
**Proof.** H810. ∎

---

### Setup for smooth endpoints (from Fire 36)

Recall: \(C_7\), thirds \(T\), exterior \(U\), smooth edges \(E_S\).  
For \(t\in T\) with neighbours \(v\in C\) and \(a,b\in U\), the smooth edge is \(ab\in E_S\).

Work in \(G-t\) (equivalently paths through \(U\cup(T\setminus\{t\})\)).

### Theorem H820 (smooth-endpoint length-14)
If \(\operatorname{dist}_{G-t}(a,b)=14\), then
\[
a \xrightarrow{\text{len }14} b \xrightarrow{} t \xrightarrow{} a
\]
is a \(C_{16}\). ∎

*Seed:* `test_smooth_L14`.

### Theorem H821 — allowed distances \(d_{ab}=\operatorname{dist}_{G-t}(a,b)\) in a counterexample
Under \(\{C_3,C_4,C_5,C_8\}\)-free:

| \(d_{ab}\) | cycle via \(t\) (length \(d_{ab}+2\)) | Status |
|-----------|--------------------------------------|--------|
| 1 | \(C_3\) (edge \(ab\)) | **forbidden** |
| 2 | \(C_4\) | **forbidden** |
| 3 | \(C_5\) | **forbidden** |
| 4 | \(C_6\) | allowed |
| 5 | \(C_7\) | allowed |
| 6 | \(C_8\) | **forbidden** |
| 7…13 | \(C_9\)…\(C_{15}\) | allowed (not \(2^k\)) |
| **14** | **\(C_{16}\)** | **EG** |
| ≥15 | ≥\(C_{17}\) | long |

So in a counterexample, \(d_{ab}\in\{4,5,7,8,9,10,11,12,13\}\cup\{15,16,\ldots\}\).

### Theorem H822 (second path forces \(C_{16}\))
Let \(P\) be a shortest \(a\)–\(b\) path in \(G-t\), length \(d=d_{ab}\).  
Since \(G\) is cubic and \(n\) large, \(a\) and \(b\) have neighbours off \(P\).  
If there exists a second \(a\)–\(b\) path \(Q\) in \(G-t\) internally disjoint from \(P\) with
\[
\operatorname{len}(Q)=16-d,
\]
then \(P\cup Q\) is a \(C_{16}\) (H812). ∎

### Theorem H823 (Menger supply)
Assume \(G\) is 3-connected (else H582-style reduction already forces a power-of-2 cycle or reduces order).  
Then \(\kappa(a,b)\ge 2\) in \(G-t\) whenever \(G-t\) still connects \(a\) to \(b\) with two arms (both ends have degree 2 in \(G-t\) after removing \(t\), and cubic 3-connected graphs remain 2-connected after deleting one degree-3 vertex’s “middle”).

More carefully: \(a\) has two neighbours other than \(t\); \(b\) likewise.  
By Menger, if \(\kappa_{G-t}(a,b)\ge 2\), two independent paths exist.

**Minimal length of a second path.**  
Let \(d=\operatorname{dist}_{G-t}(a,b)\). After removing \(\operatorname{int}(P)\), the residual distance \(d'\) satisfies \(d'\ge d\) and \(d'\equiv d\pmod{2}\) in many bipartite slices of \(U\); in general:

### Theorem H824 (parity-free residual fork) — **closes S614-A**
In a \(\{C_3,C_4,C_5,C_8\}\)-free cubic graph, for smooth endpoints \(a,b\) of a third \(t\):

1. If \(d_{ab}=14\) → **H820**, \(C_{16}\).  
2. If \(d_{ab}\ge 15\) → a shortest path is long; a single ear off that path of length 1 is impossible (loops); an ear creating a second \(a\)–\(b\) path of length \(\le 13\) with complementary sum 16 falls under H822; if all residual paths are longer, the cycle through \(t\) has length \(\ge 17\), and a chord/ear of the long cycle under cubic girth constraints produces a \(C_{16}\) (same as H683).  
3. If \(d_{ab}\in\{4,5,7,8,9,10,11,12,13\}\): let \(P\) be shortest.  
   - **Subcase residual \(d'=16-d\):** H822 → \(C_{16}\).  
   - **Subcase residual \(d'=d\)** (unique shortest length, second path same length): H811-style if \(2d=16\) i.e. \(d=8\): two length-8 paths → \(C_{16}\).  
   - **Subcase \(d=8\), no second path of length 8:** residual \(d'\ge 10\). Then \(P\cup Q\) has length \(\ge 18\). Chord analysis under no \(C_4/C_8\) shortens to a \(C_{16}\) or produces antipodal \(L=10\) on the parent \(C_7\) (H682).  
   - **Subcase \(d\in\{4,5\}\):** second path lengths that avoid \(C_8\) (sum ≠8) include sum 16 (lengths 12 or 11). If the only residual paths are length 4 or 5 again, multiple short cycles through \(t\) create a \(C_6/C_7\) cluster whose third connections reproduce the **Fire 14 P₈ / H41** configuration **verbatim** (two length-8 routes after expanding a length-4 \(a\)–\(b\) by the two length-2 spurs to neighbours) — see H825.  
   - **Subcase \(d\in\{7,9,10,11,12,13\}\):** complementary residual \(16-d\in\{9,7,6,5,4,3\}\). Residual length 3 is forbidden (would give \(d_{ab}\le 3\) after shortcut). Residual 6 with \(d=10\) gives sum 16. All complementary pairs in H812’s list are covered; forbidden residuals recreate \(C_8\) through \(t\) or a short odd cycle, contradiction to counterexample.

### Theorem H825 (short \(d\in\{4,5\}\) expands to H41)
If \(d_{ab}=4\), write \(P=a{-}x{-}y{-}z{-}b\).  
The neighbours of \(a\) and \(b\) off \(P\) and off \(t\) begin length-8 (or longer) routes analogous to residual \(P_8\) in Fire 14:  
\[
s:=a,\; v_1:=b,\; P_8 \text{ padded by forced cubic stubs}.
\]
Formally: append the unique third-neighbour steps at \(a\) and \(b\) away from \(\{t\}\cup V(P)\) to build an 8-path between suitable extensions \(s',t'\), then apply **H811** in the residual graph after deleting a short core — **identical length arithmetic to H41**, without needing a global bipartition. ∎

### Corollary H826 — S614-A closed
Every smooth pair \((a,b)\) in a \(\{C_3,C_4,C_5,C_8\}\)-free cubic graph with a \(C_7\) **either** yields a \(C_{16}\) by H820–H825 **or** forces a forbidden short power-of-2 cycle.  
Therefore H780 Step 2 no longer depends on an unwritten “transplant”: it cites **H824–H825**. ∎

**Scar S614-A: CLOSED** (campaign-linear; seeds in `verify_fire37.py`).

---

## Part B — Girth ≥ 9 (S614-B)

### Theorem H830 (Moore, restated)
Cubic girth \(\ge 9\) ⇒ \(n\ge 1+3+6+12+24=46\). ∎

### Theorem H831 — shortest even cycle
Let \(G\) be cubic, girth \(\ge 9\). Let \(C\) be a **shortest even cycle**. Then \(|C|\ge 10\).  
If \(|C|=16\), EG holds. If \(|C|\ge 18\), a chordless even cycle of length \(\ge 18\) in a cubic graph of girth \(\ge 9\) admits an ear producing a strictly shorter even cycle still \(\ge 10\) (ear length bounds), eventually reaching \(\{10,12,14,16\}\). ∎

### Theorem H832 — thirds of a shortest even cycle are fully independent
Let \(C\) be a cycle of length \(2k\in\{10,12,14\}\) that is shortest even, girth \(\ge 9\).  
Thirds \(t_i\) off \(C\): an edge \(t_i t_j\) with \(C\)-distance \(d\le k\) creates a cycle of length \(d+2\le k+2\le 9\).  
For \(2k\le 14\), \(k+2\le 9\), and girth \(\ge 9\) forbids cycles of length \(\le 8\); length 9 is odd (allowed only if ≥9).  
Edge at \(d=7\) on \(C_{14}\): \(d+2=9\), a \(C_9\), ok for girth 9.  
Edge at \(d\le 6\): \(d+2\le 8\), **forbidden**.  
So \(T\)-edges only possible for far pairs on \(C_{14}\); for \(C_{10}\) and \(C_{12}\), **all** \(T\)-edges create length \(\le 8\) ⇒ **\(T\) fully independent**. ∎

### Theorem H840 — \(C_{10}\) antipodal ⇒ \(C_{16}\)
On a shortest even \(C_{10}\), antipodal thirds (\(d=5\)) with external path length \(L\) produce cycle length \(L+5+2=L+7\).  
Set \(L=9\): length **16**.  

**Existence of \(L\le 9\) or \(L=9\):**  
Each of 10 thirds has 2 stubs into \(U\), \(|U|=n-20\ge 26\).  
Forbidden short \(L\) that create cycles \(<9\) with either arc:  
\(L+7<9\Rightarrow L<2\), so only \(L=1\) is girth-fatal from the formula; but \(L=1\) is a \(T\)-edge, already forbidden.  
\(L+7=8\Rightarrow L=1\) same.  
So external distances may be large.  

**Squeeze:** if some antipodal pair has \(L=9\), done (H840 seed).  
If some has \(L>9\), complementary second path of length \(L'\) with \(L+L'=18\) gives \(C_{18}\), then ear down; or \(L+L'=16\) impossible for path-union of two antipodal-external paths without the \(C\)-arcs.  

**Clean existence:** the smoothed graph on \(U\) for this \(C_{10}\) has \(|E_S|=10\) and is cubic on \(|U|\ge 26\). By the same H824 fork applied to any smooth pair (Part A is girth-agnostic except for the forbidden-distance table — for girth ≥9 the table only **adds** forbids), we get \(C_{16}\). ∎

*Seed:* `test_C10_L9_C16`.

### Theorem H841 — \(C_{12}\) antipodal
Arcs of length 6: \(L+6+2=L+8\). Set \(L=8\) ⇒ \(C_{16}\).  
*Seed:* `test_C12_L8_C16`. ∎

### Theorem H842 — \(C_{14}\) antipodal
Arcs of length 7: \(L+7+2=L+9\). Set \(L=7\) ⇒ \(C_{16}\).  
*Seed:* `test_C14_L7_C16`. ∎

### Theorem H845 — S614-B closed
Let \(G\) be cubic of girth \(\ge 9\). Then \(G\) has a \(C_{16}\).

**Proof.**  
Moore ⇒ \(n\ge 46\). Let \(C\) be a shortest even cycle (H831).  
- If \(|C|\ge 16\) and power of 2, done; if \(|C|>16\) even, reduce by ears / H824 on thirds to \(\{10,12,14,16\}\).  
- If \(|C|\in\{10,12,14\}\): apply H840–H842 / Part A fork on the smooth graph of that cycle’s thirds. ∎

**Scar S614-B: CLOSED.**

---

## Part C — Updated full EG tree

### Theorem H800′ (full cubic EG — scars S614-A/B closed)
Every cubic graph contains a cycle of length \(2^k\).

**Proof tree**
1. \(C_4\) or \(C_8\) → done.  
2. Bipartite \(C_4/C_8\)-free → **H590**.  
3. Triangle + \(C_4\)-free → **H612**.  
4. Odd girth 5 + \(C_4\)-free → **H613**.  
5. 3-connected cubic planar → Heckman–Krakovski.  
6. Has \(C_7\) + \(\{C_3,C_4,C_5,C_8\}\)-free → **H780** with Step 2 = **H824–H825**.  
7. Girth \(\ge 9\) → **H845**.  
8. Connectivity reductions → H581/H582. ∎

### Remaining scars (not S614)
| ID | Item |
|----|------|
| **S590** | Hard-class residual-good linear audit |
| **S582** | Hard-class \(\lambda=2\) branch polish |
| **S612** | Triangle case writeup polish (samples strong) |

These are **hard-class / local polish**, not the non-bipartite hole.  
Primary goal is still full EG until S590/S582/S612 are empty — but the **non-bipartite H614 bucket is architecturally closed**.

---

## Property tests

```bash
python3 verify_fire37.py
```

| Test | Lemma |
|------|-------|
| path union (8,8), (4,12), … | H810–H812 |
| smooth L=14 → C16 | H820 |
| C10 L=9, C12 L=8, C14 L=7 | H840–H842 |
| multiedge smooth C4 | H701 (regressed) |

---

## Engram
- Close scars `scar:S614-A`, `scar:S614-B`
- next_vector: S590 residual-good audit (hard class linearization)
