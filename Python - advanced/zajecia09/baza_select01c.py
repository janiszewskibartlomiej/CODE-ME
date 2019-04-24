import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty;
"""

c.execute(zapytanie)

print(c.fetchone())  # tutaj bierzemy jeden
print('---')
print(c.fetchall())  # tutaj bierzemy wszystkie POZOSTAŁE

conn.close()
