from string import ascii_letters, ascii_lowercase, digits, ascii_uppercase
from random import choices, choice


def generuj_haslo(ile_znakow=8, trudnosc=0):
    global haslo
    znaki = ascii_lowercase + digits + ascii_uppercase
    if trudnosc==2:
        haslo = choices(znaki, k=ile_znakow)
    elif trudnosc==1:
        haslo = choices(ascii_letters, k=ile_znakow)
    else:
        haslo = choices(ascii_lowercase, k=ile_znakow)
    haslo = ''.join(haslo)
    return haslo


print('------------------')

print(generuj_haslo(10,0))

print('------------------')

print(generuj_haslo(10,1))

print('------------------')

print(generuj_haslo(10,2))