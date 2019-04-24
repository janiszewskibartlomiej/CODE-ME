import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
INSERT INTO 'produkty' ('nazwa', 'cena', 'jednostka') 
VALUES ('Herbata DELUXE torebki 100g', ?, 'op');
"""

cena = 105.99

c.execute(zapytanie, (cena,))

conn.commit()
conn.close()
