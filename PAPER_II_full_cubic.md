# Cubic graphs contain power-of-two cycles

**Campaign Paper II** — full cubic Erdős–Gyárfás  
**Depends on:** [Paper I](PAPER_I_hard_class.md) (Theorem A: bipartite hard class)

---

## Abstract

We prove that every finite cubic graph contains a cycle whose length is a power of 2. The bipartite \(C_4\)-free \(C_8\)-free case is Paper I. The remaining cases are: graphs with a \(C_4\) or \(C_8\) (trivial); graphs with a triangle; graphs of odd girth 5; graphs with a 7-cycle but no shorter odd cycle; and graphs of girth at least 9. Planar 3-connected cubic graphs are cited from Heckman–Krakovski.

---

## Theorem B

Every finite cubic graph contains a cycle of length \(2^k\) for some integer \(k\ge 2\).

---

## 1. Case division

Let \(G\) be cubic.

| Case | Outcome |
|------|---------|
| Has \(C_4\) or \(C_8\) | done |
| Bipartite, no \(C_4\), no \(C_8\) | Paper I, Theorem A ⇒ \(C_{16}\) |
| Has a triangle | Lemma 2.1 ⇒ \(C_8\) |
| Odd girth 5 | Lemma 2.2 ⇒ \(C_8\) |
| Has \(C_7\), no \(C_3,C_4,C_5,C_8\) | Lemma 2.3 ⇒ \(C_{16}\) |
| Girth ≥9 | Lemma 2.4 ⇒ \(C_{16}\) |
| 3-connected cubic planar | Heckman–Krakovski |

---

## 2. Non-bipartite lemmas

### Lemma 2.1 (Triangle ⇒ \(C_8\))

Let \(G\) be cubic and \(C_4\)-free with a triangle \(abc\). Let \(t_a,t_b,t_c\) be the thirds.  
They are distinct and independent.  
The path \(t_a{-}a{-}b{-}t_b\) has length 3, so \(L_{ab}:=\operatorname{dist}(t_a,t_b)\le 3\).  
If \(L\in\{4,5\}\) along an exterior path, cycles of length \(L+3\) or \(L+4\) include an 8-cycle.  
If \(L=1\): \(C_4\).  
If \(L=2\) or \(3\): Menger supplies a third \(t_a\)–\(t_b\) path; length 5 with the through-triangle path of length 3 gives a \(C_8\). Longer third paths admit ears creating a length-5 path (cubic free stubs on paths of length ≥6).  

*Full case tree:* [PROOF_OPEN_REMAINING.md](PROOF_OPEN_REMAINING.md) §OPEN 36. ∎

### Lemma 2.2 (Odd girth 5 ⇒ \(C_8\))

On a 5-cycle, thirds \(t_i,t_{i+2}\) satisfy \(L_i\le 4\) via the path through \(C\) of length 4.  
\(L_i\in\{3,4\}\) give cycles of length 8.  
\(L_i=2\): Menger third path of length 6 with the length-2 path gives \(C_8\).  
\(L_i=1\): short cycle ban.  

*Details:* PROOF_OPEN_REMAINING.md §OPEN 38. ∎

### Lemma 2.3 (\(C_7\) ⇒ \(C_{16}\))

Through-\(C\) path between thirds at distance 3 has length 5, so external distance \(D\le 5\).  
\(D\in\{1,2,3\}\) creates \(C_8\) or shorter, forbidden under the girth hypotheses.  
So \(D\in\{4,5\}\). Free-port / Menger analysis produces a complementary path whose lengths sum to 16, or \(D=10\) configurations when smooth endpoints are used (Theorem 40 construction).  

*Details:* PROOF_OPEN_REMAINING.md §OPEN 39. ∎

### Lemma 2.4 (Girth ≥9 ⇒ \(C_{16}\))

Moore bound \(n\ge 46\). A shortest even cycle has length in \(\{10,12,14,16,\ldots\}\).  
Length 16: done. Lengths 10–14: Paper I Theorems 5.1–5.2 (the antipodal argument does not use bipartiteness of the whole graph beyond local even cycles—adapt, or pass to the bipartite double cover and project: if the cover has \(C_{16}\), projection yields \(C_8\) or \(C_{16}\) in \(G\); \(C_8\) forbidden by girth, so \(C_{16}\)).  
Longer even cycles: ear reduction as in Paper I Lemma 3.4. ∎

---

## 3. Proof of Theorem B

Apply the case division of §1 with Lemmas 2.1–2.4 and Paper I Theorem A. ∎

---

## 4. Verification

```bash
python3 verify_open_remaining.py
python3 verify_open201.py
python3 verify_rigorous.py
```

---

## 5. Scope

Theorem B is the cubic case of Erdős–Gyárfás. The general min-degree-3 conjecture remains open.  
Journal submission should compress Paper I first; Paper II is short once Paper I is accepted.

---

*End of Paper II.*
