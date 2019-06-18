from sqlalchemy.orm import sessionmaker

from baza_model2 import Base, Produkt

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    wynik = session.query(Produkt) \
        .filter(Produkt.jednostka == 'kg') \
        .filter(Produkt.promocja == True) \
        .all()

    print(wynik)
