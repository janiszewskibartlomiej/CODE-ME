import unittest

from zaddom01 import CzasBiegacza


class TestEtap1(unittest.TestCase):
    def test_init(self):
        cz = CzasBiegacza(10, 20)

        self.assertTrue(cz._minuty == 10)
        self.assertTrue(cz._sekundy == 20)

        with self.assertRaises(ValueError):
            cz = CzasBiegacza(10, 70)

        with self.assertRaises(ValueError):
            cz = CzasBiegacza(10, -10)

        with self.assertRaises(ValueError):
            cz = CzasBiegacza(-10, 10)

    def test_repr(self):
        cz = CzasBiegacza(10, 20)

        self.assertTrue(str(cz) == 'czas: 10min, 20sek')


if __name__ == '__main__':
    unittest.main()
