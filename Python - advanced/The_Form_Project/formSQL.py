import datetime
import json
import sqlite3
import time
import hashlib

from flask import Flask, render_template, request, redirect, session, get_flashed_messages, flash

app = Flask(__name__)

with open('session_key.txt', 'r') as f:
    key = f.readline()
app.secret_key = key


def get_connection():
    conn = sqlite3.connect('questionDataBase.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    if not session:
        return redirect('/login')

    id = session.get('user_id')
    user = session.get('user')
    return redirect('/formularz')


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('log_in.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        print(username)
        print(password)
        password = password.encode()

        password = hashlib.sha256(password)
        password = password.digest()

        zapytanie_password = """
            SELECT id, user, password FROM "login" WHERE user = ?;
            """
        c.execute(zapytanie_password, (username,))
        line_from_base = c.fetchone()

        if line_from_base == None or line_from_base[1] is not username:
            flash('błędna nazwa użytkownika lub hasło')
            return redirect('/login')
        
        print('hasła:', password, list(line_from_base))

        if line_from_base[2] and password == line_from_base[2]:
            session['user_id'] = line_from_base[0]
            session['user'] = line_from_base[1]

            return redirect('/formularz')


@app.route('/formularz', methods=['GET', 'POST'])
def formularz():
    if session:
        return render_template('input_question.html')

    return redirect('/')


@app.route('/dodaj', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        conn = sqlite3.connect('questionDataBase.db')
        c = conn.cursor()
        question = request.form['question']
        autor = 'test'
        # yes = request.form['answer_yes']
        # no = request.form['answer_no']
        # dknow = request.form['answer_dknow']
        # discribe = request.form['answer_discribe']
        # print(question, yes, no, dknow, discribe)

        dodaj_pytanie = """
        INSERT INTO "questions" ("id", "tworca", "pytanie", "typ") VALUES (NULL, ?, ?,'tn')"""

        parametry = (autor, question)
        print(parametry)

        c.execute(dodaj_pytanie, parametry)
        conn.commit()
        return redirect('/dodaj')

    if request.method == 'GET':
        return render_template('input_question.html')


@app.route('/baza')
def data():
    conn = sqlite3.connect('questionDataBase.db')
    c = conn.cursor()
    zapytanie = """
    SELECT id, pytanie FROM "questions";
    """
    c.execute(zapytanie)
    pytania = c.fetchall()
    # print(pytania)
    slownik = {}
    for x in pytania:
        # print(x)
        dodaj_do_slownika = {x[0]: x[1]}
        slownik.update(dodaj_do_slownika)
    # print(slownik)
    context = {'pytania': slownik}
    return render_template('data.html', **context)


@app.route('/usun')
def delete():
    conn = sqlite3.connect('questionDataBase.db')
    c = conn.cursor()
    zapytanie = """
        DELETE FROM "questions" WHERE id = ?;
        """
    usun = request.args.get('id')
    # print(usun)
    c.execute(zapytanie, (usun,))
    conn.commit()

    return redirect('/baza')


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
