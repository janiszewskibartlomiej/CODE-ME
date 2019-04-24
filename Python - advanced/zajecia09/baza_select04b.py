import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

zapytanie = """
SELECT * FROM produkty WHERE cena > ? AND cena < ? ORDER BY cena ASC;
"""

cena_min = input("Podaj dolny zakres ceny: ")
cena_max = input("Podaj górny zakres ceny: ")

c.execute(zapytanie, (cena_min, cena_max))

for produkt in c:
    print(produkt)

conn.close()
