# Erdős–Gyárfás (Erdős #64) — Campaign status

**Full conjecture:** OPEN.  
**Detailed proof draft:** `PROOF_H4_draft.md`

---

## Unconditional theorems

### Theorem E
Every connected **cubic bipartite** graph on **n ≤ 24** satisfies EG.  
(Exhaustive `genbg -d3 -D3`: 56 025 graphs at n=24, 0 failures.)

### Theorem A′
Every cubic **arc-transitive** Foster CAT graph on **n ≤ 150** satisfies EG.

### Theorem H1 (path–cycle lemma) — proved
Cubic bipartite, girth 6, C6 with consecutive thirds tᵢ, tᵢ₊₁:  
a path of length **d** in H = G−V(C) between them yields a cycle of length **d+3**.  
Hence **d=5 ⇒ C₈**, **d=13 ⇒ C₁₆**.

### Theorem H5 — proved
If G is C₈-free then H has **no** simple length-5 path between consecutive thirds.

### Theorem H_struct — proved
H has exactly six degree-2 vertices (the thirds) and the rest degree 3;  
|E(H)| = 3(n−8)/2. (Verified: deg2 set = thirds; biconnected on all CAT samples.)

### Theorem B′ — computational
All C₄-free C₈-free Foster CAT graphs checked have C₁₆, via explicit 13-paths on **every** C6.

---

## Conditional main theorem (Fire 4)

**Theorem 5.** If Claims B and C hold, then every cubic bipartite girth-6 C₈-free graph
with n ≥ 24 has a C₁₆ (hence satisfies EG).

| Claim | Statement | Status |
|-------|-----------|--------|
| **B** | dist_H(tᵢ,tᵢ₊₁) = 3 always (girth 6) | Verified universally in tests; proof sketch only |
| **C** | Path lengths = all odds in [3,L] except 5; L≥13 for n≥24 | Verified on all C₈-free CAT; C₃ fills spectrum, C₄ bound L |
| **A** | H is 2-connected | Verified on all CAT samples |

**Path spectrum (C₈-free CAT):**  
`S = {3, 7, 9, 11, 13, 15, …, L}` — **only 5 missing**, and 5 is exactly forbidden by H5.

---

## Proof architecture

```text
girth 6 cubic bipartite C8-free, n≥24
    │
    ├─ H1: d-path in H between consec thirds ⇒ (d+3)-cycle
    ├─ H5: no 5-path (else C8)
    ├─ Claim B: shortest path length = 3
    ├─ Claim C: S ⊇ {3,7,9,11,13}   (all odds ≤13 except 5)
    │
    └─⇒ 13-path exists ⇒ C16 ⇒ EG
```

---

## Next vector (strict)
1. Prove Claim B (configuration at depth 3).  
2. Prove Claim C (ear decomposition / path lengthening by +2 in almost-cubic bipartite H).  
3. Girth 10/12/14 parallel lifts.

## Engram tiles
`tile:eg64_theorem_E_genbg_n24`, `tile:eg64_theorem_H_path_cycle`,  
`tile:eg64_theorem_H_struct`, `tile:eg64_open_lemma_c16_forcing` (refined to Claims B,C)

---

## Fire 4 update — C₁₂-ear reduction

See **[PROOF_H4_C16_forcing.md](PROOF_H4_C16_forcing.md)** for the full writeup.

**Headline:** C₁₆-forcing for girth-6 C₈-free cubic bipartite graphs reduces to:
1. external distance 3 between consecutive thirds, and  
2. a C₁₂ through the middle edge of a length-3 path in H = G−V(C).

Both verified on all Foster CAT hard examples; Moore bound proves (1) for n≤34.

---

## Fire 5 — Theorem H9 (PROVED)

**C₆ + C₁₂ sharing one edge (and only its endpoints) ⇒ C₁₆.**

Hard bipartite class reduced to: *every edge of a 3-connected cubic bipartite graph lies on a C₁₂* (Open H11).  
Verified for all 3-conn cubic bipartite n≤20 (genbg) and all hard Foster CAT C₆-edges.

Full writeup: [PROOF_H4_C16_forcing.md](PROOF_H4_C16_forcing.md)

---

## Fire 6 — H11 refined + case split

- **H11′:** every edge on C₁₂ only claimed for **girth ≤ 12** (girth ≥ 14 has no C₁₂).
- **L1–L2 proved:** C₈-free ⇒ local girth ∈ {6} ∪ {≥10}.
- Full **case split** for cubic bipartite EG in [PROOF_H11_and_case_split.md](PROOF_H11_and_case_split.md).
- Hard class still: Claim A (edge on C₆) + Claim B (exclusive C₁₂) + H9.

