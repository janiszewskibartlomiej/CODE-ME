import sqlite3

from flask import Flask, render_template, request, session, redirect, flash, get_flashed_messages
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'


def get_connection():
    conn = sqlite3.connect('baza.db')
    conn.row_factory = sqlite3.Row
    return conn


def login_required(view):
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect('/login')

    return wrapped_view


@app.route('/')
@login_required
def index():
    id = session.get('user_id')
    username = session.get('username')
    is_admin = session.get('is_admin')

    conn = get_connection()
    c = conn.cursor()

    if is_admin:
        result = c.execute('SELECT * FROM data')
    else:
        result = c.execute('SELECT * FROM data WHERE user_id = ?', (id,))

    przedmioty = result.fetchall()

    context = {
        'username': username,
        'przedmioty': przedmioty,
        'is_admin': is_admin
    }

    return render_template('index.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        result = c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = result.fetchone()

        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']
                session['is_admin'] = bool(user_data['is_admin'])
                return redirect('/')

        flash('błędna nazwa użytkownika lub hasło')
        return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
