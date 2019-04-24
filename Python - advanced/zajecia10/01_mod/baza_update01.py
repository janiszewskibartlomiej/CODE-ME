import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
UPDATE "produkty" SET "promocja" = 0 WHERE "nazwa" = 'Gruszki' ;
"""

c.execute(zapytanie)

conn.commit()
conn.close()
