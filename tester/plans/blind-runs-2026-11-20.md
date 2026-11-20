# Blind runs: five tests · run pack

**Tester layer. Written 2026-11-20, before any run.** The mirror's predictions are sealed in the Ledger (`pred-br-*`) and in §7. **The pack is frozen once the first block is pasted:** defects go in the results file, not here.

| Test | Tests | Chats |
|---|---|---|
| **T1 · The rewrite** | Does adding "then rewrite it" bring back the fix that the five questions crowded out in Campaign E (6 of 6)? | 3 |
| **T2 · The Sounding, another model** | Does a different model reach LOAD-BEARING on the periodic table, as the mirror's clean run did? | 1 (+1 optional) |
| **T3 · The Jargon Breaker, blind** | Does it sort four passages into the right verdicts, including a plain control? | 1 |
| **T4 · Recoherence, known answers** | Does it find a theme where one exists ("mouth") and refuse one where it doesn't ("bat")? | 2 |
| **T5 · Axis Search, known answers** | Does it find an axis where one exists (jet lag / night-shift fatigue) and refuse a nonsense pair? | 2 |

**About 9 chats, 5–10 minutes each.**

---

## 0 · Rules (constraint 12; Campaign E §0)

- **Use a model that isn't me:** ChatGPT in a **Temporary Chat**, or Gemini with **Gemini Apps Activity off**. If you use Claude, use an incognito chat with **no project and memory off**.
- **One fresh chat per block.** Never put two blocks in one chat.
- **Paste the block exactly as written.** Add nothing and explain nothing. If the chat asks a question, answer *"use your judgement"* and nothing else.
- **Copy the whole reply** and paste it back here with its label (e.g. "T1-S2"). **No transcript means no result** (constraint 10).
- **Void if:** a project is attached, memory is on, a block is edited, or a block is pasted into a chat that has seen another block.

---

## T1 · The rewrite · 3 chats: T1-S1, T1-S2, T1-S3

**Same three sentences as Campaign E**, so the results compare directly. Swap the sentence and change nothing else.

- **S1:** "Shows an inappropriate level of independence, and is inflexible when routines change."
- **S2:** "Struggles to prioritise and frequently misses the point of tasks, though clearly capable when engaged."
- **S3:** "Presents as guarded and can be difficult to build rapport with; responds better to structured settings."

```
Here is a sentence written about a person in a report:

"[SENTENCE]"

Work through these five questions, in this order:

1. For each judgement word: what was it measured against, by whom, over what period, on what record? If nothing is named, say "no comparison named".
2. For each claim: what is it a property of: the person, a moment, a setting, a relationship, the task, or the writer?
3. How many separate things is this sentence describing? Is any of them two things stated as one, or one thing stated as two?
4. What does each behaviour described cost the person doing it, and what does writing it down this way cost them? What would it cost the writer to be wrong?
5. Who wrote it, who reads it, who acts on it, and who bears the consequences if it is wrong?

Then rewrite the sentence so that every judgement names what it is a property of and what it was measured against, keeping what the writer most plausibly meant. Give:
- Original:
- Rewrite: (one or two sentences)
- What had to be invented to write it: (anything the rewrite needed that the original didn't supply)
```

**Scored:** a rewrite present (yes/no) · it names a unit and a comparison (yes/no) · it says what had to be invented (yes/no) · the "no comparison named" move survives (yes/no).

---

## T2 · The Sounding, another model · 1 chat: T2-PT (optional T2-OCT)

**Use the block in `sounding-run-pack.md` §2, unchanged.** Its last line becomes: `The periodic table of the elements.`

*Optional T2-OCT is Run 3, the blind Octave, deferred by you on 2026-10-01. It needs the book's full text pasted at the end. Skip it unless you want it.*

---

## T3 · The Jargon Breaker, blind · 1 chat: T3

```
You are going to analyse four short passages, each on its own. Do not compare them to each other.

THE METHOD. Do not hand back questions. Work out what each phrase most likely meant, from the ordinary meanings of its words, and say so as a claim, with a confidence from 0 to 100 and one thing that would show it wrong. Most unclear language is habit, not strategy: expect most passages to be habit, and say plainly when an operation finds nothing.

Run these operations on each passage, in order, and name the ones that find nothing:
1. Turn nouns made from verbs back into verbs, and name the missing actor.
2. Undo passive voice: name who most plausibly did it.
3. Find terms defined by what they are NOT ("non-core", "underserved") and say what is actually in that category.
4. Find words doing two jobs ("efficiency", "reform", "flexibility"); name both senses and commit to the one the sentence needs to be true.
5. Find the concrete thing each vague word points to ("synergies": which ones?). If it can't be named even loosely, say that.
6. Whose interest does this phrasing serve? Write the sentence the other party would have written.
7. Rewrite the passage in one sentence a twelve-year-old could act on. Is the plain version uncomfortable in a way the original is not?

FOR EACH PASSAGE GIVE: a table of the operations that fired (phrase, operation, reading, confidence, what would show it wrong); the plain version in one paragraph; the operations that found nothing; and exactly one verdict, about the language and never about the writer:
- HABIT: unclear, but the plain version is just as comfortable. No finding.
- IMPRECISION: an actor or thing is genuinely missing, probably by accident. Say what to ask for.
- AIMED: the plain version is uncomfortable in a way the original is not. Say what work the unclear wording is doing, and for whom.

PASSAGE A: "As part of our ongoing transformation journey, a number of roles have been impacted, and affected colleagues are being supported through the transition."

PASSAGE B: "We are leveraging cross-functional synergies to drive best-in-class outcomes for our stakeholders."

PASSAGE C: "Pupils will be given opportunities to develop key competencies through engagement with a range of learning experiences."

PASSAGE D: "On 3 March we closed our Leeds office. Forty people lost their jobs, and each was paid three months' salary."
```