---

## Fire 7 — Moore + Claim A

- **M10 proved:** cubic bipartite girth ≥ 10 ⇒ n ≥ 62; local girth ≥ 10 on an edge ⇒ n ≥ 62 (tree balls).
- **Claim A** (every edge on C₆ in girth-6 C₈-free): holds on all known examples; follows from M10′ for n<62 in the girth≥10 regime.
- **Girth-10 CAT:** all have **C₁₆** (EG verified).
- Middle edge of third 3-path always has local girth 6 (structural).
- Details: [PROOF_claimA_moore_fire7.md](PROOF_claimA_moore_fire7.md)

---

## Fire 8 — Single gate H16

**Theorem H13 (PROVED):** path of length 9 between consecutive thirds in \(H=G-V(C)\)
⇒ exclusive C₁₂ on the C-edge ⇒ **C₁₆** by H9.

**Open H16:** that length-9 path always exists (100% verified; port geometry uniform:
unique bridge a₁b₁, dist(a₁,b₂) in H−{s,t} = 5, path a₁–b₂ of length 7).

Details: [PROOF_H11b_path9_fire8.md](PROOF_H11b_path9_fire8.md)

---

## Fire 9 — H17 + constructive H18

- **H17 PROVED:** no *s–t* path of length 1 or 5 ⇒ dist_H ∈ {3,7,9,…} in C₄/C₈-free graphs.
- **H18 PROVED:** config C* (second C₆ + dist(y,b₂)=3) ⇒ path length 9 ⇒ C₁₆.
- Construction succeeds on **all** tested hard CAT (explicit C₁₆ in hand).
- **H16 open pin:** prove dist_H = 3 and C*.

[PROOF_H16_fire9.md](PROOF_H16_fire9.md)

---

## Fire 10 — dist_H = 3 structure

- **H19:** dist_H=3 ⇔ H-bridge (proved)
- **H22:** dist_{G−v₀}(s,v₁) ∈ {4,8,10,…} (no 2, no 6 — proved)
- **H24:** A2 with portal third ⇒ C₈ (proved)
- Census: unique path₄ is always **A1** (bridge)
- n<62: local girth 6 (H26)
- [PROOF_dist3_fire10.md](PROOF_dist3_fire10.md)

---

## Fire 11 — **H31: hard-class EG for n < 62**

- **H28:** dist(x,y) ∈ {3,7,…} in G−{a₁,b₁} (proved: no 1, no 5).
- **H29:** dist=3 ⇒ C* free of s,t (proved).
- **H27:** A2 ⇒ C₈ or H-bridge (main cases proved).
- **H31:** cubic bipartite girth-6 C₈-free **n<62 ⇒ C₁₆ ⇒ EG** (proved).
- [PROOF_Cstar_A2_fire11.md](PROOF_Cstar_A2_fire11.md)

---

## Fire 12 — Walk formula

- **H32:** exactly **7** through-walks s→v₁ via v₀ (proved by enumeration)
- **H33–H34:** dist_{G−v₀}(s,v₁)=4 **⟺ k≥2** where k=|L₂(s)∩L₂(v₁)|
- **P(k):** k≥2 on girth-6 C₈-free — the single pin for unlimited-n hard EG
- [PROOF_walks_fire12.md](PROOF_walks_fire12.md)

---

## Fire 13 — P(k) attack

- **H36:** dist_{G−v}(x,y) ∈ {4,8,…} under C₄/C₈-free (**proved**)
- **H38:** ζ=v₄ mixed case killed (**proved**)
- Residual: ζ=T₅ ⇒ induced P₇ of length 6
- Census: **0** bad pairs on all C₈-free graphs checked
- [PROOF_Pk_fire13.md](PROOF_Pk_fire13.md)

---

## Fire 14 — C₁₆ fork

- **H39:** pendant edge calculus; T₂ isolated; w−t is C₈
- **H40:** under bad, dist(a\*,t) ≥ 6
- **H41:** residual bad ⇒ **C₁₆** (two len-8 paths) **or** double-stretch
- [PROOF_P7_fire14.md](PROOF_P7_fire14.md)

---

## Fire 15 — Double-stretch reduction

- **H42:** T₂–T₅ ⇒ explicit **C₈** (proved)
- **H43:** path₄(v₁,T₂) ⇔ E–Bset under residual bad
- **H44:** E–Bset ⇒ dist_{G''}(t,T₂)=3; double-stretch ⇒ dist(a\*,e)≥6
- [PROOF_double_stretch_fire15.md](PROOF_double_stretch_fire15.md)

