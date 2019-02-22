from string import ascii_lowercase
from random import choices, choice


# rozwiązanie 1, ok
haslo = ''
for i in range(8):
    haslo += choice(ascii_lowercase)

print(haslo)

# rozwiązanie 2, lepiej
haslo = []
for i in range(8):
    haslo.append(choice(ascii_lowercase))
haslo = ''.join(haslo)

print(haslo)

# rozwiązanie 3, najlepiej
haslo = choices(ascii_lowercase, k=8)
haslo = ''.join(haslo)

print(haslo)