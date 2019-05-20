import datetime
import json
import sqlite3
import time
import hashlib

from flask import Flask, render_template, request, redirect, session, get_flashed_messages, flash

app = Flask(__name__)

with open('session_k.txt', 'r') as f:
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
    return redirect('/wpisz_pytanie')


@app.route('/registerghuewrdb', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        validator = get_flashed_messages()
        double_user = get_flashed_messages()
        return render_template('register_user.html', validator=validator, double_user=double_user)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        conn = get_connection()
        c = conn.cursor()

        print(username)
        print(password)
        print(password2)

        password = password.encode()

        password = hashlib.sha256(password)
        password = password.digest()

        password2 = password2.encode()

        password2 = hashlib.sha256(password2)
        password2 = password2.digest()

        print(password)
        print(password2)

        if password == password2:
            password_ok = password

            zapytanie = """
                        INSERT INTO "login" ("id", "user", "password", "admin") VALUES (NULL, ?, ?,'false');"""

            try:
                c.execute(zapytanie, (username, password_ok))
            except sqlite3.IntegrityError:
                double_user = flash('Ten login już istnije')
                return redirect('/registerghuewrdb')


            print('dane:', username, password2)
            conn.commit()

            return redirect('/login')

        else:
            flash('Wpisane hasła nie są identyczne')
            return redirect('/registerghuewrdb')


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
            SELECT id, user, password, admin FROM "login" WHERE user = ?;
            """
        c.execute(zapytanie_password, (username,))
        line_from_base = c.fetchone()

        print('hasła:', password, line_from_base)

        if line_from_base == None or password != line_from_base[2]:
            flash('Błędna nazwa użytkownika lub hasło')
            return redirect('/login')

        if password == line_from_base[2]:
            session['user_id'] = line_from_base[0]
            session['user'] = line_from_base[1]

            if line_from_base[3] == 'true':
                return redirect('/wpisz_pytanie')

            else:
                return redirect('/ankieta')


@app.route('/ankieta', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':

        conn = sqlite3.connect('questionDataBase.db')
        c = conn.cursor()
        zapytanie = """
            SELECT id, question FROM "questions";
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

        return render_template('form_for_user.html', **context)

    if request.method == 'POST':
        # conn = get_connection()
        # c = conn.cursor()
        # # answers = request.form
        # print(answers)
        # print(type(answers))

        answers = dict(
            (key, request.form.getlist(key) if len(request.form.getlist(key)) > 1 else request.form.getlist(key)[0]) for
            key in request.form.keys())

        print(answers)

        answers = answers.values()

        print(answers)
        answers_dict = {}
        for i in answers:
            for one in i:
                print(one)
                id = one.strip(' NT')
                id = int(id)
                # if one[0].isnumeric() or one[0:2].isnumeric():
                # print(one[0:2])
                odp = one[-1]
                # l = one[:2]
                # l = l.strip()
                answers_dict[id] = odp

        print(answers_dict)

        # wprowadzenie_ankiety = """
        # INSERT INTO "answers" ("id", "id_user", "id_question", "answer", "is_answer") VALUES (NULL, ?, ?, ?, ?);
        # """

        conn = get_connection()
        c = conn.cursor()

        id_user = session.get('user_id')
        is_answer = 'not now'

        for key, volume in answers_dict.items():
            key= f'"{key}"'
            # volume = f'"{volume}"'
            wprowadzenie_ankiety = f'INSERT INTO "answers" ("id", "id_user", "id_question", "answer", "is_answer") VALUES (NULL, {id_user}, {key}, {volume}, {is_answer});'
            # wprowadzenie_ankiety = f'"""{wprowadzenie_ankiety}"""'

            print(wprowadzenie_ankiety)
            c.execute(wprowadzenie_ankiety)
            conn.commit()
            conn.close()

        # INSERT
        # INTO
        # "answers"("id", "id_user", "id_question", "answer", "is_answer")
        # VALUES(NULL, 1, 5, 'N', 'notnow');

        # print(f'odp z ankiety id user: {id_user}, id question: {id_question}, answer:  {answer}')




        # c.execute(wpisz_pytanie, (id_user, id_question, answer, is_answer))

        # print(f'id = {answer[0]} odpowiedź: {answer[1]}')

        return 'Dziekujemy za wypełnienie ankiety'


@app.route('/wpisz_pytanie', methods=['GET', 'POST'])
def wpisz_pytanie():
    if session:
        return render_template('input_question.html')

    return redirect('/')


@app.route('/dodaj', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        conn = get_connection()
        c = conn.cursor()
        question = request.form['question']
        autor = session.get('user_id')

        add_question = """
        INSERT INTO "questions" ("id", "id_user", "question", "type") VALUES (NULL, ?, ?,'tn')"""

        parametry = (autor, question)
        print(parametry)

        c.execute(add_question, parametry)
        conn.commit()
        return redirect('/dodaj')

    if request.method == 'GET':
        return render_template('input_question.html')


@app.route('/baza')
def data():
    conn = sqlite3.connect('questionDataBase.db')
    c = conn.cursor()
    zapytanie = """
    SELECT id, question FROM "questions";
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
