from sqlalchemy.orm import sessionmaker

from baza_model import Base, Produkt

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    produkty = [
        Produkt(nazwa='Mleko Świeże 2%', cena=1.99, jednostka='op', promocja=True),
        Produkt(nazwa='Karkówka bez kości', cena=8.99, jednostka='kg', promocja=True),
        Produkt(nazwa='Twaróg sernikowy 1000g', cena=5.99, jednostka='op', promocja=True),
        Produkt(nazwa='Ser w plasterkach', cena=5.49, jednostka='op'),
        Produkt(nazwa='Herbata torebki 200g', cena=9.99, jednostka='op'),
        Produkt(nazwa='Cytryny', cena=7.99, jednostka='kg'),
        Produkt(nazwa='Gruszki', cena=2.99, jednostka='kg', promocja=True),
        Produkt(nazwa='Czekolada', cena=2.49, jednostka='op', promocja=True),
    ]

    session.bulk_save_objects(produkty)
    session.commit()
