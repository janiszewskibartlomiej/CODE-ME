from random import choices

import string

#print(string.ascii_letters, string.digits)

znaki = string.ascii_letters + string.digits

print(znaki)

#print(choices(string.ascii_letters, k=8))

haslo = ''.join(choices(znaki, k=8))
print(haslo)