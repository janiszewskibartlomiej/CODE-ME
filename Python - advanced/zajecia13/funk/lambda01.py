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

posortowani_ludzie = sorted(ludzie, key=lambda s: s.split()[1])

print(posortowani_ludzie)
