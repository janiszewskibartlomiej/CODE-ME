import sqlite3

from flask import Flask, render_template

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

    suma = 0
    for i in przedmioty:
        if i['waga'] is not None:
            suma = suma + i['waga'] * i['ilosc']
            suma = round(suma, 4)


    context = {'przedmioty': przedmioty, 'suma' : suma}

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
