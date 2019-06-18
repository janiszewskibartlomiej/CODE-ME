from baza_model import Base

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///baza.db')
    Base.metadata.create_all(engine)  # stworzenie bazy