---

## Fire 16 — Arm structure

- **H46:** Arm B edge massacre; **|F|=4** exact
- **H47:** Arm B ⇒ B1 (n>62) or B2 (T₃ path₄ + Z)
- **H48:** Arm A geodesic forms (q₅ ∈ {T₂,f})
- [PROOF_arms_fire16.md](PROOF_arms_fire16.md)

---

## Fire 17 — C₈ massacre

- **H50:** f−v₄, f−T₃ are C₈ under E–Bset; f−t is C₄
- **H52:** dist(a\*,e)≤4 ⇒ C₁₆ (Arm A threshold)
- **H53:** Arm B QB ∩ QF = ∅
- [PROOF_C8_fire17.md](PROOF_C8_fire17.md)

---

## Fire 18 — L2-block

- **H55:** c ↛ L2(e) without C₁₆
- **H56:** s−T₃ is path₄ (residual-only)
- **H59:** {c₁,c₂,s} outside B(e,3)
- **H58/H60:** L1 full; L2 dumps 6–8 stubs to L3+
- [PROOF_L2block_fire18.md](PROOF_L2block_fire18.md)

---

## Fire 19 — H70

- **H65:** length-6 a\*–e geodesic has p₂∈L₄
- **H70:** cannot end with b−e (swap to t ⇒ dist(a\*,t)≤6 ⇒ C₁₆)
- Remaining: p₅∈{f,T₂} only
- [PROOF_L3L4_fire19.md](PROOF_L3L4_fire19.md)
- **GitHub:** https://github.com/staticroostermedia-arch/eg64-hard-class


---

## Fire 20 — u_g C₈ + layer law

- **H105–H109:** u_g cannot meet v0,v2,v4,T3,δ,e,t,q (explicit C₈/path₆)
- **H115:** under DS, a\* ∈ L₆(e), c ∈ L₅, q ∈ L₄
- **H89/H90:** s−g path₆, c−g path₄
- [PROOF_ug_fire20.md](PROOF_ug_fire20.md)


---

## Fire 21 — endgame structure

- **H125:** u_g ∈ L₃(e) (layer adjacency)
- **H120:** no r₁−β (H70)
- **H141:** C₁₆ ⇔ length-8 s–v₁ path interior-disjoint from P₈
- **H133:** pure T2 ⇒ r₁ third stub in L₄
- **H140:** b₂ refuses {e′,g₁,g₂} stubs
- **H149:** e′-third ≠ s,a\*
- [PROOF_endgame_fire21.md](PROOF_endgame_fire21.md)


---

## Fire 22 — handshake / dual kill

- **H178:** L₃ ⊆ neighbors in L₂∪L₄ only
- **H154–H156:** 6 critical stubs → L₃\*, |L₃\*|≥3
- **H183–H189:** dual |L₃\*|=3 skeleton (r₁,u_g,z)/(q,y,w)
- **H202:** dual |L₃\*|=3 ⇒ explicit C₈ family — **DEAD**
- [PROOF_handshake_fire22.md](PROOF_handshake_fire22.md)


---

## Fire 23 — C₄ law; H202 scar; dual rebuild

- **SCAR:** H183/H202 retracted — skeleton had C₄ g−f−g′−u_g−g
- **H215/H222:** fundamental C₄ law (no vertex meets both L₂ children of one L₁)
- **H216:** dual ⇒ \|L₃\*\|≥4, disjoint stars for g and g′
- Dual k=4 tight config + H227/H228/H240/H241/H245 forbids
- [PROOF_c4law_fire23.md](PROOF_c4law_fire23.md)


---

## Fire 24 — a*-bridge; dual k=4 partial collapse

- **H289:** a*-bridge C₈ — L₄ nbrs of u_g/p_a cannot meet c₂
- **H261/H267:** U0a main c₁/c₂ branches dead
- **H293/H297/H299:** L₅ exclusivity C₈s for U2
- [PROOF_bridge_fire24.md](PROOF_bridge_fire24.md)


---

## Fire 25 — U0/U1 dead; U2 only on dual k=4

- **H311:** U0 impossible (L₂ frees of u_g expand L₃\*)
- **H337:** U1 impossible (same)
- **H338:** dual k=4 tight ⇒ **U2 only**
- U2 forced into \|T\|≥5 exclusive L₅ regime
- [PROOF_U0dead_fire25.md](PROOF_U0dead_fire25.md)


---

## Fire 26 — H247/U2a dead by C₈

