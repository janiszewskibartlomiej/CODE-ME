from flask import Flask, render_template, session, Blueprint

from auth import login_required
from db_utils import get_connection

tabela_bp = Blueprint('/_endpoit', __name__)

@tabela_bp.route('/')
@login_required
def index():
    id = session.get('user_id')
    username = session.get('username')
    is_admin = session.get('is_admin')

    conn = get_connection()
    c = conn.cursor()

    if is_admin:
        result = c.execute('SELECT * FROM data JOIN users ON data.user_id = users.id')
    else:
        result = c.execute('SELECT * FROM data WHERE user_id = ?', (id,))

    przedmioty = result.fetchall()

    context = {
        'username': username,
        'przedmioty': przedmioty,
        'is_admin': is_admin
    }

    return render_template('index.html', **context)
