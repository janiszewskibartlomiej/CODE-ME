import unittest
from prostokat import Prostokat


class TestProstokata(unittest.TestCase):
    def test_udaje_sie_utworzyc_prostokat(self):
        p = Prostokat(3, 5)

        oczekiwana = 3
        aktualna = p.bok_a
        self.assertEqual(oczekiwana, aktualna)

        self.assertEqual(5, p.bok_b)

    def test_prostokat_z_ujemnymi_bokami_rzuca_wyjatek(self):
        with self.assertRaises(ValueError):
            Prostokat(-3, 5)
        with self.assertRaises(ValueError):
            Prostokat(3, -5)
        with self.assertRaises(ValueError):
            Prostokat(-3, -5)

    def test_prostokat_z_zerowymi_bokami_rzuca_wyjatek(self):
        with self.assertRaises(ValueError):
            Prostokat(0, 0)
        with self.assertRaises(ValueError):
            Prostokat(3, 0)
        with self.assertRaises(ValueError):
            Prostokat(0, 4)

    def test_repr_zwraca_dobry_opis(self):
        p = Prostokat(3, 5)

        oczekiwana = 'Prostokąt o bokach: a=3, b=5'
        aktualna = p.__repr__()

        self.assertEqual(oczekiwana, aktualna)

    def test_pole_jest_obliczone_prawidlowo(self):
        p = Prostokat(3, 5)
        self.assertEqual(p.pole(), 15)

    def test_czy_kwadrat(self):
        p1 = Prostokat(3, 5)
        self.assertFalse(p1.czy_kwadrat())

        p2 = Prostokat(4, 4)
        self.assertTrue(p2.czy_kwadrat())
