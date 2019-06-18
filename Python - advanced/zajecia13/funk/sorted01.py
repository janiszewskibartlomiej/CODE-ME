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


# sortowanie po nazwisku

def zwroc_nazwisko(czlowiek):
    nazwisko = czlowiek.split()[1]
    return nazwisko


posortowani_ludzie = sorted(ludzie, key=zwroc_nazwisko)

print(posortowani_ludzie)
