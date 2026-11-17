"""Load and save Ledger records: one JSON file per record in ledger/records/."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORDS = ROOT / "ledger" / "records"


def load(directory: Path = RECORDS) -> dict[str, dict]:
    records = {}
    for path in sorted(directory.glob("*.json")):
        r = json.loads(path.read_text(encoding="utf-8"))
        rid = r.get("id") or path.stem
        if rid != path.stem:
            raise ValueError(f"{path.name}: id {rid!r} doesn't match the file name")
        records[rid] = r
    return records


def save(record: dict, directory: Path = RECORDS) -> Path:
    path = directory / f"{record['id']}.json"
    body = {"id": record["id"], **{k: v for k, v in sorted(record.items()) if k != "id"}}
    path.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path
