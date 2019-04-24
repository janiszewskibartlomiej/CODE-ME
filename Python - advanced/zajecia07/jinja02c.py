from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))

template = env.get_template('template02.txt')

context = {'fraza': "Now is better than never."}

wyrenderowany_tekst = template.render(context)  # składnia bez rozpakowania nie zadziała we Flasku

print(wyrenderowany_tekst)
