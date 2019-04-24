import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
UPDATE "produkty" SET "promocja" = ? WHERE "nazwa" = 'Cytryny' ;
"""

czy_promocja = True  # typ bool jest dobrze interpretowany

c.execute(zapytanie, (czy_promocja,))

conn.commit()
conn.close()
