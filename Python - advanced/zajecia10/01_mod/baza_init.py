import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

with open('db_init.sql', encoding='utf-8') as f:
    zapytanie = f.read()
c.executescript(zapytanie)

conn.commit()
conn.close()
