from duzy_sklep import slodycze, warzywa_i_owoce
from funkcje_sklep import wypisz_artykuly, dodaj_artykul, zmien_cene, podaj_cene

wypisz_artykuly(slodycze)
podaj_cene('czekolada', slodycze)
zmien_cene('czekolada', 3.99, slodycze)
podaj_cene('czekolada', slodycze)
dodaj_artykul('baton', 1.99, slodycze)
wypisz_artykuly(slodycze)

wypisz_artykuly(warzywa_i_owoce)
