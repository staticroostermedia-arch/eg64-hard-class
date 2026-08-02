# Fire 25 — U0/U1 dead on dual k=4; only U2 remains

## Headline

**Dual k=4 tight cannot use L₂ free stubs on \(u_g\).**  
U0 and U1 expand \(|L_3^*|\) or break the budget. Only **U2** (both free of \(u_g\) in L₄) survives — and it is forced into a large exclusive L₅ regime.

---

## Theorem H311 (PROVED) — U0 impossible for dual k=4 tight

**U0:** \(N(u_g)=\{g,\beta_1,\beta_2\}\) with both free in L₂.  
Budget (H256) forces W-L₄ and P₂, so \(L_3^*=\{r_1,u_g,p_a,p_b\}\) is L₂∪L₄–saturated.

Each free L₂-nbr \(\beta_i\) needs two more part-A neighbours:

| Target | Status |
|--------|--------|
| L₁ = {T₂,b,f} | full or creates β=b's free (see below) |
| r₁ | **H307 / H120** — residual C₁₆ |
| p_a, p_b | neighbourhoods full under W-L₄ + P₂ |

**Case β = b's free:** third neighbour must leave L₃\* ⇒ **k≥5**.  
**Case pure exterior L₂:** no L₁ available (f,T₂ full; b ⇒ previous case) ⇒ needs **2 new L₃ each** ⇒ **k≥6**.

**⇒ U0 contradicts k=4.** ∎

---

## Theorem H337 (PROVED) — U1 impossible for dual k=4 tight

**U1:** \(N(u_g)=\{g,\beta,y\}\) with β∈L₂, y∈L₄.  
Budget forces W-L₄+P₂; same saturation; β needs new L₃ ⇒ **k≥5**. ∎

---

## Theorem H338 (PROVED) — dual k=4 tight ⇒ U2 only

Combine H311 + H337: both free stubs of \(u_g\) lie in L₄.
\[
N(u_g)=\{g,y,y'\},\quad y,y'\in L_4\setminus\{q\}.
\]
Budget forces W-L₄ and P₂. ∎

---

## U2 regime (remaining dual k=4)

### With H247 (\(p_b{-}q\))

| Constraint | ID |
|------------|-----|
| a*-bridge: y,y',w ↛ c₂ | H289 |
| sibling L₄s disjoint L₅ | H293 |
| w disjoint L₅ from y,y' | H297 |
| s disjoint L₅ from y,y',w | H299, H322 |
| c₁−s ⇒ C₈ | H315 / H261 |
| \|T\|=2 impossible | H318 |
| \|T\|≥5 (actually ≥6 with s) | H321–H322 |

L₅ must be large and **pairwise exclusive** for \(\{y,y',w,s\}\). Not yet a global contradiction — open microbranch at large |T|.

### Without H247 (\(N(p_b)=\{g',s,s'\}\))

Demand 10 exclusive L₅ slots (H339) — even larger; open.

---

## Pure branches (structure)

| Branch | Stars | \|L₃\*\| min |
|--------|-------|-------------|
| **Pure f** | star(g)={r₁,u_g}; star(g')={p_a,p_b}; star(e')={z₁,z₂}≠r₁ | ≥4 (merges) |
| **Pure T2** | star(g)={u₁,u₂}; star(g')={u₃,u₄}; star(e')={r₁,z} | **≥5** (H252) |

Same C₄ law H215 applies throughout.

---

## Arm A map after Fire 25

```
dual k=4 tight
├─ U0  DEAD (H311)
├─ U1  DEAD (H337)
└─ U2  only — large exclusive L5 (open)
dual k≥5     open (relaxed saturation)
pure f       open
pure T2      open (|L3*|≥5)
```

## Next vector
1. Kill U2 at |T|≥6 (L₆ cascade H330 / C₁₆).  
2. pure f with e′ free star.  
3. pure T2.  
4. dual k≥5 as U2-with-extra-L₃.

## Property tests
- No dual k=4 model with u_g adjacent to an L₂ vertex outside {g}  
- No dual k=4 U0/U1 model  
- U2 models have |L₅ \ {c₁,c₂}| ≥ 5  
