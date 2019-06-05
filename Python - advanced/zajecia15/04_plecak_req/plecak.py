import requests
from flask import Flask, render_template, request, redirect, abort, get_flashed_messages, flash

from api import api_bp
from db import get_connection

app = Flask(__name__)
app.secret_key = 'q645$56a3w7s'
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def index():
    r = requests.get(f'http://{request.host}/api/przedmioty')

    dane = r.json()

    messages = get_flashed_messages()

    return render_template('index.html', **dane, messages=messages)


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'GET':
        return render_template('dodaj.html')

    if request.method == 'POST':
        nazwa = request.form['nazwa']
        ilosc = request.form['ilosc']
        waga = request.form['waga']

        payload = {'nazwa': nazwa, 'ilosc': ilosc, 'waga': waga}

        r = requests.post(f'http://{request.host}/api/przedmioty', json=payload)  # UWAGA! zmiana na json

        if not r.status_code == 201:
            flash('Nie udało się dodać przedmiotu')
        return redirect('/')


@app.route('/usun', methods=['GET', 'POST'])
def usun():
    if request.method == 'GET':
        return render_template('usun.html')

    if request.method == 'POST':
        id = request.form['id']
        print('id ze strony przekazane postem:', id)
        payload = {'id': id}

        r_del = requests.post(f'http://{request.host}/api/usun', json=payload)

        print('zapytanie:', r_del)

    if not r_del.status_code == 302:
        flash(f'Nie można usunąć przedmiotu o id:{id}')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
