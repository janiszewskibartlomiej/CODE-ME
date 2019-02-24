import unittest

from zaddom01 import CzasBiegacza


class TestEtap2(unittest.TestCase):
    def test_porownania(self):
        self.assertTrue(CzasBiegacza(3, 3) > CzasBiegacza(2, 2))
        self.assertTrue(CzasBiegacza(2, 3) > CzasBiegacza(2, 2))

        self.assertTrue(CzasBiegacza(1, 1) == CzasBiegacza(1, 1))
        self.assertTrue(CzasBiegacza(0, 1) != CzasBiegacza(0, 2))

        self.assertFalse(CzasBiegacza(0, 1) < CzasBiegacza(0, 1))


if __name__ == '__main__':
    unittest.main()
