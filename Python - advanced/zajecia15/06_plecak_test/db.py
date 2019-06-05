import sqlite3


def get_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def create_db(db_file):
    conn = get_connection(db_file)
    c = conn.cursor()

    def wykonaj_skrypt_sql(skrypt):
        with open(skrypt, encoding='utf-8') as f:
            zapytanie = f.read()
        c.executescript(zapytanie)

    wykonaj_skrypt_sql('01_db_init.sql')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db('plecak_baza.db')
