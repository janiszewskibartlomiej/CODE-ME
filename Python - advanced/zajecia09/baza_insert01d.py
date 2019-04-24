import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
INSERT INTO 'produkty' ('nazwa', 'cena', 'jednostka') 
VALUES 
    ('Herbata torebki 200g', 5.99, 'op'),
    ('Cytryny', 7.99, 'op');
"""

c.execute(zapytanie)

conn.commit()
conn.close()
