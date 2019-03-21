nazwa_pliku = 'dane2.txt'

plik = open(nazwa_pliku, mode='w')

tekst_do_zapisania = 'XXX\nJakiś tekst w pierwszej linii.\nDruga linia.'

plik.write(tekst_do_zapisania)
