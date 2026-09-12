import unittest

from proof_lab.morphic_recognition.verify import run_all, verify_mr01, verify_mr02, verify_mr03


class MorphicRecognitionProofContractTests(unittest.TestCase):
    def test_mr01_contract_closes(self):
        result = verify_mr01()
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED", result)
        self.assertTrue(all(x["status"] == "pass" for x in result["checks"]), result)

    def test_mr02_contract_closes(self):
        result = verify_mr02()
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED", result)
        self.assertTrue(all(x["status"] == "pass" for x in result["checks"]), result)

    def test_mr03_contract_closes(self):
        result = verify_mr03()
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED", result)
        self.assertTrue(all(x["status"] == "pass" for x in result["checks"]), result)

    def test_full_packet_is_hash_bound(self):
        result = run_all()
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED", result)
        self.assertEqual(result["theorem_count"], 3)
        self.assertEqual(len(result["certificate_sha256"]), 64)
        self.assertFalse(result["claim_boundary"]["formal_proof_assistant"])
        self.assertIsNone(result["claim_boundary"]["domain_adapter"])


if __name__ == "__main__":
    unittest.main()
