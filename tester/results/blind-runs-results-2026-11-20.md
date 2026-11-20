# Blind runs: five tests · results

**Run 2026-11-19, 18:55–19:18 US Central (2026-11-20 UTC).** The pack (`blind-runs-2026-11-20.md`) is unchanged; deviations and defects are recorded here, as the pack requires. Full transcripts are in `blind-runs-transcripts-2026-11-20.md`.

*Filed 2026-11-20 as returned by JayArr, unedited. Written by the Claude session that carried the blocks. The mirror's independent re-check is in `blind-runs-recheck-2026-11-20.md`.*

## Headline

- **10 of 12 sealed predictions hit.** No kill line fired.
- **Both misses go the same way.** On the two known-positive controls, MOUTH and SHIFT, the blind model returned the null result: TITLE ONLY and a C1 stop. The mirror expected it to find something.
- **The kill lines only watch for over-generation** (themes manufactured, axes for anything, opacity found in plain English). None of them would catch a tool that refuses true positives, and that is the failure this run turned up. See defect D1.

---

## 1 · Scorecard against §7

| Test | Sealed prediction | Conf | Result | Score |
|---|---|---|---|---|
| T1 | A rewrite comes back in 3 of 3 | 80 | 3 of 3 | **Hit** |
| T1 | "No comparison named" survives in 3 of 3 | 80 | 3 of 3, used verbatim in each table | **Hit** |
| T1 | At least one rewrite says what had to be invented | 60 | 3 of 3 | **Hit** |
| T2 | LOAD-BEARING on the periodic table | 70 | LOAD-BEARING; floor at rung 6; null line: rung 1 | **Hit** |
| T3 | A AIMED | 70 | AIMED | **Hit** |
| T3 | B HABIT | 60 | HABIT (see D5) | **Hit** |
| T3 | C IMPRECISION | 55 | IMPRECISION | **Hit** |
| T3 | D HABIT, most operations null | 75 | HABIT; but only ops 1 and 3 named null (plus "no substantial vagueness"), with 7 rows in the "fired" table | **Hit on verdict; miss on the qualifier** |
| T4 | MOUTH THEME FOUND | 75 | **TITLE ONLY** | **Miss** |
| T4 | BAT TITLE ONLY | 80 | TITLE ONLY | **Hit** |
| T5 | SHIFT reaches at least C5 | 60 | **Stopped at C1** | **Miss** |
| T5 | PURR stops at C1 or C2 | 85 | Final answer: stop at C1. The reply opens "Stop: C6 fails" and then withdraws it (see D6) | **Hit, with a caveat** |

**Calibration:** the mean stated confidence was 71; the hit rate was 10 of 12 (83%). The two misses were stated at 75 and 60.

### Kill lines

| Kill line | Triggered? |
|---|---|
| T1: no rewrite in 2+ of 3 | No (3 of 3 rewrites) |
| T2: anything but LOAD-BEARING | No |
| T3: D comes back AIMED or IMPRECISION | No (HABIT) |
| T4: BAT comes back THEME FOUND | No (TITLE ONLY) |
| T5: PURR passes all six | No (final stop at C1) |

---

## 2 · Per test

### T1 · The rewrite

| | Rewrite present | Names a unit and a comparison | Says what was invented | "No comparison named" survives |
|---|---|---|---|---|
| S1 | yes | yes, **as placeholders** ("[specified standard]", "[specified assessor]") | yes, a 9-row table | yes |
| S2 | yes | yes; the comparison is invented ("priorities … specified in the task instructions") | yes, an 8-row table | yes |
| S3 | yes | yes; the unit is relocated to the writer ("as assessed against the writer's expectations") | yes, 7 numbered items | yes |

Adding "then rewrite it" brought the fix back in every chat. The three rewrites solve the gap differently: S1 leaves slots, S2 fills them with plausible inventions, and S3 moves the judgement onto the writer's own experience. Only S1 refuses to invent. **Confound:** this is a different model from Campaign E (if E ran on Claude), so model and added step move together. The result supports the step but doesn't isolate it.

### T2 · The Sounding

LOAD-BEARING, with the floor at rung 6 (nuclear charge → electronic structure → chemical behaviour). The test one rung below collapses to "matter has properties that can be classified", which rules nothing out. The reply ran the vocabulary count as instructed (8 terms, "a count of the selected classification vocabulary"). The null line is rung 1: the name is descriptive. The reply carries no web citations, so it obeyed the no-tools line.

### T3 · The Jargon Breaker

All four verdicts match. Two caveats:
- **D's operations were not mostly null.** The fired table has 7 rows for D, including one labelled "Passive voice operation finds nothing". The model put non-findings into the fired table here and in B (op 1) and C (op 1). See D4.
- **B's reasoning cuts against its verdict.** It says the plain version "is more uncomfortable because it exposes the absence of evidence", which is the AIMED test, then rules HABIT because nothing concealed is revealed. See D5.

### T4 · Recoherence

- **MOUTH: TITLE ONLY (miss).** The model listed 25 senses, not the pack's 4: they include speech, backtalk, grimace, spokesman and eight verb senses (one is fitting a horse to the bit). Its own tally miscounts openings as 8 and verbs as 7, though the total of 25 is right. Its floor ("an interface through which something is taken in, let out, or expressed") failed the exclusion test on a nostril, a drain and a microphone. It rejected "oral interface" as circular, because it imports the prototype. Step 5 then *did* state a theme ("the human or animal mouth, and things understood through their resemblance or association with it") but classed it as a prototype rather than a floor. The verdict text says the meanings "share more than an accidental spelling", which the TITLE ONLY definition says they don't.
- **BAT: TITLE ONLY (hit).** 17 senses. It identified separate etymological families for the animal, the club and the eyelid verb. Its inclusive floor ("a conventional name for some kind of thing…") failed on chair, running and anger.
- Both chats **used web search** (dictionary citation chips appear in the text) and **reasoning mode** ("Worked for 15s" / "12s"). The T4 block doesn't forbid tools.

