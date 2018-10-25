import unittest
from prostokat import Prostokat


class TestProstokata(unittest.TestCase):
    def test_udaje_sie_utworzyc_prostokat(self):
        p = Prostokat(3, 5)

        oczekiwana = 3
        aktualna = p.bok_a
        self.assertEqual(oczekiwana, aktualna)

        self.assertEqual(5, p.bok_b)

    def test_repr_zwraca_dobry_opis(self):
        p = Prostokat(3, 5)

        oczekiwana = 'Prostokąt o bokach: a=3, b=5'  # Wypełnij tę wartość aby test przechodził
        aktualna = p.__repr__()

        self.assertEqual(oczekiwana, aktualna)

    def test_pole_jest_obliczone_prawidlowo(self):
        p = Prostokat(3, 5)
        oczekiwana = p.pole()
        self.assertEqual(oczekiwana, 15)  # napisz test, który sprawdzi, czy metoda pole() zwraca prawidłowy wynik

    def test_czy_kwadrat(self):
        p1 = Prostokat(3, 5)
        oczekiwana = p1.czy_kwadrat()
        self.assertFalse(oczekiwana)

        p2 = Prostokat(3,3)
        self.assertTrue(p2.czy_kwadrat())

    def test_cz_ujemne(self):
        with self.assertRaises(ValueError):
            Prostokat(3,-5)
        with self.assertRaises(ValueError):
            Prostokat(-3,5)
        with self.assertRaises(ValueError):
            Prostokat(-3,-5)
        with self.assertRaises(ValueError):
            Prostokat(0,0)

