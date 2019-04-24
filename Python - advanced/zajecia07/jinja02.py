# Jest bardzo ważny powód, dlaczego ten plik nie nazywa się jinja2.py

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))

template = env.get_template('template02.txt')

wyrenderowany_tekst = template.render(fraza="Now is better than never.")  # PEP20 "Zen of Python"

print(wyrenderowany_tekst)
