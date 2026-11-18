<!-- Canonical tool file. The procedure below is the operative version, copied unchanged from the installed skill on 2026-11-17. Edit here first; the skill is rebuilt from this file (Rule 4). -->

> **Tool:** five-questions · **For:** A sentence about a person: a label, a judgement, a report line
>
> **Test record:** **Blind-tested:** Campaign E, two clean runs on two models: a partial pass (10 of 30), with question 2 carrying it (CORROBORATED). **Logged runs:** 2. **Open:** the person test (Two Sentences).
>
> **Custody:** The five questions are RULED (2026-09-25), and so is the rewrite step (2026-10-03). This file is the procedure that runs them, written by the mirror.
>
> **Status of this file:** **RULED 2026-11-17 as his tool** ("Rule all six as my tools"). Each step stays open to correction when a test says so.

---

# The Five Questions

**The frame is five questions. The Octave is the container that teaches them.** *(RULED, JayArr, 2026-09-25.)* The frame is made of questions, not claims, so it can't be refuted, only found useless. Its test is whether asking the five produces anything a capable reader wouldn't get without them.

**Test record:** Campaign E, two clean blind runs on two models. Frame beat plain on **10 of 30** cells, a partial pass. **Q2 carried it (5 of 6). Q1 and Q5 added nothing measurable (0 of 6).** The frame **crowded out the rewrite in 6 of 6.** So: **ask Q2 first, and always finish with the rewrite.** *(This order is the build plan's design rule 5, FILED; the book's order is a separate, deferred question.)*

## Input

One sentence written or said about a person. If it's longer, take the single sentence carrying the most weight and say which you took.

**Privacy:** the person described must be JayArr, someone who has consented, or a sentence with no identifiable subject. Otherwise stop (see `process-this`).

## The run, in this order

**Q2 · Where is the ruler?** For each judgement word: what was it measured against, by whom, over what period, on what record? Was the comparator declared? If nothing is named, say "no ruler named", which is itself the main finding.

**Q1 · Name the unit.** For each claim: what is it a property of? The person, a moment, a setting, a relationship, the task, or the writer? A word that slides between units is doing two jobs; say which two.

**Q3 · How many things are there?** How many separate things is the sentence describing? Is any of them two things stated as one, or one thing stated as two? Can it be told from inside the sentence, or would it take a case the writer didn't see?

**Q4 · What does the step cost?** What does each behaviour described cost the person doing it, and what does writing it down this way cost them? What would it cost the writer to be wrong?

**Q5 · Who holds the pen, and who pays for the error?** Who wrote it, who reads it, who acts on it, and who bears the consequences if it's wrong? Can the person described answer it?

## Then: the Jargon Breaker on the words

Hand the sentence to the **jargon-breaker** skill for its posited plain reading of each opaque term, with a verdict of HABIT / IMPRECISION / AIMED about the language, never about the speaker. **Jargon Breaker test record: UNTESTED.** Label its output as a candidate.

## Then: the rewrite (never skip)

Rewrite the sentence so that every judgement **names its unit and its ruler**, keeping what the writer plausibly meant (the steelman rule). Format:

- **Original:** the sentence as given.
- **Rewrite:** one or two sentences.
- **What had to be invented to write it:** anything the rewrite needed that the original didn't supply. If the rewrite can only be written by inventing the ruler, say so. That is the finding.

**Rewrite test record: UNTESTED.** It's the move the frame crowded out in Campaign E, which is why it's mandatory here.

## Close

- **Plain answer:** one or two sentences on what the five questions found that a plain read wouldn't.
- **The honest null:** if the questions added nothing beyond a plain read, say so. That's the frame's falsifier firing, and it gets logged like any other result.
- Then run `log-run` with `tool: five-questions`. The Jargon Breaker part is logged as its own run record with `tool: jargon-breaker`, linked to this one with `derived_from`.
