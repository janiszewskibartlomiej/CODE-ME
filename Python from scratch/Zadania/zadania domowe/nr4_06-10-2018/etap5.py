from etap_1_2_3_4 import czy_jest_zwyciezca, chybil_trafil, dodaj_zaklad, moj_zaklad

wszystkie_zaklady = []
print(wszystkie_zaklady)

dodaj_zaklad(moj_zaklad, wszystkie_zaklady)

for r in range(10):
    dodaj_zaklad(chybil_trafil(), wszystkie_zaklady)

print(wszystkie_zaklady)

czy_jest_zwyciezca(moj_zaklad, wszystkie_zaklady)