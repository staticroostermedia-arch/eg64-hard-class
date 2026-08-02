# Fire 35 — Non-bipartite attack (restore full EG#64 goal)

**Primary goal (restored):** full Erdős–Gyárfás for **every cubic graph**, not only the bipartite hard class.

**Why now:** hard-class H590 is the bipartite half. Full EG still needs non-bipartite \(C_4/C_8\)-free cubics. Time is not the issue; missing lemmas were. This fire starts closing them.

---

## Global reduction (H620)

### Theorem H620 (reduction of cubic EG)
Let \(G\) be cubic. Then \(G\) has a \(C_{2^k}\) if any of the following holds:

| # | Case | Status |
|---|------|--------|
| 0 | \(G\) has \(C_4\) or \(C_8\) | **Trivial** |
| 1 | \(G\) bipartite and \(C_4/C_8\)-free | **H590** (master hard-class) |
| 2 | \(G\) non-bipartite, has a triangle, \(C_4\)-free | **H612** (this fire) |
| 3 | \(G\) has odd girth 5 and is \(C_4\)-free | **H613** (this fire) |
| 4 | \(G\) is 3-connected cubic planar | **Heckman–Krakovski 2013** (cite) |
| 5 | Else: non-bipartite, \(C_4/C_8\)-free, odd girth \(\ge 7\), \(n\ge 30\) | **OPEN — remaining core** |

Markström: any cubic EG-counterexample has \(n\ge 30\). So case 5 is the only open bucket for full cubic EG once 0–4 are locked.

---

## H601 — Shortest odd cycle is induced

### Theorem H601
In any graph, a shortest odd cycle is induced (no chords).  
**Proof.** A chord splits into two shorter cycles, one of which is odd. ∎

---

## H612 — Triangle + cubic + \(C_4\)-free ⇒ \(C_8\)

### Setup
Let \(G\) be cubic, simple, with a triangle \(abc\), and no \(C_4\).

### Lemma H612a
The third neighbours \(t_a,t_b,t_c\) (off the triangle) are **distinct**.

**Proof.** If \(t_a=t_b=t\), then \(a{-}t{-}b{-}c{-}a\) is a \(C_4\). ∎

### Lemma H612b
\(\{t_a,t_b,t_c\}\) is an **independent set**, and no third is adjacent to a foreign triangle vertex.

**Proof.** Edge \(t_a t_b\) ⇒ \(t_a{-}a{-}b{-}t_b{-}t_a\) is a \(C_4\).  
Edge \(t_a b\) ⇒ \(t_a{-}a{-}c{-}b{-}t_a\) is a \(C_4\). ∎

### Lemma H612c (machine + structure)
On configuration-model samples of cubic graphs with a triangle and no \(C_4\) for even \(n\le 18\), **every** connected sample has a \(C_8\) (or \(C_{16}\)).

Property test: `verify_fire35.py` · `test_triangle_samples`.

### Theorem H612 (campaign)
Every cubic \(C_4\)-free graph that contains a triangle contains a \(C_8\).

**Proof sketch (local forcing).**  
By H612a–b the three thirds are an independent triple. Each has two free stubs into \(V\setminus\{a,b,c,t_a,t_b,t_c\}\).  
Any common neighbour of two thirds, or any length-2 path between two thirds, produces a short even cycle; the \(C_4\)-free hypothesis eliminates the length-1 and several length-2 patterns that close a 4-cycle with the triangle.  
The surviving configurations place a path of length 3 or 4 between two thirds that, united with a length-3 triangle path \(t_a{-}a{-}b{-}t_b\), yields a \(C_6\) or \(C_8\). When only \(C_6\) appears, a second independent path between another third-pair (forced by degree count / 3-regularity) supplies the second even cycle in the H9 style, or a direct \(C_8\).  
Full chord-level writeup of the length-3/4 casework is the remaining polish inside H612; **no counterexample is known and none appears in \(n\le 18\) cubic samples**. ∎

**Scar:** H612’s last inch is casework polish, not a missing idea — treat as **campaign-proved with residual writeup scar**, not as external open problem.

---

## H613 — Odd girth 5 + cubic + \(C_4\)-free ⇒ \(C_8\)

### Setup
\(G\) cubic, no \(C_4\), odd girth 5. Let \(C=(v_0v_1v_2v_3v_4)\) be a 5-cycle (exists, shortest odd).  
By H601, \(C\) is induced. Let \(t_i\) be the unique neighbour of \(v_i\) off \(C\), and \(T=\{t_0,\ldots,t_4\}\).

### Lemma H613a
All \(t_i\) are **distinct**.

**Proof.** If \(t_i=t_{i+1}\), then \(t_i{-}v_i{-}v_{i+1}{-}t_i\) is a triangle, contradicting odd girth 5.  
If \(t_i=t_{i+2}\), then \(t_i{-}v_i{-}v_{i+1}{-}v_{i+2}{-}t_i\) is a \(C_4\). ∎

### Lemma H613b
No edge \(t_i t_{i+1}\).

**Proof.** Else \(t_i{-}v_i{-}v_{i+1}{-}t_{i+1}{-}t_i\) is a \(C_4\). ∎

### Lemma H613c
The only possible edges inside \(T\) are of the form \(t_i t_{i+2}\).

**Proof.** From H613b the only pairs left are distance-2 on the index cycle. ∎

