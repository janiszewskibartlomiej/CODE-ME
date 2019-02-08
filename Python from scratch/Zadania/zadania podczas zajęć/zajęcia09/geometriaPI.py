def pole_prostokonta(a, b):
    if a < 0 or b < 0:
        return None
    else:
        pole = a * b
        return pole

import math
WARTOSC_PI = math.pi

def pole_kola(r):
    if r >= 0:
        pole = WARTOSC_PI * r ** 2
        return pole
    else:
         return None