"""The framework's custody, layer, source-call and privacy rules, as checks.

Each check takes the full record set and yields Problem objects. A record that
breaks a rule can't be committed (see `ck check`). The rules come from the
project's prose; the citation for each is in its docstring.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

TYPES = {"claim", "entry", "ruling", "rule", "prediction", "run", "issue", "task"}
CUSTODY = {"RULED", "CORROBORATED", "FILED", "MIXED"}
DECIDED_BY = {"jayarr", "mirror", "mixed", "blind"}
PRIVACY = {"none", "own_pii", "third_party_consented", "safety"}
LAYERS = {"framework", "tester"}

# Verdict vocabularies never mix (process-this, step 4). Each vocabulary's
# values must start with one of its own terms.
VOCABULARIES = {
    "screen": ["SUPPORTED", "OVERSTATED", "UNSUPPORTED", "REFUTED", "NOT EVEN WRONG", "CONTAMINATED", "NOT LOCATED"],
    "recoherence": ["THEME FOUND", "TITLE ONLY", "UNSOUNDED"],
    "inversion": ["TRUE DICHOTOMY", "SINGLE AXIS", "TWO INDEPENDENT DIMENSIONS", "UNRESOLVED", "TITLE-LEVEL COINCIDENCE"],
    "jargon": ["HABIT", "AIMED", "IMPRECISION", "MIXED"],
    "axis": ["AXIS FOUND", "NO AXIS", "STOPPED AT"],
    "sounding": ["SOUND", "ORNAMENTED", "HOLLOW", "UNSOUND"],
    "five-questions": [],  # free text: what the frame added
    "prediction": ["HELD", "FAILED", "UNTESTABLE", "OPEN"],
}

SOURCE_CALL = re.compile(
    r"^(JayArr: (source|scaffolding)|SCAFFOLDING: JayArr|asked, awaiting his answer)"
)
DOI = re.compile(r"\b10\.\d{4,9}/\S+")
ID = re.compile(r"^[a-z0-9]+(-[a-z0-9.]+)*$")

# Constraint 4: his own personal details stay out by default.
PII_PATTERNS = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "an email address"),
    (re.compile(r"\b(born|DOB|date of birth)\b", re.I), "a birth detail"),
    (re.compile(r"\b\d{9,}\b"), "a long reference number"),
]


@dataclass
class Problem:
    record: str
    rule: str
    message: str

    def __str__(self) -> str:
        return f"{self.record}: [{self.rule}] {self.message}"


def _text(r: dict) -> str:
    return " ".join(str(r.get(k, "")) for k in ("plain", "body", "evidence", "seam"))


def check_shape(records):
    """Every record has a known type, a valid id and the four required fields."""
    for rid, r in records.items():
        if not ID.match(rid):
            yield Problem(rid, "shape", "id must be lowercase words joined by hyphens")
        if r.get("type") not in TYPES:
            yield Problem(rid, "shape", f"unknown type {r.get('type')!r}")
        for f in ("plain", "custody", "decided_by", "privacy"):
            if not r.get(f):
                yield Problem(rid, "shape", f"missing {f}")


def check_custody(records):
    """Four tiers only (ruled-or-filed.md §1). Each tier has one kind of decider.
    MIXED must say where the seam is (§2). The mirror never rules: nothing
    decided_by mirror can be RULED or CORROBORATED."""
    pairs = {"RULED": {"jayarr"}, "FILED": {"mirror"}, "CORROBORATED": {"blind"}, "MIXED": DECIDED_BY}
    for rid, r in records.items():
        c, d = r.get("custody"), r.get("decided_by")
        if c not in CUSTODY:
            yield Problem(rid, "custody", f"unknown tier {c!r}")
            continue
        if d not in DECIDED_BY:
            yield Problem(rid, "custody", f"unknown decided_by {d!r}")
        elif d not in pairs[c]:
            yield Problem(rid, "custody", f"{c} can't be decided_by {d}")
        # Older entries name the seam in register_basis (the custody pass's own field).
        if c == "MIXED" and not (r.get("seam") or r.get("register_basis")):
            yield Problem(rid, "custody", "MIXED must name its seam")


def check_layers(records):
    """Three layers, never mixed (RULED 2026-10-03). Predictions belong to the
    tester. A framework run can't be CORROBORATED or use the prediction vocabulary."""
    for rid, r in records.items():
        layer = r.get("layer")
        if layer is not None and layer not in LAYERS:
            yield Problem(rid, "layers", f"unknown layer {layer!r}")
        if r.get("type") == "prediction" and layer != "tester":
            yield Problem(rid, "layers", "predictions belong to the tester layer")
        if layer == "framework":
            if r.get("custody") == "CORROBORATED":
                yield Problem(rid, "layers", "a framework run can't be CORROBORATED; only a blind tester run can")
            if (r.get("verdict") or {}).get("vocabulary") == "prediction":
                yield Problem(rid, "layers", "a framework run can't carry a prediction verdict")


def check_source_call(records):
    """Constraint 28 (RULED 2026-10-07): source or scaffolding is asked every
    time, never guessed. Findings, Why-log entries and framework runs from
    2026-10-05 on must carry his call, or say it is awaited."""
    for rid, r in records.items():
        needs = rid.startswith(("finding-", "why-", "claim-dimensional-")) or (
            r.get("type") == "run" and r.get("layer") == "framework" and str(r.get("date", "")) >= "2026-10-05"
        )
        sc = r.get("source_call")
        if needs and not sc:
            yield Problem(rid, "source-call", "missing source_call (ask him; write 'asked, awaiting his answer' until he does)")
        if sc and not SOURCE_CALL.match(sc):
            yield Problem(rid, "source-call", f"source_call must start with his call or 'asked, awaiting his answer', not {sc[:40]!r}")


def check_privacy(records):
    """Constraints 3 and 4 (RULED). A privacy field on every record, and a scan
    for his personal details in the text."""
    for rid, r in records.items():
        if r.get("privacy") not in PRIVACY:
            yield Problem(rid, "privacy", f"unknown privacy value {r.get('privacy')!r}")
        if r.get("privacy") == "safety":
            continue  # the safety rules themselves name the categories they protect
        text = DOI.sub("", _text(r))
        for pat, what in PII_PATTERNS:
            if pat.search(text):
                yield Problem(rid, "privacy", f"text contains {what}; strip it or mark the record own_pii")


def check_verdicts(records):
    """Verdict vocabularies never mix. A verdict names its vocabulary and uses
    that vocabulary's own terms."""
    for rid, r in records.items():
        v = r.get("verdict")
        if v is None:
            continue
        if not isinstance(v, dict) or "vocabulary" not in v or "value" not in v:
            yield Problem(rid, "verdict", "verdict needs a vocabulary and a value")
            continue
        voc, val = v["vocabulary"], str(v["value"])
        if voc not in VOCABULARIES:
            yield Problem(rid, "verdict", f"unknown vocabulary {voc!r}")
            continue
        terms = VOCABULARIES[voc]
        if terms and not any(val.upper().startswith(t) for t in terms):
            yield Problem(rid, "verdict", f"{val[:40]!r} isn't a {voc} verdict ({', '.join(terms)})")


def check_links(records):
    """Every link points to a record that exists."""
    for rid, r in records.items():
        for link in r.get("links", []) or []:
            if link.get("to") not in records:
                yield Problem(rid, "links", f"links to missing record {link.get('to')!r}")


ALL_CHECKS = [check_shape, check_custody, check_layers, check_source_call, check_privacy, check_verdicts, check_links]


def run_all(records):
    problems = []
    for check in ALL_CHECKS:
        problems.extend(check(records))
    return problems
