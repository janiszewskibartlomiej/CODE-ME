import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT instrumenty.instrument FROM instrumenty JOIN beatles ON beatles.id = instrumenty.muzyk_id WHERE beatles.imie = ?;
"""

imie = input("Podaj imię Beatlesa: ")


c.execute(zapytanie, (imie,))

instrumenty = c.fetchall()

if instrumenty:
    print(f'{imie} gra na: ')
    for linia in instrumenty:
        print('-', linia[0])
else:
    print('Najwyraźniej nie ma takiego Beatlesa :)')

conn.close()
