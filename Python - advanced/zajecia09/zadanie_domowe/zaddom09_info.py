# BARTŁOMIEJ JANISZEWSKI
import sqlite3

conn = sqlite3.connect('zaddom09.db')
c = conn.cursor()

zapytanie_sprzet = """
SELECT "nazwa" FROM PLECAK WHERE RODZAJ = 'sprzet' ORDER BY "nazwa";
"""

zapytanie_jedzenie = """
SELECT NAZWA FROM PLECAK WHERE RODZAJ = 'jedzenie' ORDER BY "nazwa";
"""

zapytanie_waga = """
SELECT SUM("waga") FROM "plecak";
"""

print('Sprzęt:')


c.execute(zapytanie_sprzet)
lista_sprzet = c.fetchall()
ile = len(lista_sprzet)
#print(lista_sprzet)

for sprzet in lista_sprzet:
    # print(sprzet)
    sprzet_pojedynczo = sprzet[0]
    print(sprzet_pojedynczo)
print()
print(f'Liczba sprzętów: {ile}')
print()

print('Jedzenie:')

c.execute(zapytanie_jedzenie)
lista_jedzenie = c.fetchall()
ile_jem = len(lista_jedzenie)
# print(lista_jedzenie)

for jedzenie in lista_jedzenie:
    # print(jedzenie)
    jedenie_pojedynczo = jedzenie[0]
    print(jedenie_pojedynczo)
print()
print(f'Liczba produktów do jedzenia: {ile_jem}')
print()
c.execute(zapytanie_waga)

suma = c.fetchmany()[0][0]

print(f'Waga zawartości: {suma*1000}g')

conn.close()