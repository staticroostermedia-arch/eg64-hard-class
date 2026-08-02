# Erdős–Gyárfás for cubic graphs — campaign write-up for review

**Repository:** [staticroostermedia-arch/eg64-hard-class](https://github.com/staticroostermedia-arch/eg64-hard-class)  
**Problem:** Erdős–Gyárfás conjecture (#64 on erdosproblems.com): every graph of minimum degree 3 contains a cycle of length a power of 2.  
**Scope of this campaign:** **cubic** (3-regular) graphs, with a complete case tree claimed at campaign strength; strongest machine-backed core is the **bipartite hard class**.

---

## Executive answer (read this first)

| Question | Answer |
|----------|--------|
| Is EG#64 fully solved as a journal theorem? | **Not yet claimed as such.** This is a **campaign proof tree** with many solid lemmas, exhaustive small-order checks, and some steps that still need referee-grade compression. |
| Can you review a complete write-up? | **Yes — this document.** It is the single entry point. Leaf proofs live in `PROOF_*.md` + `verify_*.py`. |
| What is safest to trust today? | **Tier A** below (enumeration + short combinatorial lemmas with property tests). |
| What is the strongest theoretical claim? | **H590 / H881:** every cubic bipartite \(C_4\)-free \(C_8\)-free graph has a \(C_{16}\) — campaign-complete with residual-good/bad linearization. |
| What is the full cubic claim? | **H800′′:** every cubic graph has a \(C_{2^k}\) — **campaign architecture complete**, dependent on Tier B/C steps. |

**Confidence (honest):**

| Layer | Confidence | Notes |
|-------|------------|-------|
| Small \(n\) bipartite EG (genbg ≤24, Foster hard CAT) | **High** | Dual oracle; 0 counterexamples in tested census |
| Short lemmas (H9, H13, H36, H41 seeds, H682, path-union) | **High** | Machine-checked seeds |
| Residual-bad arms (Fires 30–33) | **Medium–high** | Explicit constructions + property tests |
| Residual-good gap (H860–H862) | **Medium** | Linearized; micro-scar S590-μ optional |
| λ=2 full table (H904–H906) | **Medium** | Matching no-bridge solid; some L=6 gadget prose is campaign |
| Triangle ⇒ C₈ (H928) | **Medium** | Core distance cases solid; large-\(n\) induction campaign |
| Non-bipartite C₇ / girth ≥9 (H780, H845) | **Medium** | Architecture + seeds; H\* fork prose campaign-linearized |
| **Full EG#64 for all cubics** | **Campaign — needs external audit** | Do **not** announce as settled without independent check |

---

## 1. Problem statement

**Conjecture (Erdős–Gyárfás).** Every graph with minimum degree at least 3 contains a cycle whose length is a power of 2.

**Restriction here.** \(G\) finite, simple, **cubic** (3-regular). Target: existence of some \(C_{2^k}\) with \(k\ge 2\) (usually \(C_4,C_8,C_{16},\ldots\)).

**Why cubic is the heart.** The general min-degree-3 case reduces in spirit to rich cubic structure; cubic already contains the classical hard cages and bipartite extremal examples.

**Prior art used.**
- Markström: no cubic counterexample on \(n<30\).
- Heckman–Krakovski: 3-connected cubic **planar** graphs satisfy EG.
- Foster census / genbg: enumeration backbone.
- Chen–Saito: \(\delta\ge 3\) ⇒ cycle length \(0\bmod 4\).

---

## 2. Case tree (H800′′)

```
cubic G
│
├─ has C₄ or C₈ ──────────────────────────────────────── DONE (trivial EG)
│
├─ bipartite, C₄/C₈-free  ["hard class" ℋ]
│     ├─ n < 62 ──────────────────────────────────────── H31 (Moore + census + H9)
│     ├─ κ < 3 ───────────────────────────────────────── H910 (⇒ C₂ᵏ or reduce)
│     ├─ residual good (dist_{G−v₀}(s,v₁)=4) ─────────── H880
│     └─ residual bad  (dist ≥ 8) ─────────────────────── H579 / Fires 30–33
│
├─ non-bipartite
│     ├─ has triangle ────────────────────────────────── H928 ⇒ C₈
│     ├─ odd girth 5 ─────────────────────────────────── H613 ⇒ C₈
│     ├─ has C₇ (og ≥ 7) ─────────────────────────────── H780 + H824
│     └─ girth ≥ 9 ───────────────────────────────────── H845
│
└─ 3-connected cubic planar ──────────────────────────── Heckman–Krakovski (cite)
```

---

## 3. Tier A — high confidence (review these first)

### 3.1 Enumeration
| Result | Statement | Evidence |
|--------|-----------|----------|
| **E** | Cubic bipartite \(n\le 24\) ⇒ EG | genbg exhaustive + dual cycle oracle |
| **A′** | Foster CAT hard graphs ≤150 ⇒ EG | `results_foster_eg.json` |
| Markström | No cubic counterexample \(n<30\) | literature |

### 3.2 Core combinatorial lemmas (property-tested)

| ID | Statement | Proof file | Test |
|----|-----------|------------|------|
| **H9** | \(C_6\) + exclusive \(C_{12}\) through one edge ⇒ \(C_{16}\) | Fire 6/9 | `verify_fire38` |
| **H13** | Third-path length 9 ⇒ exclusive \(C_{12}\) ⇒ H9 | Fire 8 | `verify_fire38` |
| **H17** | \(\operatorname{dist}_H(s,t)\in\{3,7,9,\ldots\}\) in \(C_4/C_8\)-free | Fire 9 | structural |
| **H32–H34** | Walk formula; \(d_0=4\Leftrightarrow\) path-4 in \(G-v_0\) | Fire 12 | |
| **H36** | Neighbours of \(v\): dist in \(G-v\) ∉ \{2,6\} | Fire 13 | `verify_fire38` |
| **H41** | Two length-8 paths ⇒ \(C_{16}\); residual fork | Fire 14 | |
| **H810–H812** | Abstract path-union \(C_{L_1+L_2}\) | Fire 37 | `verify_fire37` |
| **H682** | C₇ antipodal external L=10 ⇒ \(C_{16}\) | Fire 36 | `verify_fire36` |
| **H840–H842** | C₁₀/₁₂/₁₄ antipodal ⇒ \(C_{16}\) | Fire 37 | `verify_fire37` |

### 3.3 How to re-run verification

```bash
cd eg64-hard-class
for f in verify_fire30.py verify_fire33.py verify_fire36.py verify_fire37.py verify_fire38.py verify_fire39.py; do
  python3 "$f" || exit 1
done
```

---

## 4. Tier B — campaign-complete bipartite hard class (H590 / H881)

**Definition.** \(\mathcal{H} =\) connected cubic bipartite \(C_4\)-free \(C_8\)-free graphs.

### 4.1 Connectivity — H910 (Fire 39)
- **H900:** cubic ⇒ \(\kappa=\lambda\in\{1,2,3\}\).
- **H901:** no bridge in bipartite cubic (perfect matching vs odd component of \(G-e\)).
- **H902–H906:** λ=2 ⇒ cut cycle length \(L=r_1+r_2+2\notin\{4,8\}\) ⇒ case table forces \(C_{2^k}\).
- **H910:** \(G\in\mathcal{H}\) is 3-connected **or** already has \(C_{2^k}\).

**Reviewer watchpoints:** L=6 inductive gadget; L≥18 ear arithmetic (H906).

### 4.2 Residual good — H880 (Fire 38)
Linear chain:

```
d₀ = 4
 → path of length 4 in G−v₀     (H34)
 → H-bridge                       (H850/H851; A2 kills C₈)
 → C* or bridge-gap ≥7            (H852/H853)
 → path-9                         (H854 or H860–H862)
 → exclusive C₁₂ → C₁₆            (H13, H9)
```

**Reviewer watchpoints:** H862 stub-counting (optional micro-scar S590-μ); uniqueness of C* on CAT is census, proof uses H861–H862.

### 4.3 Residual bad — H579 (Fires 14–33)
- H41: second path length 8 ⇒ \(C_{16}\); else double-stretch.
- Arm A (geodesic / pure-f / T2): H470 explicit \(C_{16}\) (`verify_fire30`).
- Arm B: B2 Menger 3-gate H555; B1 dist collapse H577; double-stretch empty H578.
- **H579:** residual-bad ⇒ \(C_{16}\).

**Reviewer watchpoints:** Arm labeling bipartiteness; B1/B2 case completeness in Fire 31–33 writeups.

### 4.4 Small n — H31
Girth ≥10 ⇒ Moore \(n\ge 62\). Below that, girth 6 + census + H9.

### 4.5 Girth ≥10 bipartite — H870
Antipodal thirds (Fire 37 tools) force \(C_{16}\).

---

## 5. Tier C — non-bipartite and full cubic (H800′′)

### 5.1 Triangle — H928 (Fire 39)
Thirds distinct and independent under \(C_4\)-free.  
External distance \(L\in\{4,5\}\) ⇒ \(C_8\) (tested).  
Universal common neighbour + second hub ⇒ \(C_4\).  
Samples \(n\le 16\): always \(C_8\) or \(C_{16}\).  
**Watchpoint:** large-\(n\) induction step in H928.

### 5.2 Odd girth 5 — H613 (Fire 35)
C₅ thirds + \(C_4\)-free forces \(C_8\) (distance law).

### 5.3 C₇ case — H780 (Fires 36–37)
Partition \(V=C\sqcup T\sqcup U\); smooth → cubic \(H^*\);  
antipodal L=10 ⇒ \(C_{16}\); smooth-endpoint fork H824–H825.  
**Watchpoint:** completeness of H824 residual subcases.

### 5.4 Girth ≥9 — H845 (Fire 37)
Moore \(n\ge 46\); shortest even cycle in {10,12,14,16}; antipodal theorems H840–H842.  
**Watchpoint:** reduction of even cycles longer than 16 down to that set.

### 5.5 Planar
Cite Heckman–Krakovski; not re-proved here.

---

## 6. What a referee should demand next

Priority order for turning this into a **journal submission**:

1. **Compress H880 + H579 into one bipartite chapter** with all H-numbers renumbered and no “Fire” references.
2. **Expand H862 / S590-μ** to pure double counting (no CAT appeal).
3. **Rewrite H904 L=6** with a single bipartite cubic restoration gadget (no triangle gadget).
4. **Finish H928 large-n** without sample appeal (or cite a classification of cubic graphs with triangles and girth ≥5).
5. **One chapter for non-bipartite** (H613, H780, H845) with figures for C₇ smoothing.
6. Independent re-run of genbg + Foster scripts; freeze hashes of `results_foster_eg.json`.
7. **Do not** submit full EG#64 until (1)–(5) pass hostile reading; bipartite hard class (1)–(3) is the natural first paper.

---

## 7. Suggested paper split

| Paper | Title sketch | Depends on |
|-------|--------------|------------|
| **I** | Power-of-two cycles in cubic bipartite \(C_4/C_8\)-free graphs | Tier A+B |
| **II** | Connectivity and cut cycles in the hard class | H900–H910 |
| **III** | Cubic graphs with odd girth 5 or 7 | H613, H780 |
| **IV** | Full cubic EG (if I–III hold) | H800′′ |

---

## 8. File map

| Path | Role |
|------|------|
| `FOR_REVIEW.md` | **This document** — start here |
| `PROOF_MASTER_hard_class.md` | Bipartite master |
| `PROOF_S590_fire38.md` | Residual-good linearization |
| `PROOF_S582_S612_fire39.md` | Connectivity + triangle |
| `PROOF_scars_fire37.md` | Abstract fork + girth ≥9 |
| `PROOF_H614_fire36.md` | C₇ partition / smooth |
| `PROOF_nonbip_fire35.md` | Non-bipartite reduction |
| `PROOF_ArmA_dead_fire30.md` … `PROOF_B1dead_fire33.md` | Residual-bad arms |
| `PROOF_hard_class_status.md` | Running status |
| `verify_fire*.py` | Property tests |
| `results_foster_eg.json` | Foster EG certificates |
| `NOTE_eg64_foster_census.md` | Census notes |

---

## 9. Continuity substrate (Engram)

This campaign was run with a local Engram store (cryptographic `.leg` memory, scar tracking, session handoff). That is **process integrity**, not a substitute for mathematical review. Scars S582, S590, S612, S614-A/B are marked closed in-campaign; **S590-μ remains optional prose**.

---

## 10. Bottom line for the author / reviewer

- **We have a complete case architecture and a large body of checked lemmas.**  
- **We do not yet have a single polished, referee-closed proof of EG for all cubic graphs.**  
- **Best publishable core now:** bipartite hard class → always \(C_{16}\) (Paper I), after tightening H862 and λ=2 L=6.  
- **Full H800′′** is the right *program*; calling it a *theorem* requires the watchpoints in §6 to be closed under external scrutiny.

### One-sentence status

> **Campaign-complete proof tree for cubic EG#64 with high-confidence bipartite core and machine-checked seeds; full claim is ready for hostile audit, not for unconditional announcement.**

---

## Appendix — theorem index (campaign numbers)

| Range | Topic |
|-------|-------|
| H9–H18 | Exclusive C₁₂, path-9, C\* |
| H23–H29 | H-bridge, A2, C\* |
| H31–H38 | Small n, walks, bad pairs |
| H41 | Residual fork |
| H470–H580 | Arm kills, hard-class claim |
| H590 / H881 | Bipartite hard class |
| H612–H613 | Triangle / og 5 (early) |
| H640–H800 | C₇, full tree |
| H810–H845 | Abstract fork, girth ≥9 |
| H850–H880 | Residual-good linear |
| H900–H928 | Connectivity + triangle final |

*End of review packet.*
