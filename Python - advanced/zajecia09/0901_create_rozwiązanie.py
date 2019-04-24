import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
CREATE TABLE "zwierzaki" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "imie"	TEXT NOT NULL,
    "gatunek"	TEXT,
    "wiek"	REAL
);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
