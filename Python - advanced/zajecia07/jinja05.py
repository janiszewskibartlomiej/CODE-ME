from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))

# template = env.get_template('template05.txt')
template = env.get_template('template05b.txt')

ludzie = [{'imie': 'Alojzy', 'nazwisko': 'Abacki'},
          {'imie': 'Barbara', 'nazwisko': 'Babacka'},
          {'imie': 'Celina', 'nazwisko': 'Cabacka'},
          {'imie': 'Dariusz', 'nazwisko': 'Dabacki'}]

context = {'ludzie': ludzie}

wyrenderowany_tekst = template.render(context)
print(wyrenderowany_tekst)
