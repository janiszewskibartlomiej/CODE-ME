from panstwa import panstwa

# Państwa o nazwie dłuższej niż 13 znaków
wynik1 = [nazwa for nazwa in panstwa if len(nazwa) > 13]
# print(wynik1)

# Lista pierwszych sześciu znaków nazw państw
wynik2 = [nazwa[:6] for nazwa in panstwa]
print(wynik2)

