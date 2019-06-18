from model import Wydatek
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    engine = create_engine('sqlite:///zadanie_baza.db')
    DBSession = sessionmaker(bind=engine)
    return DBSession()


if __name__ == '__main__':
    id = input('Podaj id użytkownika: ')

    session = get_session()

    wydatki = session.query(Wydatek).filter(Wydatek.id_uzytkownika == id).all()

    for w in wydatki:
        print(w.nazwa, w.kwota, w.data)

    print()
    print('Wprowadzanie nowego wydatku')
    nazwa = input('Podaj nazwę: ')
    kwota = float(input('Podaj kwotę: '))

    nowy_wydatek = Wydatek(id_uzytkownika=id, nazwa=nazwa, kwota=kwota)
    session.add(nowy_wydatek)
    session.commit()

    print(f'Dodano {nazwa} do wydatków użytkownika {id}')
