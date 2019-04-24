import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# "Ile jest produktów w promocji?"

zapytanie = """
SELECT COUNT(*) FROM produkty WHERE promocja = 1;
"""

c.execute(zapytanie)

print(c.fetchall())

conn.close()
