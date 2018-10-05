from sklep import slodycze

from sklep import warzywa_i_owoce

from funkcje_sklepy import wypisz_artykuly, podaj_cene, zmien_cene, dodaj_artykul

from random import choice
print()
wypisz_artykuly(slodycze)
podaj_cene('czekolada',slodycze)
print()
zmien_cene('czekolada', 3.99, slodycze)
print()
dodaj_artykul('baton', 1.99, warzywa_i_owoce)
print()
wypisz_artykuly(warzywa_i_owoce)

print(choice(slodycze))
