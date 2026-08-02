# Status: Theorem A refuted in present form

**Date:** 2026-08-02  
**Trigger:** Independent review (GPT Sol 5.6) + literature check.

## The error

**Paper I, Theorem A (as written):**  
> Every connected cubic bipartite graph without \(C_4\) or \(C_8\) contains a \(C_{16}\).

**This is false.**

### Counterexample family

There exist **cubic bipartite graphs of arbitrarily large girth** (classical; e.g. incidence graphs of high-girth Steiner systems / hypergraphs, LPS-type constructions, known cages for even girth).  

In particular, any cubic bipartite graph of **girth ≥ 18** has:
- no \(C_4\), no \(C_8\) (and no \(C_6,\ldots,C_{16}\)),
- hence no \(C_{16}\).

Concrete reference points:
- Dynamic Cage Survey: records for \((3,g)\)-graphs at large even \(g\); bipartite cages exist for even girth.
- Erskine–Tuite (Electron. J. Combin. 30, 2023): incidence graphs of \(3\)-regular \(3\)-uniform hypergraphs of girth \(g\) are cubic bipartite of girth \(2g\).
- Exoo and others: explicit small trivalent graphs of girth 18 (order 2560); whether that specific graph is bipartite is secondary — the **existence of some** cubic bipartite graph with girth ≥ 18 is enough and is standard.

High-girth graphs exist precisely because the “every long cycle has a short chord/ear reducing to \(C_{16}\)” step fails.

## What fails in the campaign assembly

| Piece | Status |
|-------|--------|
| Theorem A global (all \(C_4/C_8\)-free cubic bipartite ⇒ \(C_{16}\)) | **Refuted** |
| Reduction “girth ≥ 10 ⇒ reduce long cycles to \(C_{16}\)” | **False** for high girth |
| Paper II “triangle ⇒ \(C_8\)” in cubic \(C_4\)-free graphs | **False** (blow-up / replace vertex by triangle in girth-10 cubic graph) |
| Free-port Theorem 4.5 under **residual-good** (graph already has a \(C_6\) + H-bridge setup) | **Not automatically refuted** — local; needs independent re-audit |
| Seed scripts (`verify_*.py`) | Check **examples / arithmetic**, not universal quantifiers |

## What remains valuable

1. **Architecture:** named lemmas, dependency order, gap log, commit history, reviewer packet.  
2. **Local configuration lemmas** that assume a \(C_6\) / residual-good H-bridge — these are candidate **conditional** statements, not a proof of EG#64.  
3. **Census oracles** (genbg / Foster) for small \(n\): still useful empirical checks, not proofs.  
4. **Engram continuity experiment:** process value independent of the math error.

## Required re-scope

- **Do not claim** Theorem A, Theorem B, or “EG#64 solved.”  
- **Do claim at most:** “Atlas of local cycle-forcing configurations in cubic bipartite graphs that already contain a \(C_6\), with free-port case analysis; global assembly to all \(C_4/C_8\)-free graphs is invalid.”  
- README status: **refuted in present form** (global theorem).  
- Next work if continued: re-state free-port as a conditional lemma; prove or drop each local claim under explicit hypotheses; never re-assert high-girth reduction.

## EG#64 itself

The Erdős–Gyárfás conjecture remains **open** (as of 2026 literature). A full cubic proof would be a major result and needs independent expert verification. This campaign did not produce one.

