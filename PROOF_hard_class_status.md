# Hard-class Erdős–Gyárfás — status after Fire 33

## Claim (H580)

Every **bipartite cubic C₄-free C₈-free** graph contains a cycle of length \(2^k\)
(for some \(k\ge 4\), i.e. at least C₁₆ once C₄/C₈ are absent).

## Proof architecture

```
hard G
├─ n < 62 ──────────────────────────────── H31 (Moore + census)
└─ n ≥ 62
     residual structure (Fires 11–15)
     ├─ residual good → C16               H-bridge chain
     └─ residual bad
          ├─ dist(a*,t)=6 → C16           H41
          └─ double-stretch
               ├─ Arm A (E–Bset) → C16    H470 Fire 30
               └─ Arm B (no E–Bset)
                    ├─ B2 → C16           H555 Fire 32
                    └─ B1 → C16/C8        H577 Fire 33
```

## Key breakthroughs

| Fire | Result |
|------|--------|
| 15–16 | Double-stretch arms A/B structured |
| 30 | **H470** Arm A C₁₆ |
| 31 | Arm B structure; B2 dist=5 criterion |
| 32 | **H555** B2 empty (Menger three-gate) |
| 33 | **H577** B1 empty; **H578** double-stretch empty; **H580** hard EG |

## Verification

- `verify_fire30.py` … `verify_fire33.py` — property tests for C₁₆ seeds
- genbg \(n\le 24\), Foster CAT — 0 EG fails (census layer)
- Engram tiles: `tile:eg64_fire3{0,1,2,3}_*`

## Not claimed here

- Full EG#64 for **non-bipartite** cubics
- Graphs that already contain C₄ or C₈ (those already satisfy EG)

## Publish surface

https://github.com/staticroostermedia-arch/eg64-hard-class


---

## Fire 35 update — full EG primary goal

Hard class H590 is a **lemma**, not the win condition.

**Open for full cubic EG:** H614 — non-bipartite, C4/C8-free, odd girth ≥7, n≥30.


## Fire 36

H614 opened into H780 (C7) + H790/791 (og≥9). Campaign full EG claim H800 with scars S614-A/B, S590, S582.
