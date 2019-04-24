import sqlite3

conn = sqlite3.connect('baza.db')

c = conn.cursor()

zapytanie = """
CREATE TABLE "produkty" (
    "nazwa"	TEXT,
    "cena"	REAL,
    "jednostka"	TEXT,
    "promocja"	INTEGER DEFAULT 0
);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
