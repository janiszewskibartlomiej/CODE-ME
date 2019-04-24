import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
INSERT INTO 'produkty' ('nazwa', 'cena', 'jednostka') 
VALUES (:nazwa, :cena, :jednostka);
"""

produkt = {'nazwa': 'Gruszki', 'cena': 2.99, 'jednostka': 'kg', 'promocja': True}

c.execute(zapytanie, produkt)

conn.commit()
conn.close()
