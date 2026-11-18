"""Generate framework/findings.md from the Ledger's finding-audhd-* records.

The Ledger is the source; this file is a readable view. Groups follow
framework/octave.md §4–5 (placements RULED 2026-11-17 for Root, Polarity,
Friction and Surrender; the rest proposed or left unforced).
"""
from __future__ import annotations

from . import ledger
from .ledger import ROOT

GROUPS = [
    ("1 · Root", "RULED", [11, 13, 17]),
    ("2 · Spark", "proposed", [5, 6, 59]),
    ("3 · Polarity (hot)", "RULED", [2, 21, 28, 33, 49, 55, 62]),
    ("4 · Friction (cold)", "RULED", [23, 50, 51]),
    ("5 · Execution", "proposed", [10]),
    ("6 · Shadow", "proposed", [30, 44, 48]),
    ("7 · Surrender", "RULED", [24, 31, 34, 37, 47, 52]),
    ("8 · Gestalt", "proposed", [1, 18]),
    ("The energy economy (the dials)", "unforced", [7, 12, 14, 16, 19, 20]),
    ("Severity (a depth across notes)", "unforced", [42, 43, 45]),
    ("History (where the settings came from)", "unforced", [9, 15, 27]),
    ("The master axis (hypothesis)", "unforced", [38, 39, 40, 41]),
    ("People and patterns", "unforced", [29, 53, 54, 66, 67]),
    ("The two-poles law (sources of the law)", "RULED law", [63, 64, 65]),
    ("Language and definitions", "unplaced", [3, 4, 8, 22, 25, 26, 32, 35, 36, 46, 56, 57, 58, 60, 61]),
]


def build() -> str:
    records = ledger.load()
    found = {int(k.rsplit("-", 1)[1]): r for k, r in records.items() if k.startswith("finding-audhd-")}
    placed = [n for _, _, ns in GROUPS for n in ns]
    missing = sorted(set(found) - set(placed))
    doubled = sorted({n for n in placed if placed.count(n) > 1})
    lines = [
        "# The AuDHD findings",
        "",
        f"**Generated from the Ledger ({len(found)} findings, `finding-audhd-01` to `-{max(found):02d}`). Don't edit this file: edit the records and run `python -m ck findings`.**",
        "",
        "The long form, with sections and evidence tags, is JayArr's doc *AuDHD Findings — Unification* (https://claude.ai/code/artifact/37774554-b8d4-4945-97ea-2d57f26a9fcc). Grouping follows `octave.md`.",
        "",
        "**Personal details (constraint 4):** findings marked 🔒 hold his own history. Their text stays in the records and his doc, not in this view.",
        "",
    ]
    for title, status, ns in GROUPS:
        lines += [f"## {title} · {status}", ""]
        for n in ns:
            r = found[n]
            text = "🔒 *personal history: see the record*" if r.get("privacy") == "own_pii" else r["plain"]
            ev = r.get("evidence_kind", "")
            lines.append(f"- **{n}.** {text} *({r['custody']}{'; ' + ev if ev else ''})*")
        lines.append("")
    if missing or doubled:
        lines += ["## ⚠ Check", "", f"Not placed in any group: {missing or 'none'} · In two groups: {doubled or 'none'}", ""]
    return "\n".join(lines)


def write() -> str:
    path = ROOT / "framework" / "findings.md"
    path.write_text(build(), encoding="utf-8")
    return str(path)
