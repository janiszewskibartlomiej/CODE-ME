import sqlite3

conn = sqlite3.connect('baza.db')

c = conn.cursor()

zapytanie = """
CREATE TABLE "produkty" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"	TEXT,
    "cena"	REAL,
    "jednostka"	TEXT,
    "promocja"	INTEGER DEFAULT 0
);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
