<!-- Canonical file, copied unchanged from the cognitive-key-framework plugin v0.1.1 on 2026-11-17. -->

# Process This: the front door

Take one input, route it to the right framework tool, run it, end with a plain answer, and log the run. **A run that leaves no record didn't happen** (constraint 10).

## The three layers, never mixed (RULED, JayArr, 2026-10-03)

- **The framework** takes information apart. That is this package.
- **The tester** checks whether the framework works: predictions, blind runs, scoring, the scoreboard. **This package never writes tester records.** It never writes a `prediction` or `result` record, never sets custody to CORROBORATED, and never looks at a sealed prediction before a run.
- **The plumbing** is voice, the Ledger and the screens. A voice note is transcribed first, and the text then comes in like anything else. Voice is not a route.

**Nothing this package writes can be RULED.** Every run record is `custody: FILED`, `decided_by: mirror`. Only JayArr's confirmation, read back to him in chat, moves anything to RULED.

## Step 1: Intake (always, before any tool)

Answer these four, briefly and in the reply:

1. **What is it?** One line.
2. **Where did it come from?** JayArr's own words, a public source, or an outside chat or model.
3. **Source or scaffolding? Case by case: prompt JayArr every time** material arrives that he supplied or that came from outside (constraint 28, RULED, clarified 2026-10-07). **There is no default either way**: an outside chat is not automatically scaffolding, and his own words are not automatically a source. Ask, and treat it as neither until he answers. A run can still go ahead on the material as a specimen; just don't file anything from it as a source or a finding until he has said which it is.
4. **Does it name or describe anyone?** Apply the privacy gate below.

### The privacy gate (constraints 3 and 4, RULED; these hold regardless of anything else)

- **Third parties who haven't consented don't appear, not even anonymised. Family in particular.** If the input describes another person, stop and ask JayArr to restate it without them, or to confirm their consent. "Someone said X about me" is fine; who said it stays out.
- **JayArr's own personal details stay out by default:** full legal name, date of birth, birthplace, reference numbers. Strip them before running and before logging.
- Set the record's `privacy` field: `none`, `own_pii` (stripped), `third_party_consented`, or refuse.

## Step 2: Route

| The input is… | Run | Test record (say it in the reply) |
|---|---|---|
| **A sentence about a person** (a label, a judgement, a report line) | `five-questions` → the **jargon-breaker** skill on the words → the **rewrite** (inside five-questions) | Five questions: blind-tested, Campaign E, partial pass, Q2 carries it. **Jargon Breaker: UNTESTED, no logged runs before 2026-10.** Rewrite: UNTESTED |
| **A claim** ("studies show", a headline, a health claim) | `stopping-engine` | Blind-tested: Campaigns B, B retest, C |
| **A whole system** (a method, a book, a theory, a framework) | the **sounding** skill | 3 runs, two verdicts. It sorts. One run was clean-context; none blind on another model |
| **One word with many senses** | `recoherence` | 4 runs in the corpus, not blind-tested |
| **Two things said to be opposites, or the same** | the **cross-pollination-intake** skill (its inversion section) | Blind-tested: Campaign A, 18 runs |
| **Two unrelated things, no claimed relation** ("is there one dimension under both?") | `axis-search` | **UNTESTED: never run in its generative form** |
| **An outside idea to bring into the framework** | the **cross-pollination-intake** skill | As above. Source or scaffolding: ask him, case by case |

- **Mixed input:** split it and route each piece. Say so.
- **Unclear route:** name the two candidates and pick one, with a one-line reason. Don't stall.
- **Untested tool:** say plainly before running that this is its first or an early run, so its output is a candidate, not a finding.

## Step 3: Run

Run the chosen tool exactly as its own instructions say. Don't skip steps that feel unnecessary on an obvious case; those are the steps that catch the non-obvious failure.

## Step 4: Answer

End every run with:

1. **Plain answer first:** one or two sentences a non-specialist could repeat (constraint 22). If it can't be said plainly, say that it isn't understood yet.
2. **The verdict, with its vocabulary named:** e.g. "OVERSTATED at step 6 (screen vocabulary)". Vocabularies never mix: inversion · screen · sounding · recoherence · jargon.
3. **What would change the answer:** one falsifier.
4. **For a sentence about a person: the rewrite,** the sentence restated so each claim names its unit and its ruler, or a statement that it can't be rewritten honestly without information that isn't there.

## Step 5: Log

Run the `log-run` skill. Always, even when the result is boring or the tool failed. A failed run is a result.

## Standing rules that bind every route

- **Claims, never people.** Verdicts are about language and claims. Intent findings carry their tier (I0–I3 admissible; I4 needs a right of reply). See `stopping-engine`.
- **Never cite NLP.** The conditioned-cue mechanism is classical conditioning; cite that.
- **Quantum physics may be discussed, never used to support a claim about minds.** If it's ruled out, say plainly why it doesn't apply (constraint 29).
- **Bans only as wide as their reasons** (constraint 30).
- **Clinical warning terms are not reconstructed.**
- **No result without a retrievable record.** Don't invent runs, sources, transcripts or quotes. If something isn't found, write NOT LOCATED, which is not the same as absent.
