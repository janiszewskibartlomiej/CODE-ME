import pytest

from api import _policz_sume, ZlyFormatDanych


class TestPoliczSume:
    def test_policz_sume_gdy_poprawne_dane(self):
        dane = [{'id': 1, 'nazwa': 'Szczoteczka do zębów', 'rodzaj': 'sprzet', 'ilosc': 1, 'waga': 0.08},
                {'id': 2, 'nazwa': 'Skarpety', 'rodzaj': 'sprzet', 'ilosc': 4, 'waga': None},
                {'id': 3, 'nazwa': 'Wafelek czekoladowy', 'rodzaj': 'jedzenie', 'ilosc': 6, 'waga': 0.17},
                {'id': 4, 'nazwa': 'Latarka czołowa', 'rodzaj': 'sprzet', 'ilosc': 1, 'waga': 0.1}]

        wynik = _policz_sume(dane)
        assert wynik == 1.2000000000000002

    def test_policz_sume_gdy_brak_danych(self):
        dane = []

        wynik = _policz_sume(dane)
        assert wynik == 0

    def test_policz_sume_gdy_zle_dane(self):
        dane = [{'id': 1, 'nazwa': 'Szczoteczka do zębów', 'rodzaj': 'sprzet', 'ilosc': 1},
                {'id': 4, 'nazwa': 'Latarka czołowa', 'rodzaj': 'sprzet', 'waga': 0.1}]

        with pytest.raises(ZlyFormatDanych) as ex:
            _policz_sume(dane)

        assert str(ex.value) == 'Przedmiot nie posiada klucza "ilosc" lub "waga"'

        print('Żeby zobaczyć ten tekst uruchom `pytest -s`')  # spróbuj!
