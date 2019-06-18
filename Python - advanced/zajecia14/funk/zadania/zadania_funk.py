# zadanie 1

lista = [-10, -7, 0.5, 3, 101]

lista_kwadratow = map(lambda x: x ** 2, lista)
print(list(lista_kwadratow))
print()

# zadanie 2

zespoly = ['AFC Bournemouth', 'ARSENAL', 'Brighton & Hove Albion', 'Burnley', 'Cardiff City', 'CHELSEA',
           'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leicester City', 'LIVERPOOL', 'MANCHESTER CITY',
           'MANCHESTER UNITED', 'Newcastle United', 'Southampton', 'TOTTENHAM HOTSPUR', 'Watford', 'West Ham United',
           'WOLVERHAMPTON WANDERERS']

zespoly_ham = filter(lambda x: 'ham' in x.lower(), zespoly)
print(list(zespoly_ham))
print()

# zadanie 3

zespoly_jednoczlonowe = filter(lambda x: len(x.split()) == 1, zespoly)
print(list(zespoly_jednoczlonowe))