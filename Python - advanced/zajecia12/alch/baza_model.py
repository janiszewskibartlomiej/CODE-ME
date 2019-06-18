from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Produkt(Base):
    __tablename__ = 'produkty'

    id = Column(Integer, primary_key=True)
    nazwa = Column(String(255))
    cena = Column(Float)
    jednostka = Column(String(255))
    promocja = Column(Boolean(), default=False)
