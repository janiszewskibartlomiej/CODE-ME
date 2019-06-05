import json

from flask import Blueprint, request

from db import get_connection

api_bp = Blueprint('api_endpoints', __name__)


def _policz_sume(przedmioty):
    suma = 0
    for przedmiot in przedmioty:
        if przedmiot['waga']:
            suma += przedmiot['ilosc'] * przedmiot['waga']
    return suma


@api_bp.route('/przedmioty', methods=['GET'])
def przedmioty():
    conn = get_connection()
    c = conn.cursor()

    if request.method == 'GET':
        result = c.execute('SELECT * FROM plecak')
        przedmioty = result.fetchall()

        # przepakowanie z obiektów Row na słowniki
        przedmioty = [dict(p) for p in przedmioty]

        suma = _policz_sume(przedmioty)

        wynik = {'przedmioty': przedmioty,
                 'suma': suma}

        return json.dumps(wynik)
