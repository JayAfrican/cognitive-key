<!-- Canonical file, copied unchanged from the cognitive-key-framework plugin v0.1.1 on 2026-11-17. -->

# Log the Run

Every framework run writes one `run` record to the Ledger. **A run that leaves no record didn't happen** (constraint 10). Failed, boring and null runs are logged too.

## Where

- **Ledger page:** https://claude.ai/artifact/417QksxiXA1r8CPV3LmU1B
- **Write with** the `ArtifactData` tool: `action: "set"`, `collection: "records"`, `doc_id` = the record id. It's a new document, so no `if_version`.
- **If the tool isn't available, or the write fails:** don't pretend it was logged. Show the full record as JSON in the reply, say "NOT LOGGED, needs filing", and ask JayArr to bring it to a session that can write it.

## The record

```json
{
  "type": "run",
  "layer": "framework",
  "tool": "five-questions | jargon-breaker | stopping-engine | sounding | recoherence | axis-search | cross-pollination-intake",
  "plain": "One plain sentence: what went in and what came out.",
  "body": "Input (after the privacy gate) · route taken · steps run, in order · where it halted, if it halted · the rewrite, if any · falsifier",
  "custody": "FILED",
  "decided_by": "mirror",
  "date": "YYYY-MM-DD",
  "verdict": { "vocabulary": "five-questions | jargon | screen | sounding | recoherence | inversion | axis", "value": "…", "confidence": 0 },
  "status": "first run | early run | routine",
  "links": [ { "rel": "derived_from", "to": "<another record id>" } ],
  "privacy": "none | own_pii | third_party_consented",
  "source_call": "JayArr: source | JayArr: scaffolding | asked, awaiting his answer"
}
```

- **id:** `run-<tool>-<YYYYMMDD>-<short-slug>`, lowercase, hyphens only. If an id already exists, add `-2`.
- **source_call is never guessed.** If he hasn't answered, write "asked, awaiting his answer" (constraint 28: case by case, no default).
- **Omit empty fields.** Use `confidence` only where the tool gives a number.
- **Verdict vocabularies never mix.** Name the one used.

## The hard limits on what this skill may write

- **custody is always FILED.** Never RULED, never CORROBORATED, never MIXED. Those are set only by JayArr's ruling (RULED) or by the tester from a blind run (CORROBORATED).
- **Never write a `prediction`, `result` or `ruling` record.** Those belong to the tester and to JayArr.
- **Never edit an existing record.** If a run changes the standing of an earlier record, write the new run with a `links` entry (`supports`, `contradicts` or `supersedes`) and tell JayArr. He decides whether the earlier record changes.
- **Privacy:** no third party who hasn't consented, no JayArr personal details. If the input had to be stripped, log the stripped version and set `privacy` accordingly.

## After writing

Confirm in the reply in one line: "Logged to the Ledger as `<id>` (FILED)." If the page should show something new to JayArr, give the record id so he can find it there.
