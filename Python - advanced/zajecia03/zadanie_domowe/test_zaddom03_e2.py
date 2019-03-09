import unittest
import hashlib

from zaddom03_e2 import unikalne_adresy_ip


class Etap2(unittest.TestCase):
    def test_apache_log_byl_modyfikowany(self):
        plik = open('apache_logs', mode='r')
        zawartosc = plik.read()
        obliczony_hash = hashlib.md5(zawartosc.encode()).digest()
        orginalny_hash = b'\xf2\xec\xff:>\xea\x96\xcc\x08\xbf\xb1,\x06]-\x1b'
        self.assertEqual(orginalny_hash, obliczony_hash)
        plik.close()

    def test_typ_zwracanej_wartosci(self):
        wynik = unikalne_adresy_ip()
        self.assertTrue(isinstance(wynik, list))
        if len(wynik):
            self.assertTrue(isinstance(wynik[0], str))

    def test_poprawna_odpowiedz(self):
        wynik = unikalne_adresy_ip()
        spodziewany_wynik = ['66.249.73.135', '86.1.76.62', '81.220.24.207', '46.105.14.53', '207.241.237.228',
                             '207.241.237.227', '50.16.19.13', '50.150.204.184', '74.125.40.20', '121.107.188.202',
                             '91.177.205.119', '93.114.45.13', '200.49.190.101', '200.49.190.100', '198.46.149.143',
                             '24.236.252.67', '207.241.237.225', '123.125.71.35', '209.85.238.199', '207.241.237.220',
                             '207.241.237.101', '108.174.55.234', '83.149.9.216', '87.169.99.232', '218.30.103.62',
                             '66.249.73.185', '67.214.178.190', '71.212.224.97', '110.136.166.128']
        self.assertEqual(set(spodziewany_wynik), set(wynik))


if __name__ == '__main__':
    unittest.main()