- **H363:** dual + p_b−q ⇒ C₈ e−T₂−e′−r₁−q−p_b−g′−f−e (**U2a dead**)
- **H369:** dual k=4 U2 ⇒ U2b only
- **H368:** pure f cannot set N(e′)⊇{p_a,p_b} (C₄)
- Core-graph cycle search as property test
- [PROOF_H247dead_fire26.md](PROOF_H247dead_fire26.md)


---

## Fire 27 — U2b forbids; pure-f C₈

- H371/H375/H384/H387/H391 U2b constraints
- H399 pure f forbids s−c₁
- H390 main pattern c₁−y + c₂−s survives (boxed)
- [PROOF_U2b_fire27.md](PROOF_U2b_fire27.md) · [verify_fire27.py](verify_fire27.py)


---

## Fire 28 — L₆-bridge map; H390 still open (honest)

- H413: complete L₆-bridge C₈/C₄ classification under H390
- H404: τ↛σ; τ↛w-L₅; τ↛y′-L₅
- H424: **private L₆ completion is C₄/C₈-free** — kill needs cascade/C₁₆
- [PROOF_L6bridge_fire28.md](PROOF_L6bridge_fire28.md) · [verify_fire28.py](verify_fire28.py)


---

## Fire 29 — PF4 pure-f; H390 cascade cover exists (honest)

- H430: free L₆ cover under H413 **exists** (no cascade kill)
- H435–H439: residual length-10 chords forbidden
- **PF4**: pure f k=4 with N(e′)={T₂,p_a,u_g}
- H453–H455: PF4 forbids x−c₁ (C₄), y−c₂ (C₈), y−c₁+w−c₂ (C₈)
- [PROOF_PF4_fire29.md](PROOF_PF4_fire29.md) · [verify_fire29.py](verify_fire29.py)


---

## Fire 30 — ★ BREAKTHROUGH: Arm A dead (H470)

**What was stopping us:** dual analyzed without residual P₈.

**H470:** residual bad + E–Bset + dist(a\*,e)=6 geodesic ⇒ **C₁₆**  
(both f-ending and T₂-ending). Machine-checked; C₄=C₈=0 on core.

**Corollaries:** dual, pure f, pure T2, H390 all die under Arm A.  
**Arm A branch empty.** Remaining open: **Arm B only**.

- [PROOF_ArmA_dead_fire30.md](PROOF_ArmA_dead_fire30.md)
- [verify_fire30.py](verify_fire30.py)


---

## Fire 31 — Arm B locked; B2 C₁₆ criterion H490

- Arm A empty (H470); focus Arm B
- H475–H493: T₃/F forbids; T₃−c ⇒ C₈
- **H490:** dist(a\*,f₁)=5 ⇒ **C₁₆** (B2)
- **H491:** dist(a\*,f₁)∈{3,5,7}; open pins dist=3,7 exterior
- B1: n>62; C₁₆ still open
- [PROOF_ArmB_fire31.md](PROOF_ArmB_fire31.md) · [verify_fire31.py](verify_fire31.py)


---

## Fire 32 — ★ B2 DEAD (H555)

- **H553:** 3-connected ⇒ three a\*–f₁ paths enter via e₁, T₃, y
- **H547 / H541:** length-7 y-path or 7+9 disjoint ⇒ C₁₆
- **H546:** dist=7 ⇒ C₁₆; **H550:** dist=3 ⇒ C₁₆
- **H555: B2 empty.** Only **B1** remains in double-stretch.
- [PROOF_B2dead_fire32.md](PROOF_B2dead_fire32.md) · [verify_fire32.py](verify_fire32.py)


---

## Fire 33 — ★★ B1 DEAD; double-stretch empty; hard-class EG (H580)

- **H577:** B1 empty (Menger free-gates; H566/H571/H572)
- **H578:** double-stretch empty (A+B2+B1)
- **H579:** residual bad ⇒ C₁₆
- **H580:** hard-class EG (bipartite cubic C₄/C₈-free) — campaign claim
- [PROOF_B1dead_fire33.md](PROOF_B1dead_fire33.md) · [PROOF_hard_class_status.md](PROOF_hard_class_status.md)


---

## Fire 34 — Master theorem H590 + connectivity patch H581/H582

- Linear proof: [PROOF_MASTER_hard_class.md](PROOF_MASTER_hard_class.md)
- H581: cubic κ=λ; H582: hard class 3-connected or already C16
- Full EG#64 still open (double-cover projection scar)
- `verify_fire34.py` chains 30/32/33 + connectivity
