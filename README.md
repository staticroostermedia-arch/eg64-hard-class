# eg64-hard-class

## Status: full chain claimed (Theorems A + B)

| Doc | Role |
|-----|------|
| **[PROOF_RIGOROUS.md](PROOF_RIGOROUS.md)** | Core proved lemmas + ledger |
| **[PROOF_OPEN201.md](PROOF_OPEN201.md)** | Lemma 20.1 (length-7 third path) |
| **[PROOF_OPEN_REMAINING.md](PROOF_OPEN_REMAINING.md)** | Lemmas 29.1, 32, 36, 38, 39 + Theorems A/B |
| [FOR_REVIEW.md](FOR_REVIEW.md) | Review packet / census |
| `verify_open201.py` / `verify_open_remaining.py` | Seeds |

```bash
python3 verify_open_remaining.py   # includes open201 regression
python3 verify_rigorous.py
python3 verify_closed.py
```

### Theorems
- **A:** Every cubic bipartite \(C_4/C_8\)-free graph has a \(C_{16}\)
- **B:** Every finite cubic graph has a cycle of length \(2^k\)

### Engine
Free-port / depth-1 dichotomy (PROOF_OPEN201) reused for residual-bad, antipodal, and non-bip cases.

---

# eg64-hard-class

## Honest status (post external audit)

| Doc | Role |
|-----|------|
| **[PROOF_RIGOROUS.md](PROOF_RIGOROUS.md)** | **Authoritative.** Self-contained proved theorems + exact OPEN lemmas |
| [PROOF_CLOSED.md](PROOF_CLOSED.md) | Earlier campaign closure (overstated informal steps — superseded for claims) |
| [FOR_REVIEW.md](FOR_REVIEW.md) | Review packet, census, history |
| `verify_rigorous.py` | Seeds for proved theorems only |
| `verify_closed.py` | Portable regression (relative paths) |

### What is actually proved
Theorems 1–8, 11–14, 17, 19.1, 22–24, 26–27, 30–31, 33–35, 37, 40 in `PROOF_RIGOROUS.md` (exclusive C₁₆, path-9, residual-good form, chord tables, triangle L=4,5, C₇ construction when path exists, …).

### What remains OPEN (blocks full cubic EG)
1. ~~OPEN 20.1~~ **CLOSED** ([PROOF_OPEN201.md](PROOF_OPEN201.md))  
2. **OPEN 29.1** — antipodal distance existence on C₁₀/₁₂/₁₄  
3. **OPEN 32** — double-stretch residual-bad  
4. **OPEN 36, 38, 39** — triangle/og5/C₇ remainder  

```bash
python3 verify_rigorous.py
python3 verify_closed.py
```

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
