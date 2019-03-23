import datetime

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def log_in():
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
    app.run()