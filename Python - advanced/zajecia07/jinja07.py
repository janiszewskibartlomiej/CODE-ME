from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'), trim_blocks=True)
# template = env.get_template('template07.txt')
# template = env.get_template('template07b.txt')
template = env.get_template('template07c.txt')

produkty = [
    {'nazwa': 'Karkówka bez kości', 'cena': 8.99, 'jednostka': 'kg', 'promocja': True},
    {'nazwa': 'Twaróg sernikowy 1kg', 'cena': 5.99, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Mleko Świeże 2%', 'cena': 1.99, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Herbata torebki 200g', 'cena': 9.99, 'jednostka': 'op', 'promocja': False},
    {'nazwa': 'Czekolada', 'cena': 2.49, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Gruszki', 'cena': 2.99, 'jednostka': 'kg', 'promocja': True},
    {'nazwa': 'Cytryny', 'cena': 4.99, 'jednostka': 'kg', 'promocja': False},
]

context = {'produkty': produkty}

wyrenderowany_tekst = template.render(context)

print(wyrenderowany_tekst)
