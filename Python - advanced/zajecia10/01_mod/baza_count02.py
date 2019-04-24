import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# "Ile jest produktów bez promocji? Ile jest produktów w promocji?"

zapytanie = """
SELECT promocja, COUNT(*) FROM produkty GROUP BY promocja;
"""

c.execute(zapytanie)

print(c.fetchall())

conn.close()
