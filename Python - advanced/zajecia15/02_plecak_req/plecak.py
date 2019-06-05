import requests
from flask import Flask, render_template, request, redirect, abort

from api import api_bp
from db import get_connection

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def index():
    r = requests.get(f'{request.base_url}api/przedmioty')

    dane = r.json()

    return render_template('index.html', **dane)


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'GET':
        return render_template('dodaj.html')

    if request.method == 'POST':
        nazwa = request.form['nazwa']
        ilosc = request.form['ilosc']
        waga = request.form['waga']

        # tutaj powinna być walidacja powyższych wartości

        conn = get_connection()
        c = conn.cursor()

        zapytanie = 'INSERT INTO "plecak" ("nazwa", "rodzaj", "ilosc", "waga") VALUES (?, "jedzenie", ?, ?)'
        parametry = (nazwa, ilosc, waga)

        c.execute(zapytanie, parametry)
        conn.commit()

        return redirect('/')


@app.route('/usun', methods=['GET', 'POST'])
def usun():
    if request.method == 'GET':
        return render_template('usun.html')

    if request.method == 'POST':
        id = request.form['id']

        conn = get_connection()
        c = conn.cursor()

        zapytanie = 'DELETE FROM "plecak" WHERE id = ?'
        parametry = (id,)

        c.execute(zapytanie, parametry)
        conn.commit()

        if c.rowcount != 1:
            abort(404, {'message': f"Nie można usunąć przedmiotu o id:{id}"})

        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
