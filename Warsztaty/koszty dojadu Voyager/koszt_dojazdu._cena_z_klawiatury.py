spalanie_na_trasie = 17

spalanie_w_mieście = 20

spalanie_srednie = (spalanie_na_trasie + spalanie_w_mieście) / 2

odpowiedz = input('Wpisz ile przejedziesz kilometów: ')

if not odpowiedz.isdigit() or odpowiedz == '':
    print('Wpisana ilość nie jest liczbą!')
    exit()

ilosc_kilometrow = int(odpowiedz)

odpowiedz2 = input('Podaj cenę LPG [użyj kropki zamiast przecinka]:')

if not odpowiedz2.isdecimal() or odpowiedz == '':
   print('Wpisana ilość nie jest liczbą!')
   exit()

cena_lpg = float(odpowiedz2)

wynik_trasa = round((((ilosc_kilometrow / 100 )* spalanie_na_trasie) * cena_lpg), 2)

wynik_miasto = round((((ilosc_kilometrow / 100 )* spalanie_w_mieście) * cena_lpg),2)

wynik_srd = round((((ilosc_kilometrow / 100 )* spalanie_srednie) * cena_lpg), 2)

print()
print('Koszt przejazdu {} km na trasie to: {}'.format(ilosc_kilometrow, wynik_trasa))
print()
print('Koszt przejazdu {} km w mieście to: {}'.format(ilosc_kilometrow, wynik_miasto))
print()
print('Koszt przejazdu {} km w cyklu mieszanym to: {}'.format(ilosc_kilometrow, wynik_srd))
print()
