from geometria import pole_kola, pole_prostokata, WARTOSC_PI

print('Pole prostokonta o bokach {} i {} wynosi: {:.2f}'.format(7.5, 8.3, pole_prostokata(7.5, 8.3)))
print()
print('Pole prostokonta o bokach {} i {} wynosi: {}'.format(4, -3, pole_prostokata(4, -3)))
print()
print('Pole koła o premieniu {} wynosi: {:.2f}, dla PI={}'.format(3.57, pole_kola(3.57), WARTOSC_PI))

