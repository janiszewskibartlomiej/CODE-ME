from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))
template = env.get_template('template06.txt')

# wybrane zespoły z Premier League, stan na: 2.04.2019
zespoly = [{'position': 1, 'name': 'Liverpool', 'goals_for': 72, 'goals_against': 19},
           {'position': 2, 'name': 'Manchester City', 'goals_for': 81, 'goals_against': 21},
           {'position': 9, 'name': 'Leicester City', 'goals_for': 42, 'goals_against': 43},
           {'position': 16, 'name': 'Southampton', 'goals_for': 35, 'goals_against': 50}]

context = {'zespoly': zespoly}

wyrenderowany_tekst = template.render(context)
print(wyrenderowany_tekst)
