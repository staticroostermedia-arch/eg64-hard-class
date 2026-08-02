# Status for reviewers

## Theorem 4.5 (free-port engine)

**Proof:** [PROOF_THEOREM_45_FINAL.md](PROOF_THEOREM_45_FINAL.md)

Structure:
1. Dichotomy on shortest A*–B* path length ℓ in H = G − V(P*)
2. ℓ = 1,3: PROOF_FREEPORT_CLOSED Parts I–II (finite tables)
3. ℓ ≥ 5: direct path-9 when attachments fit; free-edge landing lemma; pure-new balloon handshaking (e_out=0 impossible); induction on ℓ via C6 flips
4. ℓ = ∞: distance-4 in K_A; free edge of p3 → path 9

Seeds: `verify_freeport.py`, `verify_ell5_path9.py` (all 9 pairs at ℓ=5)

## Theorem A (hard class)

Paper I chain: residual good/bad → free-port 4.5 → C16. Census oracles green.

## Not claimed without referee

Full journal acceptance of EG#64; independent check of Lemma 2.7 (balloon) and Lemma 2.5 (a1 tables for all pairs) recommended.
