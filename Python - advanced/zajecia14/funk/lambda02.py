ludzie = ['Jakub Malinowski',
          'Jadwiga Brzezińska',
          'Roman Sawicki',
          'Marcin Szymczak',
          'Joanna Baranowska',
          'Maciej Szczepański',
          'Czesław Wróbel',
          'Grażyna Górska',
          'Wanda Krawczyk',
          'Renata Urbańska']

# UWAGA! Poniższa linijka jest poprawna, ale zaprzecza idei funkcji anonimowych. Nie powinno się pisać takiego kodu!
zwroc_nazwisko = lambda s: s.split()[1]

posortowani_ludzie = sorted(ludzie, key=zwroc_nazwisko)

print(posortowani_ludzie)
