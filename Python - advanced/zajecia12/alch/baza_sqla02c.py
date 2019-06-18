from baza_model import Base

from sqlalchemy import create_engine, text

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')

    with engine.connect() as con:
        zapytanie = text("""
        INSERT INTO "produkty"
        VALUES (NULL, 'Karkówka bez kości', 8.99, 'kg', 1);
        """)

        con.execute(zapytanie)
