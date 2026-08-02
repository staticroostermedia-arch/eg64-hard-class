# Fire 26 — H247 dead (C₈); U2a eliminated; U2b only

## Theorem H363 (PROVED) — dual forbids p_b−q

Under dual ending with \(p_b\in\mathrm{star}(g')\):
\[
e{-}T_2{-}e'{-}r_1{-}q{-}p_b{-}g'{-}f{-}e
\]
is an **8-cycle**. All edges forced by dual + \(p_b{-}q\) + \(p_b{-}g'\).

**⇒ H247 is illegal. U2a (dual k=4 with \(N(p_b)\ni q\)) is dead.** ∎

*Verified computationally on the dual core graph (networkx `simple_cycles`).*

---

## Corollary H369 — dual k=4 U2 must be U2b

\[
N(p_b)=\{g',s,s_2\}\quad\text{both free in }L_4\setminus\{q,w\},
\]
\[
N(q)=\{r_1,c_1,c^*\}\quad c^*\in L_5\setminus\{c_1,c_2\}.
\]

(No \(p_b{-}q\); q’s third is a new L₅ vertex.)

---

## Theorem H368 (PROVED) — pure f cannot park both e′ stubs on star(g′)

Under pure f, if \(N(e')=\{T_2,p_a,p_b\}\) (both free on star(g′)):
\[
p_b{-}e'{-}p_a{-}g'{-}p_b \quad\text{is C₄}.
\]
**⇒ at most one of \(\{p_a,p_b\}\) meets e′.** ∎

---

## Dual k=4 status (complete case split on u_g frees)

| Case | Status |
|------|--------|
| U0 | DEAD H311 |
| U1 | DEAD H337 |
| U2a (p_b−q) | **DEAD H363** |
| **U2b** (p_b both free L₄ ≠q) | **only remaining dual k=4** |

### U2b constraints (inherited)

- a*-bridge H289: L₄ nbrs of \(\{u_g,p_a\}\) ↛ c₂  
- sibling L₅ exclusivity H293 / H297 / H299 / H322  
- five L₄ verts \(\{y,y',w,s,s_2\}\) each demand 2 exclusive L₅ slots  
- plus \(c^*\) for q  
- skeleton alone is C₄/C₈-free (computational); obstruction must use L₅–L₆ fill  

---

## Pure f (structure + H368)

| star | members |
|------|---------|
| star(g) | {r₁, u_g} |
| star(g′) | {p_a, p_b} disjoint |
| star(e′) | {z₁, z₂} ≠ r₁; **at most one in {p_a,p_b}** (H368) |

Merges z₁=u_g and/or z₁=p_a are C₄-free at skeleton level (computational).

---

## Pure T2

star(g)={u₁,u₂}, star(g′)={u₃,u₄}, star(e′)={r₁,z}, |L₃*|≥5.  
Skeleton C₄/C₈-free including z=u₁ merge.

---

## Method note

Fire 26 used **constructive core graphs** + exhaustive short-cycle search as a
property test for candidate skeletons — complementary to pure hand casework.
H363 is hand-checkable; the machine confirmed no hidden C₄ in the dual core
before the p_b−q edge is added.

## Next vector
1. Kill **U2b** via exclusive L₅–L₆ demand overflow or C₈ after mandatory L₅ attach.  
2. Pure f with partial e′ merge (z₁=p_a or z₁=u_g).  
3. Pure T2.  
4. dual k≥5.

## Property tests
- Every dual model with p_b−q contains C₈ e-T2-e'-r1-q-pb-g'-f-e  
- No dual k=4 U2a model  
- Pure f with N(e')⊇{p_a,p_b} contains C₄  
