import datetime
import json
import sqlite3
import time
from werkzeug.security import generate_password_hash, check_password_hash
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

    if session['is_admin'] == False:
        return redirect('ankieta')

    id = session.get('user_id')
    user = session.get('user')
    is_admin = session.get('is_admin')

    return redirect('/dodaj')


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

        print('user: ', username, 'password: ', password, 'pasword2: ', password2)

        if password == password2:

            conn = get_connection()
            c = conn.cursor()

            password_hash = generate_password_hash(password)
            isn_admin = 0
            zapytanie = """
                        INSERT INTO "login" ("id", "user", "password", "admin") VALUES (NULL, ?, ?, ?);"""

            try:
                c.execute(zapytanie, (username, password_hash, isn_admin))
            except sqlite3.IntegrityError:
                double_user = flash('Ten login już istnije')
                return redirect('/registerghuewrdb')

            conn.commit()
            print('dane:', username, password)
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

        print('user: ', username, 'password: ', password)

        zapytanie_password = """
            SELECT id, user, password, admin FROM "login" WHERE user = ?;
            """
        c.execute(zapytanie_password, (username,))
        line_from_base = c.fetchone()

        print('hasła:', password, line_from_base)

        if line_from_base:
            password_hash = line_from_base['password']

            if check_password_hash(password_hash, password):
                session['user_id'] = line_from_base['id']
                session['user'] = line_from_base['user']
                session['is_admin'] = bool(line_from_base['admin'])

                if line_from_base['admin']:
                    return redirect('/dodaj')

                return redirect('/ankieta')

        flash('Błędna nazwa użytkownika lub hasło')
        return redirect('/login')


@app.route('/ankieta', methods=['GET', 'POST'])
def form():
    if not session:
        return redirect('/login')

    if request.method == 'GET':

        conn = get_connection()
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
        conn = get_connection()
        c = conn.cursor()

        answers = dict(
            (key, request.form.getlist(key) if len(request.form.getlist(key)) > 1 else request.form.getlist(key)[0]) for
            key in request.form.keys())

        print(answers)

        answers_dict = {}

        for k, v in answers.items():
            id = k.strip(' answer')
            # for one in i:
            # print(one)
            # id = one.strip(' NT')
            # id = int(id)
            # if one[0].isnumeric() or one[0:2].isnumeric():
            # print(one[0:2])
            odp = v[-1]
            # l = one[:2]
            # l = l.strip()
            answers_dict[id] = odp

        print(answers_dict)

        for k, volume in answers_dict.items():
            add_answers_to_data = """
                    INSERT INTO "answers" ("id", "id_user", "id_question", "answer", "is_answer") VALUES (NULL, ?, ?, ?, ?);
                    """
            id_user = session.get('user_id')
            id_question = k
            answer = volume
            is_answer = 1

            print(add_answers_to_data)

            try:
                c.execute(add_answers_to_data, (id_user, id_question, answer, is_answer))
                conn.commit()
            except sqlite3.OperationalError:
                conn.close()
                return redirect('/ankieta')

            except sqlite3.IntegrityError:
                redirect('/')

    session.clear()
    return render_template('thank_you.html')


