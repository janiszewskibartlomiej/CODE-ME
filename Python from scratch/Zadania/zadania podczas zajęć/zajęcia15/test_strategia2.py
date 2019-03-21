import unittest

from jednostki.rycerz import Rycerz
from jednostki2.wojownik import Wojownik, WojownikError
from druzyna2 import Druzyna


class TestWojownik(unittest.TestCase):
    def test_stworzenie_udane(self):
        ZYCIE = 30  # lepiej wyciągnąć stałą w jedno miejsce
        w = Wojownik(ZYCIE)
        self.assertEqual(w._zycie, ZYCIE)
        self.assertEqual(w._doswiadczenie, 0)

    def test_stworzenie_z_ujemnym_zyciem(self):
        with self.assertRaises(WojownikError):
            w = Wojownik(-100)

    def test_repr(self):
        w = Wojownik(30)
        spodziewany = 'Wojownik: hp=30, exp=0'
        aktualny = w.__repr__()
        self.assertEqual(spodziewany, aktualny)

    def test_marsz(self):
        w = Wojownik(30)
        w.maszeruj(1000)
        self.assertEqual(20.0, w._doswiadczenie)


class TestRycerz(unittest.TestCase):
    def test_atakuj(self):
        r = Rycerz()
        r.atakuj()
        self.assertEqual(0.3, r._doswiadczenie)

    def test_stworzenie_udane(self):
        r = Rycerz()
        self.assertEqual(r._zycie, 60)
        self.assertEqual(r._doswiadczenie, 0)


class TestDruzyna(unittest.TestCase):
    def test_stworzenie(self):
        d = Druzyna()
        self.assertEqual(d.wojownicy, [])

    def test_dodawanie(self):
        d = Druzyna()
        r1 = Rycerz()
        d.dodaj_wojownika(r1)
        self.assertEqual(d.wojownicy, [r1])