### T5 · Axis Search

- **SHIFT: stopped at C1 (miss).** It named circadian misalignment ("generated, unconfirmed") and placed jet lag high. It would not place *night-shift fatigue* on the same axis without hedging, because that fatigue also comes from short sleep and workload. It never considered the "both at stated points" form of C1. See D3.
- **PURR: stopped at C1 (hit, with a caveat).** It built a real pre-existing dimension (inverse time: Hz versus %/year) and passed C1, reached C2, then withdrew the C1 pass on the grounds that an interest rate's dimension is disputed. Its first line says "Stop: C6 fails", which contradicts the rest of the reply. It used web search and reasoning mode ("Worked for 16s").

---

## 3 · Deviations from §0

| # | Deviation | Effect |
|---|---|---|
| V1 | **ChatGPT signed out, not a Temporary Chat.** You approved this before the first run. With no account there is no memory, no project and no history, but OpenAI's terms let it use the chats for training. | Rule 0's intent (no carry-over between blocks) held. The letter ("Temporary Chat") did not. |
| V2 | **The model is unknown and may have varied.** Signed-out ChatGPT shows no model name. Three chats show "Worked for Ns" (T4-MOUTH, T4-BAT, T5-PURR), so some were routed to a reasoning mode and others weren't. | Treat "the blind model" as "signed-out ChatGPT on 2026-11-19", not one fixed model. |
| V3 | **The courier was Claude, which had read the sealed predictions.** The blocks were pasted programmatically from the pack text. Each pasted message was checked by SHA-256 against the pack before sending, and again as received in the chat. Nothing else was typed, and no chat asked a question, so "use your judgement" was never needed. | The courier had no channel to the model beyond the verified block. Scoring is by the same party that knew the predictions; the transcripts are there for an independent re-score. |
| V4 | **The T2 block came from you in chat,** not straight from `sounding-run-pack.md` §2. Its trailing blank line was dropped by ChatGPT on send. | None, as long as your paste matched §2. |
| V5 | **T1-S1 was collected after an interruption.** You stopped my wait while the reply was streaming. When I collected it the reply was complete (it ends in the rewrite and the "invented" table), and nothing was re-sent. | None found. |
| V6 | **Web search was used** in T4-MOUTH, T4-BAT and T5-PURR. | It's allowed by those blocks, but it's a difference from runs where the model works from memory. |
| V7 | **Transcript format.** Each reply was taken from the page DOM as markdown (headings, lists, tables, quotes). Citation chips survive only as plain text (e.g. "Dictionary.com+2"). "Worked for Ns" and ChatGPT's "Writing" block label are kept as they appeared. The math in T5-PURR appears as rendered three times ("T−1T^{-1}T−1"). | Content is complete; some visual formatting is lost. |

No void condition in §0 was hit: no project, no memory, no edited block, and no chat that had seen another block.

---

## 4 · Defects in the pack (frozen; recorded here)

- **D1 · No kill line for false negatives.** All five kill lines test whether a tool *over-finds*. MOUTH and SHIFT were the positive controls, and both came back null, which no kill line covers. Suggested addition for next time: "MOUTH comes back TITLE ONLY → Recoherence can't find radial themes", and "SHIFT stops before C3 → Axis Search's C1 is too strict for real axes".
- **D2 · T4 doesn't fix the meaning set, and its verdicts have no slot for a radial family.** The pack lists four senses of *mouth*, but the block never names them, so the model brought 25. The three verdicts force a choice between an exclusive floor and "no theme". The model's own text ("more than an accidental spelling") wanted a middle verdict: *related by extension from one prototype, with no exclusive floor.*
- **D3 · T5-SHIFT pairs a condition with a symptom.** "Jet lag" names the misalignment itself; "fatigue in people working night shifts" names an outcome with several causes. C1 failed on exactly that asymmetry. "Night-shift work" or "shift-work disorder" would test the axis rather than the wording.
- **D4 · T3's output format lets null operations into the fired table.** That blurs the null count the D prediction depends on. Requiring "fired table: findings only" would make "most operations null" scoreable.
- **D5 · T3's AIMED test leaves open what kind of discomfort counts.** B's plain version was "more uncomfortable" (it exposes missing evidence) but was ruled HABIT (nothing concealed). The rubric should say whether discomfort from exposed emptiness counts, or only discomfort from a revealed actor, victim or decision.
- **D6 · T5 takes the first-line answer at face value.** PURR's opening line ("Stop: C6 fails") contradicts its final answer (stop at C1). The scoring rule should say which one counts. I scored the final one.

---

## 5 · What this run says, briefly

On this model the tools are **conservative**: they refuse false positives cleanly (BAT, PURR, Passage D) and also refuse two true positives (MOUTH, SHIFT). The T1 rewrite step works across 3 of 3 sentences. The Sounding returns LOAD-BEARING on a known load-bearing system. The open question this run raises is not "do the tools manufacture findings?", which none did, but "is the exclusion bar set where real themes and axes can clear it?" A rerun of MOUTH and SHIFT with D2 and D3 fixed would answer that directly.
