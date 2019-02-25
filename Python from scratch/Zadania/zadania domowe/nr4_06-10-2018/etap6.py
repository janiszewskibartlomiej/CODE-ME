from etap_1_2_3_4 import czy_jest_zwyciezca, chybil_trafil, dodaj_zaklad, moj_zaklad

wszystkie_zaklady = []
#print(wszystkie_zaklady)

moje_liczby = [2,6,0,10]


zwycieskie_liczby = chybil_trafil()


dodaj_zaklad(moje_liczby, wszystkie_zaklady)

for r in range(100):
    dodaj_zaklad(chybil_trafil(), wszystkie_zaklady)

print(f'Zwycięskie liczby dzisiaj to: {zwycieskie_liczby}')

if moje_liczby == wszystkie_zaklady:
    print('Moje liczby wygrały')

print('Lista zakładów : {}'.format(wszystkie_zaklady))

czy_jest_zwyciezca(zwycieskie_liczby, wszystkie_zaklady)