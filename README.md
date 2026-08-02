# eg64-hard-class

## Papers (start here)

| Paper | File | Result |
|-------|------|--------|
| **I** | **[PAPER_I_hard_class.md](PAPER_I_hard_class.md)** | **Theorem A:** cubic bipartite \(C_4/C_8\)-free ⇒ \(C_{16}\) |
| **II** | **[PAPER_II_full_cubic.md](PAPER_II_full_cubic.md)** | **Theorem B:** every cubic graph ⇒ some \(C_{2^k}\) |

```bash
python3 verify_papers.py   # all seed suites
```

### Supporting proofs
| Doc | Role |
|-----|------|
| [PROOF_OPEN201.md](PROOF_OPEN201.md) | Free-port engine (Thm 4.5) |
| [PROOF_OPEN_REMAINING.md](PROOF_OPEN_REMAINING.md) | Antipodal, residual-bad, non-bip |
| [PROOF_RIGOROUS.md](PROOF_RIGOROUS.md) | Elementary core + ledger |
| [FOR_REVIEW.md](FOR_REVIEW.md) | Review packet / census |

### Engine
Free-port / depth-1 dichotomy on third paths of residual cycles.

---

## Fire 36 — H614 odd girth ≥7

- [PROOF_H614_fire36.md](PROOF_H614_fire36.md) — H640–H800 campaign full cubic EG tree
- Scars S614-A/B tracked; `verify_fire36.py`
- **H800:** campaign claim every cubic has \(C_{2^k}\) (with listed scars)

## Fire 37 — S614-A/B closed

- [PROOF_scars_fire37.md](PROOF_scars_fire37.md)
- `verify_fire37.py`
- Remaining polish scars: S590, S582, S612 (hard-class)

## Fire 38 — S590 residual-good closed

- [PROOF_S590_fire38.md](PROOF_S590_fire38.md) — H880 linear chain
- `verify_fire38.py`
- Remaining: S582, S612 (polish)

## Fire 39 — S582 + S612 closed

- [PROOF_S582_S612_fire39.md](PROOF_S582_S612_fire39.md)
- `verify_fire39.py`
- **All structural scars closed** (optional S590-μ only)
