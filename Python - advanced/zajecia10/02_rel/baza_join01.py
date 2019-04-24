import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * 
FROM "zespoly" 
JOIN "muzycy" ON "zespoly"."id" = "muzycy"."zespol_id";
"""

c.execute(zapytanie)

for linia in c:
    print(linia)

conn.close()
