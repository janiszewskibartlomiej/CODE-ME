import unittest

from zaddom02_e1 import TaliaKart


class Etap1(unittest.TestCase):
    def test_jedno_losowanie(self):
        talia = TaliaKart()

        karta = next(talia)
        self.assertEqual(len(talia._karty), 51)

    def test_losowanie_wszystkich(self):
        talia = TaliaKart()
        wszystkie_rozne_karty = set(talia)

        self.assertEqual(len(wszystkie_rozne_karty), 52)

    def test_wyczerpanie_talii(self):
        talia = TaliaKart()

        with self.assertRaises(StopIteration):
            for _ in range(53):
                next(talia)

    def test_losowosci(self):
        for _ in range(100):
            talia1 = TaliaKart()
            talia2 = TaliaKart()
            if next(talia1) != next(talia2):
                return
        self.fail()


if __name__ == '__main__':
    unittest.main()
