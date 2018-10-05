from random import choices

import string

print(string.ascii_letters)

#print(choices(string.ascii_letters, k=8))

haslo = ''.join(choices(string.ascii_letters, k=8))
print(haslo)