@app.route('/wyniki', methods=['GET', 'POST'])
def results():
    if not session:
        return redirect('/login')
    if session['is_admin'] == False:
        return redirect('ankieta')

    conn = get_connection()
    c = conn.cursor()

    def id_pytan_z_odp():
        zapytanie1 = """
        SELECT id_question FROM "answers" GROUP BY id_question;
        """
        c.execute(zapytanie1)
        lista_id_pytan = c.fetchall()
        print(lista_id_pytan)
        return lista_id_pytan

    def odpowiedzi_na_pytanie(id_question):
        zapytanie2 = """
        SELECT id_question, answer, question FROM "answers" INNER JOIN "questions" ON answers.id_question = questions.id WHERE id_question = ?;"""

        c.execute(zapytanie2, (id_question,))
        odpowiedzi = c.fetchall()
        print(odpowiedzi)
        return odpowiedzi

    def policz_odpowiedzi(odpowiedzi):
        odp_tak, odp_nie = 0, 0
        for id_question, answer, question in odpowiedzi:
            if answer == 'T':
                odp_tak += 1
            if answer == 'N':
                odp_nie += 1
            pytanie = question
        wynik = {'id_question': id_question, 'pytanie': pytanie, 'odp_tak': odp_tak, 'odp_nie': odp_nie}
        print(wynik)
        return wynik

    pogrupowana_lista_odpowiedzi = []

    for id in id_pytan_z_odp():
        id = id[0]
        odpowiedzi = odpowiedzi_na_pytanie(id)
        wynik = policz_odpowiedzi(odpowiedzi)
        pogrupowana_lista_odpowiedzi.append(wynik)

    print(pogrupowana_lista_odpowiedzi)

    def udzial_procentowy(i):
        suma_pytan = i['odp_tak'] + i['odp_nie']
        na_tak = (i['odp_tak'] / suma_pytan) * 100
        na_tak = f'{na_tak:.2f} %'
        na_tak = na_tak.replace('.', ',')
        id_question = i['id_question']
        na_nie = (i['odp_nie'] / suma_pytan) * 100
        na_nie = f'{na_nie:.2f} %'
        na_nie = na_nie.replace('.', ',')
        tresc_pytania = i['pytanie']
        wynik = {'id_pytania': id_question, 'pytanie': tresc_pytania, 'na tak': na_tak, 'na nie:': na_nie}
        return wynik

    def spr_ilosci_wszystkich_pytan():
        zapytanie = """
        SELECT id, question FROM "questions";
        """
        c.execute(zapytanie)
        lista_id = c.fetchall()
        return lista_id

    wyniki = []
    for i in pogrupowana_lista_odpowiedzi:
        wynik = udzial_procentowy(i)
        wyniki.append(wynik)

    print('----------------------')
    print(wyniki)
    lista_wszystkich_pytan = spr_ilosci_wszystkich_pytan()

    def spr_pytan_bez_odp(lista_odp):
        for i in lista_odp:
            print(i)
            # print(lista)
            for element in lista_wszystkich_pytan:
                print(element)
                if i[0] == element[0]:
                    lista_wszystkich_pytan.remove(element)
            print('lista do dodania: ', lista_wszystkich_pytan)
        return lista_wszystkich_pytan

    def dodanie_do_wyniku_pytan_bez_odp(lista_bez_odp):
        lista_bez_odp = spr_pytan_bez_odp(id_pytan_z_odp())
        for pytanie in lista_bez_odp:
            id_pytania = pytanie[0]
            tresc_pytania = pytanie[1]
            wynik = {'id_pytania': id_pytania, 'pytanie': tresc_pytania, 'na tak': '0,00 %', 'na nie:': '0,00 %'}
            wyniki.append(wynik)

    pytania = id_pytan_z_odp()
    sprawdzenie = spr_pytan_bez_odp(pytania)
    dodanie = dodanie_do_wyniku_pytan_bez_odp(sprawdzenie)
    print(wyniki)

    context = {'wyniki': wyniki}
    return render_template('results.html', **context)


@app.route('/dodaj', methods=['GET', 'POST'])
def add():
    if not session:
        return redirect('/login')

    if session['is_admin'] == False:
        return redirect('ankieta')

    if request.method == 'GET':
        if session:
            # session.pop('_flashes', None)
            added = get_flashed_messages()
            return render_template('input_question.html', added=added)

    if request.method == 'POST':

        conn = get_connection()
        c = conn.cursor()

        question = request.form['question']
        autor = session.get('user_id')

        # print(type(question))

        if question == '':
            return redirect('/dodaj')

        add_question = """
        INSERT INTO "questions" ("id", "id_user", "question", "type") VALUES (NULL, ?, ?,'tn')"""

        parametry = (autor, question)
        print(parametry)

        c.execute(add_question, parametry)
        conn.commit()
        flash('Pytanie zapisano w bazie')

        return redirect('/dodaj')


@app.route('/baza')
def data():
    if not session:
        return redirect('/login')

    conn = get_connection()
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
    if not session:
        return redirect('/login')

    conn = get_connection()
    c = conn.cursor()

    zapytanie = """
        DELETE FROM "questions" WHERE id = ?;
        """
    usun = request.args.get('id')
    # print(usun)
    c.execute(zapytanie, (usun,))
    conn.commit()
    conn.close()
    return redirect('/baza')


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
