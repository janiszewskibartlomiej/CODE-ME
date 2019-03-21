a = 'tekst'
b = a

print(a, id(a))
print(b, id(b))

a = 'inny tekst'

print(a, id(a))
print(b, id(b))
