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

    context = {'przedmioty': przedmioty}

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
