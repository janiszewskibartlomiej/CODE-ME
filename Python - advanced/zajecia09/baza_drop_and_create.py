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
"""

c.executescript(dwa_zapytania)

conn.commit()
conn.close()