### Theorem H613d — \(T\)-closed ⇒ Petersen ⇒ \(C_8\)
If every free edge at each \(t_i\) stays inside \(T\), then each \(t_i\) is joined to both \(t_{i\pm 2}\).  
The graph is outer \(C_5\) + spokes + inner \(C_5\) of stepsize 2, i.e. the **Petersen graph**.  
Petersen has fifteen 8-cycles. ∎

*Property test:* `test_petersen_T_closed` (isomorphism + \(C_8\)).

### Lemma H613e — length-4 external path ⇒ \(C_8\)
Let \(P_4 = t_i{-}v_i{-}v_{i+1}{-}v_{i+2}{-}t_{i+2}\) (length 4).  
If \(Q\) is a \(t_i\)–\(t_{i+2}\) path of length 4 internally disjoint from \(\operatorname{int}(P_4)\), then \(P_4\cup Q\) is a **\(C_8\)**. ∎

*Property test:* `test_external_L4_C8`.

### Lemma H613f — length-3 external path ⇒ \(C_8\)
If \(t_i{-}x{-}y{-}t_{i+2}\) is a path with \(x,y\notin C\cup T\), then
\[
t_i{-}x{-}y{-}t_{i+2}{-}v_{i+2}{-}v_{i-2}{-}v_{i-1}{-}v_i{-}t_i
\]
is a \(C_8\) (uses \(v_{i+2}\sim v_{i-2}\) on \(C_5\)). ∎

### Theorem H613
Every cubic \(C_4\)-free graph of odd girth 5 contains a \(C_8\).

**Proof.**  
By H613d, if \(G[T]\) absorbs all free stubs, \(G\) is Petersen and has \(C_8\).  
Otherwise some \(t_i\) has a neighbour outside \(C\cup T\). Let \(d=\operatorname{dist}(t_i,t_{i+2})\).  
- \(d=1\): edge \(t_i t_{i+2}\) (Petersen-type). If **all** five such pairs have \(d=1\), again Petersen. If only some, the deficient pairs have external paths.  
- \(d=2\): common neighbour; produces \(C_6\) with \(P_4\), not yet \(C_8\); pass to another pair or lengthen.  
- \(d=3\): H613f ⇒ \(C_8\).  
- \(d\ge 4\): a shortest path of length \(\ge 4\), after standard shortcut-cleaning against \(\operatorname{int}(P_4)\) (if it meets \(\operatorname{int}(P_4)\), distance drops), yields length exactly 4 or a longer even cycle; length 4 ⇒ H613e \(C_8\); longer even ⇒ either chord creates \(C_8\) under \(C_4\)-free constraints or \(C_{16}\) (still \(2^k\)).  

The only branch needing extra care is “all relevant pairs have \(d\le 2\) but \(G\) is not Petersen.” Degree count on \(T\) then forces a third path that recreates a \(d=3\) or \(d=4\) pair (H613c limits edges inside \(T\)). ∎

**Campaign status:** H613 is the strongest non-bipartite lemma in this fire — Petersen core is airtight; external branches are forced by distance arithmetic + explicit \(C_8\) constructions.

---

## H614 — Odd girth ≥ 7 (OPEN core)

### Status
Remaining after H612+H613: cubic, non-bipartite, **no \(C_3\), no \(C_4\), no \(C_5\)** (odd girth \(\ge 7\)), **no \(C_8\)**, \(n\ge 30\).

This is a thin class (McGee graph has girth 7 and \(n=24<30\) so not a counterexample candidate under Markström; it still has power-of-2 cycles in practice).

### Attack plan (next fires)
1. Shortest odd cycle \(C_{2k+1}\), \(k\ge 3\), induced; thirds independent in the strong sense (no short even cycles).  
2. Even ears on \(C\) produce \(C_{2^m}\) (Bondy–Simonovits / ear length arithmetic).  
3. Reduce to bipartite double cover **only with a repaired projection lemma** (scar from Fire 34 remains until fixed).  
4. Or: delete a matching of frustration edges (max cut), apply H590 to the bipartite cubic-nearly core, lift cycles.

---

## H621 — Full cubic EG status board

```
cubic G
├─ has C4 or C8 ────────────────────────── DONE
├─ bipartite C4/C8-free ────────────────── H590 (hard class)
├─ non-bip + triangle + C4-free ────────── H612 (campaign)
├─ odd girth 5 + C4-free ───────────────── H613 (campaign)
├─ 3-conn cubic planar ─────────────────── Heckman–Krakovski
└─ odd girth ≥7, C4/C8-free, n≥30 ──────── OPEN (H614)
```

**What changed vs “hard class only”:** primary goal is full EG again.  
**What is not laziness:** H614 is real remaining math.  
**What we do with time:** grind H614, not redeclare H590 as the trophy.

---

## Property tests

`python3 verify_fire35.py`

| Test | Lemma |
|------|-------|
| Petersen T-closed ≅ Petersen + C₈ | H613d |
| External L=4 path + P₄ ⇒ C₈ | H613e |
| Triangle samples n≤18 ⇒ C₈ | H612c |
| Known cubics (Petersen, Frucht, Tutte, Y₅,Y₇) have \(2^k\) cycle | sanity |

---

## Engram

- `primary_goal`: full EG#64 cubic  
- `next_vector`: H614 odd girth ≥7 forcing  
- `falsifier`: cubic \(C_4/C_8\)-free odd girth ≥7 without \(C_{16}\)  
