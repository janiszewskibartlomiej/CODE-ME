import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_create02.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# nie wyrzuci błędu, jeśli tabela nie istnieje
dwa_zapytania = """
DROP TABLE IF EXISTS 'produkty';

CREATE TABLE "produkty" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"	TEXT,
    "cena"	REAL,
    "jednostka"	TEXT,
    "promocja"	INTEGER DEFAULT 0
);

INSERT INTO 'produkty' 
VALUES 
    (NULL, 'Karkówka bez kości', 8.99, 'kg', 1), 
    (NULL, 'Twaróg sernikowy 1kg', 5.99, 'op', 1), 
    (NULL, 'Mleko Świeże 2%', 1.99, 'op', 1), 
    (NULL, 'Herbata torebki 200g', 9.99, 'op', 0), 
    (NULL, 'Czekolada', 2.49, 'op', 1), 
    (NULL, 'Gruszki', 2.99, 'kg', 1), 
    (NULL, 'Cytryny', 7.99, 'kg', 0);
"""

c.executescript(dwa_zapytania)

conn.commit()
conn.close()
