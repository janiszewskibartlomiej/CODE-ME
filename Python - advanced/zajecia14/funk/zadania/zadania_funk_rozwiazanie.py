# zadanie 1

lista = [-10, -7, 0.5, 3, 101]

wynik = map(lambda x: x ** 2, lista)

print(list(wynik))

# zadanie 2

zespoly = ['AFC Bournemouth', 'ARSENAL', 'Brighton & Hove Albion', 'Burnley', 'Cardiff City', 'CHELSEA',
           'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leicester City', 'LIVERPOOL', 'MANCHESTER CITY',
           'MANCHESTER UNITED', 'Newcastle United', 'Southampton', 'TOTTENHAM HOTSPUR', 'Watford', 'West Ham United',
           'WOLVERHAMPTON WANDERERS']

wynik = filter(lambda x: 'ham' in x.lower(), zespoly)

print(list(wynik))

# zadanie 3

wynik = filter(lambda x: len(x.split()) == 1, zespoly)

print(list(wynik))
