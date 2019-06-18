import sqlite3

conn = sqlite3.connect('baza_rozwiazanie.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('01_db_init_rozwiazanie_zadania.sql')

conn.commit()

conn.close()
