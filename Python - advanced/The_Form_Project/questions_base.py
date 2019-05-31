from flask import Blueprint, session, render_template, redirect

from get_connection import polaczenie

question_load = Blueprint('/baza', __name__)


@question_load.route('/baza')
def data():
    if not session:
        return redirect('/login')

    conn = polaczenie()
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
