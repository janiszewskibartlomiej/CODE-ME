import sqlite3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('plecak_baza.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM "plecak"')
    przedmioty = result.fetchall()

    # liczenie sumy
    suma = 0
    for przedmiot in przedmioty:
        if przedmiot['waga']:
            suma += przedmiot['ilosc'] * przedmiot['waga']

    context = {'przedmioty': przedmioty, 'suma': suma}

    return render_template('index.html', **context)


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


if __name__ == '__main__':
    app.run(debug=True)
