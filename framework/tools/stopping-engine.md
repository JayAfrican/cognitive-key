<!-- Canonical tool file. The procedure below is the operative version, copied unchanged from the installed skill on 2026-11-17. Edit here first; the skill is rebuilt from this file (Rule 4). -->

> **Tool:** stopping-engine · **For:** A claim: "studies show", a headline, a health or neuroscience claim
>
> **Test record:** **Blind-tested:** Campaigns B, B retest and C (CORROBORATED). **Logged runs:** 5 (2026-10-24 ×2, 2026-10-30 ×3).
>
> **Custody:** The name is RULED (his). The rest of the procedure is the mirror's: 19 FILED and 2 MIXED items at the 2026-10-01 custody pass. **issue-03:** the older document cites a calibration set and a run its own "missing" section says don't exist.
>
> **Status of this file:** **RULED 2026-11-17 as his tool** ("Rule all six as my tools"). Each step stays open to correction when a test says so.

---

# The Stopping Engine

**A brake, not an oracle.** It can't say a claim is true. It says where a claim stops being supported and names the step where it stopped. The output is always "here is the procedure, here is where it halted", never "here is the truth".

**Test record:** blind calibration, Campaigns B, B retest and C. Roughly 14% verdict instability across repeated runs of the same item. **Prompt v2 asks for numeric confidence, so give one.**

**Claims, never people.** No verdict about a claimant's honesty, competence or motives without the intent ladder (`references/intent-ladder.md`).

## Running order: cheap first, stop at the first decisive failure, name the step

| # | Step | Halts on → verdict |
|---|---|---|
| 1 | **Is it falsifiable?** What observation would make it false? | Nothing would → **NOT EVEN WRONG** |
| 2 | **What exactly is claimed?** Define every term. Is a word doing two jobs? | Two referents under one word → restate, or halt *(steelman rule below)* |
| 3 | **Source check.** Does the source say what the sentence says? How many hops to primary data? Is any agreement contaminated? | Source doesn't support the sentence → **UNSUPPORTED** (or **CONTAMINATED** if the sourcing carries no weight) |
| 4 | **Level check.** Is the link only title-level: a shared word, no shared referent? | → **NOT EVEN WRONG** |
| 5 | **Detectable vs effective.** Is measurability standing in for efficacy? State both thresholds in the same units | → **OVERSTATED** |
| 6 | **Effect size.** Is a magnitude reported? Would a person notice it? Precision, replication, single-study rule. Say the number, never "significant" | No magnitude, or trivial, or one unreplicated study carrying a general claim → **OVERSTATED** |
| 7 | **Causal inference.** Design, direction (could B cause A?), a nameable confounder, selection and collider effects | Observational design stated causally with an unaddressed confounder → **UNSUPPORTED** |
| 8 | **Mechanism.** Is one proposed? List what would have to be true as numbered conditions; check each against hard constraints | A condition fails on physics no future instrument changes → **REFUTED** (nameable missing piece → shelved, not refuted) |
| 9 | **Inversion**, if the claim rests on an opposition | False dichotomy → restate (hand to **cross-pollination-intake**) |
| 10 | **Novelty**, if newness is claimed | Prior art exists → strike the novelty, keep the claim |

**Steps 1–5 dispose of most claims.** Don't spend steps 6–8 on something that halts at step 2. Module detail for steps 3 and 5–8 is in `references/modules.md`.

### Continuing past a halt
A halt at a **warrant** step (3) doesn't end the run if the **world** question is still answerable. Continue, report the most decisive verdict, and list the earlier halts in order: *"REFUTED at 8; contaminated at 3 and overstated at 5 on the way."*

### The steelman rule at step 2
If the claim can be restated in a strongest specific form that keeps what the claimant plainly means, **restate it and proceed.** Halt at step 2 only when the term has no checkable referent at all. **A cheap halt is not a result; it is an avoided analysis.**

## Verdicts (screen vocabulary; never mix with the others)

| Verdict | Means |
|---|---|
| **SUPPORTED** | Backed by evidence proportionate to the claim. Expected to be rare |
| **OVERSTATED** | A real finding inflated in scope, size or certainty. **The most useful category** |
| **UNSUPPORTED** | No adequate evidence either way. Not the same as false |
| **REFUTED** | Evidence against, or a necessary condition fails on grounds no instrument changes |
| **NOT EVEN WRONG** | Unfalsifiable, or malformed: a title-level match, or a term with no fixed referent |
| **CONTAMINATED** | The claim may be fine; the sourcing carries no evidential weight. **A verdict about the warrant, not the world**, and it must be said that way |

**Every verdict names its step.** "OVERSTATED at step 6." A verdict without a step is inadmissible.

## Harm tier: mandatory for anything health-adjacent

- **H0:** no action implied → ordinary output.
- **H1:** a benign behaviour change → ordinary output; "no evidence" ≠ "harmful".
- **H2:** replacing or delaying care, or a physiological intervention → state the risk explicitly. **Evaluate the claim, never recommend.** Direct to a clinician.
- **H3:** minors, acute mental-health content, or documented adverse events → **halt. No verdict without a clinician reading it.**

## Close

Plain answer first (one or two sentences) → verdict with step → harm tier → one falsifier → run `log-run` with `tool: stopping-engine`, `verdict.vocabulary: screen`.
