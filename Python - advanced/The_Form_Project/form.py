import datetime
import json
import sqlite3
import time

from flask import Flask, render_template, request


app = Flask(__name__)

def pobierz_dane():
    with open('user.json') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def log_in():

    return render_template('log_in.html')

@app.route('/input_question', methods=['GET', 'POST'])
def input_question():
    conn = sqlite3.connect('loginDataBase.db')
    c = conn.cursor()
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)

    # zapytanie_user = """
    # SELECT user FROM "login";
    # """
    # c.execute(zapytanie_user)
    # user = c.fetchall()
    # print(user)

    zapytanie_password = """
    SELECT password FROM "login" WHERE user = ?;
    """
    c.execute(zapytanie_password, (username,))
    password_base = c.fetchone()
    password_base = password_base[0]

    print('hasła:', password, password_base)

    if password == password_base:
        return render_template('input_question.html')
    else:
        return 'Brak uprawnień'
        # time.sleep(2)
        # return redirect('/')

    # return '???'


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
