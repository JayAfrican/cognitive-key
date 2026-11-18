"""ck: the Cognitive Key command.

    python -m ck check            run every rule over the Ledger; exit 1 on any problem
    python -m ck status           where everything stands: waiting on JayArr, owed by the mirror, recent
    python -m ck export-ledger    write the Ledger page's batch file (the page is a view of this repo)
    python -m ck findings         regenerate framework/findings.md from the AuDHD finding records
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date, timedelta

from . import ledger, rules


def cmd_check() -> int:
    records = ledger.load()
    problems = rules.run_all(records)
    for p in problems:
        print(p)
    print(f"{len(records)} records, {len(problems)} problems")
    return 1 if problems else 0


def _open(r: dict) -> bool:
    return str(r.get("status", "")).split(" ")[0] in {"open", "pending"} or r.get("status") == "open"


def cmd_status(today: date | None = None) -> int:
    records = ledger.load()
    today = today or date.today()
    tiers = Counter(r["custody"] for r in records.values())
    types = Counter(r["type"] for r in records.values())

    print("WHERE WE ARE")
    print(f"  {len(records)} records · " + " · ".join(f"{t} {n}" for t, n in sorted(types.items())))
    print("  custody: " + " · ".join(f"{t} {tiers.get(t, 0)}" for t in ("RULED", "CORROBORATED", "MIXED", "FILED")))

    problems = rules.run_all(records)
    print(f"  rule check: {'clean' if not problems else f'{len(problems)} PROBLEMS, run `python -m ck check`'}")

    print("\nWAITING ON JAYARR")
    waiting = [(k, r) for k, r in records.items() if r.get("type") == "task" and _open(r) and r.get("owner") == "jayarr"]
    awaiting = [(k, r) for k, r in records.items() if r.get("source_call") == "asked, awaiting his answer"]
    for k, r in sorted(waiting):
        print(f"  · {r['plain']}  [{k}]")
    for k, r in sorted(awaiting):
        print(f"  · Source or scaffolding? {r['plain']}  [{k}]")
    if not (waiting or awaiting):
        print("  nothing")

    print("\nOWED BY THE MIRROR")
    owed = [(k, r) for k, r in records.items() if r.get("type") in {"task", "issue"} and _open(r) and r.get("owner") != "jayarr"]
    for k, r in sorted(owed):
        print(f"  · {r['plain']}  [{k}]")

    print("\nOPEN TESTS")
    for k, r in sorted(records.items()):
        if r.get("layer") == "tester" and r.get("type") == "run" and _open(r):
            preds = [p for p, pr in records.items() if pr.get("type") == "prediction" and _open(pr)
                     and any(l.get("to") == k for l in pr.get("links", []) or [])]
            print(f"  · {r['plain']}  [{k}]" + (f" ({len(preds)} sealed predictions)" if preds else ""))

    print("\nLAST 30 DAYS")
    since = (today - timedelta(days=30)).isoformat()
    recent = Counter((r.get("date", ""), r["type"]) for r in records.values() if str(r.get("date", "")) >= since)
    by_day: dict[str, list[str]] = {}
    for (d, t), n in recent.items():
        by_day.setdefault(d, []).append(f"{n} {t}")
    for d in sorted(by_day, reverse=True):
        print(f"  {d}: " + ", ".join(sorted(by_day[d])))
    if not by_day:
        print("  nothing new")
    return 0


def cmd_export_ledger(path: str = "ledger-page-writes.json") -> int:
    """Writes `set` entries for the Ledger page (collection `records`), 50 per batch."""
    records = ledger.load()
    writes = [{"op": "set", "collection": "records", "doc_id": k,
               "data": {kk: vv for kk, vv in r.items() if kk != "id"}} for k, r in sorted(records.items())]
    batches = [writes[i:i + 50] for i in range(0, len(writes), 50)]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(batches, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(writes)} records in {len(batches)} batches to {path}")
    return 0


def main(argv: list[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "status"
    if cmd == "check":
        return cmd_check()
    if cmd == "status":
        return cmd_status()
    if cmd == "findings":
        from . import findings
        print("wrote", findings.write())
        return 0
    if cmd == "export-ledger":
        return cmd_export_ledger(*argv[2:3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
