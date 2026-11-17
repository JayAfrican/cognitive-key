# Restoring the repository in a new session (until GitHub is connected)

The code lives in the project as `claude/code/*`. The records live in the Ledger page.

1. Copy `claude/code/ck/*.py`, `claude/code/tests/test_rules.py`, `claude/code/CLAUDE.md` and `claude/code/README.md` into a folder named `cognitive-key/`, keeping the `ck/` and `tests/` folders. Add an empty `__init__.py` to both folders.
2. Pull the records: ArtifactData `list` on https://claude.ai/artifact/417QksxiXA1r8CPV3LmU1B, collection `records`, limit 1000, with `out_dir`. Write each one to `ledger/records/<id>.json` as `{"id": ..., **data}` with sorted keys.
3. Run `python -m ck check` and `python -m unittest`.

Once the GitHub repo exists, it replaces all of this.
