import unittest

from zaddom03 import CzasBiegacza


class TestEtap3(unittest.TestCase):
    def test_dodawania(self):
        wynik = CzasBiegacza(1, 1) + CzasBiegacza(2, 2)
        self.assertTrue(wynik == CzasBiegacza(3, 3))

    def test_przepelnienia(self):
        wynik = CzasBiegacza(0, 59) + CzasBiegacza(0, 59)
        self.assertTrue(wynik == CzasBiegacza(1, 58))


if __name__ == '__main__':
    unittest.main()
