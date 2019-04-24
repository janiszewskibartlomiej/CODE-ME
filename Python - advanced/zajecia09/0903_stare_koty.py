import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
SELECT IMIE, WIEK FROM zwierzaki WHERE wiek > 7 ORDER BY wiek;
"""

c.execute(zapytanie)

for zwierzak in c:
    print(zwierzak)
conn.close()
