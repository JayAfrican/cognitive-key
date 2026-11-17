"""Each rule refuses the thing it exists to refuse. Run: python -m unittest"""
import unittest

from ck import ledger, rules


def rec(**kw):
    base = {"type": "claim", "plain": "x", "custody": "FILED", "decided_by": "mirror", "privacy": "none"}
    base.update(kw)
    return base


def problems(records, check):
    return [p.rule for p in check(records)]


class Custody(unittest.TestCase):
    def test_mirror_cannot_rule(self):
        self.assertTrue(problems({"a": rec(custody="RULED")}, rules.check_custody))

    def test_mirror_cannot_corroborate(self):
        self.assertTrue(problems({"a": rec(custody="CORROBORATED")}, rules.check_custody))

    def test_mixed_needs_seam(self):
        self.assertTrue(problems({"a": rec(custody="MIXED", decided_by="mixed")}, rules.check_custody))
        self.assertFalse(problems({"a": rec(custody="MIXED", decided_by="mixed", seam="his claim, my verdict")}, rules.check_custody))

    def test_unknown_tier(self):
        self.assertTrue(problems({"a": rec(custody="PROBABLY")}, rules.check_custody))


class Layers(unittest.TestCase):
    def test_prediction_is_tester(self):
        self.assertTrue(problems({"a": rec(type="prediction", layer="framework")}, rules.check_layers))

    def test_framework_run_not_corroborated(self):
        r = rec(type="run", layer="framework", custody="CORROBORATED", decided_by="blind")
        self.assertTrue(problems({"a": r}, rules.check_layers))


class SourceCall(unittest.TestCase):
    def test_finding_needs_call(self):
        self.assertTrue(problems({"finding-x": rec()}, rules.check_source_call))

    def test_awaiting_is_allowed(self):
        self.assertFalse(problems({"finding-x": rec(source_call="asked, awaiting his answer")}, rules.check_source_call))

    def test_guessing_is_refused(self):
        self.assertTrue(problems({"finding-x": rec(source_call="probably source")}, rules.check_source_call))

    def test_new_framework_run_needs_call(self):
        r = rec(type="run", layer="framework", date="2026-11-17")
        self.assertTrue(problems({"a": r}, rules.check_source_call))


class Privacy(unittest.TestCase):
    def test_email_caught(self):
        self.assertTrue(problems({"a": rec(plain="write to someone@example.com")}, rules.check_privacy))

    def test_doi_not_mistaken_for_reference_number(self):
        self.assertFalse(problems({"a": rec(body="doi 10.1177/1362361318766571")}, rules.check_privacy))


class Verdicts(unittest.TestCase):
    def test_vocabularies_do_not_mix(self):
        r = rec(type="run", verdict={"vocabulary": "screen", "value": "THEME FOUND"})
        self.assertTrue(problems({"a": r}, rules.check_verdicts))

    def test_own_vocabulary_passes(self):
        r = rec(type="run", verdict={"vocabulary": "screen", "value": "OVERSTATED at step 6"})
        self.assertFalse(problems({"a": r}, rules.check_verdicts))


class Links(unittest.TestCase):
    def test_dangling_link(self):
        self.assertTrue(problems({"a": rec(links=[{"rel": "about", "to": "nowhere"}])}, rules.check_links))


class TheRealLedger(unittest.TestCase):
    def test_ledger_is_clean(self):
        found = rules.run_all(ledger.load())
        self.assertEqual([], [str(p) for p in found])


if __name__ == "__main__":
    unittest.main()
