from model import Wydatek
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    id = input('Podaj id użytkownika: ')

    engine = create_engine('sqlite:///zadanie_baza.db')
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    wynik = session.query(Wydatek) \
        .filter(Wydatek.id_uzytkownika == id) \
        .all()
    # tutaj pobierz wydatki i wypisz je na ekran
    print(f'Wydytki użytkownika nr {id} to:')
    for w in wynik:
        print(w.nazwa, end=" ")

    print()
    print('Wprowadzanie nowego wydatku')
    nazwa = input('Podaj nazwę: ')
    kwota = float(input('Podaj kwotę: '))

    dodanie = Wydatek(id_uzytkownika=id, nazwa=nazwa, kwota=kwota)
    session.add(dodanie)
    # tutaj dodaj nowy wydatek w bazie
    session.commit()
    print(f'Dodano {nazwa} do wydatków użytkownika {id}')
