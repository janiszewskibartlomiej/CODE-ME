from sqlalchemy.orm import sessionmaker

from baza_model import Produkt

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    nowy_produkt = Produkt(nazwa='Mleko Świeże 2%',
                           cena=1.99,
                           jednostka='op')

    # uwaga! autoincrement dostajemy "za darmo"

    session.add(nowy_produkt)
    session.commit()