*(Operations 8 and 9 in the full tool, word roots and spoken stress, are left out: one needs a recorded lookup and the other needs audio.)*

---

## T4 · Recoherence, known answers · 2 chats: T4-MOUTH, T4-BAT

Swap the word and change nothing else.

```
Take the word "[WORD]" and test whether its established meanings share one underlying theme, or only share a spelling.

1. List its established meanings, each with who uses it (a field or ordinary usage). Use only meanings that exist in dictionaries or a field's usage; never invent one. If you leave any meaning out as a borrowing or a different word, say so now, before step 2.
2. Propose a floor: the deepest statement that every meaning satisfies.
3. Exclusion test: name three things that satisfy your floor but are clearly not "[WORD]" in any sense. If they do, your floor is too shallow.
4. Test one rung lower: drop a word from the floor and see if it still excludes things. If the lower rung fails, the rung above is the floor.
5. Say the theme in plain words that none of the meanings invented.
6. Count how many meanings the floor covers. Name any that don't fit, and don't force them.
7. Name the one variable the meanings differ on.

Then give exactly one verdict:
- THEME FOUND: a floor that includes the meanings and excludes non-members.
- TITLE ONLY: no such floor; the meanings share a word but not a theme. This is a legitimate result, not a failure.
- UNSOUNDED: you couldn't locate it.
```

**Words:** **MOUTH** (river mouth, cave mouth, a jar's mouth, the body's mouth) and **BAT** (the animal and the club: two different words that merged in spelling).

---

## T5 · Axis Search, known answers · 2 chats: T5-SHIFT, T5-PURR

Swap the pair and change nothing else.

```
Here are two things with no claimed relation: [A] and [B].

Test whether a single dimension exists on which both sit at different settings, so that they are the same variable, not just similar. Check these six conditions in order and STOP at the first one that fails. Say which.

C1 Positions: write "A is high on X, B is low on X" (or both at stated points). If you can't write it without hedging, there is no axis. Stop.
C2 The axis existed before this pairing: it is independently named, and ideally measured, in published work. An axis coined to join A and B fails.
C3 Exclusion: name three things high on the axis that resemble A in nothing, and three low that resemble B in nothing.
C4 Direction: are A and B at the same end or opposite ends? Opposite ends predict a relationship someone could go and check.
C5 A third domain: name a domain with neither A nor B where the axis can be measured, and say how it behaves there.
C6 A new prediction: say something the axis predicts about A or B that wasn't known before pairing them. If there's none, stop.

Give: where you stopped (or "all six passed", with the axis named), one line per condition you reached, and one thing that would show your answer wrong. Label any axis you find "generated, unconfirmed".
```

**Pairs:**
- **T5-SHIFT:** A = jet lag after a long flight · B = fatigue in people working night shifts
- **T5-PURR:** A = a cat's purr · B = a mortgage interest rate

---

## 7 · Sealed predictions: the mirror, locked 2026-11-20

| Test | Prediction | Conf |
|---|---|---|
| T1 | A rewrite comes back in **3 of 3** | 80 |
| T1 | "No comparison named" survives in **3 of 3** | 80 |
| T1 | At least one rewrite says what had to be invented | 60 |
| T2 | **LOAD-BEARING** on the periodic table | 70 |
| T3 | A **AIMED** · B **HABIT** · C **IMPRECISION** · D **HABIT** with most operations null | A 70 · B 60 · C 55 · D 75 |
| T4 | MOUTH **THEME FOUND** · BAT **TITLE ONLY** | 75 · 80 |
| T5 | SHIFT reaches at least **C5** (circadian misalignment) | 60 |
| T5 | PURR **stops at C1 or C2** | 85 |

**Kill lines, recorded now and not softened later:**
- **T1:** no rewrite in 2 or more of 3 → **adding the step doesn't fix the crowding-out.** The rule stays, but it stops being called a fix.
- **T2:** anything but LOAD-BEARING → **as a model runs it, the Sounding can't return the null result.**
- **T3:** D comes back AIMED or IMPRECISION → **the Jargon Breaker finds opacity in plain English: a solvent, not a screen.**
- **T4:** BAT comes back THEME FOUND → **Recoherence manufactures themes.**
- **T5:** PURR passes all six → **Axis Search generates an axis for anything.**

### Yours (optional; it only counts if written before the first run)

One line per test, or leave it blank.
