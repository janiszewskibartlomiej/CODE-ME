import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('00_drop_tables.sql')
wykonaj_skrypt_sql('01_beatles_init.sql')
wykonaj_skrypt_sql('02_instrumenty_init.sql')
# wykonaj_skrypt_sql('02_instrumenty_init_rozwiazanie.sql')

conn.commit()

conn.close()
