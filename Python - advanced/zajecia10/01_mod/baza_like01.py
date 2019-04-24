import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty WHERE nazwa LIKE '%ser%';
"""

c.execute(zapytanie)

print(c.fetchall())

conn.close()
