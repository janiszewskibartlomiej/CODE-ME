import datetime
import json
import sqlite3
import time
import hashlib


from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def log_in():
    return render_template('log_in.html')


@app.route('/formularz', methods=['POST'])
def formularz():
    conn = sqlite3.connect('questionDataBase.db')
    c = conn.cursor()
    username = request.form['username']

    password = request.form['password']
    print(username)
    print(password)
    password = password.encode()

    password = hashlib.sha256(password)
    password = password.digest()

    zapytanie_password = """
    SELECT password FROM "login" WHERE user = ?;
    """
    c.execute(zapytanie_password, (username,))
    password_base = c.fetchone()

    print('hasła:', password, password_base)

    if password_base and password == password_base[0]:
        # session['user_id'] = password_base['id']
        # session['username'] = password_base['username']

        return render_template('input_question.html')

    else:
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
    c.execute(zapytanie, (usun, ))
    conn.commit()


    return redirect('/baza')


if __name__ == "__main__":
    app.run(debug=True)
