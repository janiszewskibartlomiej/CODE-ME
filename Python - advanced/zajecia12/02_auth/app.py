import sqlite3

from flask import Flask, render_template, request, session, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'


def get_connection():
    conn = sqlite3.connect('baza.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    if not session:
        return redirect('/login')

    id = session.get('user_id')
    username = session.get('username')
    return f'Witaj {username}, twoje id: {id}'


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
            password_from_db = user_data['password']

            if password_from_db == password:
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']
                return redirect('/')

        flash('błędna nazwa użytkownika lub hasło')
        return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
