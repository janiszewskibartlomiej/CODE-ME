from string import ascii_lowercase, digits
from random import choices, choice

znaki = ascii_lowercase + digits

haslo = choices(znaki, k=8)
haslo = ''.join(haslo)

print(haslo)