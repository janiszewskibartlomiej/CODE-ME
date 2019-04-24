import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
DELETE FROM "produkty" WHERE "id" = 1;
"""

c.execute(zapytanie)

conn.commit()
conn.close()
