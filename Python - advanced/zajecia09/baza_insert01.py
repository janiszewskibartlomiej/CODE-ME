import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = "INSERT INTO 'produkty' VALUES (NULL, 'Karkówka bez kości', 8.99, 'kg', NULL)"

c.execute(zapytanie)

conn.commit()
conn.close()
