import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
DROP TABLE IF EXISTS 'zwierzaki';

CREATE TABLE 'zwierzaki' (
    'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    'imie'	TEXT NOT NULL,
    'gatunek'	TEXT,
    'wiek'	REAL
);
"""

c.executescript(zapytanie)  # executescript, a nie execute!

conn.commit()
conn.close()
