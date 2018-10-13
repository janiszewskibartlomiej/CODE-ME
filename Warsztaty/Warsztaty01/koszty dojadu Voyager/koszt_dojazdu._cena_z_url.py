import html

url_strony = 'https://www.e-petrol.pl/notowania/rynek-krajowy/ceny-stacje-paliw'

xpath_lpg = '/html/body/div[2]/div/div[3]/div[3]/div[1]/div[1]/table/tbody/tr/td[6]'

#strona_lpg = open(url_strony)

cena_lpg = xpath_lpg(url_strony)

spalanie_na_trasie = 17

spalanie_w_mieście = 20

spalanie_srednie = (spalanie_na_trasie + spalanie_w_mieście) / 2

while True:
    odpowiedz = input('Wpisz ile przejedziesz kilometów: ')

    try:
        ilosc_kilometrow = int(odpowiedz)
        break
    except ValueError:
        print('Wpisana wartość nie jest liczbą!')
        continue

while True:
    odpowiedz2 = input('Podaj cenę LPG w formacie X.X:')

    try:
        cena_lpg = float(odpowiedz2)
        break
    except ValueError:
        print('Wpisana wielkość nie jest liczbą!')
        continue

wynik_trasa = (((ilosc_kilometrow / 100) * spalanie_na_trasie) * cena_lpg)
wynik_miasto = (((ilosc_kilometrow / 100) * spalanie_w_mieście) * cena_lpg)
wynik_srd = (((ilosc_kilometrow / 100) * spalanie_srednie) * cena_lpg)

print()
print('Koszt przejazdu {} km na trasie to: {:.2f}'.format(ilosc_kilometrow, wynik_trasa))
print()
print('Koszt przejazdu {} km w mieście to: {:.2f}'.format(ilosc_kilometrow, wynik_miasto))
print()
print('Koszt przejazdu {} km w cyklu mieszanym to: {:.2f}'.format(ilosc_kilometrow, wynik_srd))

