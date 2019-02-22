from string import ascii_lowercase, digits
from random import choices, choice


def generuj_haslo(ile_znakow=8):
    global haslo
    znaki = ascii_lowercase + digits
    haslo = choices(znaki, k=ile_znakow)
    haslo = ''.join(haslo)
    return haslo

nowe_haslo = generuj_haslo()
print(nowe_haslo)

nowe_haslo = generuj_haslo(10)
print(nowe_haslo)