from flask import session, Blueprint, redirect

home_page = Blueprint('/', __name__)


@home_page.route('/')
def index():
    if not session:
        return redirect('/login')

    if session['is_admin'] == False:
        return redirect('ankieta')

    id = session.get('user_id')
    user = session.get('user')
    is_admin = session.get('is_admin')
    # print('id: ', id, 'user: ', user, 'is admin: ', is_admin)

    return redirect('/dodaj')
