# Blind rerun: MOUTH, BAT and SHIFT · run pack

**Tester layer. Written 2026-11-20, after the first blind run and before this one.** It fixes defects D1, D2 (via the FAMILY verdict, RULED today), D3 and D6. Predictions are sealed in the Ledger (`pred-br2-*`). Frozen once the first block is pasted.

**Same rules as `blind-runs-2026-11-20.md` §0:**
- Use a model that isn't me, with one fresh chat per block.
- Paste each block exactly as written.
- Answer any question with "use your judgement".
- Return the whole reply with its label.

**Scoring rule (D6):** when a reply's opening line and its final answer disagree, **the final answer counts**, and the disagreement is noted.

---

## T4R · Recoherence with four verdicts · 2 chats: T4R-MOUTH, T4R-BAT

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
- FAMILY: the meanings grow by extension from one starting meaning, but no floor short of that starting meaning both includes them all and excludes non-members.
- TITLE ONLY: no relation beyond the spelling; separate words that merged.
- UNSOUNDED: you couldn't locate it.
All four are legitimate results.
```

**Words:** `mouth` · `bat`

---

## T5R · Axis Search, fixed pairing · 1 chat: T5R-SHIFT

```
Here are two things with no claimed relation: jet lag after a long flight and working night shifts.

Test whether a single dimension exists on which both sit at different settings, so that they are the same variable, not just similar. Check these six conditions in order and STOP at the first one that fails. Say which.

C1 Positions: write "A is high on X, B is low on X" (or both at stated points). If you can't write it without hedging, there is no axis. Stop.
C2 The axis existed before this pairing: it is independently named, and ideally measured, in published work. An axis coined to join A and B fails.
C3 Exclusion: name three things high on the axis that resemble A in nothing, and three low that resemble B in nothing.
C4 Direction: are A and B at the same end or opposite ends? Opposite ends predict a relationship someone could go and check.
C5 A third domain: name a domain with neither A nor B where the axis can be measured, and say how it behaves there.
C6 A new prediction: say something the axis predicts about A or B that wasn't known before pairing them. If there's none, stop.

Give: where you stopped (or "all six passed", with the axis named), one line per condition you reached, and one thing that would show your answer wrong. Label any axis you find "generated, unconfirmed".
```

---

## Sealed predictions: the mirror, locked 2026-11-20

| Test | Prediction | Conf |
|---|---|---|
| T4R-MOUTH | **FAMILY** | 70 |
| T4R-BAT | **TITLE ONLY** | 80 |
| T5R-SHIFT | Reaches at least **C3**, with circadian misalignment as the axis | 60 |

**Kill lines, in both directions this time (D1):**
- **Over-finding:**
  - BAT comes back THEME FOUND or FAMILY → **Recoherence manufactures relations.**
- **Under-finding:**
  - MOUTH comes back TITLE ONLY, even with FAMILY available → **Recoherence can't recognise a family when it's named.**
  - SHIFT stops at C1 again, with the pairing fixed → **Axis Search's C1 is too strict for real axes.**

### Yours (optional; it only counts if written before the first run)
