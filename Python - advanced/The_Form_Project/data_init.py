import sqlite3
from create_admin_account import create_admin
def wykonaj_skrypt_sql(skrypt='data_sql_creating.sql'):
    conn = sqlite3.connect('questionDataBase.db')
    c = conn.cursor()
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    wykonaj_skrypt_sql()
    create_admin()
