from sqlalchemy.orm import sessionmaker

from baza_model import Produkt

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    nowy_produkt = Produkt()

    nowy_produkt.nazwa = 'Twaróg sernikowy 1000g'
    nowy_produkt.cena = 5.99
    nowy_produkt.jednostka = 'op'
    nowy_produkt.promocja = True

    session.add(nowy_produkt)
    session.commit()
