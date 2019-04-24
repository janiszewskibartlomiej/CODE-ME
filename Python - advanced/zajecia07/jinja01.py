from jinja2 import Template

template = Template("Mądrość na dziś to: '{{ fraza }}'")

wynik = template.render(fraza="Now is better than never.")  # PEP20 "Zen of Python"

print(wynik)
