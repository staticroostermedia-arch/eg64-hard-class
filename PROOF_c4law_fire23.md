# Fire 23 — C₄ law (H215); H202 premise scar; dual rebuild

## Scar (scientific correction)

**H183 / H202 are retracted as proofs that dual+|L₃\*|=3 dies.**

The H183 skeleton set \(N(u_g)=\{g,g',y\}\), so \(u_g\) met **both** free L₂-neighbours
of \(f\). That immediately yields
\[
g{-}f{-}g'{-}u_g{-}g \qquad\text{(C₄)},
\]
forbidden in the hard class. The H202 C₈ casework sat on an already-impossible
configuration. Continuity requirement: **scar the overclaim**, keep the tools that
survived (H178, H154–H156 stub census, H141, H195-style L₅ C₄ on a\*).

---

## Theorem H215 / H222 (PROVED) — fundamental C₄ law

**Statement.** If \(x\in L_1\) has two part-B neighbours \(a,b\in L_2\), then no vertex
is adjacent to both \(a\) and \(b\).

**Proof.** Else \(v{-}a{-}x{-}b{-}v\) is a C₄. ∎

### Corollaries

| ID | Corollary |
|----|-----------|
| **H214** | No L₃\* vertex meets both \(g\) and \(g'\) (children of \(f\)) |
| **H215** | \(r_1\) meets **at most one** of \(\{g,g'\}\) |
| **H213** | \(u_g\) (neighbour of \(g\)) does **not** meet \(g'\) |
| **H220** | Pure-f with \(r_1{-}g\) and \(r_1{-}g'\) is dead |

---

## Theorem H216 (PROVED) — dual rebuilt lower bound

Under dual ending \(N(r_1)=\{e',g,q\}\) (so \(r_1{-}g\), not \(r_1{-}g'\) by H215):

| L₂ vertex | L₃\* star (size 2 free each) |
|-----------|------------------------------|
| \(g\) | \(\{r_1,\,u_g\}\) |
| \(g'\) | \(\{p_a,\,p_b\}\) **disjoint** from star(\(g\)) |
| \(e'\) | \(\{r_1,\,z\}\) with \(z\notin\{r_1,u_g\}\) (H167) |

**⇒ |L₃\*| ≥ 4**, and \(z\in\{p_a,p_b\}\) or \(z\) new (⇒ k≥5). ∎

*(H202’s |L₃\*|=3 was not just incomplete — it violated H214.)*

---

## Dual k=4 tight config (z=p_a)

\[
\begin{align*}
N(r_1)&=\{e',g,q\},&
N(g)&=\{f,r_1,u_g\},&
N(g')&=\{f,p_a,p_b\},\\
N(e')&=\{T_2,r_1,p_a\},&
N(p_a)&=\{g',e',w\},&
N(u_g)&=\{g,y_1,y_2\},\\
N(p_b)&=\{g',x_1,x_2\}.
\end{align*}
\]

### New forbids on this config

| ID | Forbid | Reason |
|----|--------|--------|
| H227 | \(p_a{-}q\) | C₄ \(p_a{-}q{-}r_1{-}e'{-}p_a\) |
| H228 | \(p_b{-}e'\) | C₄ \(p_b{-}e'{-}p_a{-}g'{-}p_b\) |
| H240 | \(p_b{-}v_2\) | C₈ through \(e{-}b{-}t{-}v_1\) |
| H241 | \(p_b{-}v_0\) | C₈ through spine |
| H245 | \(p_a,p_b\) share L₄ nbr | C₄ via \(g'\) |
| H247 | \(p_b{-}q\) allowed | may set \(N(q)=\{r_1,c_1,p_b\}\) (no new c₃) |

**Open:** kill this tight dual k=4 (C₈ / C₁₆ / handshake overflow on L₄–L₅).

---

## Pure branches (structure only)

| Branch | Star geometry | \|L₃\*\| min |
|--------|---------------|-------------|
| **Pure f** (\(r_1{-}g\), not e′) | star(g)={r₁,u_g}; star(g')={p_a,p_b}; star(e')={z₁,z₂} both ≠r₁ | ≥4 (merges possible) |
| **Pure T2** (no r₁−g) | star(g)={u₁,u₂}; star(g')={u₃,u₄} disjoint; star(e')={r₁,z} | **≥5** (H252) |

---

## What still stands from Fire 22

| Kept | Retracted |
|------|-----------|
| H178 L₃→L₂∪L₄ only | H183 skeleton |
| H154–H156 6-stub census | H202 dual\|L₃\*|=3 kill |
| H141 C₁₆ criterion | H205 “idle verts don’t help H202” |
| H167 no u_g−e′ under dual | |
| H195 C₄ a\*−c₁−q−c₂−a\* | |

---

## Next vector

1. **Kill dual k=4 tight** with L₄–L₅ demand + H245/H247.  
2. **Pure f** as dual-without-r₁−e′ (same stars + free e′).  
3. **Pure T2** at |L₃\*|≥5.  
4. Keep scar `scar:H202_invalid_C4_premise` hot in Engram.

## Property tests
- No graph with a vertex adjacent to both free L₂-nbrs of an L₁ vertex  
- Dual models have disjoint star(g) and star(g′)  
- No dual model with |L₃\*|<4  
