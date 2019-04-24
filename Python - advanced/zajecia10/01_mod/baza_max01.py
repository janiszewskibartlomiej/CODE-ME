import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# "Jaki jest najdroższy przedmiot w bez promocji, jaki w promocji?"

zapytanie = """
SELECT promocja, MAX(cena) FROM produkty GROUP BY promocja;
"""

c.execute(zapytanie)

print(c.fetchall())

conn.close()
