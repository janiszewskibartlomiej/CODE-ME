panstwa = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
           'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
           'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco',
           'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia and Montenegro',
           'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']

DLUGOSC = 10


# map + funkcja

def skracaj(nazwa, dlugosc=DLUGOSC):
    return nazwa[:dlugosc]


skrocone = map(skracaj, panstwa)
print(list(skrocone))

# map + lambda

skrocone = map(lambda x: x[:DLUGOSC], panstwa)
print(list(skrocone))

# list comprehension

skrocone = [x[:DLUGOSC] for x in panstwa]
print(skrocone)
