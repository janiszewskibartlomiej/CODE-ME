import unittest
from jednostki2.wojownik import Wojownik, WojownikError


class TestWojownik(unittest.TestCase):
    def test_stworzenie_udane(self):
        w = Wojownik(30)
        self.assertEqual(w._zycie, 30)
        self.assertEqual(w._doswiadczenie, 0)

    def test_stworzenie_z_ujemnym_zyciem(self):
        with self.assertRaises(WojownikError):
            w = Wojownik(-100)

    def test_repr(self):
        w = Wojownik(30)
        spodziewany = 'Wojownik: hp=30, exp=0'
        aktualny = w.__repr__()

        self.assertEqual(spodziewany, aktualny)
