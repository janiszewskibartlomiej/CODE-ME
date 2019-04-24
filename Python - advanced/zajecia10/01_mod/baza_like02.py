import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty WHERE nazwa LIKE ?;
"""

fraza = input("Podaj szukaną frazę: ")

fraza = f'%{fraza}%'

c.execute(zapytanie, (fraza,))

print(c.fetchall())

conn.close()
