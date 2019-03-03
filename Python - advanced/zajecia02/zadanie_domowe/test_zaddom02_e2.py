import unittest

from zaddom02_e2 import rozdaj_karty, TaliaKart


class Etap2(unittest.TestCase):
    def test_proste_rozdanie(self):
        talia = TaliaKart()

        karty = rozdaj_karty(talia)
        self.assertEqual(len(karty), 1)

    def test_rozdanie_wielu(self):
        talia = TaliaKart()

        karty = rozdaj_karty(talia, 10)
        self.assertEqual(len(karty), 10)

    def test_rozdanie_z_wytraceniem(self):
        talia = TaliaKart()

        karty50 = rozdaj_karty(talia, 50)
        karty10 = rozdaj_karty(talia, 10)
        self.assertEqual(len(karty10), 2)

        karty_z_pustego = rozdaj_karty(talia, 10)
        self.assertEqual(len(karty_z_pustego), 0)

    def test_rozdanie_nieprawidlowej_liczby(self):
        talia = TaliaKart()

        karty0 = rozdaj_karty(talia, 0)
        self.assertEqual(karty0, [])

        karty_minus = rozdaj_karty(talia, -10)
        self.assertEqual(karty_minus, [])


if __name__ == '__main__':
    unittest.main()
