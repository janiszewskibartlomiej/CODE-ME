import datetime
import json
import sqlite3

from flask import Flask, render_template, request

conn = sqlite3.connect('loginDataBase.db')
c = conn.cursor()

app = Flask(__name__)

def pobierz_dane():
    with open('user.json') as f:
        return json.load(f)

@app.route('/', methods=['get', 'post'])
def log_in():

    return render_template('log_in.html')

    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)

    zapytanie_user = """
    SELECT user FROM "login";
    """
    c.execute(zapytanie_user)
    user = c.fetchall()
    print(user)

    zapytanie_password = """
    SELECT 'password' FROM "login" WHERE 'user' = ?;
    """
    c.execute(zapytanie_password, (user))
    password_base = c.fetchone()
    print(password_base)
    try:
        username in user#_baza
        if password == password_base:
            return render_template('input_question.html')
    except ValueError:
        print('Brak uprawnień')


@app.route('/questions', methods=['POST', 'GET'])
def enter_questions():
    question = request.args.get('question')
    correct_answer = request.args.get('answer')

    element = {
        'question': question,
        'correct_answer': correct_answer,
    }
    try:
        f = open('answer.json', mode='r')
        zestaw_pytan = json.load(f)
    except FileNotFoundError:
        zestaw_pytan = []

    if question and correct_answer:
        zestaw_pytan.append(element)
        plik = open('answer.json', mode='w')
        json.dump(zestaw_pytan, plik)

    # print(f"user {id} yes {yes} no {no} I don't know {d_know}")
    teraz = datetime.datetime.now()

    return render_template('input_question.html', echo=teraz)


if __name__ == "__main__":
    app.run(debug=True)
