import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# Brak WHERE powoduje, że UPDATE wykonany będzie dla wszystkich

zapytanie = """
UPDATE "produkty" SET "promocja" = 0;
"""

c.execute(zapytanie)

conn.commit()
conn.close()
