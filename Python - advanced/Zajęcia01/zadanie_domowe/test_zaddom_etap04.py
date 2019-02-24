import unittest

from zaddom01 import CzasBiegacza


class TestEtap3(unittest.TestCase):
    def test_odejmowania(self):
        wynik = CzasBiegacza(10, 10) - CzasBiegacza(1, 1)
        self.assertTrue(wynik == CzasBiegacza(9, 9))

        wynik = CzasBiegacza(10, 1) - CzasBiegacza(0, 59)
        self.assertTrue(wynik == CzasBiegacza(9, 2))

        wynik = CzasBiegacza(10, 1) - CzasBiegacza(1, 0)
        self.assertTrue(wynik == CzasBiegacza(9, 1))

        with self.assertRaises(ValueError):
            wynik = CzasBiegacza(0, 1) - CzasBiegacza(0, 2)

        with self.assertRaises(ValueError):
            wynik = CzasBiegacza(0, 3) - CzasBiegacza(1, 0)


if __name__ == '__main__':
    unittest.main()
