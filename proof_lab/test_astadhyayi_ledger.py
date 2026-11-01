from __future__ import annotations

import json
import unittest
from pathlib import Path

from proof_lab.astadhyayi_ledger import COMPILED, HAND_CODED, META, OUT_DIR, PACKET_OF, ROOT, TEXT, THEOREM_FILE, build, key


class AstadhyayiLedgerTests(unittest.TestCase):
    def test_committed_ledger_matches_rebuild(self) -> None:
        committed = json.loads((OUT_DIR / "ASTADHYAYI_LEDGER.json").read_text(encoding="utf-8"))
        self.assertEqual(committed, build())

    def test_every_executed_entry_points_at_an_existing_theorem_and_packet(self) -> None:
        for table in (COMPILED, META, HAND_CODED):
            for t in table:
                self.assertTrue((ROOT / THEOREM_FILE[t]).exists(), t)
                if t in PACKET_OF:
                    self.assertTrue((ROOT / "proof_lab" / f"{PACKET_OF[t]}.py").exists(), t)

    def test_hand_coded_numbers_are_carried_by_their_packets(self) -> None:
        for t, nums in HAND_CODED.items():
            src = (ROOT / "proof_lab" / f"{PACKET_OF[t]}.py").read_text(encoding="utf-8")
            for n in nums:
                self.assertIn(n, src, (t, n))

    def test_numbers_are_well_formed_and_sorted(self) -> None:
        ledger = build()
        nums = list(ledger["sutras"])
        self.assertEqual(nums, sorted(nums, key=key))
        for n in nums:
            a, p, s = key(n)
            self.assertTrue(1 <= a <= 8 and 1 <= p <= 4 and 1 <= s <= 223, n)  # 6.1 is the longest pāda of the pinned sūtrapāṭha (223 sūtras)

    def test_texts_have_no_latin_numbering_errors(self) -> None:
        # a curated text never repeats under two numbers — except where the pinned sūtrapāṭha itself repeats it
        identical_in_edition = {"avyayībhāvaś ca": {"1.1.41", "2.4.18"}}   # अव्ययीभावश्च at both numbers (the avyaya saṁjñā; the napuṁsaka rule)
        seen = {}
        for n, t in TEXT.items():
            if t:
                if t in identical_in_edition and n in identical_in_edition[t]:
                    continue
                self.assertNotIn(t, seen, (n, seen.get(t)))
                seen[t] = n


if __name__ == "__main__":
    unittest.main()
