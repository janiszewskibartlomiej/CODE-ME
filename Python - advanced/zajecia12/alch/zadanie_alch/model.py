import datetime

from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Wydatek(Base):
    __tablename__ = 'wydatki'

    id = Column(Integer, primary_key=True)
    id_uzytkownika = Column(Integer(), nullable=False)
    nazwa = Column(String())
    kwota = Column(Float(), nullable=False)
    data = Column(DateTime(), nullable=False, default=datetime.datetime.now())
