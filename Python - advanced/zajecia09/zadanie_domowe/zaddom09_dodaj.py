# BARTLOMIEJ JANISZEWSKI
import sqlite3

conn = sqlite3.connect('zaddom09.db')
c = conn.cursor()

zapytanie = """
INSERT INTO 'plecak' ('id', 'nazwa', 'rodzaj', 'ilosc', 'waga') 
VALUES (NULL, :nazwa, :rodzaj, :ilosc, :waga);
"""

while True:
    try:
        nazwa = input('Podaj nazwę przedmiotu: ')
        ilosc = int(input(f'Ile {nazwa} dołożyć do plecaka: '))
        waga = float(input(f'Waga jednej sztuki {nazwa}: '))
        rodzaj = input('[s]przęt czy [j]edzenie? ')
        if rodzaj not in ['s', 'sprzet', 'j', 'jedzenie']:
            print('Wprowadzono będne dane, proszę spróbowac jeszcze raz')
            continue
        if rodzaj in ['s', 'sprzet', 'j', 'jedzenie']:
            if rodzaj == 's':
                rodzaj = 'sprzet'
            elif rodzaj == 'j':
                rodzaj = 'jedzenie'
        wybrany_rodzaj = rodzaj
        break
    except ValueError:
        print('Wprowadzono będne dane, proszę spróbowac jeszcze raz')
        continue

przedmiot = {'nazwa': nazwa, 'rodzaj': wybrany_rodzaj, 'ilosc': ilosc, 'waga': waga}
print(przedmiot)

c.execute(zapytanie, przedmiot)

conn.commit()
conn.close()