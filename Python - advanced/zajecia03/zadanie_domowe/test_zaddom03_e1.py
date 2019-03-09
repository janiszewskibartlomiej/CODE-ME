import unittest

from zaddom03_e1 import ile_cyfr


class Etap1(unittest.TestCase):
    def test_poprawne_dzialanie(self):
        liczby = [0, 12, 123, 1234]
        spodziewany_wynik = ['0 (1 cyfr)', '12 (2 cyfr)', '123 (3 cyfr)', '1234 (4 cyfr)']
        wynik = ile_cyfr(liczby)
        self.assertEqual(spodziewany_wynik, wynik)

    def test_usuwanie_liczb_ujemnych(self):
        liczby = [10, 1, 0, -1, -10]
        spodziewany_wynik = ['10 (2 cyfr)', '1 (1 cyfr)', '0 (1 cyfr)']
        wynik = ile_cyfr(liczby)
        self.assertEqual(spodziewany_wynik, wynik)

    def test_pusta_lista(self):
        liczby = []
        spodziewany_wynik = []
        wynik = ile_cyfr(liczby)
        self.assertEqual(spodziewany_wynik, wynik)


if __name__ == '__main__':
    unittest.main()
