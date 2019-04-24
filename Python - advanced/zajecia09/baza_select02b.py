import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
conn.row_factory = sqlite3.Row  # tutaj zmieniamy to, co otrzymujemy w wyniku `execute`
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty;
"""

c.execute(zapytanie)

produkty = c.fetchall()
print(produkty)

print(produkty[0]['nazwa'])

conn.close()
