lista = [1, 2, 'jakiś tekst', True, None, [1, 2, 3]]

print(enumerate(lista))

for index, element in enumerate(lista):
    print('index:', index, ', element:', element, ', typu:', type(element))
#
# for element in lista:
#   print('index:', lista.index(element), ', element:',
#        element, ', typu:', type(element))
