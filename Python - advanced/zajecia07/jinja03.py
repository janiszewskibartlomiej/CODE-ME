from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))

# template = env.get_template('template03.txt')
template = env.get_template('template03b.txt')

lista_fraz = ['Beautiful is better than ugly.',
              'Explicit is better than implicit.',
              'Simple is better than complex.',
              'Complex is better than complicated.']

context = {'frazy': lista_fraz}

wyrenderowany_tekst = template.render(context)
print(wyrenderowany_tekst)
