from flask import Blueprint, request, session, redirect

from get_connection import polaczenie

del_question = Blueprint('/usun', __name__)


@del_question.route('/usun')
def delete():
    if not session:
        return redirect('/login')

    conn = polaczenie()
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
