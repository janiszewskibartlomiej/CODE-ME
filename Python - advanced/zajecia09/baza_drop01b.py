import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_create02.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# nie wyrzuci błędu, jeśli tabela nie istnieje
zapytanie = "DROP TABLE IF EXISTS 'produkty'"

c.execute(zapytanie)

conn.commit()
conn.close()
