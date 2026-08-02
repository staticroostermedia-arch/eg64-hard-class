# EG#64 Hard Class — Engram Proof Campaign

**Target:** [Erdős–Gyárfás conjecture](https://www.erdosproblems.com/64) restricted to **cubic bipartite** graphs that are **C₄-free and C₈-free** (“hard class”).

**Method:** computational census (Foster CAT, genbg n≤24) + structural H-theorems, with continuity stored in [Engram](https://github.com/staticroostermedia-arch/engram) (`.leg` cryptographic memory / MCP session handoff).

**Status (Fire 28):** Hard EG for **n < 62** proved (H31). Unlimited *n* reduced to residual-bad double-stretch arms with an **L2-block** on the a\*-star; open hinge is L3–L4 adjacency forcing dist(a\*,e)≤4 (⇒ C₁₆) or Arm B stub overflow.

---

## What’s in this repo

| Path | Role |
|------|------|
| `NOTE_eg64_foster_census.md` | Living campaign log + theorem index |
| `PROOF_*.md` | Fire-by-fire proof notes (H-theorems) |
| `results_foster_*.json` | Foster CAT power-of-2 cycle census |
| `data/` | Sparse6 Foster extracts used in checks |

---

## Headline theorems (selected)

| ID | Statement | Status |
|----|-----------|--------|
| H31 | Hard-class EG for n<62 (Moore / local girth) | **Proved** |
| H41 | Residual bad + dist_{G''}(a\*,t)=6 ⇒ C₁₆ | **Proved** |
| H42 | T₂–T₅ creates explicit C₈ under residual | **Proved** |
| H50 | f−v₄ / f−T₃ are C₈ under E–Bset | **Proved** |
| H52 | dist(a\*,e)≤4 under E–Bset ⇒ C₁₆ | **Proved** |
| H55–H60 | L2-block: {c₁,c₂,s} outside B(e,3); L1 saturated | **Proved** |
| H70 | length-6 a\*–e geodesic cannot end b−e | **Proved** |
| H105–H109 | u_g C₈ massacre (v0,v2,v4,T3,δ,…) | **Proved** |
| H115 | DS layer law: a\*∈L₆(e) | **Proved** |
| H125 | u_g ∈ L₃(e) | **Proved** |
| H141 | C₁₆ ⇔ disjoint length-8 s–v₁ path | **Proved** |
| H178 | L₃ meets only L₂∪L₄ | **Proved** |
| H202 | dual ending + \|L₃\*\|=3 ⇒ C₈ | **Retracted (C₄ premise)** |
| H215 | C₄ law: no vertex meets both L₂ children of one L₁ | **Proved** |
| H216 | dual ⇒ \|L₃\*\|≥4, disjoint g/g′ stars | **Proved** |
| H289 | a*-bridge C₈ (L₄ of u_g/p_a ↛ c₂) | **Proved** |
| H261 | U0a + c₁−s ⇒ C₈ | **Proved** |
| H311 | U0 impossible on dual k=4 | **Proved** |
| H338 | dual k=4 tight ⇒ U2 only | **Proved** |
| H363 | dual + p_b−q ⇒ C₈ (U2a dead) | **Proved** |
| H368 | pure f: e′ meets ≤1 of star(g′) | **Proved** |
| H384 | U2b forbids s−c₁ (C₈) | **Proved** |
| H387 | U2b + c₁−w + c₂−s ⇒ C₈ | **Proved** |
| H375 | y,s cannot share L₅ | **Proved** |
| H413 | L₆-bridge map under H390 | **Proved** |
| H424 | private L₆ of H390 is C₄/C₈-free | **Observed** |
| — | Full hard EG all n (double-stretch empty) | **Open** |

Decision tree (abbreviated):

```
hard cubic bipartite C4/C8-free
├─ n < 62  →  EG  (H31)
└─ all n
   residual bad?
   ├─ no  → H-bridge / walk chain → C16
   └─ yes → P8 length 8
        ├─ dist(a*,t)=6 → C16 (H41)
        └─ double-stretch
             ├─ Arm A (E–Bset): L2-block; need dist(a*,e)≤4
             └─ Arm B (no E–Bset): |F|=4, QB⊥QF, B1/B2
```

---

## How to re-check census (optional)

Requires NetworkX + Foster sparse6 under `data/Sparse6/`.

```bash
python3 - <<'PY'
import json, networkx as nx
from pathlib import Path
# see NOTE_eg64_foster_census.md for power2_cycles harness
print('campaign assets present:', list(Path('.').glob('PROOF_*.md')).__len__())
PY
```

---

## Continuity

Session tiles and handoffs live in a local Engram store during agent runs (`tile:eg64_fire*`). This repo is the **publishable** surface: proofs, census, and next vectors.

---

## License

CC0-1.0 (or as declared by the repo owner). Math notes are offered for verification and collaboration; cite erdosproblems.com/#64 for the open problem statement.

## Links

- Problem: https://www.erdosproblems.com/64  
- Engram substrate: https://github.com/staticroostermedia-arch/engram  
