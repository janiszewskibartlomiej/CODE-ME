import json
import os
import tempfile
import pytest

from plecak import app
from db import create_db


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    create_db(app.config['DATABASE'])

    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_przedmioty_get_all(client):
    rv = client.get('api/przedmioty')
    print(rv.response)
    print(rv.status)

    data = json.loads(rv.data)

    poprawne_dane = {
        'przedmioty': [{'id': 1, 'nazwa': 'Szczoteczka do zębów', 'rodzaj': 'sprzet', 'ilosc': 1, 'waga': 0.08},
                       {'id': 2, 'nazwa': 'Skarpety', 'rodzaj': 'sprzet', 'ilosc': 4, 'waga': None},
                       {'id': 3, 'nazwa': 'Wafelek czekoladowy', 'rodzaj': 'jedzenie', 'ilosc': 6, 'waga': 0.17},
                       {'id': 4, 'nazwa': 'Latarka czołowa', 'rodzaj': 'sprzet', 'ilosc': 1, 'waga': 0.1}],
        'suma': 1.2000000000000002}

    assert data == poprawne_dane
