liczba = int(input("Podaj liczbę naturalną: "))

lista_dzielnikow=[]

for dzielnik in range(1,liczba+1):
    if liczba % dzielnik == 0:
        lista_dzielnikow.append(dzielnik)
        #print('Liczba: ', liczba, 'jest podzielna przez', dzielnik)
print('Liczba: ', liczba, 'jest podzielna przez: ', lista_dzielnikow)

#

#mój pomysł
# lista_dzielnikow =[]
#
# liczba = int(input('Proszę podać liczbę: '))
#
# for dzielnik in range(1,100):
#     if liczba % dzielnik == 0:
#         lista_dzielnikow.append(dzielnik)
#         #print(f'liczba {liczba} jest podzielna przez: {dzielnik}')
#
# print(f'liczba {liczba} jest podzielna przez: {lista_dzielnikow}')