# Blind runs 2026-11-20 · the mirror's re-check

**FILED (the mirror's).** Checked against the transcripts, not against the results file's summary. **This is not an independent re-score:** the mirror also wrote and knew the predictions (V3 applies to it too). The transcripts are in the repo for anyone else to re-score.

## 1 · The blocks were the pack's blocks · verified

Every block was extracted from the transcripts and compared, character for character, with the frozen pack. **9 of 9 match.** The SHA-256 prefixes recorded in the transcripts match hashes computed from the pack. T2's block matches the one given in chat: 27 lines, ending in "The periodic table of the elements."

## 2 · The scorecard · agreed, all 12 rows

Each verdict was read in the reply itself:
- T2 is "ONE VERDICT: LOAD-BEARING" with null line rung 1.
- T3's verdict record reads A AIMED, B HABIT, C IMPRECISION, D HABIT.
- T4-MOUTH and T4-BAT both say "TITLE ONLY".
- T5-SHIFT says "stopped at C1".
- T5-PURR's final answer is "Stop at C1", after an opening line that says C6.

**10 hit, 2 missed.** No kill line fired.

## 3 · What the mirror adds

**A · The missed MOUTH prediction is a defect in Recoherence's verdict menu, not only in the pack.**
- TITLE ONLY currently covers two different results: **homonyms** (BAT: separate words that merged in spelling) and **family resemblance** (MOUTH: meanings radiating from one prototype, the bodily mouth, with no floor that excludes non-members).
- The blind model saw the difference. MOUTH's verdict says the meanings "share more than an accidental spelling", BAT's says they don't, and the menu gave both the same label.
- **That is master question 3 failing inside the tool: two things stated as one.**
- Recoherence's own standing opponent is Wittgenstein's family resemblance. The tool was built to take that result seriously and then gave it no name of its own.
- **Proposed (for JayArr's ruling):** split TITLE ONLY into **TITLE ONLY** (no relation: homonyms) and **FAMILY** (related by extension from a prototype, no exclusive floor).

**B · The missed SHIFT prediction says more about the pack than about Axis Search.**
- The pair set a condition (jet lag) against a symptom with several causes (fatigue). C1 refused it for exactly that reason, which is C1 doing its job.
- What the run does show: the model never tried C1's "both at stated points" form.
- A rerun with "night-shift work" would test the axis instead of the wording (D3).

**C · A slip in T1-S1 that its own "invented" list missed.**
- The original says "an *inappropriate* level of independence", which doesn't say whether there was too much or too little.
- The rewrite says independence "was **below** the level expected", picking a direction. Its nine-row "what had to be invented" table doesn't list the direction.
- So the rewrite step can quietly settle an ambiguity. **Suggested addition to the rewrite step:** list the direction of any deviation as something that had to be invented, unless the original states it.

**D · The rewrite step works, with an open question about confounding.**
- 3 of 3 rewrites came back, against 0 of 6 in Campaign E. The "no comparison named" move survived in all three, and in the transcripts the phrase appears 14 times across the three.
- Campaign E's clean runs used ChatGPT and Gemini, not Claude. So the confound named in the results file is smaller than it suggests: this is still a different run of ChatGPT, but the model family is the same.

## 4 · Standing after this run

| Tool | Before | After |
|---|---|---|
| Five questions + rewrite | Rewrite untested; crowded out 6 of 6 in Campaign E | **Rewrite returned 3 of 3, blind** |
| Sounding | Clean-context run by the mirror only | **LOAD-BEARING on another model, blind** |
| Jargon Breaker | 3 runs, none blind | **4 of 4 verdicts right, blind, including the plain control** |
| Recoherence | Not blind-tested | **Refuses a false theme (BAT); refuses a real family (MOUTH). Verdict menu defect A** |
| Axis Search | 1 run, stopped at C1 | **Refuses a nonsense pair (PURR); refuses a badly paired real axis (SHIFT)** |

**One run, one model, scored by a party that knew the predictions.** Directional.
