from flask import Flask, render_template
import json

app = Flask(__name__)


def pobierz_dane():
    with open('ludzie.json') as f:
        return json.load(f)


@app.route('/')
def index():
    lista_osob = pobierz_dane()
    return render_template('lista.html', lista_osob=lista_osob)


@app.route('/osoba/<int:indeks>')
def osoba(indeks):
    lista_osob = pobierz_dane()

    context = {}
    for x in lista_osob:
        if indeks == x['id']:
            context.update(x)
            break
        #     context.update(no_id=f'Brak osoby o id: {indeks}')

    return render_template('osoba.html', **context, index=indeks)


if __name__ == '__main__':
    app.run(debug=True)
