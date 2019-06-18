from model import Base, Wydatek

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def wstaw_przykladowe_dane(engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    wydatki = [
        Wydatek(id_uzytkownika=1, nazwa='Jedzenie', kwota=10.50),
        Wydatek(id_uzytkownika=1, nazwa='Rozrywka', kwota=30.20),
        Wydatek(id_uzytkownika=1, nazwa='Transport', kwota=4.20),
        Wydatek(id_uzytkownika=2, nazwa='Jedzenie', kwota=70.23),
        Wydatek(id_uzytkownika=2, nazwa='Transport', kwota=8.40),
        Wydatek(id_uzytkownika=1, nazwa='Jedzenie', kwota=22.90),
        Wydatek(id_uzytkownika=2, nazwa='Rozrywka', kwota=52),
        Wydatek(id_uzytkownika=1, nazwa='Naprawy', kwota=120),
    ]

    session.bulk_save_objects(wydatki)
    session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///zadanie_baza.db')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)  # stworzenie bazy

    wstaw_przykladowe_dane(engine)
