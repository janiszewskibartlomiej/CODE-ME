from flask import Blueprint, flash, request, session, render_template, get_flashed_messages, redirect

from get_connection import polaczenie

add_question = Blueprint('/dodaj', __name__)


@add_question.route('/dodaj', methods=['GET', 'POST'])
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

        conn = polaczenie()
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
