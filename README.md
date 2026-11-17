# Cognitive Key

JayArr's framework as code: the Ledger of findings, rulings and runs, plus the rules that keep it honest, enforced by checks instead of memory.

- `ledger/records/`: one file per record (286 at the start).
- `ck/rules.py`: the rules as checks: custody, layers, source calls, privacy, verdict vocabularies and links.
- `python -m ck status`: where everything stands.
- `python -m ck check`: refuses anything that breaks a rule.
- `CLAUDE.md`: what every Claude session reads first.

Plan: `build-plan-code-2026-11-17.md` in the Claude project. Phase 1 (this) is the Ledger as code. Next come the status report and CLAUDE.md, done here early; then one canonical framework in place of the 120+ docs; then the app.

No dependencies beyond Python 3.10+.
