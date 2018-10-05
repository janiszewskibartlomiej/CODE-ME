from random import choices

import string

def generuj_kod(ilosc_znakow=8):
    znaki = string.ascii_letters + string.digits
    haslo = ''.join(choices(znaki, k=ilosc_znakow))
    return haslo

nowe_haslo = generuj_kod(10)
print(nowe_haslo)