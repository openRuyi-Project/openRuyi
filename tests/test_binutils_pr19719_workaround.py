from pathlib import Path
import unittest


class Pr19719WorkaroundTest(unittest.TestCase):
    def test_riscv_failure_is_xfailed_without_deleting_tests(self):
        spec = Path("SPECS/binutils/binutils.spec").read_text(encoding="utf-8")
        patch = Path("SPECS/binutils/2005-ld-riscv-xfail-pr19719-test.patch")
        self.assertNotIn("sed -i '/\"pr19719/d'", spec,
                         "unconditional pr19719 deletion remains")
        self.assertIn("Patch2005:", spec)
        self.assertTrue(patch.exists(), "RISC-V pr19719 xfail patch is missing")
        contents = patch.read_text(encoding="utf-8")
        self.assertEqual(contents.count('"riscv*-*-*"'), 2)


if __name__ == "__main__":
    unittest.main()
