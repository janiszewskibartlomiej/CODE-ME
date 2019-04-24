import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')  # tutaj utwórz połączenie z bazą

c = conn.cursor()

zapytanie = """
    CREATE TABLE "zwierzaki" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "imie"	TEXT,
    "gatunek"	TEXT,
    "wiek"	REAL
    
);
"""  # tutaj stwórz zapytanie, które utworzy bazę danych

c.execute(zapytanie)

conn.commit()
conn.close()
