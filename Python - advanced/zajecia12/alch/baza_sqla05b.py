from sqlalchemy.orm import sessionmaker

from baza_model2 import Produkt

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    wynik = session.query(Produkt) \
        .filter(Produkt.id == 2) \
        .update({'nazwa': 'Karkówka z kością'})

    print('Ilość zmodyfikowanych wierszy:', wynik)  # wynikiem jest ile wierszy zostało zmodyfikowanych

    session.commit()
