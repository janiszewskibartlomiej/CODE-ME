import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty;
"""

c.execute(zapytanie)

produkty = c.fetchall()
print(produkty)

print('---')

print(produkty[0][1])

conn.close()
