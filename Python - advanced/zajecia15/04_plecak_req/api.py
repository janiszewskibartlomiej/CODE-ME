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


@api_bp.route('/przedmioty', methods=['GET', 'POST'])
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

    if request.method == 'POST':
        try:
            data = json.loads(request.data)
        except json.JSONDecodeError:
            return '{"message": "przesłane dane nie są poprawnym JSONem"}', 400

        nazwa = data.get('nazwa')
        ilosc = data.get('ilosc')
        waga = data.get('waga')

        if not (nazwa and ilosc and waga):
            return '{"message": "brak co najmniej jednego parametru"}', 400

        zapytanie = 'INSERT INTO "plecak" ("nazwa", "rodzaj", "ilosc", "waga") VALUES (?, "jedzenie", ?, ?)'
        parametry = (nazwa, ilosc, waga)

        c.execute(zapytanie, parametry)
        conn.commit()

        return '{"message": "nowy przedmiot został utworzony"}', 201


@api_bp.route('/usun', methods=['GET', 'POST'])
def usun():
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

    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            print('odczyt json: ', data)
        except json.JSONDecodeError:
            return '{"message": "przesłane dane nie są poprawnym JSONem"}', 400

        usun_id = data.get('id')
        print('id ze strony: ', usun_id)
        if not usun_id:
            return '{"message": "brak poprawnego id"}', 400

        zapytanie = 'DELETE FROM "plecak" WHERE id = ?'
        parametry = (usun_id,)

        c.execute(zapytanie, parametry)
        conn.commit()

        return '{"message": "Przedmiot został usuniety"}', 302
